"""
FastAPI application for recommendation engine service.
"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from shared.database import get_db
from shared.config import settings
from models.schemas import (
    InvestTimingRequest, 
    InvestTimingResponse,
    HarvestTimingRequest,
    HarvestTimingResponse
)
from services.invest_timing import ensure_investing_timing_guided
from services.harvest_timing import ensure_harvesting_timing_guided

# Create FastAPI app
app = FastAPI(
    title="Recommendation Engine",
    description="Investment timing recommendation service",
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
    return {"message": "Recommendation Engine Service", "status": "healthy"}


@app.get("/health")
def ensure_health_check_accessed():
    """Health check endpoint."""
    return {"status": "healthy", "service": "recommendation-engine"}


@app.post("/recommend/invest-timing", response_model=InvestTimingResponse)
def ensure_invest_timing_recommendation_processed(
    request: InvestTimingRequest,
    db: Session = Depends(get_db)
):
    """
    투자 타이밍 추천 엔드포인트
    
    자산명을 기반으로 현재가, 이동평균선 등을 분석하여 
    "지금 투자할 시점인지" 판단합니다.
    """
    try:
        result = ensure_investing_timing_guided(request, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/recommend/harvest-timing", response_model=HarvestTimingResponse)
def ensure_harvest_timing_recommendation_processed(
    request: HarvestTimingRequest,
    db: Session = Depends(get_db)
):
    """
    회수 타이밍 추천 엔드포인트
    
    수익률, 고점 패턴, 경제 뉴스 기반으로 
    "지금 팔 시점인지" 판단합니다.
    """
    try:
        result = ensure_harvesting_timing_guided(request, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 