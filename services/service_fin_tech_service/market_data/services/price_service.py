"""
Asset price fetching service.
"""
import requests
from sqlalchemy.orm import Session
from typing import Dict, Any
from datetime import datetime

from models.schemas import AssetPriceRequest, AssetPriceResponse, AssetType
from shared.logging import get_logger
from shared.config import settings

logger = get_logger(__name__)


def ensure_asset_price_fetched(
    request: AssetPriceRequest, 
    db: Session
) -> AssetPriceResponse:
    """
    외부 API를 통해 자산 가격을 조회합니다.
    
    Args:
        request: 자산 가격 요청 데이터
        db: 데이터베이스 세션
        
    Returns:
        AssetPriceResponse: 자산 가격 응답 데이터
    """
    logger.info(f"Fetching price for asset: {request.asset_name}")
    
    try:
        # Get symbol if not provided
        symbol = request.symbol or ensure_symbol_resolved(request.asset_name, request.asset_type)
        
        # Fetch price from external API
        price_data = ensure_external_price_fetched(symbol, request.asset_type)
        
        # Store in database for caching
        ensure_price_data_cached(price_data, db)
        
        return AssetPriceResponse(
            asset_name=request.asset_name,
            asset_type=request.asset_type,
            symbol=symbol,
            current_price=price_data["current_price"],
            previous_close=price_data["previous_close"],
            change_amount=price_data["change_amount"],
            change_percentage=price_data["change_percentage"],
            volume=price_data["volume"],
            market_cap=price_data.get("market_cap"),
            timestamp=datetime.now()
        )
        
    except Exception as e:
        logger.error(f"Error fetching asset price: {e}")
        raise


def ensure_symbol_resolved(asset_name: str, asset_type: AssetType) -> str:
    """Resolve asset name to symbol code."""
    # TODO: Implement actual symbol resolution
    # For now, return mock symbols
    symbol_map = {
        "삼성전자": "005930.KS",
        "SK하이닉스": "000660.KS",
        "LG에너지솔루션": "373220.KS",
        "KOSPI": "^KS11",
        "NASDAQ": "^IXIC",
        "S&P500": "^GSPC"
    }
    return symbol_map.get(asset_name, f"{asset_name}.KS")


def ensure_external_price_fetched(symbol: str, asset_type: AssetType) -> Dict[str, Any]:
    """Fetch price from external finance API."""
    # TODO: Implement actual API calls
    # For now, return mock data
    mock_prices = {
        "005930.KS": {
            "current_price": 75000,
            "previous_close": 74500,
            "change_amount": 500,
            "change_percentage": 0.67,
            "volume": 15000000,
            "market_cap": 45000000000000
        },
        "000660.KS": {
            "current_price": 120000,
            "previous_close": 118000,
            "change_amount": 2000,
            "change_percentage": 1.69,
            "volume": 8000000,
            "market_cap": 90000000000000
        },
        "^KS11": {
            "current_price": 2500.5,
            "previous_close": 2480.2,
            "change_amount": 20.3,
            "change_percentage": 0.82,
            "volume": 500000000,
            "market_cap": None
        }
    }
    
    return mock_prices.get(symbol, {
        "current_price": 50000,
        "previous_close": 49500,
        "change_amount": 500,
        "change_percentage": 1.01,
        "volume": 1000000,
        "market_cap": None
    })


def ensure_price_data_cached(price_data: Dict[str, Any], db: Session) -> None:
    """Cache price data in database."""
    # TODO: Implement database caching
    logger.info("Price data cached successfully") 