"""
Harvest timing analysis service.
"""
import numpy as np
from sqlalchemy.orm import Session
from typing import Dict, Any
from datetime import datetime, timedelta

from models.schemas import (
    HarvestTimingRequest, 
    HarvestTimingResponse,
    RecommendationType,
    ConfidenceLevel
)
from shared.logging import get_logger

logger = get_logger(__name__)


def ensure_harvesting_timing_guided(
    request: HarvestTimingRequest, 
    db: Session
) -> HarvestTimingResponse:
    """
    회수 타이밍을 분석하여 추천을 제공합니다.
    
    Args:
        request: 회수 타이밍 요청 데이터
        db: 데이터베이스 세션
        
    Returns:
        HarvestTimingResponse: 회수 타이밍 추천 결과
    """
    logger.info(f"Analyzing harvest timing for asset: {request.asset_name}")
    
    try:
        # Calculate current profit rate if not provided
        current_profit_rate = request.current_profit_rate or ensure_profit_rate_calculated(
            request.current_price, request.purchase_price
        )
        
        # Analyze market conditions
        market_analysis = ensure_market_conditions_analyzed(request.asset_name, db)
        
        # Analyze profit patterns
        profit_analysis = ensure_profit_patterns_analyzed(
            current_profit_rate, request.target_profit_rate, request.purchase_date
        )
        
        # Generate recommendation
        recommendation, confidence, reasoning = ensure_harvest_recommendation_generated(
            current_profit_rate, market_analysis, profit_analysis
        )
        
        # Generate suggested action
        suggested_action = ensure_harvest_action_generated(
            recommendation, confidence, current_profit_rate, request.target_profit_rate
        )
        
        return HarvestTimingResponse(
            asset_name=request.asset_name,
            current_price=request.current_price,
            purchase_price=request.purchase_price,
            current_profit_rate=current_profit_rate,
            recommendation=recommendation,
            confidence=confidence,
            reasoning=reasoning,
            market_analysis=market_analysis,
            profit_analysis=profit_analysis,
            suggested_action=suggested_action
        )
        
    except Exception as e:
        logger.error(f"Error in harvest timing analysis: {e}")
        raise


def ensure_profit_rate_calculated(current_price: float, purchase_price: float) -> float:
    """Calculate current profit rate."""
    return ((current_price - purchase_price) / purchase_price) * 100


def ensure_market_conditions_analyzed(asset_name: str, db: Session) -> Dict[str, Any]:
    """Analyze current market conditions."""
    # TODO: Implement actual market analysis
    # For now, return mock analysis
    return {
        "trend": "upward",
        "volume": "increasing",
        "news_sentiment": "positive",
        "market_volatility": "medium",
        "sector_performance": "strong"
    }


def ensure_profit_patterns_analyzed(
    current_profit_rate: float,
    target_profit_rate: float,
    purchase_date: datetime
) -> Dict[str, Any]:
    """Analyze profit patterns and trends."""
    remaining_gap = target_profit_rate - current_profit_rate
    holding_period = (datetime.now() - purchase_date).days
    
    # Calculate risk-reward ratio
    risk_reward_ratio = 1.0  # TODO: Implement actual calculation
    
    return {
        "target_profit_rate": target_profit_rate,
        "remaining_gap": remaining_gap,
        "holding_period_days": holding_period,
        "risk_reward_ratio": risk_reward_ratio,
        "profit_trend": "stable" if current_profit_rate > 0 else "declining"
    }


def ensure_harvest_recommendation_generated(
    current_profit_rate: float,
    market_analysis: Dict[str, Any],
    profit_analysis: Dict[str, Any]
) -> tuple[RecommendationType, ConfidenceLevel, str]:
    """Generate harvest recommendation based on analysis."""
    
    target_profit_rate = profit_analysis.get("target_profit_rate", 0)
    remaining_gap = profit_analysis.get("remaining_gap", 0)
    market_trend = market_analysis.get("trend", "neutral")
    news_sentiment = market_analysis.get("news_sentiment", "neutral")
    
    # Decision logic
    if current_profit_rate >= target_profit_rate:
        if market_trend == "upward" and news_sentiment == "positive":
            recommendation = RecommendationType.HOLD
            confidence = ConfidenceLevel.HIGH
            reasoning = "목표 수익률 달성했으나 시장 동향이 긍정적"
        else:
            recommendation = RecommendationType.SELL
            confidence = ConfidenceLevel.HIGH
            reasoning = "목표 수익률 달성으로 매도 권장"
    elif current_profit_rate >= target_profit_rate * 0.8:  # 80% of target
        if market_trend == "upward":
            recommendation = RecommendationType.HOLD
            confidence = ConfidenceLevel.MEDIUM
            reasoning = "목표 수익률에 근접했으며 시장 동향이 긍정적"
        else:
            recommendation = RecommendationType.SELL
            confidence = ConfidenceLevel.MEDIUM
            reasoning = "목표 수익률에 근접했으나 시장 동향이 불안정"
    elif current_profit_rate < 0:
        if market_trend == "downward":
            recommendation = RecommendationType.SELL
            confidence = ConfidenceLevel.HIGH
            reasoning = "손실 상태이며 시장 하락으로 인한 추가 손실 위험"
        else:
            recommendation = RecommendationType.HOLD
            confidence = ConfidenceLevel.LOW
            reasoning = "손실 상태이나 시장 회복 기대"
    else:
        recommendation = RecommendationType.HOLD
        confidence = ConfidenceLevel.LOW
        reasoning = "수익률이 목표에 미달하여 관망 권장"
    
    return recommendation, confidence, reasoning


def ensure_harvest_action_generated(
    recommendation: RecommendationType,
    confidence: ConfidenceLevel,
    current_profit_rate: float,
    target_profit_rate: float
) -> str:
    """Generate suggested harvest action."""
    if recommendation == RecommendationType.SELL:
        if confidence == ConfidenceLevel.HIGH:
            return "즉시 매도 권장"
        else:
            return "분할 매도 고려"
    elif recommendation == RecommendationType.HOLD:
        if current_profit_rate >= target_profit_rate * 0.9:
            return "목표 수익률 도달 시 매도 준비"
        else:
            return "추가 상승 기대하며 관망"
    else:
        return "시장 상황 모니터링" 