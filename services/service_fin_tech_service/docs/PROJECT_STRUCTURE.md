# Finance Investment Assistant - 프로젝트 구조

## 📊 최종 구조

```
pkg_finance_invest_assist/
├── api_gateway/
│   ├── api/v1/
│   │   ├── ensure_invest_timing_recommended.py
│   │   ├── ensure_market_data_provided.py
│   │   ├── ensure_news_analysis_delivered.py
│   │   └── ensure_health_status_checked.py
│   ├── core/
│   │   ├── ensure_config_loaded.py
│   │   └── ensure_middleware_applied.py
│   ├── utils/
│   │   ├── ensure_logging_configured.py
│   │   └── ensure_exceptions_handled.py
│   └── ensure_app_started.py
├── investment_advisor/
│   ├── api/v1/
│   │   ├── ensure_invest_timing_analyzed.py
│   │   ├── ensure_harvest_timing_calculated.py
│   │   └── ensure_health_status_verified.py
│   ├── services/
│   │   ├── ensure_invest_timing_analyzed.py
│   │   └── ensure_harvest_timing_calculated.py
│   └── ensure_app_started.py
├── market_data/
│   ├── api/v1/
│   │   ├── ensure_price_data_fetched.py
│   │   ├── ensure_market_data_retrieved.py
│   │   └── ensure_health_status_confirmed.py
│   └── ensure_app_started.py
├── news_analyzer/
│   ├── api/v1/
│   │   ├── ensure_news_crawled.py
│   │   ├── ensure_analysis_performed.py
│   │   └── ensure_health_status_validated.py
│   └── ensure_app_started.py
├── shared/
│   ├── config.py
│   ├── database.py
│   └── models.py
├── deployment/
│   ├── docker-compose.yml
│   ├── Dockerfile.api_gateway
│   ├── Dockerfile.investment_advisor
│   ├── Dockerfile.market_data
│   ├── Dockerfile.news_analyzer
│   └── nginx/
├── scripts/
│   ├── deploy.sh
│   ├── deploy.bat
│   └── docker_uv_dev.sh
├── tests/
│   ├── __init__.py
│   ├── test_smart_person_ai_container_build.py
│   └── test_smart_person_ai_container_build.md
├── docs/
│   ├── OVERVIEW.md
│   ├── GETTING_STARTED.md
│   ├── DEVELOPMENT_ROADMAP.md
│   ├── PROJECT_STRUCTURE.md
│   ├── NAMING_CONVENTION.md
│   ├── REFACTORING_EXAMPLES.md
│   ├── API_VERSIONING.md
│   ├── ARCHITECTURE.md
│   └── WSL_GUIDE.md
├── pyproject.toml
├── env.example
└── README.md
```

## 🏗️ 아키텍처 레이어

### 1. API Layer (`api/v1/`)
- **목적**: API 엔드포인트 정의 및 라우팅
- **패턴**: `ensure_[기능]_[동작].py`
- **예시**: `ensure_invest_timing_recommended.py`

### 2. Core Layer (`core/`)
- **목적**: 설정, 미들웨어 등 핵심 모듈
- **패턴**: `ensure_[기능]_[동작].py`
- **예시**: `ensure_config_loaded.py`, `ensure_middleware_applied.py`

### 3. Services Layer (`services/`)
- **목적**: 비즈니스 로직 구현
- **패턴**: `ensure_[기능]_[동작].py`
- **예시**: `ensure_invest_timing_analyzed.py`

### 4. Utils Layer (`utils/`)
- **목적**: 공통 유틸리티 함수
- **패턴**: `ensure_[기능]_[동작].py`
- **예시**: `ensure_logging_configured.py`, `ensure_exceptions_handled.py`

### 5. Models Layer (`models/`)
- **목적**: 데이터 모델 정의
- **패턴**: Pydantic 스키마
- **예시**: `schemas.py`

### 6. Providers Layer (`providers/`) - Market Data 전용
- **목적**: 외부 서비스 연동
- **패턴**: `ensure_[서비스]_[동작].py`
- **예시**: `ensure_yahoo_finance_connected.py`

### 7. Crawlers Layer (`crawlers/`) - News Analyzer 전용
- **목적**: 웹 크롤링 로직
- **패턴**: `ensure_[사이트]_[동작].py`
- **예시**: `ensure_naver_news_crawled.py`

### 8. Analyzers Layer (`analyzers/`) - News Analyzer 전용
- **목적**: 분석 엔진
- **패턴**: `ensure_[분석]_[동작].py`
- **예시**: `ensure_sentiment_analyzed.py`

## 🎯 마이크로서비스 구조

### API Gateway (포트: 8000)
- **역할**: 모든 요청의 진입점
- **기능**: 라우팅, 로드 밸런싱, 인증/인가
- **구조**: `api/v1/` + `core/` + `utils/`

### Investment Advisor (포트: 8001)
- **역할**: 투자 추천 엔진
- **기능**: 투자 타이밍 분석, 수익률 계산
- **구조**: `api/v1/` + `services/` + `core/` + `utils/`

### Market Data (포트: 8002)
- **역할**: 금융 데이터 제공
- **기능**: 자산 가격 조회, 시장 데이터 수집
- **구조**: `api/v1/` + `providers/` + `core/` + `utils/`

### News Analyzer (포트: 8003)
- **역할**: 뉴스 크롤링 및 분석
- **기능**: 뉴스 수집, 감정 분석, 트렌드 분석
- **구조**: `api/v1/` + `crawlers/` + `analyzers/` + `core/` + `utils/`

## 📋 공통 디렉토리

### Shared (`shared/`)
- **목적**: 모든 서비스가 공유하는 모듈
- **내용**: 설정, 데이터베이스 연결, 공통 모델

### Deployment (`deployment/`)
- **목적**: 배포 관련 설정
- **내용**: Docker Compose, Dockerfile, Nginx 설정

### Scripts (`scripts/`)
- **목적**: 실행 스크립트
- **내용**: 배포, 개발 환경 설정 스크립트

### Tests (`tests/`)
- **목적**: 테스트 코드
- **내용**: 단위 테스트, 통합 테스트

### Docs (`docs/`)
- **목적**: 프로젝트 문서
- **내용**: 가이드, 아키텍처 문서, 개발 로드맵 