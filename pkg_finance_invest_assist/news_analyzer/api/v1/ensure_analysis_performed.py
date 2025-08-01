"""
News analysis API endpoint.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
import logging

from shared.database import get_db
from models.schemas import NewsAnalysisRequest, NewsAnalysisResponse
from services.ensure_analysis_service_running import ensure_analysis_service_running

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/news/analyze", response_model=NewsAnalysisResponse)
async def ensure_analysis_performed(
    request: NewsAnalysisRequest,
    db: Session = Depends(get_db)
):
    """
    뉴스 분석을 확실히 수행합니다.
    """
    try:
        result = ensure_analysis_service_running(request, db)
        logger.info(f"News analysis performed for {request.analysis_type}")
        return result
    except Exception as e:
        logger.error(f"Error in news analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e)) 