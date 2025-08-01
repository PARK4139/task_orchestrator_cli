"""
Investment timing recommendation API endpoint.
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

@router.get("/recommend/invest-timing")
@ensure_exceptions_handled
async def ensure_invest_timing_recommended(
    asset_name: str,
    current_price: Optional[float] = None,
    investment_amount: Optional[float] = None,
    risk_tolerance: str = "medium",
    db: Session = Depends(get_db)
):
    """
    투자 타이밍 추천을 확실히 제공합니다.
    """
    config = ensure_config_loaded()
    
    # Investment Advisor 서비스로 요청 전달
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{config.investment_advisor_url}/recommend/invest-timing",
            json={
                "asset_name": asset_name,
                "current_price": current_price,
                "investment_amount": investment_amount,
                "risk_tolerance": risk_tolerance
            },
            timeout=30.0
        )
        
        result = ensure_service_response_valid(response)
        logger.info(f"Investment timing recommendation provided for {asset_name}")
        return result 