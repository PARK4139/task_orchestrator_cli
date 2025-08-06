"""
News analysis delivery API endpoint.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
import httpx
import logging

from shared.database import get_db
from core.ensure_config_loaded import ensure_config_loaded
from utils.ensure_exceptions_handled import ensure_exceptions_handled, ensure_service_response_valid

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/news/crawl")
@ensure_exceptions_handled
async def ensure_news_analysis_delivered(
    keywords: str,
    sources: Optional[str] = None,
    max_articles: int = 50,
    time_period: str = "1d",
    db: Session = Depends(get_db)
):
    """
    뉴스 분석을 확실히 제공합니다.
    """
    config = ensure_config_loaded()
    
    # News Analyzer 서비스로 요청 전달
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{config.news_analyzer_url}/news/crawl",
            params={
                "keywords": keywords,
                "sources": sources,
                "max_articles": max_articles,
                "time_period": time_period
            },
            timeout=60.0  # 뉴스 크롤링은 시간이 더 걸릴 수 있음
        )
        
        result = ensure_service_response_valid(response)
        logger.info(f"News analysis delivered for keywords: {keywords}")
        return result 