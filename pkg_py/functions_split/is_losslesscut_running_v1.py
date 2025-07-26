def is_losslesscut_running_v1():
    from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
    from pkg_py.functions_split.ensure_printed import ensure_printed
    # too slow

    f_losslesscut_exe = get_pnx_windows_style(pnx=F_LOSSLESSCUT_EXE)
    std_list = ensure_command_excuted_to_os(cmd='tasklist.exe | findstr "LosslessCut.exe"')
    if len(std_list) == 0:
        ensure_printed(f"{get_nx(f_losslesscut_exe)} is not running", print_color='red')
        return False
    ensure_printed(f"{get_nx(f_losslesscut_exe)} is running", print_color='green')
    return True




"""이 유틸은  데코레이터 형태 + 직접 get/set 형태 모두 지원하는 구조"""
# 파일 위치 예시: pkg_py/functions_split/ttl_cache.py
# 파일: pkg_py/utils/cache/ttl_cache_sqlite.py
db_path = os.path.join(D_PKG_DB, "ttl_cache.sqlite")


# 파일: pkg_py/utils/cache/ttl_cache_sqlite.py

import sqlite3
import time
from pathlib import Path
from functools import wraps

class SqliteTTLCache:
    def __init__(self, db_path: str = 'ttl_cache.sqlite', ttl_seconds: int = 5, maxsize: int = 128):
        self.db_path = Path(db_path)
        self.ttl = ttl_seconds
        self.maxsize = maxsize
        self._ensure_table()

    def _ensure_table(self):
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

    def set(self, key: str, value: str):
        now = time.time()
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT OR REPLACE INTO ttl_cache (cache_key, cache_value, timestamp)
                VALUES (?, ?, ?)
            ''', (key, value, now))
            self._enforce_maxsize(conn)

    def get(self, key: str):
        now = time.time()
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute('''
                SELECT cache_value, timestamp FROM ttl_cache
                WHERE cache_key = ?
            ''', (key,)).fetchone()

            if row:
                value, ts = row
                if now - ts < self.ttl:
                    return value
                else:
                    self.invalidate(key)
        return None

    def invalidate(self, key: str):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('DELETE FROM ttl_cache WHERE cache_key = ?', (key,))
            conn.commit()

    def clear(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('DELETE FROM ttl_cache')
            conn.commit()

    def decorator(self):
        """함수를 TTL + LRU 캐시로 감싸는 데코레이터"""
        def wrapper_factory(func):
            @wraps(func)
            def wrapped(*args, **kwargs):
                key = str((args, tuple(sorted(kwargs.items()))))
                cached_result = self.get(key)
                if cached_result is not None:
                    return cached_result
                result = func(*args, **kwargs)
                self.set(key, result)
                return result
            return wrapped
        return wrapper_factory

def sqlite_ttl_cache(ttl_seconds=5, maxsize=128, db_path="ttl_cache.sqlite"):
    """데코레이터 방식으로 사용 가능하게"""
    return SqliteTTLCache(
        db_path=db_path,
        ttl_seconds=ttl_seconds,
        maxsize=maxsize
    ).decorator()


@sqlite_ttl_cache(ttl_seconds=3, maxsize=64, db_path='my_cache.sqlite') # 최대 64개 캐시
def ensure_command_excuted_to_os_cashed(cmd):
    import subprocess
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip().splitlines()

