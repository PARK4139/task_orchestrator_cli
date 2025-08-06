# Refactoring Examples - ensure_ 패턴 적용

## 🔄 기존 파일명 → ensure_ 패턴 변환

### 1. API Gateway 서비스

#### 기존 구조
```
api_gateway/
├── main.py
└── __init__.py
```

#### 개선된 구조
```
api_gateway/
├── api/
│   └── v1/
│       ├── ensure_invest_timing_recommended.py
│       ├── ensure_market_data_provided.py
│       ├── ensure_news_analysis_delivered.py
│       └── ensure_health_status_checked.py
├── core/
│   ├── ensure_config_loaded.py
│   ├── ensure_security_enforced.py
│   └── ensure_middleware_applied.py
├── services/
│   ├── ensure_gateway_service_running.py
│   └── ensure_proxy_service_forwarded.py
├── utils/
│   ├── ensure_logging_configured.py
│   └── ensure_exceptions_handled.py
├── ensure_app_started.py (기존 main.py)
└── __init__.py
```

### 2. Investment Advisor 서비스

#### 기존 구조
```
investment_advisor/
├── main.py
├── services/
│   ├── invest_timing.py
│   └── harvest_timing.py
├── models/
│   └── schemas.py
└── __init__.py
```

#### 개선된 구조
```
investment_advisor/
├── api/
│   ├── ensure_invest_timing_analyzed.py
│   ├── ensure_harvest_timing_calculated.py
│   └── ensure_health_status_verified.py
├── services/
│   ├── ensure_invest_timing_analyzed.py (기존 invest_timing.py)
│   ├── ensure_harvest_timing_calculated.py (기존 harvest_timing.py)
│   ├── ensure_technical_analysis_performed.py
│   └── ensure_risk_analysis_evaluated.py
├── models/
│   ├── ensure_schemas_defined.py (기존 schemas.py)
│   └── ensure_enums_created.py
├── utils/
│   ├── ensure_indicators_calculated.py
│   ├── ensure_calculations_performed.py
│   └── ensure_validators_applied.py
├── ensure_app_started.py (기존 main.py)
└── __init__.py
```

## 🔧 실제 리팩토링 예시

### 1. main.py → ensure_app_started.py

#### 기존 코드
```python
# api_gateway/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Finance Investment Assistant")

@app.get("/")
def root():
    return {"message": "Finance Investment Assistant"}
```

#### 개선된 코드
```python
# api_gateway/ensure_app_started.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.ensure_config_loaded import ensure_config_loaded
from core.ensure_middleware_applied import ensure_middleware_applied
from utils.ensure_logging_configured import ensure_logging_configured

def ensure_app_started() -> FastAPI:
    """
    FastAPI 애플리케이션을 확실히 시작합니다.
    """
    # 설정 로드
    config = ensure_config_loaded()
    
    # 로깅 설정
    logger = ensure_logging_configured()
    
    # FastAPI 앱 생성
    app = FastAPI(
        title="Finance Investment Assistant - API Gateway",
        description="API Gateway for finance investment assistant services",
        version="1.0.0"
    )
    
    # 미들웨어 적용
    ensure_middleware_applied(app)
    
    # 라우터 등록
    from api.v1.ensure_invest_timing_recommended import router as invest_router
    from api.v1.ensure_market_data_provided import router as market_router
    from api.v1.ensure_health_status_checked import router as health_router
    
    app.include_router(invest_router, prefix="/api/v1")
    app.include_router(market_router, prefix="/api/v1")
    app.include_router(health_router, prefix="/api/v1")
    
    logger.info("API Gateway application started successfully")
    return app

# 애플리케이션 인스턴스 생성
app = ensure_app_started()
```

### 2. invest_timing.py → ensure_invest_timing_analyzed.py

#### 기존 코드
```python
# investment_advisor/services/invest_timing.py
import pandas as pd
from typing import Dict, Any

def analyze_investment_timing(asset_name: str, price_data: pd.DataFrame) -> Dict[str, Any]:
    # RSI 계산
    rsi = calculate_rsi(price_data)
    
    # 추천 생성
    if rsi < 30:
        recommendation = "buy"
    elif rsi > 70:
        recommendation = "sell"
    else:
        recommendation = "hold"
    
    return {
        "asset_name": asset_name,
        "recommendation": recommendation,
        "rsi": rsi
    }
```

#### 개선된 코드
```python
# investment_advisor/services/ensure_invest_timing_analyzed.py
import pandas as pd
from typing import Dict, Any, Optional
from utils.ensure_indicators_calculated import ensure_indicators_calculated
from utils.ensure_validators_applied import ensure_validators_applied

class InvestmentTimingAnalyzer:
    def __init__(self):
        self.indicators_calculator = ensure_indicators_calculated()
        self.validator = ensure_validators_applied()
    
    async def ensure_invest_timing_analyzed(
        self,
        asset_name: str,
        price_data: pd.DataFrame,
        risk_tolerance: str = "medium",
        include_technical_indicators: bool = True
    ) -> Dict[str, Any]:
        """
        투자 타이밍 분석을 확실히 수행합니다.
        """
        # 입력 데이터 검증
        self.validator.ensure_price_data_valid(price_data)
        self.validator.ensure_asset_name_valid(asset_name)
        
        # 기술적 지표 계산
        indicators = await self.indicators_calculator.ensure_all_indicators_calculated(
            price_data, include_technical_indicators
        )
        
        # 투자 추천 생성
        recommendation = self._generate_recommendation(indicators, risk_tolerance)
        
        # 결과 검증
        self.validator.ensure_recommendation_valid(recommendation)
        
        return {
            "asset_name": asset_name,
            "recommendation": recommendation["action"],
            "confidence": recommendation["confidence"],
            "risk_level": recommendation["risk_level"],
            "indicators": indicators,
            "analysis_date": pd.Timestamp.now().isoformat()
        }
    
    def _generate_recommendation(
        self, 
        indicators: Dict[str, float], 
        risk_tolerance: str
    ) -> Dict[str, Any]:
        """
        지표를 기반으로 투자 추천을 생성합니다.
        """
        rsi = indicators.get("rsi", 50)
        macd_signal = indicators.get("macd_signal", "neutral")
        
        # RSI 기반 기본 추천
        if rsi < 30:
            base_action = "buy"
            confidence = 0.8
        elif rsi > 70:
            base_action = "sell"
            confidence = 0.8
        else:
            base_action = "hold"
            confidence = 0.6
        
        # 리스크 프로파일 조정
        risk_adjustment = self._adjust_for_risk_tolerance(risk_tolerance)
        confidence *= risk_adjustment
        
        return {
            "action": base_action,
            "confidence": min(confidence, 1.0),
            "risk_level": risk_tolerance,
            "reason": f"RSI: {rsi:.2f}, MACD: {macd_signal}"
        }
    
    def _adjust_for_risk_tolerance(self, risk_tolerance: str) -> float:
        """
        리스크 프로파일에 따른 신뢰도 조정
        """
        adjustments = {
            "conservative": 0.8,
            "medium": 1.0,
            "aggressive": 1.2
        }
        return adjustments.get(risk_tolerance, 1.0)
```

### 3. schemas.py → ensure_schemas_defined.py

#### 기존 코드
```python
# investment_advisor/models/schemas.py
from pydantic import BaseModel
from typing import Optional

class InvestTimingRequest(BaseModel):
    asset_name: str
    current_price: Optional[float] = None
```

#### 개선된 코드
```python
# investment_advisor/models/ensure_schemas_defined.py
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum

class RiskTolerance(str, Enum):
    CONSERVATIVE = "conservative"
    MEDIUM = "medium"
    AGGRESSIVE = "aggressive"

class InvestTimingRequest(BaseModel):
    """
    투자 타이밍 분석 요청 스키마
    """
    asset_name: str = Field(..., description="분석할 자산명", min_length=1, max_length=50)
    current_price: Optional[float] = Field(None, description="현재 가격", ge=0)
    risk_tolerance: RiskTolerance = Field(RiskTolerance.MEDIUM, description="리스크 허용도")
    include_technical_indicators: bool = Field(True, description="기술적 지표 포함 여부")
    
    @validator('asset_name')
    def ensure_asset_name_valid(cls, v):
        if not v.strip():
            raise ValueError('자산명은 비어있을 수 없습니다')
        return v.strip()
    
    @validator('current_price')
    def ensure_price_valid(cls, v):
        if v is not None and v < 0:
            raise ValueError('가격은 0 이상이어야 합니다')
        return v

class InvestTimingResponse(BaseModel):
    """
    투자 타이밍 분석 응답 스키마
    """
    asset_name: str = Field(..., description="분석된 자산명")
    recommendation: str = Field(..., description="투자 추천", regex="^(buy|sell|hold)$")
    confidence: float = Field(..., description="신뢰도", ge=0, le=1)
    risk_level: str = Field(..., description="리스크 레벨")
    indicators: dict = Field(..., description="기술적 지표")
    analysis_date: str = Field(..., description="분석 일시")
    
    class Config:
        schema_extra = {
            "example": {
                "asset_name": "삼성전자",
                "recommendation": "buy",
                "confidence": 0.8,
                "risk_level": "medium",
                "indicators": {
                    "rsi": 25.5,
                    "macd": "bullish"
                },
                "analysis_date": "2024-01-15T10:30:00"
            }
        }
```

## 📋 리팩토링 체크리스트

### 1. **파일명 변경**
- [ ] `main.py` → `ensure_app_started.py`
- [ ] `invest_timing.py` → `ensure_invest_timing_analyzed.py`
- [ ] `harvest_timing.py` → `ensure_harvest_timing_calculated.py`
- [ ] `schemas.py` → `ensure_schemas_defined.py`

### 2. **함수명 변경**
- [ ] `analyze_investment_timing()` → `ensure_invest_timing_analyzed()`
- [ ] `calculate_harvest_timing()` → `ensure_harvest_timing_calculated()`
- [ ] `get_market_data()` → `ensure_market_data_retrieved()`

### 3. **클래스명 변경**
- [ ] `InvestmentTimingAnalyzer` → `InvestmentTimingAnalyzer` (유지)
- [ ] `MarketDataService` → `MarketDataService` (유지)

### 4. **import 경로 업데이트**
- [ ] 모든 import 문에서 새 파일명 반영
- [ ] 상대 경로 vs 절대 경로 통일

### 5. **문서화 업데이트**
- [ ] README.md 파일명 참조 업데이트
- [ ] API 문서 경로 업데이트
- [ ] 테스트 파일 경로 업데이트

이러한 리팩토링을 통해 코드의 의도가 더 명확해지고, 유지보수성이 향상됩니다. 