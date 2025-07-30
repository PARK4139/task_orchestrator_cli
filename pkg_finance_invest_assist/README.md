# Finance Investment Assistant

## 🎯 프로젝트 개요
재테크에 필요한 정보(금융 뉴스, 자산 가격, 공공 금융 API 등)를 수집하여
투자자에게 유의미한 정보를 분석·추천해주는 핀테크 서비스입니다.

## 📁 프로젝트 구조

```
pkg_finance_invest_assist/
├── api_gateway/          # API Gateway (FastAPI)
├── investment_advisor/    # 투자 추천 엔진
├── market_data/          # 금융 데이터 API
├── news_analyzer/        # 뉴스 크롤링 서비스
├── shared/               # 공통 설정 및 데이터베이스 모듈
├── deployment/           # Docker Compose 및 Nginx 설정
├── scripts/              # 실행 스크립트
├── pyproject.toml        # 프로젝트 설정
└── README.md             # 프로젝트 문서
```

## ⚙️ 기술 스택

| 항목         | 내용 |
|--------------|------|
| 언어         | Python 3.8.1+
| 백엔드       | FastAPI
| 프론트엔드   | Django
| DB           | PostgreSQL (Docker 컨테이너로 EC2에서 운영)
| 캐시         | Redis
| 의존성 관리  | `uv` + `pyproject.toml`
| 배포         | AWS EC2 + Docker
| 통신         | HTTP 기반, 추후 HTTPS로 전환 예정

## 🚀 시작하기

### 1. 환경 설정 (WSL + Docker)

#### WSL 환경에서 실행
```bash
# WSL 진입
wsl

# 프로젝트 디렉토리 이동
cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist/infra

# 모든 서비스 실행
docker-compose up -d
```

#### Windows에서 브라우저 접속
```bash
# WSL IP 확인
wsl hostname -I

# Swagger UI 접속 (브라우저에서)
http://[WSL_IP]:8000/docs
# 예: http://172.27.169.136:8000/docs
```

### 2. 서비스 상태 확인
```bash
# 컨테이너 상태 확인
docker-compose ps

# API 테스트
curl http://localhost:8000/
curl "http://localhost:8000/api/v1/recommend/invest-timing?asset_name=삼성전자"
```

### 3. 개발 환경 설정 (로컬)
```bash
# 가상환경 생성 및 활성화
uv venv
source .venv/bin/activate  # Linux/Mac
# 또는
.venv\Scripts\activate     # Windows

# 의존성 설치
uv sync
```

## 📌 주요 기능

### 투자 타이밍 추천
- ✅ `/api/v1/recommend/invest-timing` - 자산명 기반 투자 시점 분석 (구현 중)
- ❌ `/api/v1/recommend/harvest-timing` - 수익률 기반 회수 시점 분석 (미구현)

### 뉴스 크롤링
- ❌ `/api/v1/news/crawl` - 금융 뉴스 자동 수집 및 분석 (미구현)
- ❌ 감정 분석을 통한 시장 동향 파악 (미구현)

### 자산 가격 모니터링
- ❌ `/api/v1/finance/price` - 실시간 자산 가격 조회 (미구현)
- ❌ 이동평균선 기반 기술적 분석 (미구현)

### 사용자 관리
- ❌ 사용자 인증/정보 처리 (미구현)
- ❌ Django 웹 인터페이스 (미구현)

### 데이터베이스 연동
- ✅ PostgreSQL 연결 (구현 완료)
- ✅ Redis 캐시 연결 (구현 완료)
- ❌ 데이터베이스 스키마 및 마이그레이션 (미구현)

### API Gateway
- ✅ 기본 엔드포인트 `/` (구현 완료)
- ✅ 서비스 상태 확인 (구현 완료)
- ❌ 인증/인가 미들웨어 (미구현)
- ❌ 요청/응답 로깅 (미구현)

## 🔧 개발 가이드

### 함수 작성 규칙
- 함수명은 항상 `ensure_`로 시작하고, **완료형 동사**를 접미사로 사용
- 예: `ensure_investing_timing_guided()`, `ensure_asset_price_fetched()`

### 코드 스타일
- 설명은 **한국어**, 코드 및 주석은 **영어**로 작성
- Windows / Linux / WSL 모두에서 **호환되는 코드** 작성
- 명확하게 분리된 구조 선호:
  - `/main.py` : FastAPI 진입점
  - `/services/logic.py` : 기능 로직
  - `/models/schemas.py` : Pydantic 모델
  - `/database/session.py` : DB 연결

## 🐳 Docker 환경

### MSA 구조
```
Gateway (8000) → Recommendation Engine (8001)
              → Finance API Client (8002)
              → News Crawler (8003)
```

### 컨테이너 서비스
- **finance_gateway**: API Gateway (포트 8000)
- **finance_db**: PostgreSQL 데이터베이스 (포트 5432)
- **finance_redis**: Redis 캐시 (포트 6379)
- **finance_nginx**: Nginx 리버스 프록시 (포트 80, 443)

### 개발 워크플로우
```bash
# 1. 코드 수정 (Windows에서)
# 2. 컨테이너 재빌드
docker-compose build [service-name]

# 3. 서비스 재시작
docker-compose up -d [service-name]

# 4. API 테스트
curl http://172.27.169.136:8000/api/v1/...
```

## 📝 오늘 작업 내용 (2024-01-XX)

### ✅ 완료된 작업

#### 1. MSA 환경 구축
- ✅ **Docker Compose**: 모든 마이크로서비스 컨테이너화
- ✅ **API Gateway**: FastAPI 기반 게이트웨이 구현
- ✅ **데이터베이스**: PostgreSQL + Redis 연결
- ✅ **Nginx**: 리버스 프록시 설정

#### 2. 의존성 관리 개선
- ✅ **pyproject.toml**: requirements.txt → pyproject.toml 마이그레이션
- ✅ **uv 도입**: pip → uv로 패키지 관리 개선
- ✅ **Python 호환성**: 3.8.1+ 버전 지원
- ✅ **Hatchling 설정**: 패키지 빌드 시스템 구성

#### 3. 개발 환경 통합
- ✅ **WSL + Windows**: "Windows에서 편집, WSL에서 실행" 방식
- ✅ **Docker 자동화**: 컨테이너 빌드 및 실행 자동화
- ✅ **API 테스트**: Swagger UI를 통한 실시간 테스트
- ✅ **네트워크 연결**: WSL IP를 통한 Windows 브라우저 접속

#### 4. 문제 해결
- ✅ **Python 버전 충돌**: flake8 호환성 문제 해결
- ✅ **Hatchling 패키지 경로**: 실제 디렉토리 구조 반영
- ✅ **의존성 충돌**: numpy/pandas 버전 호환성 해결
- ✅ **uv sync**: 자동 lock 파일 생성 및 의존성 해결

## 📝 오늘 작업 내용 (2024-01-XX)

### ✅ 완료된 작업

#### 1. MSA 환경 구축
- ✅ **Docker Compose**: 모든 마이크로서비스 컨테이너화
- ✅ **API Gateway**: FastAPI 기반 게이트웨이 구현
- ✅ **데이터베이스**: PostgreSQL + Redis 연결
- ✅ **Nginx**: 리버스 프록시 설정

#### 2. 의존성 관리 개선
- ✅ **pyproject.toml**: requirements.txt → pyproject.toml 마이그레이션
- ✅ **uv 도입**: pip → uv로 패키지 관리 개선
- ✅ **Python 호환성**: 3.8.1+ 버전 지원
- ✅ **Hatchling 설정**: 패키지 빌드 시스템 구성

#### 3. 개발 환경 통합
- ✅ **WSL + Windows**: "Windows에서 편집, WSL에서 실행" 방식
- ✅ **Docker 자동화**: 컨테이너 빌드 및 실행 자동화
- ✅ **API 테스트**: Swagger UI를 통한 실시간 테스트
- ✅ **네트워크 연결**: WSL IP를 통한 Windows 브라우저 접속

#### 4. 문제 해결
- ✅ **Python 버전 충돌**: flake8 호환성 문제 해결
- ✅ **Hatchling 패키지 경로**: 실제 디렉토리 구조 반영
- ✅ **의존성 충돌**: numpy/pandas 버전 호환성 해결
- ✅ **uv sync**: 자동 lock 파일 생성 및 의존성 해결

### 🎯 다음 단계

#### Phase 1: 핵심 API 구현 (우선순위)
1. **투자 타이밍 추천 로직** - 기술적 지표 기반 분석 알고리즘
2. **자산 가격 조회** - 외부 금융 API 연동 (Yahoo Finance, Alpha Vantage 등)
3. **뉴스 크롤링** - BeautifulSoup/Selenium을 활용한 뉴스 수집

#### Phase 2: 고급 기능 구현
1. **머신러닝 모델** - 예측 알고리즘 및 감정 분석
2. **포트폴리오 최적화** - 자산 배분 및 리스크 관리
3. **실시간 알림** - WebSocket을 활용한 실시간 데이터 전송

#### Phase 3: 프론트엔드 및 보안
1. **Django 웹 인터페이스** - 관리자 대시보드 및 사용자 인터페이스
2. **인증/인가 시스템** - JWT 토큰 기반 보안
3. **API 문서화** - 자동화된 API 문서 생성

#### Phase 4: 운영 및 모니터링
1. **로깅 시스템** - 구조화된 로그 수집 및 분석
2. **모니터링 대시보드** - Prometheus + Grafana 연동
3. **CI/CD 파이프라인** - GitHub Actions를 활용한 자동 배포 