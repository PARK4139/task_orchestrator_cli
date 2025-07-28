




def initialize_and_customize_logging_config(__file__):
    """
    프로젝트 기본 규칙: 모든 로그 파일은 D_PKG_LOG 디렉토리에 저장
    
    로깅 설정:
    - 로그 레벨: DEBUG (모든 레벨 기록)
    - 로그 포맷: [시간] [레벨] [파일명:라인] [함수명] [메시지]
    - 로그 위치: D_PKG_LOG/pk_log_[파일명]_[타임스탬프].log
    - 인코딩: UTF-8
    
    사용 예시:
        initialize_and_customize_logging_config(__file__)
        logging.warning(msg)
        logging.error(msg)
        logging.critical(msg)
        logging.debug(msg)
        logging.info(msg)
    """
    import logging
    import os
    from pkg_py.system_object.directories import D_PKG_LOG
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_time_as_ import get_time_as_
    
    # 로그 디렉토리 생성
    os.makedirs(D_PKG_LOG, exist_ok=True)
    
    # 로그 파일명 생성 (프로젝트 기본 규칙: D_PKG_LOG에 저장)
    log_filename = f"pk_log_{get_nx(__file__)}_{get_time_as_('now')}.log"
    log_file_path = os.path.join(D_PKG_LOG, log_filename)
    
    # 더 자세한 로그 포맷
    log_format = "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] [%(funcName)s] [%(message)s]"
    
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
    logging.info(f"프로젝트 기본 규칙: 모든 로그는 D_PKG_LOG 디렉토리에 저장")


