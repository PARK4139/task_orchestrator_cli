"""
Logging configuration module for API Gateway.
"""
import logging
from typing import Optional
import sys

def ensure_logging_configured(
    log_level: str = "INFO",
    log_file: Optional[str] = None,
    service_name: str = "api-gateway"
) -> logging.Logger:
    """
    로깅 설정을 확실히 구성합니다.
    """
    # 로거 생성
    logger = logging.getLogger(service_name)
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # 기존 핸들러 제거 (중복 방지)
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # 콘솔 핸들러
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    
    # 포맷터 설정
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    
    # 파일 핸들러 (선택적)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    logger.addHandler(console_handler)
    
    # 로거가 상위로 전파되지 않도록 설정
    logger.propagate = False
    
    return logger 