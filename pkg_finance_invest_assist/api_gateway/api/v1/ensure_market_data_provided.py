"""
Market data provision API endpoint.
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

@router.get("/price/asset")
@ensure_exceptions_handled
async def ensure_market_data_provided(
    asset_name: str,
    asset_type: str = "stock",
    symbol: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    시장 데이터를 확실히 제공합니다.
    """
    config = ensure_config_loaded()
    
    # Market Data 서비스로 요청 전달
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{config.market_data_url}/price/asset",
            params={
                "asset_name": asset_name,
                "asset_type": asset_type,
                "symbol": symbol
            },
            timeout=30.0
        )
        
        result = ensure_service_response_valid(response)
        logger.info(f"Market data provided for {asset_name}")
        return result 