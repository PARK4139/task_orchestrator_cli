"""
News analysis service.
"""
import numpy as np
from sqlalchemy.orm import Session
from typing import Dict, Any, List
from datetime import datetime

from models.schemas import (
    NewsAnalysisRequest, 
    NewsAnalysisResponse, 
    NewsAnalysisResult,
    SentimentType
)
from shared.logging import get_logger
from shared.config import settings

logger = get_logger(__name__)


def ensure_news_analyzed(
    request: NewsAnalysisRequest, 
    db: Session
) -> NewsAnalysisResponse:
    """
    뉴스 기사의 감정 분석을 수행합니다.
    
    Args:
        request: 뉴스 분석 요청 데이터
        db: 데이터베이스 세션
        
    Returns:
        NewsAnalysisResponse: 분석 결과
    """
    logger.info(f"Analyzing news for {len(request.article_ids)} articles")
    
    try:
        results = []
        
        # Analyze each article
        for article_id in request.article_ids:
            analysis_result = ensure_article_analyzed(
                article_id, request.analysis_type, db
            )
            results.append(analysis_result)
        
        # Calculate overall sentiment
        overall_sentiment = ensure_overall_sentiment_calculated(results)
        
        return NewsAnalysisResponse(
            analysis_type=request.analysis_type,
            total_analyzed=len(results),
            results=results,
            overall_sentiment=overall_sentiment,
            analysis_timestamp=datetime.now()
        )
        
    except Exception as e:
        logger.error(f"Error analyzing news: {e}")
        raise


def ensure_article_analyzed(
    article_id: str, 
    analysis_type: str, 
    db: Session
) -> NewsAnalysisResult:
    """Analyze a single article."""
    # TODO: Implement actual sentiment analysis
    # For now, return mock analysis
    import random
    
    # Mock sentiment analysis
    sentiments = [SentimentType.POSITIVE, SentimentType.NEUTRAL, SentimentType.NEGATIVE]
    sentiment = random.choice(sentiments)
    confidence = random.uniform(0.7, 0.95)
    
    # Mock keywords extraction
    keywords = ["투자", "시장", "경제", "주식", "금융"]
    selected_keywords = random.sample(keywords, random.randint(2, 4))
    
    # Mock summary
    summary = f"기사 {article_id}에 대한 요약 분석 결과입니다."
    
    return NewsAnalysisResult(
        article_id=article_id,
        sentiment=sentiment,
        confidence=confidence,
        keywords=selected_keywords,
        summary=summary if analysis_type == "summary" else None
    )


def ensure_overall_sentiment_calculated(results: List[NewsAnalysisResult]) -> SentimentType:
    """Calculate overall sentiment from multiple analysis results."""
    if not results:
        return SentimentType.NEUTRAL
    
    # Count sentiments
    sentiment_counts = {
        SentimentType.POSITIVE: 0,
        SentimentType.NEUTRAL: 0,
        SentimentType.NEGATIVE: 0
    }
    
    for result in results:
        sentiment_counts[result.sentiment] += 1
    
    # Return most common sentiment
    return max(sentiment_counts, key=sentiment_counts.get) 