# Naming Convention - ensure_ 접두사 기반 파일명

## 🎯 ensure_ 접두사의 의미

`ensure_`는 **"확실히 하다", "보장하다"**의 의미로, 파일의 목적과 기능을 명확하게 표현합니다.

## 📁 디렉토리 구조별 파일명 예시

### 1. API Gateway 서비스

```
api_gateway/
├── api/
│   └── v1/
│       ├── ensure_invest_timing_recommended.py      # 투자 타이밍 추천 API
│       ├── ensure_market_data_provided.py           # 시장 데이터 제공 API
│       ├── ensure_news_analysis_delivered.py        # 뉴스 분석 제공 API
│       └── ensure_health_status_checked.py          # 헬스체크 API
├── core/
│   ├── ensure_config_loaded.py                      # 설정 로드
│   ├── ensure_security_enforced.py                  # 보안 강제
│   └── ensure_middleware_applied.py                 # 미들웨어 적용
├── services/
│   ├── ensure_gateway_service_running.py            # 게이트웨이 서비스 실행
│   └── ensure_proxy_service_forwarded.py            # 프록시 서비스 전달
├── models/
│   ├── ensure_request_validated.py                  # 요청 검증
│   └── ensure_response_formatted.py                 # 응답 포맷팅
└── utils/
    ├── ensure_logging_configured.py                 # 로깅 설정
    └── ensure_exceptions_handled.py                 # 예외 처리
```

### 2. Investment Advisor 서비스

```
investment_advisor/
├── api/
│   ├── ensure_invest_timing_analyzed.py             # 투자 타이밍 분석 API
│   ├── ensure_harvest_timing_calculated.py          # 회수 타이밍 계산 API
│   └── ensure_health_status_verified.py             # 헬스체크 API
├── services/
│   ├── ensure_invest_timing_analyzed.py             # 투자 타이밍 분석 서비스
│   ├── ensure_harvest_timing_calculated.py          # 회수 타이밍 계산 서비스
│   ├── ensure_technical_analysis_performed.py       # 기술적 분석 수행
│   └── ensure_risk_analysis_evaluated.py            # 리스크 분석 평가
├── models/
│   ├── ensure_schemas_defined.py                    # 스키마 정의
│   └── ensure_enums_created.py                      # 열거형 생성
└── utils/
│   ├── ensure_indicators_calculated.py              # 지표 계산
│   ├── ensure_calculations_performed.py             # 계산 수행
│   └── ensure_validators_applied.py                 # 검증 적용
```

### 3. Market Data 서비스

```
market_data/
├── api/
│   ├── ensure_price_data_fetched.py                 # 가격 데이터 조회 API
│   ├── ensure_market_data_retrieved.py              # 시장 데이터 조회 API
│   └── ensure_health_status_confirmed.py            # 헬스체크 API
├── services/
│   ├── ensure_price_service_operating.py            # 가격 서비스 운영
│   ├── ensure_market_data_service_running.py        # 시장 데이터 서비스 실행
│   ├── ensure_data_provider_connected.py            # 데이터 제공자 연결
│   └── ensure_cache_service_working.py              # 캐시 서비스 작동
├── providers/
│   ├── ensure_yahoo_finance_connected.py            # Yahoo Finance 연결
│   ├── ensure_alpha_vantage_connected.py            # Alpha Vantage 연결
│   └── ensure_base_provider_implemented.py          # 기본 제공자 구현
└── utils/
    ├── ensure_data_processed.py                     # 데이터 처리
    └── ensure_data_formatted.py                     # 데이터 포맷팅
```

### 4. News Analyzer 서비스

```
news_analyzer/
├── api/
│   ├── ensure_news_crawled.py                       # 뉴스 크롤링 API
│   ├── ensure_analysis_performed.py                 # 분석 수행 API
│   └── ensure_health_status_validated.py            # 헬스체크 API
├── services/
│   ├── ensure_crawler_service_operating.py          # 크롤러 서비스 운영
│   ├── ensure_analysis_service_running.py           # 분석 서비스 실행
│   ├── ensure_sentiment_analyzed.py                 # 감정 분석 수행
│   └── ensure_content_processed.py                  # 콘텐츠 처리
├── crawlers/
│   ├── ensure_base_crawler_implemented.py           # 기본 크롤러 구현
│   ├── ensure_news_crawler_working.py               # 뉴스 크롤러 작동
│   └── ensure_finance_crawler_operating.py          # 금융 크롤러 운영
├── analyzers/
│   ├── ensure_sentiment_analyzer_working.py         # 감정 분석기 작동
│   ├── ensure_keyword_analyzer_operating.py         # 키워드 분석기 운영
│   └── ensure_trend_analyzer_functioning.py         # 트렌드 분석기 기능
└── utils/
    ├── ensure_text_processed.py                     # 텍스트 처리
    └── ensure_url_utils_working.py                  # URL 유틸리티 작동
```

## 🔧 실제 구현 예시

### 1. API 파일 예시

```python
# api_gateway/api/v1/ensure_invest_timing_recommended.py
from fastapi import APIRouter, Depends, HTTPException
from typing import Optional

router = APIRouter()

@router.get("/recommend/invest-timing")
async def ensure_invest_timing_recommended(
    asset_name: str,
    current_price: Optional[float] = None,
    risk_tolerance: str = "medium"
):
    """
    투자 타이밍 추천을 확실히 제공합니다.
    """
    try:
        # 비즈니스 로직 구현
        recommendation = await analyze_investment_timing(asset_name, current_price)
        return {
            "status": "success",
            "recommendation": recommendation,
            "asset_name": asset_name
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### 2. 서비스 파일 예시

```python
# investment_advisor/services/ensure_invest_timing_analyzed.py
from typing import Dict, Any
import pandas as pd

class InvestmentTimingAnalyzer:
    def __init__(self):
        self.indicators = {}
    
    async def ensure_invest_timing_analyzed(
        self, 
        asset_name: str, 
        price_data: pd.DataFrame
    ) -> Dict[str, Any]:
        """
        투자 타이밍 분석을 확실히 수행합니다.
        """
        # RSI 계산
        rsi = self.calculate_rsi(price_data)
        
        # MACD 계산
        macd = self.calculate_macd(price_data)
        
        # 추천 생성
        recommendation = self.generate_recommendation(rsi, macd)
        
        return {
            "asset_name": asset_name,
            "recommendation": recommendation,
            "indicators": {
                "rsi": rsi,
                "macd": macd
            }
        }
```

### 3. 유틸리티 파일 예시

```python
# shared/utils/ensure_logging_configured.py
import logging
from typing import Optional

def ensure_logging_configured(
    log_level: str = "INFO",
    log_file: Optional[str] = None
) -> logging.Logger:
    """
    로깅 설정을 확실히 구성합니다.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # 콘솔 핸들러
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # 파일 핸들러 (선택적)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
    
    logger.addHandler(console_handler)
    return logger
```

## 📋 네이밍 규칙

### 1. **기본 패턴**
```
ensure_[목적]_[동작].py
```

### 2. **동사 선택 가이드**
- **데이터 관련**: fetched, retrieved, loaded, processed
- **분석 관련**: analyzed, calculated, evaluated, performed
- **서비스 관련**: running, operating, working, functioning
- **검증 관련**: validated, verified, confirmed, checked
- **처리 관련**: handled, managed, controlled, executed

### 3. **파일명 예시**
```python
# 데이터 관련
ensure_price_data_fetched.py
ensure_market_data_retrieved.py
ensure_news_content_loaded.py

# 분석 관련
ensure_invest_timing_analyzed.py
ensure_risk_level_calculated.py
ensure_sentiment_evaluated.py

# 서비스 관련
ensure_gateway_service_running.py
ensure_database_connected.py
ensure_cache_working.py

# 검증 관련
ensure_request_validated.py
ensure_response_formatted.py
ensure_health_status_checked.py
```

## 🎯 장점

### 1. **명확한 의도 표현**
- 파일명만 봐도 기능을 알 수 있음
- 코드의 목적이 명확함

### 2. **일관성 유지**
- 모든 파일이 동일한 패턴 사용
- 팀 전체가 이해하기 쉬움

### 3. **유지보수성 향상**
- 파일 찾기가 쉬움
- 기능 추가/수정 시 적절한 위치 파악 용이

### 4. **문서화 효과**
- 파일명 자체가 문서 역할
- README 없이도 구조 이해 가능

이러한 네이밍 컨벤션을 통해 코드베이스의 가독성과 유지보수성을 크게 향상시킬 수 있습니다. 