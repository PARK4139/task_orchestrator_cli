# Finance Investment Assistant - 프로젝트 개요

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
├── tests/                # 테스트 코드
├── docs/                 # 프로젝트 문서
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