"""
Pydantic schemas for news crawler.
"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


class SentimentType(str, Enum):
    """Sentiment types."""
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


class NewsCrawlRequest(BaseModel):
    """Request schema for news crawling."""
    keywords: List[str] = Field(..., description="검색 키워드 목록")
    sources: Optional[List[str]] = Field(None, description="뉴스 소스 목록")
    max_articles: Optional[int] = Field(50, description="최대 기사 수")
    time_period: Optional[str] = Field("1d", description="검색 기간")
    
    class Config:
        schema_extra = {
            "example": {
                "keywords": ["삼성전자", "반도체", "투자"],
                "sources": ["네이버뉴스", "다음뉴스"],
                "max_articles": 50,
                "time_period": "1d"
            }
        }


class NewsArticle(BaseModel):
    """News article schema."""
    title: str
    content: str
    url: str
    source: str
    published_at: datetime
    sentiment: Optional[SentimentType] = None
    keywords: List[str] = []


class NewsCrawlResponse(BaseModel):
    """Response schema for news crawling."""
    keywords: List[str]
    total_articles: int
    articles: List[NewsArticle]
    crawl_timestamp: datetime = Field(default_factory=datetime.now)
    
    class Config:
        schema_extra = {
            "example": {
                "keywords": ["삼성전자", "반도체"],
                "total_articles": 25,
                "articles": [
                    {
                        "title": "삼성전자, 반도체 시장 회복세",
                        "content": "삼성전자가 반도체 시장 회복세를 보이고 있다...",
                        "url": "https://example.com/news/1",
                        "source": "네이버뉴스",
                        "published_at": "2024-01-15T10:30:00",
                        "sentiment": "positive",
                        "keywords": ["삼성전자", "반도체", "회복"]
                    }
                ],
                "crawl_timestamp": "2024-01-15T10:30:00"
            }
        }


class NewsAnalysisRequest(BaseModel):
    """Request schema for news analysis."""
    article_ids: List[str] = Field(..., description="분석할 기사 ID 목록")
    analysis_type: str = Field("sentiment", description="분석 유형 (sentiment, keywords, summary)")
    
    class Config:
        schema_extra = {
            "example": {
                "article_ids": ["article_1", "article_2"],
                "analysis_type": "sentiment"
            }
        }


class NewsAnalysisResult(BaseModel):
    """News analysis result schema."""
    article_id: str
    sentiment: SentimentType
    confidence: float
    keywords: List[str]
    summary: Optional[str] = None


class NewsAnalysisResponse(BaseModel):
    """Response schema for news analysis."""
    analysis_type: str
    total_analyzed: int
    results: List[NewsAnalysisResult]
    overall_sentiment: SentimentType
    analysis_timestamp: datetime = Field(default_factory=datetime.now)
    
    class Config:
        schema_extra = {
            "example": {
                "analysis_type": "sentiment",
                "total_analyzed": 2,
                "results": [
                    {
                        "article_id": "article_1",
                        "sentiment": "positive",
                        "confidence": 0.85,
                        "keywords": ["삼성전자", "반도체", "회복"],
                        "summary": "삼성전자의 반도체 시장 회복세에 대한 긍정적 뉴스"
                    }
                ],
                "overall_sentiment": "positive",
                "analysis_timestamp": "2024-01-15T10:30:00"
            }
        } 