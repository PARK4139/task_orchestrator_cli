"""
Health status check API endpoint.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import httpx
import logging
from typing import Dict, Any

from shared.database import get_db
from core.ensure_config_loaded import ensure_config_loaded

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health")
async def ensure_health_status_checked(db: Session = Depends(get_db)) -> Dict[str, Any]:
    """
    API Gateway 헬스 상태를 확실히 확인합니다.
    """
    config = ensure_config_loaded()
    
    # 각 마이크로서비스의 헬스 상태 확인
    services_status = {}
    
    try:
        # Investment Advisor 서비스 상태 확인
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{config.investment_advisor_url}/health", timeout=5.0)
            services_status["investment_advisor"] = "healthy" if response.status_code == 200 else "unhealthy"
    except Exception as e:
        logger.warning(f"Investment Advisor service health check failed: {e}")
        services_status["investment_advisor"] = "unhealthy"
    
    try:
        # Market Data 서비스 상태 확인
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{config.market_data_url}/health", timeout=5.0)
            services_status["market_data"] = "healthy" if response.status_code == 200 else "unhealthy"
    except Exception as e:
        logger.warning(f"Market Data service health check failed: {e}")
        services_status["market_data"] = "unhealthy"
    
    try:
        # News Analyzer 서비스 상태 확인
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{config.news_analyzer_url}/health", timeout=5.0)
            services_status["news_analyzer"] = "healthy" if response.status_code == 200 else "unhealthy"
    except Exception as e:
        logger.warning(f"News Analyzer service health check failed: {e}")
        services_status["news_analyzer"] = "unhealthy"
    
    # 전체 상태 결정
    overall_status = "healthy" if all(status == "healthy" for status in services_status.values()) else "degraded"
    
    logger.info(f"Health status checked - Overall: {overall_status}")
    
    return {
        "status": overall_status,
        "service": "api-gateway",
        "services": services_status,
        "timestamp": "2024-01-15T10:30:00Z"  # 실제로는 현재 시간 사용
    } 