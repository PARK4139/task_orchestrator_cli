"""
FastAPI application for finance API client service.
"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from shared.database import get_db
from sqlalchemy.orm import Session

from models.schemas import (
    AssetPriceRequest,
    AssetPriceResponse,
    MarketDataRequest,
    MarketDataResponse
)
from services.market_data_service import ensure_market_data_fetched
from services.price_service import ensure_asset_price_fetched

# Create FastAPI app
app = FastAPI(
    title="Finance API Client",
    description="External finance API integration service",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def ensure_root_endpoint_accessed():
    """Root endpoint for health check."""
    return {"message": "Finance API Client Service", "status": "healthy"}


@app.get("/health")
def ensure_health_check_accessed():
    """Health check endpoint."""
    return {"status": "healthy", "service": "finance-api-client"}


@app.post("/price/asset", response_model=AssetPriceResponse)
def ensure_asset_price_request_processed(
        request: AssetPriceRequest,
        db: Session = Depends(get_db)
):
    """
    자산 가격 조회 엔드포인트
    
    외부 금융 API를 통해 실시간 자산 가격을 조회합니다.
    """
    try:
        result = ensure_asset_price_fetched(request, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/market/data", response_model=MarketDataResponse)
def ensure_market_data_request_processed(
        request: MarketDataRequest,
        db: Session = Depends(get_db)
):
    """
    시장 데이터 조회 엔드포인트
    
    시장 지수, 거래량, 변동성 등의 시장 데이터를 조회합니다.
    """
    try:
        result = ensure_market_data_fetched(request, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8002)
