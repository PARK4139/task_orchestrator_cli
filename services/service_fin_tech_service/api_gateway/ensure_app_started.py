"""
FastAPI application for API Gateway with ensure_ pattern.
"""
from fastapi import FastAPI
import logging

from core.ensure_config_loaded import ensure_config_loaded
from core.ensure_middleware_applied import ensure_middleware_applied
from utils.ensure_logging_configured import ensure_logging_configured

def ensure_app_started() -> FastAPI:
    """
    FastAPI 애플리케이션을 확실히 시작합니다.
    """
    # 설정 로드
    config = ensure_config_loaded()
    
    # 로깅 설정
    logger = ensure_logging_configured(
        log_level=config.log_level,
        service_name="api-gateway"
    )
    
    # FastAPI 앱 생성
    app = FastAPI(
        title="Finance Investment Assistant - API Gateway",
        description="API Gateway for finance investment assistant services",
        version="1.0.0"
    )
    
    # 미들웨어 적용
    ensure_middleware_applied(
        app, 
        cors_origins=config.cors_origins,
        trusted_hosts=config.trusted_hosts
    )
    
    # 라우터 등록
    from api.v1.ensure_invest_timing_recommended import router as invest_router
    from api.v1.ensure_market_data_provided import router as market_router
    from api.v1.ensure_news_analysis_delivered import router as news_router
    from api.v1.ensure_health_status_checked import router as health_router
    
    app.include_router(invest_router, prefix="/api/v1", tags=["investment"])
    app.include_router(market_router, prefix="/api/v1", tags=["market"])
    app.include_router(news_router, prefix="/api/v1", tags=["news"])
    app.include_router(health_router, prefix="/api/v1", tags=["health"])
    
    # 루트 엔드포인트
    @app.get("/")
    def ensure_root_endpoint_accessed():
        """루트 엔드포인트를 확실히 접근합니다."""
        return {
            "message": "Finance Investment Assistant - API Gateway",
            "status": "healthy",
            "services": {
                "investment-advisor": config.investment_advisor_url,
                "market-data": config.market_data_url,
                "news-analyzer": config.news_analyzer_url
            }
        }
    
    logger.info("API Gateway application started successfully")
    return app

# 애플리케이션 인스턴스 생성
app = ensure_app_started() 