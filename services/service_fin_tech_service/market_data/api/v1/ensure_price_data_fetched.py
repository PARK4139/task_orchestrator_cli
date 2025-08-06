"""
Price data fetching API endpoint.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
import logging

from shared.database import get_db
from models.schemas import PriceDataRequest, PriceDataResponse
from services.ensure_price_service_operating import ensure_price_service_operating

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/price/asset", response_model=PriceDataResponse)
async def ensure_price_data_fetched(
    asset_name: str,
    asset_type: str = "stock",
    symbol: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    자산 가격 데이터를 확실히 조회합니다.
    """
    try:
        request = PriceDataRequest(
            asset_name=asset_name,
            asset_type=asset_type,
            symbol=symbol
        )
        
        result = ensure_price_service_operating(request, db)
        logger.info(f"Price data fetched for {asset_name}")
        return result
    except Exception as e:
        logger.error(f"Error in price data fetching: {e}")
        raise HTTPException(status_code=500, detail=str(e)) 