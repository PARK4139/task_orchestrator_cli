"""
FastAPI application for news crawler service.
"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from shared.database import get_db
from shared.config import settings
from models.schemas import (
    NewsCrawlRequest,
    NewsCrawlResponse,
    NewsAnalysisRequest,
    NewsAnalysisResponse
)
from services.crawler_service import ensure_news_crawled
from services.analysis_service import ensure_news_analyzed

# Create FastAPI app
app = FastAPI(
    title="News Crawler",
    description="Financial news crawling and analysis service",
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
    return {"message": "News Crawler Service", "status": "healthy"}


@app.get("/health")
def ensure_health_check_accessed():
    """Health check endpoint."""
    return {"status": "healthy", "service": "news-crawler"}


@app.post("/crawl/news", response_model=NewsCrawlResponse)
def ensure_news_crawl_request_processed(
    request: NewsCrawlRequest,
    db: Session = Depends(get_db)
):
    """
    뉴스 크롤링 엔드포인트
    
    지정된 키워드로 금융 뉴스를 크롤링합니다.
    """
    try:
        result = ensure_news_crawled(request, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/analyze/news", response_model=NewsAnalysisResponse)
def ensure_news_analysis_request_processed(
    request: NewsAnalysisRequest,
    db: Session = Depends(get_db)
):
    """
    뉴스 분석 엔드포인트
    
    크롤링된 뉴스의 감정 분석을 수행합니다.
    """
    try:
        result = ensure_news_analyzed(request, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003) 