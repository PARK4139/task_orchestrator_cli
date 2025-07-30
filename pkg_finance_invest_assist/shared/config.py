"""
Configuration settings for the finance investment assistant project.
"""
import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # Database settings
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/finance_db"
    
    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Finance Investment Assistant"
    
    # Security settings
    SECRET_KEY: str = "your-secret-key-here"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # External API settings
    FINANCE_API_KEY: Optional[str] = None
    NEWS_API_KEY: Optional[str] = None
    
    # Logging settings
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Redis settings (for caching)
    REDIS_URL: str = "redis://localhost:6379"
    
    # Docker settings
    DOCKER_MODE: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = True


def ensure_settings_loaded() -> Settings:
    """Ensure settings are loaded and return settings instance."""
    return Settings()


# Global settings instance
settings = ensure_settings_loaded() 