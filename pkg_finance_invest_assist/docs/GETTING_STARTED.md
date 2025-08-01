# Finance Investment Assistant - 시작하기

## 🚀 시작하기

### 1. 환경 설정 (WSL + Docker)

#### WSL 환경에서 실행
```bash
# WSL 진입
wsl

# 프로젝트 디렉토리 이동
cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist

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