from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


# @ensure_function_ttl_cached(ttl_seconds=60, maxsize=64)
@ensure_seconds_measured
def initialize_and_customize_logging_config(__file__):
    from pkg_py.system_object.directories import D_PK_RECYCLE_BIN
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split import get_pnx_os_style

    import logging
    import os
    from pkg_py.system_object.directories import D_PKG_LOG
    from pkg_py.functions_split import get_time_as_

    if LTA:
        D_DST = D_PK_RECYCLE_BIN
    else:
        D_DST = D_PKG_LOG

    os.makedirs(D_DST, exist_ok=True)

    # 하루 이상 지난 로그 파일 삭제
    # cleanup_old_log_files(D_DST)

    # log_filename = f"{get_time_as_('now')}_{get_nx(__file__)}.log" # pk_option
    log_filename = f"{get_time_as_('now')}.log"  # pk_option
    # log_file_path = os.path.join(D_DST, log_filename)
    log_file_path = os.path.join(D_DST, log_filename)
    log_file_path = get_pnx_os_style(log_file_path)

    # pk_option
    # log_format = "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] [%({funcName})s] [%(message)s]"
    log_format = "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] [%(message)s]"

    logging.basicConfig(
        level=logging.DEBUG,  # setting to record from level DEBUG to level info
        format=log_format,
        encoding="utf-8",
        handlers=[
            logging.FileHandler(log_file_path, encoding="utf-8", mode='w'),
            logging.StreamHandler()
        ]
    )

    # yt-dlp 로그 레벨 조정
    logging.getLogger('yt_dlp').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)

    # 로그 시작 메시지
    logging.info(f"=== 로깅 시작 ===")
    logging.info(f"로그 파일: {log_file_path}")
    logging.info(f"프로젝트 기본 규칙: 모든 로그는 {D_DST} 디렉토리에 저장")

@ensure_seconds_measured
def cleanup_old_log_files(log_directory, days_to_keep=1):
    """
    지정된 일수보다 오래된 로그 파일들을 삭제합니다.
    
    Args:
        log_directory (str): 로그 파일들이 있는 디렉토리 경로
        days_to_keep (int): 보관할 일수 (기본값: 1일)
    """
    from pkg_py.functions_split.ensure_pnx_moved import ensure_pnx_moved
    from pkg_py.system_object.directories import D_PK_RECYCLE_BIN

    import os
    import glob
    import time
    from pkg_py.system_object.map_massages import PkMessages2025
    try:
        current_time = time.time()
        cutoff_time = current_time - (days_to_keep * 24 * 60 * 60)  # days_to_keep일 전 시간

        # .log 파일들 찾기
        log_pattern = os.path.join(log_directory, "*.log")
        log_files = glob.glob(log_pattern)

        deleted_count = 0
        kept_count = 0

        for log_file in log_files:
            try:
                # 파일의 수정 시간 확인
                file_modified_time = os.path.getmtime(log_file)

                if file_modified_time < cutoff_time:
                    ensure_pnx_moved(pnx=log_file, d_dst=D_PK_RECYCLE_BIN)
                    deleted_count += 1
                    print(f"️ {PkMessages2025.OLD_LOG_FILE_DELETED}: {os.path.basename(log_file)}")
                else:
                    kept_count += 1

            except OSError as e:
                print(f"️ {PkMessages2025.LOG_FILE_DELETE_FAILED}: {log_file} - {e}")

        if deleted_count > 0:
            print(f" {PkMessages2025.LOG_CLEANUP_COMPLETE}: {deleted_count}{PkMessages2025.FILES_DELETED}, {kept_count}{PkMessages2025.FILES_KEPT}")
        elif kept_count > 0:
            print(f"ℹ️ {PkMessages2025.NO_OLD_FILES_TO_DELETE}, {kept_count}{PkMessages2025.FILES_KEPT}")

    except Exception as e:
        print(f" {PkMessages2025.LOG_CLEANUP_ERROR}: {e}")
