"""
Market data retrieval API endpoint.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
import logging

from shared.database import get_db
from models.schemas import MarketDataRequest, MarketDataResponse
from services.ensure_market_data_service_running import ensure_market_data_service_running

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/market/data", response_model=MarketDataResponse)
async def ensure_market_data_retrieved(
    market_name: str = "KOSPI",
    data_type: str = "index",
    period: str = "1d",
    db: Session = Depends(get_db)
):
    """
    시장 데이터를 확실히 조회합니다.
    """
    try:
        request = MarketDataRequest(
            market_name=market_name,
            data_type=data_type,
            period=period
        )
        
        result = ensure_market_data_service_running(request, db)
        logger.info(f"Market data retrieved for {market_name}")
        return result
    except Exception as e:
        logger.error(f"Error in market data retrieval: {e}")
        raise HTTPException(status_code=500, detail=str(e)) 