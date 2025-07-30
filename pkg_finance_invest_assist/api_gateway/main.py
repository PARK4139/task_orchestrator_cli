"""
FastAPI application for API Gateway.
"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from sqlalchemy.orm import Session
from typing import List
import httpx

from shared.database import get_db
from shared.config import settings
from shared.logging import get_logger

logger = get_logger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Finance Investment Assistant - API Gateway",
    description="API Gateway for finance investment assistant services",
    version="1.0.0"
)

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]
)


@app.get("/")
def ensure_root_endpoint_accessed():
    """Root endpoint for health check."""
    return {
        "message": "Finance Investment Assistant - API Gateway",
        "status": "healthy",
        "services": {
            "investment-advisor": "http://localhost:8001",
            "market-data": "http://localhost:8002",
            "news-analyzer": "http://localhost:8003"
        }
    }


@app.get("/health")
def ensure_health_check_accessed():
    """Health check endpoint."""
    return {"status": "healthy", "service": "api-gateway"}


@app.get("/api/v1/recommend/invest-timing")
async def ensure_invest_timing_gateway_accessed(
    asset_name: str,
    current_price: float = None,
    investment_amount: float = None,
    risk_tolerance: str = "medium",
    db: Session = Depends(get_db)
):
    """
    투자 타이밍 추천 게이트웨이 엔드포인트
    """
    try:
        # Forward request to recommendation engine
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8001/recommend/invest-timing",
                json={
                    "asset_name": asset_name,
                    "current_price": current_price,
                    "investment_amount": investment_amount,
                    "risk_tolerance": risk_tolerance
                }
            )
            return response.json()
    except Exception as e:
        logger.error(f"Error in invest timing gateway: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/v1/recommend/harvest-timing")
async def ensure_harvest_timing_gateway_accessed(
    asset_name: str,
    current_price: float,
    purchase_price: float,
    purchase_date: str,
    current_profit_rate: float = None,
    target_profit_rate: float = None,
    db: Session = Depends(get_db)
):
    """
    회수 타이밍 추천 게이트웨이 엔드포인트
    """
    try:
        # Forward request to recommendation engine
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8001/recommend/harvest-timing",
                json={
                    "asset_name": asset_name,
                    "current_price": current_price,
                    "purchase_price": purchase_price,
                    "purchase_date": purchase_date,
                    "current_profit_rate": current_profit_rate,
                    "target_profit_rate": target_profit_rate
                }
            )
            return response.json()
    except Exception as e:
        logger.error(f"Error in harvest timing gateway: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/v1/price/asset")
async def ensure_asset_price_gateway_accessed(
    asset_name: str,
    asset_type: str = "stock",
    symbol: str = None,
    db: Session = Depends(get_db)
):
    """
    자산 가격 조회 게이트웨이 엔드포인트
    """
    try:
        # Forward request to finance API client
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8002/price/asset",
                json={
                    "asset_name": asset_name,
                    "asset_type": asset_type,
                    "symbol": symbol
                }
            )
            return response.json()
    except Exception as e:
        logger.error(f"Error in asset price gateway: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/v1/news/crawl")
async def ensure_news_crawl_gateway_accessed(
    keywords: str,
    sources: str = None,
    max_articles: int = 50,
    time_period: str = "1d",
    db: Session = Depends(get_db)
):
    """
    뉴스 크롤링 게이트웨이 엔드포인트
    """
    try:
        # Parse keywords string to list
        keyword_list = [k.strip() for k in keywords.split(",")]
        source_list = [s.strip() for s in sources.split(",")] if sources else None
        
        # Forward request to news crawler
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8003/crawl/news",
                json={
                    "keywords": keyword_list,
                    "sources": source_list,
                    "max_articles": max_articles,
                    "time_period": time_period
                }
            )
            return response.json()
    except Exception as e:
        logger.error(f"Error in news crawl gateway: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 