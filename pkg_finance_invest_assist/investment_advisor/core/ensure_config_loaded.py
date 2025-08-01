"""
Configuration loading module for Investment Advisor.
"""
from pydantic_settings import BaseSettings
from typing import Optional
import os

class InvestmentAdvisorConfig(BaseSettings):
    """Investment Advisor configuration settings."""
    
    # Database settings
    database_url: Optional[str] = None
    
    # External service URLs
    market_data_url: str = "http://localhost:8002"
    
    # Analysis settings
    default_risk_tolerance: str = "medium"
    default_confidence_threshold: float = 0.7
    
    # Logging settings
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

def ensure_config_loaded() -> InvestmentAdvisorConfig:
    """
    Investment Advisor 설정을 확실히 로드합니다.
    """
    config = InvestmentAdvisorConfig()
    
    # 환경 변수에서 설정 로드
    config.database_url = os.getenv("DATABASE_URL", config.database_url)
    config.market_data_url = os.getenv("MARKET_DATA_URL", config.market_data_url)
    config.default_risk_tolerance = os.getenv("DEFAULT_RISK_TOLERANCE", config.default_risk_tolerance)
    
    return config 