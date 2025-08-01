"""
Harvest timing calculation API endpoint.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
import logging

from shared.database import get_db
from models.schemas import HarvestTimingRequest, HarvestTimingResponse
from services.ensure_harvest_timing_calculated import ensure_harvest_timing_calculated

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/recommend/harvest-timing", response_model=HarvestTimingResponse)
async def ensure_harvest_timing_calculated_endpoint(
    request: HarvestTimingRequest,
    db: Session = Depends(get_db)
):
    """
    회수 타이밍 계산을 확실히 수행합니다.
    """
    try:
        result = ensure_harvest_timing_calculated(request, db)
        logger.info(f"Harvest timing calculation completed for {request.asset_name}")
        return result
    except Exception as e:
        logger.error(f"Error in harvest timing calculation: {e}")
        raise HTTPException(status_code=500, detail=str(e)) 