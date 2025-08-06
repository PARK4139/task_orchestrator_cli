"""
FastAPI application for Market Data service with ensure_ pattern.
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
        service_name="market-data"
    )
    
    # FastAPI 앱 생성
    app = FastAPI(
        title="Market Data Service",
        description="Financial market data service",
        version="1.0.0"
    )
    
    # 미들웨어 적용
    ensure_middleware_applied(app)
    
    # 라우터 등록
    from api.v1.ensure_price_data_fetched import router as price_router
    from api.v1.ensure_market_data_retrieved import router as market_router
    from api.v1.ensure_health_status_confirmed import router as health_router
    
    app.include_router(price_router, tags=["price"])
    app.include_router(market_router, tags=["market"])
    app.include_router(health_router, tags=["health"])
    
    # 루트 엔드포인트
    @app.get("/")
    def ensure_root_endpoint_accessed():
        """루트 엔드포인트를 확실히 접근합니다."""
        return {
            "message": "Market Data Service",
            "status": "healthy"
        }
    
    logger.info("Market Data application started successfully")
    return app

# 애플리케이션 인스턴스 생성
app = ensure_app_started()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002) 