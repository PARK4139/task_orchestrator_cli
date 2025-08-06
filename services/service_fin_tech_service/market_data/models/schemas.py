"""
Pydantic schemas for finance API client.
"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


class AssetType(str, Enum):
    """Asset types."""
    STOCK = "stock"
    INDEX = "index"
    CRYPTO = "crypto"
    FOREX = "forex"


class AssetPriceRequest(BaseModel):
    """Request schema for asset price."""
    asset_name: str = Field(..., description="자산명")
    asset_type: AssetType = Field(..., description="자산 유형")
    symbol: Optional[str] = Field(None, description="심볼 코드")
    
    class Config:
        schema_extra = {
            "example": {
                "asset_name": "삼성전자",
                "asset_type": "stock",
                "symbol": "005930.KS"
            }
        }


class AssetPriceResponse(BaseModel):
    """Response schema for asset price."""
    asset_name: str
    asset_type: AssetType
    symbol: str
    current_price: float
    previous_close: float
    change_amount: float
    change_percentage: float
    volume: int
    market_cap: Optional[float] = None
    timestamp: datetime = Field(default_factory=datetime.now)
    
    class Config:
        schema_extra = {
            "example": {
                "asset_name": "삼성전자",
                "asset_type": "stock",
                "symbol": "005930.KS",
                "current_price": 75000,
                "previous_close": 74500,
                "change_amount": 500,
                "change_percentage": 0.67,
                "volume": 15000000,
                "market_cap": 45000000000000,
                "timestamp": "2024-01-15T10:30:00"
            }
        }


class MarketDataRequest(BaseModel):
    """Request schema for market data."""
    market_index: str = Field(..., description="시장 지수명")
    data_type: str = Field(..., description="데이터 유형 (price, volume, volatility)")
    period: Optional[str] = Field("1d", description="기간")
    
    class Config:
        schema_extra = {
            "example": {
                "market_index": "KOSPI",
                "data_type": "price",
                "period": "1d"
            }
        }


class MarketDataResponse(BaseModel):
    """Response schema for market data."""
    market_index: str
    data_type: str
    current_value: float
    previous_value: float
    change_amount: float
    change_percentage: float
    volume: Optional[int] = None
    volatility: Optional[float] = None
    timestamp: datetime = Field(default_factory=datetime.now)
    
    class Config:
        schema_extra = {
            "example": {
                "market_index": "KOSPI",
                "data_type": "price",
                "current_value": 2500.5,
                "previous_value": 2480.2,
                "change_amount": 20.3,
                "change_percentage": 0.82,
                "volume": 500000000,
                "volatility": 1.2,
                "timestamp": "2024-01-15T10:30:00"
            }
        } 