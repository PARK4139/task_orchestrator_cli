"""
Configuration Settings

환경 설정 및 상수 관리
"""

from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # 앱 기본 설정
    app_name: str = "Smart Person AI"
    app_version: str = "0.1.0"
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # API 설정
    api_v1_prefix: str = "/api/v1"
    
    # 데이터베이스 설정
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql://smart_user:smart_password@localhost:5432/smart_person_ai"
    )
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    mongodb_url: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    
    # AI API 설정
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    anthropic_api_key: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    stable_diffusion_api_key: Optional[str] = os.getenv("STABLE_DIFFUSION_API_KEY")
    
    # AWS 설정
    aws_access_key_id: Optional[str] = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key: Optional[str] = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_s3_bucket: str = os.getenv("AWS_S3_BUCKET", "smart-person-ai-storage")
    
    # 보안 설정
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    access_token_expire_minutes: int = 30
    
    # 서비스 포트 설정
    api_gateway_port: int = 8000
    ai_image_service_port: int = 8001
    ai_book_service_port: int = 8002
    excel_automation_port: int = 8011
    web_crawler_port: int = 8012
    payment_service_port: int = 8021
    
    class Config:
        env_file = ".env"

settings = Settings()