"""
Health status validation API endpoint.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import logging
from typing import Dict, Any

from shared.database import get_db

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health")
async def ensure_health_status_validated(db: Session = Depends(get_db)) -> Dict[str, Any]:
    """
    News Analyzer 서비스 헬스 상태를 확실히 확인합니다.
    """
    try:
        # 데이터베이스 연결 확인
        db.execute("SELECT 1")
        
        logger.info("News Analyzer health check completed successfully")
        
        return {
            "status": "healthy",
            "service": "news-analyzer",
            "timestamp": "2024-01-15T10:30:00Z"
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {
            "status": "unhealthy",
            "service": "news-analyzer",
            "error": str(e),
            "timestamp": "2024-01-15T10:30:00Z"
        } 