"""
Pydantic schemas for recommendation engine API.
"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


class RecommendationType(str, Enum):
    """Recommendation types."""
    BUY = "buy"
    SELL = "sell"
    HOLD = "hold"


class ConfidenceLevel(str, Enum):
    """Confidence levels for recommendations."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class InvestTimingRequest(BaseModel):
    """Request schema for investment timing recommendation."""
    asset_name: str = Field(..., description="자산명 (예: 삼성전자, KOSPI)")
    current_price: Optional[float] = Field(None, description="현재 가격")
    investment_amount: Optional[float] = Field(None, description="투자 금액")
    risk_tolerance: Optional[str] = Field("medium", description="위험 성향 (low/medium/high)")
    
    class Config:
        schema_extra = {
            "example": {
                "asset_name": "삼성전자",
                "current_price": 75000,
                "investment_amount": 1000000,
                "risk_tolerance": "medium"
            }
        }


class InvestTimingResponse(BaseModel):
    """Response schema for investment timing recommendation."""
    asset_name: str
    current_price: float
    recommendation: RecommendationType
    confidence: ConfidenceLevel
    reasoning: str
    technical_indicators: dict
    risk_assessment: str
    suggested_action: str
    timestamp: datetime = Field(default_factory=datetime.now)
    
    class Config:
        schema_extra = {
            "example": {
                "asset_name": "삼성전자",
                "current_price": 75000,
                "recommendation": "buy",
                "confidence": "medium",
                "reasoning": "이동평균선이 상승 추세이며, RSI가 적정 구간에 위치",
                "technical_indicators": {
                    "ma_20": 73000,
                    "ma_50": 71000,
                    "rsi": 65
                },
                "risk_assessment": "보통",
                "suggested_action": "분할 매수 권장",
                "timestamp": "2024-01-15T10:30:00"
            }
        }


class HarvestTimingRequest(BaseModel):
    """Request schema for harvest timing recommendation."""
    asset_name: str = Field(..., description="자산명")
    current_price: float = Field(..., description="현재 가격")
    purchase_price: float = Field(..., description="매수 가격")
    purchase_date: datetime = Field(..., description="매수 날짜")
    current_profit_rate: Optional[float] = Field(None, description="현재 수익률")
    target_profit_rate: Optional[float] = Field(None, description="목표 수익률")
    
    class Config:
        schema_extra = {
            "example": {
                "asset_name": "삼성전자",
                "current_price": 80000,
                "purchase_price": 70000,
                "purchase_date": "2024-01-01T00:00:00",
                "current_profit_rate": 14.3,
                "target_profit_rate": 20.0
            }
        }


class HarvestTimingResponse(BaseModel):
    """Response schema for harvest timing recommendation."""
    asset_name: str
    current_price: float
    purchase_price: float
    current_profit_rate: float
    recommendation: RecommendationType
    confidence: ConfidenceLevel
    reasoning: str
    market_analysis: dict
    profit_analysis: dict
    suggested_action: str
    timestamp: datetime = Field(default_factory=datetime.now)
    
    class Config:
        schema_extra = {
            "example": {
                "asset_name": "삼성전자",
                "current_price": 80000,
                "purchase_price": 70000,
                "current_profit_rate": 14.3,
                "recommendation": "hold",
                "confidence": "high",
                "reasoning": "목표 수익률에 근접했으나 시장 동향이 긍정적",
                "market_analysis": {
                    "trend": "upward",
                    "volume": "increasing",
                    "news_sentiment": "positive"
                },
                "profit_analysis": {
                    "target_profit_rate": 20.0,
                    "remaining_gap": 5.7,
                    "risk_reward_ratio": 1.2
                },
                "suggested_action": "목표 수익률 도달 시 분할 매도",
                "timestamp": "2024-01-15T10:30:00"
            }
        }


class ErrorResponse(BaseModel):
    """Error response schema."""
    error: str
    detail: str
    timestamp: datetime = Field(default_factory=datetime.now) 