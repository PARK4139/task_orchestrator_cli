# Smart Person AI

현명한 사람들의 AI - 완전한 MSA 기반 AI 산출물 공급 서비스

## 🎯 프로젝트 개요

**Smart Person AI**는 AI를 모르는 사람들과 AI 공부가 귀찮은 사람들을 위한 완전한 마이크로서비스 아키텍처 기반의 AI 산출물 공급 서비스입니다.

### 핵심 가치 제안
> *"마차를 끄는 마차시대의 현명한 마부는 자동차시대가 되자 자동차의 운전수가 되었다.  
> AI 시대의 현명한 사람들은 AI 사용자가 될 것을 나는 믿는다."*

## 📁 **완전한 MSA 프로젝트 구조**

```
services/smart_person_ai/
├── 📋 README.md                             # 프로젝트 개요
├── ⚙️  pyproject.toml                        # 공통 의존성 설정
├── 🐳 docker-compose.yml                     # 전체 서비스 오케스트레이션
├── 🌍 .env.example                           # 환경 설정 템플릿
│
├── 🏠 service_official_home_smart_person_ai/                 # 공식 홈페이지 (포트: 3000, 8030)
│   ├── frontend/                            # Next.js SEO 최적화 사이트
│   ├── backend/                             # FastAPI 홈페이지 API
│   └── README.md                            # 홈페이지 서비스 문서
│
├── 🌐 service_api_gateway/                   # API Gateway (포트: 8000)
│   ├── __init__.py
│   └── main.py                              # 중앙 라우팅 및 프록시
│
├── 🎨 service_ai_content_image/              # AI 이미지 서비스 (포트: 8001)  
│   ├── __init__.py
│   └── main.py                              # Stable Diffusion 이미지 생성
│
├── 📖 service_ai_content_book/               # AI 동화책 서비스 (포트: 8002)
│   ├── __init__.py  
│   └── main.py                              # Claude 기반 동화책 생성
│
├── 📊 service_automation_excel_service/      # 엑셀 자동화 (포트: 8011)
│   ├── __init__.py
│   └── main.py                              # pk_system 통합 엑셀 처리
│
├── 🕷️ service_automation_web_crawler/        # 웹 크롤링 (포트: 8012)
│   ├── __init__.py
│   └── main.py                              # 주가/뉴스 데이터 수집
│
├── 💳 service_payment/                       # 결제 서비스 (포트: 8021)
│   ├── __init__.py
│   └── main.py                              # 구독/토큰 관리
│
├── 🔧 shared/                                # 공통 모듈
│   ├── config.py                            # 환경 설정
│   └── database.py                          # 데이터베이스 연결
│
├── 🐳 deployment/                            # Docker 배포 설정
│   ├── Dockerfile.api_gateway
│   ├── Dockerfile.ai_image
│   ├── Dockerfile.ai_book
│   ├── Dockerfile.excel_automation
│   ├── Dockerfile.web_crawler
│   └── Dockerfile.payment
│
├── 📚 docs/                                  # 프로젝트 문서
│   ├── README.md                            # 상세 기술 문서
│   └── architecture design.svg             # 아키텍처 다이어그램
│
└── 🧪 tests/                                 # 테스트 및 실행 스크립트
    ├── start_services.py                   # 개발 서버 실행
    └── test_services.py                    # 서비스 테스트
```

## 🚀 **빠른 시작**

### 1. 의존성 설치
```bash
cd services/smart_person_ai
pip install uv
uv sync
```

### 2. 환경 설정
```bash
# 환경 파일 복사 및 편집
cp .env.example .env
# .env 파일에서 필요한 API 키들 설정 (Claude, Stable Diffusion 등)
```

### 3. 서비스 실행

**방법 1: 개발 스크립트 사용 (추천)**
```bash
python tests/start_services.py
```

**방법 2: Docker Compose 사용**
```bash
docker-compose up -d
```

**방법 3: 개별 서비스 수동 실행**
```bash
# 터미널 1: 공식 홈페이지 (Next.js + FastAPI)
cd service_official_home_smart_person_ai
python scripts/dev.py

# 터미널 2: API Gateway
python service_api_gateway/main.py

# 터미널 3: AI Image Service  
python service_ai_content_image/main.py

# 터미널 4: AI Book Service
python service_ai_content_book/main.py

# 터미널 5: Excel Automation
python service_automation_excel_service/main.py

# 터미널 6: Web Crawler
python service_automation_web_crawler/main.py

# 터미널 7: Payment Service
python service_payment/main.py
```

### 4. 서비스 테스트
```bash
# 자동 테스트 실행
python tests/test_services.py

# 또는 브라우저에서 확인
# http://localhost:8000/health (전체 상태)
# http://localhost:8000/docs (Swagger UI)
```

## 🎯 **서비스 엔드포인트**

| 서비스 | 포트 | 엔드포인트 | 설명 |
|--------|------|------------|------|
| 🏠 **공식 홈페이지** | 3000 | http://localhost:3000 | SEO 최적화 랜딩 페이지 (Next.js) |
| 🏠 **홈페이지 API** | 8030 | http://localhost:8030 | 홈페이지 백엔드 API (문의, 뉴스레터) |
| **API Gateway** | 8000 | http://localhost:8000 | 중앙 라우팅 및 프록시 |
| **AI Image** | 8001 | http://localhost:8001 | Stable Diffusion 이미지 생성 |
| **AI Book** | 8002 | http://localhost:8002 | Claude 동화책 생성 |
| **Excel Automation** | 8011 | http://localhost:8011 | 엑셀 파일 자동화 |
| **Web Crawler** | 8012 | http://localhost:8012 | 웹 데이터 수집 |
| **Payment** | 8021 | http://localhost:8021 | 결제 및 구독 관리 |

### **통합 API 사용 (Gateway 경유)**
- **이미지 생성**: `POST /api/v1/ai/image/generate`
- **동화책 생성**: `POST /api/v1/ai/book/generate`  
- **엑셀 처리**: `POST /api/v1/automation/excel/analyze`
- **웹 크롤링**: `POST /api/v1/automation/crawler/crawl`
- **구독 관리**: `GET /api/v1/payment/plans`

## 💼 **비즈니스 모델**

### **구독 플랜**
- **베이직** (월 9,900원): 100토큰, 기본 기능
- **프리미엄** (월 19,900원): 500토큰, 고급 기능  
- **프로** (월 49,900원): 2000토큰, 모든 기능 + 지원

### **제공 서비스**
- 🎨 **AI 이미지 모음집** (Stable Diffusion, 12시간 업데이트)
- 📚 **AI 동화책 모음집** (Claude Sonnet 4 기반)
- 📊 **사무업무 자동화** (엑셀 병합/분석/변환)
- 🕷️ **웹 크롤링** (주가/뉴스 자동 수집)
- 🔄 **자동 업로더** (SNS 일괄 업로드)

## 🏗️ **기술 스택**

- **Backend**: FastAPI (Python 3.12+)
- **AI APIs**: Claude Sonnet 4, Stable Diffusion
- **Database**: PostgreSQL, Redis, MongoDB  
- **Infrastructure**: Docker, Nginx
- **Monitoring**: Structlog, Prometheus 준비
- **pk_system 통합**: 기존 자동화 함수 재사용

## 🎯 **개발 상태**

### ✅ **완성된 기능**
- [x] 완전한 MSA 아키텍처 구성
- [x] API Gateway 라우팅 시스템
- [x] AI Image Service (Stable Diffusion 준비)
- [x] AI Book Service (Claude 준비)  
- [x] Excel Automation (pk_system 통합)
- [x] Web Crawler Service (주가/뉴스)
- [x] Payment Service (구독/토큰 관리)
- [x] Docker 컨테이너화 완료
- [x] 개발/테스트 스크립트

### 🔄 **진행중**  
- [ ] 실제 AI API 연동 (Claude, Stable Diffusion)
- [ ] 데이터베이스 스키마 구현
- [ ] 실제 결제 게이트웨이 연동

### 📋 **계획중**
- [ ] 웹 프론트엔드 (React)
- [ ] 모니터링 시스템 (Prometheus + Grafana)
- [ ] CI/CD 파이프라인
- [ ] AWS 배포

## 📖 **문서**

더 자세한 기술 문서는 `docs/` 폴더를 참조하세요:
- **아키텍처 다이어그램**: `docs/architecture design.svg`
- **상세 기술 문서**: `docs/README.md`

## 🤝 **기여하기**

1. 이슈 등록 또는 기능 제안
2. 브랜치 생성 (`feature/기능명`)
3. 코드 작성 및 테스트
4. Pull Request 생성

## 📄 **라이선스**

MIT License

---

**현사AI (Smart Person AI)** - *현명한 사람들의 AI 시대*