"""
Investment timing analysis API endpoint.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
import logging

from shared.database import get_db
from models.schemas import InvestTimingRequest, InvestTimingResponse
from services.ensure_invest_timing_analyzed import ensure_invest_timing_analyzed

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/recommend/invest-timing", response_model=InvestTimingResponse)
async def ensure_invest_timing_analyzed_endpoint(
    request: InvestTimingRequest,
    db: Session = Depends(get_db)
):
    """
    투자 타이밍 분석을 확실히 수행합니다.
    """
    try:
        result = ensure_invest_timing_analyzed(request, db)
        logger.info(f"Investment timing analysis completed for {request.asset_name}")
        return result
    except Exception as e:
        logger.error(f"Error in investment timing analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e)) 