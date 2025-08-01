"""
Configuration loading module for API Gateway.
"""
from pydantic_settings import BaseSettings
from typing import Optional
import os

class GatewayConfig(BaseSettings):
    """API Gateway configuration settings."""
    
    # Service URLs
    investment_advisor_url: str = "http://localhost:8001"
    market_data_url: str = "http://localhost:8002"
    news_analyzer_url: str = "http://localhost:8003"
    
    # Database settings
    database_url: Optional[str] = None
    
    # Security settings
    cors_origins: list = ["*"]
    trusted_hosts: list = ["*"]
    
    # Logging settings
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

def ensure_config_loaded() -> GatewayConfig:
    """
    API Gateway 설정을 확실히 로드합니다.
    """
    config = GatewayConfig()
    
    # 환경 변수에서 설정 로드
    config.investment_advisor_url = os.getenv(
        "INVESTMENT_ADVISOR_URL", 
        config.investment_advisor_url
    )
    config.market_data_url = os.getenv(
        "MARKET_DATA_URL", 
        config.market_data_url
    )
    config.news_analyzer_url = os.getenv(
        "NEWS_ANALYZER_URL", 
        config.news_analyzer_url
    )
    
    return config 