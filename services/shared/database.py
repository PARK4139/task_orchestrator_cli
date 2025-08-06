"""
Database Configuration

공통 데이터베이스 설정 및 연결 관리
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis
from motor.motor_asyncio import AsyncIOMotorClient
import os

# PostgreSQL 설정
POSTGRES_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://smart_user:smart_password@localhost:5432/smart_person_ai"
)

engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Redis 설정  
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
redis_client = redis.from_url(REDIS_URL)

# MongoDB 설정
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
mongodb_client = AsyncIOMotorClient(MONGODB_URL)
mongodb_db = mongodb_client.smart_person_ai

def get_db():
    """PostgreSQL 데이터베이스 세션 의존성"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_redis():
    """Redis 클라이언트 의존성"""
    return redis_client

def get_mongodb():
    """MongoDB 데이터베이스 의존성"""
    return mongodb_db