from objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_task_orchestrator_cli_log_initialized(__file__, with_file_logging_mode=True):
    import logging

    from objects.pk_colorful_logging_formatter import PkColorfulLoggingFormatter
    from objects.task_orchestrator_cli_files import F_PK_TEMP_LOG
    from sources.functions.ansi_stripping_formatter import AnsiStrippingFormatter  # Import the new formatter
    from sources.functions.cleanup_old_log_files import cleanup_old_log_files
    from sources.functions.ensure_task_orchestrator_cli_cleared import ensure_task_orchestrator_cli_cleared
    from sources.functions.get_pk_program_language import get_pk_program_language
    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.pk_map_texts import PkTexts
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_LOGS
    from sources.objects.task_orchestrator_cli_files import F_TASK_ORCHESTRATOR_CLI_LOG
    if hasattr(ensure_task_orchestrator_cli_log_initialized, '_initialized'):
        return
    ensure_task_orchestrator_cli_log_initialized._initialized = True

    # pk_option: 콘솔 로깅 활성화/비활성화 (하드코딩 옵션)
    ENABLE_CONSOLE_LOGGING = True
    # ENABLE_CONSOLE_LOGGING = False

    logging_file = None
    if with_file_logging_mode:
        logging_file = F_TASK_ORCHESTRATOR_CLI_LOG
    else:
        logging_file = F_PK_TEMP_LOG

    # task_orchestrator_cli language setting
    try:
        lang = get_pk_program_language()
        PkTexts.set_lang(lang)
    except Exception:
        PkTexts.set_lang("korean")

    D_TASK_ORCHESTRATOR_CLI_LOGS.mkdir(parents=True, exist_ok=True)

    # pk_option : 하루 이상 지난 로그 파일 삭제
    if not LTA:
        cleanup_old_log_files(D_TASK_ORCHESTRATOR_CLI_LOGS)

    if LTA:
        ensure_task_orchestrator_cli_cleared()

    # 컬러풀 로깅 포맷터 import
    try:
        colorful_formatter = PkColorfulLoggingFormatter(use_pkmessage=True)
    except ImportError:
        # fallback: 기본 포맷터 사용
        log_format = "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] [%(message)s]"
        colorful_formatter = logging.Formatter(log_format)

    # LTA 모드에서는 새 파일로, 일반 모드에서는 append 모드로
    file_mode = "w" if LTA else "a"

    # 파일 핸들러 (ANSI 코드 제거 포맷)
    file_handler = logging.FileHandler(logging_file, encoding="utf-8", mode=file_mode)
    file_format = "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] [%(message)s]"
    file_handler.setFormatter(AnsiStrippingFormatter(file_format))  # Use AnsiStrippingFormatter

    # 콘솔 핸들러 (컬러풀 포맷)
    if ENABLE_CONSOLE_LOGGING:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(colorful_formatter)
        console_handler.setLevel(logging.DEBUG)

    # 로거 설정
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # 기존 핸들러 제거 후 새 핸들러 추가
    logger.handlers.clear()
    logger.addHandler(file_handler)
    if ENABLE_CONSOLE_LOGGING:
        logger.addHandler(console_handler)
        console_handler.flush()

    # 로깅 시스템 상태 확인 (디버깅용)
    logging.debug(PK_UNDERLINE)
    logging.debug("# 로깅 시스템 상태 ")
    logging.debug(f"루트 로거 레벨: {logging.getLevelName(logger.level)}")
    logging.debug(f"루트 로거 핸들러 수: {len(logger.handlers)}")
    for i, handler in enumerate(logger.handlers):
        logging.debug(f"핸들러 {i}:")
        logging.debug(f"타입: {type(handler)}")
        logging.debug(f"레벨: {logging.getLevelName(handler.level)}")
        if hasattr(handler, 'formatter') and handler.formatter:
            logging.debug(f"포맷터: {type(handler.formatter)}")
        else:
            logging.debug(f"포맷터: 없음")
    logging.debug(PK_UNDERLINE)

    # yt-dlp 로그 레벨 조정
    # logging.getLogger('yt_dlp').setLevel(logging.WARNING)
    # logging.getLogger('urllib3').setLevel(logging.WARNING)

    # 로그 시작 메시지
    # print(f"task_orchestrator_cli log is saved at {logging_file}")
    logging.debug(f"task_orchestrator_cli log is saved at {logging_file}")
