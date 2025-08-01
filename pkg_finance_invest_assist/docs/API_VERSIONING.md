# API Versioning Strategy

## 🎯 API 버전 관리 전략

### 현재 구조
```
api_gateway/
├── api/
│   ├── v1/                    # 현재 안정 버전
│   │   ├── recommend.py
│   │   ├── market.py
│   │   └── news.py
│   ├── v2/                    # 개발 중인 새 버전
│   │   ├── recommend.py
│   │   ├── market.py
│   │   └── news.py
│   └── __init__.py
```

## 📊 버전별 기능 비교

### v1 (현재 버전)
```python
# 투자 타이밍 추천 API v1
@app.get("/api/v1/recommend/invest-timing")
def get_invest_timing_v1(
    asset_name: str,
    current_price: float = None
):
    """
    기본 투자 타이밍 추천
    - 기술적 지표 기반
    - 단순한 buy/sell/hold 추천
    """
    return {
        "recommendation": "buy",
        "confidence": 0.7,
        "reason": "RSI oversold condition"
    }
```

### v2 (개발 중)
```python
# 투자 타이밍 추천 API v2
@app.get("/api/v2/recommend/invest-timing")
def get_invest_timing_v2(
    asset_name: str,
    current_price: float = None,
    risk_tolerance: str = "medium",
    include_sentiment: bool = False,
    include_news_analysis: bool = False
):
    """
    고급 투자 타이밍 추천
    - 기술적 지표 + 뉴스 감정 분석
    - 리스크 프로파일 기반
    - 상세한 분석 결과
    """
    return {
        "recommendation": "buy",
        "confidence": 0.8,
        "risk_level": "moderate",
        "technical_indicators": {
            "rsi": 25.5,
            "macd": "bullish",
            "moving_averages": "golden_cross"
        },
        "sentiment_analysis": {
            "overall_sentiment": "positive",
            "sentiment_score": 0.6,
            "news_count": 15
        },
        "risk_assessment": {
            "volatility": "medium",
            "market_risk": "low",
            "recommended_position_size": "25%"
        }
    }
```

## 🔄 버전 마이그레이션 전략

### 1. **점진적 마이그레이션**
```python
# 라우터 설정
from fastapi import APIRouter

v1_router = APIRouter(prefix="/api/v1", tags=["v1"])
v2_router = APIRouter(prefix="/api/v2", tags=["v2"])

# 메인 앱에 등록
app.include_router(v1_router)
app.include_router(v2_router)  # 새 버전 추가
```

### 2. **버전별 응답 형식**
```python
# v1 응답 형식
class InvestTimingResponseV1(BaseModel):
    recommendation: str
    confidence: float
    reason: str

# v2 응답 형식 (확장)
class InvestTimingResponseV2(BaseModel):
    recommendation: str
    confidence: float
    risk_level: str
    technical_indicators: dict
    sentiment_analysis: Optional[dict] = None
    risk_assessment: dict
```

### 3. **하위 호환성 유지**
```python
# v1 API는 계속 지원
@app.get("/api/v1/recommend/invest-timing", deprecated=True)
def get_invest_timing_v1_deprecated():
    """
    @deprecated Use /api/v2/recommend/invest-timing instead
    """
    return {"message": "This endpoint is deprecated. Please use v2."}
```

## 📈 버전 관리 모범 사례

### 1. **URL 기반 버전 관리**
```
✅ 좋은 예:
/api/v1/recommend/invest-timing
/api/v2/recommend/invest-timing

❌ 피해야 할 예:
/api/recommend/invest-timing?version=1
```

### 2. **헤더 기반 버전 관리**
```python
@app.get("/api/recommend/invest-timing")
def get_invest_timing(
    request: Request,
    asset_name: str
):
    version = request.headers.get("API-Version", "v1")
    
    if version == "v1":
        return get_invest_timing_v1(asset_name)
    elif version == "v2":
        return get_invest_timing_v2(asset_name)
    else:
        raise HTTPException(status_code=400, detail="Unsupported API version")
```

### 3. **버전별 문서화**
```python
# v1 API 문서
@app.get("/api/v1/recommend/invest-timing", 
         summary="Get investment timing recommendation (v1)",
         description="Basic investment timing recommendation based on technical indicators")
def get_invest_timing_v1():
    pass

# v2 API 문서
@app.get("/api/v2/recommend/invest-timing",
         summary="Get investment timing recommendation (v2)",
         description="Advanced investment timing recommendation with sentiment analysis and risk assessment")
def get_invest_timing_v2():
    pass
```

## 🚀 구현 계획

### Phase 1: v1 안정화 (현재)
- ✅ 기본 API 구현
- ✅ 핵심 기능 완성
- ✅ 문서화 완료

### Phase 2: v2 개발 (다음 단계)
- 🔄 고급 기능 추가
- 🔄 뉴스 감정 분석 통합
- 🔄 리스크 평가 강화

### Phase 3: v1 deprecation (장기)
- 📅 v1 사용 중단 예고
- 📅 마이그레이션 가이드 제공
- 📅 v1 완전 제거

## 📋 버전 관리 체크리스트

### 새 버전 출시 시
- [ ] 기존 API와의 호환성 확인
- [ ] 문서 업데이트
- [ ] 테스트 코드 작성
- [ ] 마이그레이션 가이드 작성
- [ ] 사용자 알림 계획

### 버전 deprecation 시
- [ ] 사용자에게 충분한 사전 공지
- [ ] 대체 API 제공
- [ ] 마이그레이션 도구 제공
- [ ] 점진적 사용 중단

이러한 버전 관리 전략을 통해 API의 안정성과 확장성을 보장할 수 있습니다. 