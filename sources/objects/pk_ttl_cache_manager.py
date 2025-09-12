from objects.task_orchestrator_cli_directories import D_TTL_CACHE


class TTLCacheManager:
    """이 유틸은  데코레이터 스타일 + 직접 get/set 형태 모두 지원"""

    def __init__(self, ttl_seconds: int = 5, maxsize: int = 128, db_path=None):
        from functions import ensure_pnx_made
        from pathlib import Path

        if db_path:
            self.db_path = db_path
        else:
            self.db_path = D_TTL_CACHE / "ensure_function_return_ttl_cached.sqlite"

        if self.db_path != ":memory:":
            db_path_obj = Path(self.db_path)
            if not db_path_obj.exists():
                ensure_pnx_made(db_path_obj, mode='f')
        
        self.ttl = ttl_seconds
        self.maxsize = maxsize
        self._ensure_table()

    def _ensure_table(self):
        import sqlite3

        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                         CREATE TABLE IF NOT EXISTS ttl_cache
                         (
                             cache_key
                             TEXT
                             PRIMARY
                             KEY,
                             cache_value
                             TEXT,
                             timestamp
                             REAL
                         )
                         ''')
            conn.commit()

    def count(self):
        import sqlite3
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute('SELECT COUNT(*) FROM ttl_cache').fetchone()[0]

    def _enforce_maxsize(self, conn):
        import logging  # Import logging
        count = conn.execute('SELECT COUNT(*) FROM ttl_cache').fetchone()[0]
        if count > self.maxsize:
            to_remove = count - self.maxsize
            logging.debug(f"Cache: Maxsize ({self.maxsize}) exceeded. Evicting {to_remove} oldest items.")  # Log eviction
            conn.execute('''
                         DELETE
                         FROM ttl_cache
                         WHERE cache_key IN (SELECT cache_key
                                             FROM ttl_cache
                                             ORDER BY timestamp ASC
                             LIMIT ?
                             )
                         ''', (to_remove,))
            conn.commit()

    def set(self, key: str, value):
        import json
        import sqlite3
        import time
        import logging  # Import logging

        now = time.time()
        # Check if the value has a to_dict() method and use it for serialization
        if hasattr(value, 'to_dict') and callable(getattr(value, 'to_dict')):
            serializable_value = value.to_dict()
        else:
            serializable_value = value

        value_str = json.dumps(serializable_value)  # 리스트 → 문자열 직렬화
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT OR REPLACE INTO ttl_cache (cache_key, cache_value, timestamp)
                VALUES (?, ?, ?)
            ''', (key, value_str, now))
            self._enforce_maxsize(conn)
            current_count = self.count()  # Get current count after set and enforce_maxsize
            logging.debug(f"Cache: Item '{key}' set. Current size: {current_count}/{self.maxsize}")  # Log current size

    def get(self, key: str):
        import json
        import sqlite3
        import time
        import logging  # Import logging

        now = time.time()
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute('''
                               SELECT cache_value, timestamp
                               FROM ttl_cache
                               WHERE cache_key = ?
                               ''', (key,)).fetchone()

            if row:
                value_str, ts = row
                if now - ts < self.ttl:
                    logging.debug(f"Cache: Hit for key '{key}'.")  # Log cache hit
                    return json.loads(value_str)  # 문자열 → 리스트 복원
                else:
                    self.invalidate(key)
                    logging.debug(f"Cache: Item '{key}' expired and invalidated.")  # Log expiration
            logging.debug(f"Cache: Miss for key '{key}'.")  # Log cache miss
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
        import logging
        from sources.objects.pk_map_texts import PkTexts

        def wrapper_factory(func):
            from functools import wraps

            @wraps(func)
            def wrapped(*args, **kwargs):
                key = f"{func.__module__}.{func.__name__}:{str((args, tuple(sorted(kwargs.items()))))}"
                cached_result = self.get(key)
                if cached_result is not None:
                    logging.debug(f"[{PkTexts.CASHE_USED}] cached result: {key} {func.__name__}")
                    logging.debug(f"데코레이터가 반환하는 캐시된 값: {cached_result}")  # Added debug log
                    logging.debug(f"Cache: Current size after hit: {self.count()}/{self.maxsize}")  # Log current size after hit
                    return cached_result
                result = func(*args, **kwargs)
                self.set(key, result)
                logging.debug(f"데코레이터가 반환하는 새로 계산된 값: {result}")  # Added debug log
                logging.debug(f"Cache: Current size after miss and set: {self.count()}/{self.maxsize}")  # Log current size after miss and set
                return result

            return wrapped

        return wrapper_factory


def ensure_function_return_ttl_cached(ttl_seconds=5, maxsize=10, db_path=None):
    # TBD : # TODO : get_video_filtered_list 의 결과가 None or "" 처럼 파일이 없는 경우 라면 캐시가 초기화되도록 수정. 반드시 목록 1개라도 있도록 하기 위함.
    # maxsize= 128
    return TTLCacheManager(ttl_seconds=ttl_seconds, maxsize=maxsize, db_path=db_path).decorator()
