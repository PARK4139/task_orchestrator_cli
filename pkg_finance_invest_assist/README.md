# Finance Investment Assistant

재테크에 필요한 정보(금융 뉴스, 자산 가격, 공공 금융 API 등)를 수집하여
투자자에게 유의미한 정보를 분석·추천해주는 핀테크 서비스입니다.

## 🚀 빠른 시작

```bash
# WSL 환경에서 실행
cd pkg_finance_invest_assist
docker-compose up -d

# Swagger UI 접속
http://[WSL_IP]:8000/docs
```

## 📁 프로젝트 구조

```
pkg_finance_invest_assist/
├── api_gateway/          # API Gateway (포트: 8000)
├── investment_advisor/    # 투자 추천 엔진 (포트: 8001)
├── market_data/          # 금융 데이터 API (포트: 8002)
├── news_analyzer/        # 뉴스 크롤링 서비스 (포트: 8003)
├── shared/               # 공통 설정 및 데이터베이스
├── deployment/           # Docker Compose 및 Nginx 설정
├── scripts/              # 실행 스크립트
├── tests/                # 테스트 코드
├── docs/                 # 📚 상세 문서
└── README.md             # 이 파일
```

## ⚙️ 기술 스택

- **언어**: Python 3.8.1+
- **백엔드**: FastAPI
- **데이터베이스**: PostgreSQL + Redis
- **의존성 관리**: `uv` + `pyproject.toml`
- **배포**: Docker + AWS EC2

## 📚 문서

- **[📖 프로젝트 개요](docs/OVERVIEW.md)** - 프로젝트 소개 및 주요 기능
- **[🚀 시작하기](docs/GETTING_STARTED.md)** - 환경 설정 및 개발 가이드
- **[🗺️ 개발 로드맵](docs/DEVELOPMENT_ROADMAP.md)** - 개발 계획 및 진행 상황
- **[🏗️ 프로젝트 구조](docs/PROJECT_STRUCTURE.md)** - 상세한 디렉토리 구조
- **[📋 네이밍 컨벤션](docs/NAMING_CONVENTION.md)** - ensure_ 패턴 가이드라인
- **[🔧 리팩토링 예시](docs/REFACTORING_EXAMPLES.md)** - 실제 리팩토링 사례
- **[🌐 API 버전 관리](docs/API_VERSIONING.md)** - API 버전 관리 전략
- **[🏛️ 아키텍처](docs/ARCHITECTURE.md)** - 전체 시스템 아키텍처
- **[🐧 WSL 가이드](docs/WSL_GUIDE.md)** - WSL 환경 설정 가이드

## 🎯 주요 기능

### ✅ 구현 완료
- API Gateway 기본 구조
- PostgreSQL + Redis 연결
- Docker 컨테이너화
- ensure_ 패턴 적용
- API 버전 관리 (v1)

### 🔄 구현 중
- 투자 타이밍 추천 로직
- 자산 가격 조회 API
- 뉴스 크롤링 서비스

### 📋 계획 중
- 머신러닝 모델
- Django 웹 인터페이스
- 실시간 알림 시스템

## 🔧 개발 환경

### 필수 요구사항
- Python 3.8.1+
- Docker & Docker Compose
- WSL (Windows 사용자)

### 설치 및 실행
```bash
# 의존성 설치
uv sync

# 개발 환경 실행
docker-compose up -d

# API 테스트
curl http://localhost:8000/
```

## 📊 최신 업데이트 (2025-08-01)

### ✅ 완료된 작업
- 🏗️ **코드베이스 구조 개선**: ensure_ 패턴 적용
- 📁 **일관된 디렉토리 구조**: api/v1/, core/, services/, utils/
- 🎯 **네이밍 컨벤션**: 파일명과 함수명의 명확한 의도 표현
- 📋 **문서화 개선**: 상세한 가이드라인 및 예시 문서

### 🎯 개선된 점
- **가독성 향상**: 파일명만 봐도 기능 파악 가능
- **유지보수성 향상**: 기능별 명확한 분리
- **확장성 개선**: API 버전 관리 준비 완료
- **개발 효율성 향상**: 팀 전체가 이해하기 쉬운 구조

## 🤝 기여하기

1. 이슈 등록 또는 기능 제안
2. 브랜치 생성 (`feature/기능명`)
3. 코드 작성 및 테스트
4. Pull Request 생성

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 