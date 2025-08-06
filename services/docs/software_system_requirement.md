# Smart Person AI

현명한 사람들의 AI - AI 산출물 공급 서비스

## 프로젝트 개요

**Smart Person AI**는 AI를 모르는 사람들과 AI 공부가 귀찮은 사람들을 위한 AI 산출물 공급 서비스입니다.

### 핵심 가치 제안
- **마차를 끄는 마차시대의 현명한 마부는 자동차시대가 되자 자동차의 운전수가 되었다**
- **AI 시대의 현명한 사람들은 AI 사용자가 될 것을 나는 믿는다**

## 서비스 라인업

### AI 콘텐츠 제품
- AI 이미지 모음집 (Stable Diffusion 산출물, 12시간 단위 업데이트)
- AI 동화책 모음집 (Claude Sonnet 4 산출물)

### 자동화 도구
- AI 일반사무업무 자동화툴 (엑셀파일 병합/폴더 생성)
- AI 서비스 물품 자동업로더
- AI 웹크롤러 (미국주가/주식뉴스)
- AI 유튜브 다운로더 (주식뉴스)

## 기술 스택

- **Backend**: FastAPI (Python 3.12+)
- **AI APIs**: Claude Sonnet 4, Stable Diffusion
- **Database**: PostgreSQL, Redis, MongoDB
- **Infrastructure**: Docker, AWS EC2, Nginx
- **Monitoring**: Prometheus + Grafana

## 아키텍처

Domain-driven Microservices Architecture (MSA)를 기반으로 구성:

- **AI Content Domain**: 이미지, 동화책, 카피 생성
- **Automation Domain**: 파일 처리, 웹크롤링, 업로드
- **Business Domain**: 결제, 고객관리, 분석
- **Infrastructure Domain**: 모니터링, 백업, 보안

## 개발 상태

🚀 **Phase 1 - MVP 개발 중**
- [ ] 프로젝트 구조 설정
- [ ] AI Image Service 구현
- [ ] Excel Automation Service 구현
- [ ] Payment Service 기본 구조

## 🚀 빠른 시작

### 1. 의존성 설치
```bash
cd services/smart_person_ai
pip install uv
uv sync
```

### 2. 환경 설정
```bash
# 환경 파일 복사 및 편집
cp env.example .env
# .env 파일에서 필요한 API 키들 설정
```

### 3. 서비스 실행 (개발 환경)

**방법 1: 개발 스크립트 사용 (추천)**
```bash
python scripts/start_services.py
```

**방법 2: Docker Compose 사용**
```bash
docker-compose up -d
```

**방법 3: 수동 실행**
```bash
# 터미널 1: API Gateway
python api_gateway.py

# 터미널 2: AI Image Service  
python ai_content/image_service/main.py

# 터미널 3: Excel Automation Service
python automation/excel_service/main.py
```

### 4. 서비스 테스트
```bash
# 자동 테스트 실행
python scripts/test_services.py

# 또는 브라우저에서 확인
# http://localhost:8000/health
# http://localhost:8000/docs (Swagger UI)
```

### 5. 서비스 엔드포인트
- **API Gateway**: http://localhost:8000
- **AI Image Service**: http://localhost:8001  
- **Excel Automation**: http://localhost:8011
- **Health Check**: http://localhost:8000/health
- **API Documentation**: http://localhost:8000/docs

## 라이선스

MIT License