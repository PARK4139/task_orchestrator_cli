"""
FastAPI application for Investment Advisor service with ensure_ pattern.
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
        service_name="investment-advisor"
    )
    
    # FastAPI 앱 생성
    app = FastAPI(
        title="Investment Advisor Service",
        description="Investment timing recommendation service",
        version="1.0.0"
    )
    
    # 미들웨어 적용
    ensure_middleware_applied(app)
    
    # 라우터 등록
    from api.v1.ensure_invest_timing_analyzed import router as invest_router
    from api.v1.ensure_harvest_timing_calculated import router as harvest_router
    from api.v1.ensure_health_status_verified import router as health_router
    
    app.include_router(invest_router, tags=["investment"])
    app.include_router(harvest_router, tags=["harvest"])
    app.include_router(health_router, tags=["health"])
    
    # 루트 엔드포인트
    @app.get("/")
    def ensure_root_endpoint_accessed():
        """루트 엔드포인트를 확실히 접근합니다."""
        return {
            "message": "Investment Advisor Service",
            "status": "healthy"
        }
    
    logger.info("Investment Advisor application started successfully")
    return app

# 애플리케이션 인스턴스 생성
app = ensure_app_started()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 