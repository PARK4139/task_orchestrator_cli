# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager
from pathlib import Path
from typing import List, Dict

"""
ensure_target_found_advanced.py - 대화형 타겟 검색 및 스캔 도구 (효율성 개선)
- 스캔: 연결된 모든 드라이브를 스캔하여 파일/디렉토리/모두 DB 3종에 동시 저장
- 조회: DB 조회 시 SQL 필터링을 적용하고, fzf에 직접 파이핑하여 효율성 증대
- 조회 옵션: 타겟명만 보거나, 전체 경로를 포함해서 볼 수 있는 옵션 추가
- 스캔 안정성: 스캔 시작 전 기존 DB를 자동으로 백업
"""


# --- DB 관리 ---
@contextmanager
def get_db_connection(db_path: Path):
    import logging
    import sqlite3

    try:
        conn = sqlite3.connect(db_path, timeout=10)
        yield conn
    except sqlite3.Error as e:
        logging.error(f"Database error at {db_path}: {e}")
        raise
    finally:
        if 'conn' in locals() and conn:
            conn.close()


def get_db_path(target_type: str) -> Path:
    from pathlib import Path

    from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_CACHE
    db_dir = Path(D_TASK_ORCHESTRATOR_CLI_CACHE) / "pnx_dbs_scanned"
    db_dir.mkdir(parents=True, exist_ok=True)
    db_map = {
        "파일": "drives_scanned_file_only.sqlite",
        "디렉토리": "drives_scanned_directory_only.sqlite",
        "모두": "drives_scanned_both_file_directory.sqlite",
    }
    return db_dir / db_map[target_type]


def init_db(db_path: Path):
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS targets (path TEXT PRIMARY KEY, type TEXT, last_scanned REAL)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_type ON targets(type)")
        conn.commit()


# --- 스캔 로직 ---
def _handle_walk_error(e):  # New error handler for os.walk

    import logging

    logging.warning(f"os.walk 접근 오류: {e.filename} - {e.strerror}")


def backup_existing_dbs(db_paths: Dict[str, Path]):
    import logging
    import shutil
    from datetime import datetime

    backup_dir = db_paths["모두"].parent / "backup"
    backup_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    for db_type, db_path in db_paths.items():
        if db_path.exists():
            try:
                size_mb = db_path.stat().st_size / (1024 * 1024)
                logging.info(f"기존 '{db_type}' DB 파일을 백업합니다. (크기: {size_mb:.2f} MB)")
                backup_filename = f"{db_path.stem}_backup_{timestamp}{db_path.suffix}"
                backup_path = backup_dir / backup_filename
                shutil.copy2(db_path, backup_path)
                logging.info(f"백업 완료: {backup_path}")
            except Exception as e:
                logging.error(f"DB 파일 백업 중 오류 발생 ({db_path}): {e}")


def perform_full_scan():
    import os
    import logging
    from datetime import datetime
    from pathlib import Path

    from functions.get_drives_connected import get_drives_connected
    db_paths = {tt: get_db_path(tt) for tt in ["파일", "디렉토리", "모두"]}
    backup_existing_dbs(db_paths)
    for db_path in db_paths.values(): init_db(db_path)
    scan_roots = get_drives_connected()
    logging.info(f"전체 스캔을 시작합니다. 대상 드라이브: {scan_roots}")
    files_to_insert, dirs_to_insert = [], []
    scan_time = datetime.now().timestamp()
    for scan_root in scan_roots:
        logging.info(f"드라이브 스캔 중: {scan_root}")
        # Specific log for user's Downloads folder if it's the C: drive
        if Path(scan_root) == Path('C:\\'):
            user_downloads_path = Path.home() / "Downloads"
            if user_downloads_path.exists():
                logging.info(f"사용자 Downloads 폴더 스캔 시도: {user_downloads_path}")

        try:
            for root, dirs, files in os.walk(scan_root, onerror=_handle_walk_error):  # Pass onerror handler
                # Add debug logging for Downloads folder content
                if user_downloads_path.exists() and Path(root).is_relative_to(user_downloads_path):
                    logging.debug(f"[DEBUG SCAN] Downloads content in {root}: dirs={len(dirs)}, files={len(files)}")
                    if "박정훈" in root or any("박정훈" in f for f in files):
                        logging.debug(f"[DEBUG SCAN] '박정훈' found in Downloads related path: {root}")

                for d in dirs:
                    dirs_to_insert.append((os.path.join(root, d), "directory", scan_time))
                for f in files:
                    files_to_insert.append((os.path.join(root, f), "file", scan_time))
        except Exception as e:
            logging.error(f"드라이브 스캔 중 예외 발생: {scan_root} - {e}")
    logging.info(f"총 {len(files_to_insert)}개의 파일과 {len(dirs_to_insert)}개의 디렉토리를 찾았습니다. DB에 저장합니다...")
    with get_db_connection(db_paths["파일"]) as conn:
        conn.executemany("INSERT OR REPLACE INTO targets VALUES (?, ?, ?)", files_to_insert);
        conn.commit()
    with get_db_connection(db_paths["디렉토리"]) as conn:
        conn.executemany("INSERT OR REPLACE INTO targets VALUES (?, ?, ?)", dirs_to_insert);
        conn.commit()
    with get_db_connection(db_paths["모두"]) as conn:
        conn.executemany("INSERT OR REPLACE INTO targets VALUES (?, ?, ?)", files_to_insert + dirs_to_insert);
        conn.commit()
    logging.info("전체 스캔 및 DB 저장이 완료되었습니다.")


# --- 조회 & 디버그 로직 ---
def get_system_path_filters() -> List[str]:
    return ["%.git%", "%__pycache__%", "%node_modules%", "%.venv%", "%task_orchestrator_cli%", "%System Volume Information%", "%RECYCLE.BIN%"]


def perform_query(db_path: Path, include_system: bool, display_format: str):
    import logging
    import subprocess
    from pathlib import Path

    logging.info(f"DB에서 타겟 목록을 조회합니다... (표시 형식: {display_format})")
    if not db_path.exists():
        logging.error(f"DB 파일이 존재하지 않습니다: {db_path}. 먼저 스캔을 실행해주세요.")
        return
    query = "SELECT path FROM targets"
    params = []
    if not include_system:
        filters = get_system_path_filters()
        query += " WHERE " + " AND ".join(["path NOT LIKE ?"] * len(filters))
        params.extend(filters)
    try:
        fzf_cmd = ["fzf", "--height", "80%", "--layout", "reverse", "--info", "inline", "--prompt", "🔍 검색: ", "--header", "실시간 검색"]

        if display_format == "타겟명만":
            fzf_cmd.extend(["--delimiter", "\t", "--with-nth", "1"])
        elif display_format == "경로포함":
            fzf_cmd.extend(["--preview", "ls -la {}"])

        with get_db_connection(db_path) as conn, subprocess.Popen(fzf_cmd, stdin=subprocess.PIPE, text=True, errors='ignore') as fzf_proc:
            cursor = conn.cursor()
            for row in cursor.execute(query, params):
                try:
                    path_str = row[0]
                    if display_format == "타겟명만":
                        display_and_search_str = f"{Path(path_str).name}	{path_str}"

                    else:
                        display_and_search_str = path_str

                    fzf_proc.stdin.write(display_and_search_str + "\n")
                except (IOError, BrokenPipeError):
                    break
            if fzf_proc.stdin:
                fzf_proc.stdin.close()
            fzf_proc.wait()
    except FileNotFoundError:
        logging.error("fzf가 설치되어 있지 않거나 PATH에 없습니다. fzf를 설치해주세요.")
    except Exception as e:
        logging.error(f"fzf 실행 중 오류 발생: {e}")


def perform_debug_query():
    import os
    import logging
    from pathlib import Path

    """DB 내용을 직접 조회하여 스캔 문제를 진단"""
    db_path = get_db_path("모두")
    logging.info(f"--- 디버그 모드: {db_path} DB 내용 확인 ---")
    if not db_path.exists():
        logging.error("DB 파일이 존재하지 않습니다. 스캔을 먼저 실행해주세요.")
        return

    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()

        # 1. Downloads 폴더 내용 확인
        logging.info("\n[1] 'Downloads' 포함 경로 조회 (최대 20개):")
        cursor.execute("SELECT path FROM targets WHERE path LIKE '%Downloads%' LIMIT 20")
        results_downloads = cursor.fetchall()
        if results_downloads:
            for row in results_downloads:
                logging.info(f"  - {row[0]}")
        else:
            logging.info("  -> 'Downloads' 포함 경로를 찾을 수 없습니다.")

        # 2. '박정훈' 키워드 내용 확인
        logging.info("\n[2] '박정훈' 포함 경로 조회 (최대 20개):")
        cursor.execute("SELECT path FROM targets WHERE path LIKE '%박정훈%' LIMIT 20")
        results_keyword = cursor.fetchall()
        if results_keyword:
            for row in results_keyword:
                logging.info(f"  - {row[0]}")
        else:
            logging.info("  -> '박정훈' 포함 경로를 찾을 수 없습니다.\n")

        # 3. Downloads 폴더 직접 접근 시도
        downloads_dir = Path.home() / "Downloads"
        logging.info(f"\n[3] Downloads 폴더 직접 접근 시도: {downloads_dir}")
        if downloads_dir.exists() and downloads_dir.is_dir():
            try:
                contents = os.listdir(downloads_dir)
                logging.info(f"  -> 접근 성공. 내용 (처음 5개): {contents[:5]} ... (총 {len(contents)}개)")
            except OSError as e:
                logging.error(f"  -> 접근 실패: {e}")
        else:
            logging.info("  -> Downloads 폴더가 존재하지 않거나 디렉토리가 아닙니다.")

    logging.info("--- 디버그 모드 종료 ---")


# --- 메인 함수 ---
def ensure_target_found_advanced():
    import logging

    from functions.ensure_value_completed import ensure_value_completed
    from objects.pk_local_test_activate import LTA
    logging.info("--- 대화형 타겟 검색 도구 시작 ---")
    try:
        if LTA:
            operation = "조회"
        else:
            operation = ensure_value_completed("수행할 작업을 선택하세요:", ["스캔", "조회", "디버그"]) or "조회"
        if operation == "스캔":
            perform_full_scan()
        elif operation == "조회":
            if LTA:
                target_type = "파일"
                filter_choice = "제외"
                display_format = "경로포함"
            else:
                target_type = ensure_value_completed("조회할 타겟 타입을 선택하세요:", ["파일", "디렉토리", "모두"]) or "파일"
                filter_choice = ensure_value_completed("시스템 타겟을 포함할까요?", ["포함", "제외"]) or "제외"
                display_format = ensure_value_completed("조회 방식을 선택하세요:", ["타겟명만", "경로포함"]) or "경로포함"
            db_path = get_db_path(target_type)
            include_system = (filter_choice == "포함")
            perform_query(db_path, include_system, display_format)
        elif operation == "디버그":
            perform_debug_query()

    except (KeyboardInterrupt, EOFError):
        logging.info("\n프로그램을 종료합니다.")
    except Exception as e:
        logging.error(f"예상치 못한 오류가 발생했습니다: {e}", exc_info=True)
    finally:
        logging.info("--- 대화형 타겟 검색 도구 종료 ---")


if __name__ == "__main__":
    ensure_target_found_advanced()
