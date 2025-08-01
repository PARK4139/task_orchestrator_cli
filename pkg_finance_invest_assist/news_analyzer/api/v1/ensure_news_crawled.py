"""
News crawling API endpoint.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
import logging

from shared.database import get_db
from models.schemas import NewsCrawlRequest, NewsCrawlResponse
from services.ensure_crawler_service_operating import ensure_crawler_service_operating

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/news/crawl", response_model=NewsCrawlResponse)
async def ensure_news_crawled(
    keywords: str,
    sources: Optional[str] = None,
    max_articles: int = 50,
    time_period: str = "1d",
    db: Session = Depends(get_db)
):
    """
    뉴스를 확실히 크롤링합니다.
    """
    try:
        request = NewsCrawlRequest(
            keywords=keywords,
            sources=sources,
            max_articles=max_articles,
            time_period=time_period
        )
        
        result = ensure_crawler_service_operating(request, db)
        logger.info(f"News crawled for keywords: {keywords}")
        return result
    except Exception as e:
        logger.error(f"Error in news crawling: {e}")
        raise HTTPException(status_code=500, detail=str(e)) 