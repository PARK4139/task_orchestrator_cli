class TTLCacheManager:
    """이 유틸은  데코레이터 스타일 + 직접 get/set 형태 모두 지원"""

    def __init__(self, db_path, ttl_seconds: int = 5, maxsize: int = 128):
        import os
        from pathlib import Path

        from pkg_py.system_object.directories import D_PKG_DB
        db_path = db_path or os.path.join(D_PKG_DB, "ensure_function_ttl_cached.sqlite")
        self.db_path = Path(db_path)
        self.ttl = ttl_seconds
        self.maxsize = maxsize
        self._ensure_table()

    def _ensure_table(self):
        import sqlite3

        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS ttl_cache (
                    cache_key TEXT PRIMARY KEY,
                    cache_value TEXT,
                    timestamp REAL
                )
            ''')
            conn.commit()

    def _enforce_maxsize(self, conn):
        count = conn.execute('SELECT COUNT(*) FROM ttl_cache').fetchone()[0]
        if count > self.maxsize:
            to_remove = count - self.maxsize
            conn.execute('''
                DELETE FROM ttl_cache
                WHERE cache_key IN (
                    SELECT cache_key FROM ttl_cache
                    ORDER BY timestamp ASC
                    LIMIT ?
                )
            ''', (to_remove,))
            conn.commit()

    def set(self, key: str, value):
        import json
        import sqlite3
        import time

        now = time.time()
        value_str = json.dumps(value)  # 리스트 → 문자열 직렬화
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT OR REPLACE INTO ttl_cache (cache_key, cache_value, timestamp)
                VALUES (?, ?, ?)
            ''', (key, value_str, now))
            self._enforce_maxsize(conn)

    def get(self, key: str):
        import json
        import sqlite3
        import time

        now = time.time()
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute('''
                SELECT cache_value, timestamp FROM ttl_cache
                WHERE cache_key = ?
            ''', (key,)).fetchone()

            if row:
                value_str, ts = row
                if now - ts < self.ttl:
                    return json.loads(value_str)  # 문자열 → 리스트 복원
                else:
                    self.invalidate(key)
        return None

    def invalidate(self, key: str):
        import sqlite3

        with sqlite3.connect(self.db_path) as conn:
            conn.execute('DELETE FROM ttl_cache WHERE cache_key = ?', (key,))
            conn.commit()

    def clear(self):
        import sqlite3

        with sqlite3.connect(self.db_path) as conn:
            conn.execute('DELETE FROM ttl_cache')
            conn.commit()

    def decorator(self):
        """함수를 TTL + LRU 캐시로 감싸는 데코레이터"""

        def wrapper_factory(func):
            from functools import wraps

            @wraps(func)
            def wrapped(*args, **kwargs):
                from pkg_py.system_object.map_massages import PkMessages2025
                key = str((args, tuple(sorted(kwargs.items()))))
                cached_result = self.get(key)
                if cached_result is not None:
                    print(f"[{PkMessages2025.CASHE_USED}] cached result: {key}")
                    return cached_result
                result = func(*args, **kwargs)
                self.set(key, result)
                return result

            return wrapped

        return wrapper_factory


def ensure_function_ttl_cached(db_path=None, ttl_seconds=5, maxsize=128):
    """decorator wrapper"""
    return TTLCacheManager(db_path=db_path, ttl_seconds=ttl_seconds, maxsize=maxsize).decorator()
