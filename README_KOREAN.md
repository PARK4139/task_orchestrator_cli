# pk_system

## 작성자
Earth / Korean / Anyang / Jung hoon Park

## 프로젝트 개요

**pk_system**은 Python 3.12+ 기반의 자동화, 시스템 관리, 데이터 처리, AI, 멀티미디어를 위한 다목적 툴킷입니다.  
WSL, Docker, uv, venv 환경에서 실행되며, 다양한 파일 형식, 시스템 작업, 네트워킹, 멀티미디어, 자연어 처리, 자동화, 테스트, 배포 기능을 지원합니다.

### AI 기반 개발
이 프로젝트는 생산성과 코드 품질을 향상시키기 위해 최신 AI 개발 도구를 활용합니다:

- **🖥️ [Cursor](https://cursor.sh/)**: AI 기반 코드 완성, 리팩토링, 지능형 지원이 가능한 주요 IDE
- **🤖 [ChatGPT](https://chat.openai.com/)**: 코드 생성, 디버깅, 아키텍처 결정을 위한 AI 어시스턴트
- **🧠 AI 강화 워크플로우**: 빠른 프로토타이핑, 테스트, 최적화를 위한 AI를 활용한 반복적 개발

개발 과정은 인간의 전문성과 AI 기능을 결합하여 견고하고 유지보수 가능한 코드를 생성하면서 개발 주기를 가속화합니다.

---

## 🚀 **최신 프로젝트 상태 (2025-01-XX)**

### ✅ **완료된 주요 프로젝트**

#### **1. MSA 투자 자문 시스템** (`pkg_finance_invest_assist/`)
- **✅ 완료**: Docker + WSL 환경 구축, API Gateway, PostgreSQL + Redis 연동
- **✅ 완료**: pyproject.toml + uv 마이그레이션, 의존성 관리 현대화
- **🔄 진행중**: 투자 타이밍 추천 로직 구현
- **❌ 미구현**: 뉴스 크롤링, 자산 가격 모니터링, Django 웹 인터페이스

#### **2. 핵심 시스템 도구들**
- **✅ 완료**: 시스템 자동화, 프로세스 관리, 멀티미디어 처리
- **✅ 완료**: AI 통합 (ChatGPT, OCR, 음성인식)
- **✅ 완료**: 네트워크/웹 도구 (Selenium, FastAPI, Cloudflare)

#### **3. Windows 시스템 자동화 개선** (2025-01-XX)
- **✅ 완료**: Windows 레지스트리 핸들 오류 수정
- **✅ 완료**: 환경변수 설정 로직 개선 (`D_BUSINESS_DEMO` 포함)
- **✅ 완료**: UI/UX 개선 (이모지 제거, 메시지 정리)
- **✅ 완료**: UV, FZF 설치 및 PATH 설정 자동화
- **✅ 완료**: Business Demo 디렉토리 자동 생성

### 🎯 **현재 개발 중인 프로젝트**

#### **MSA 투자 자문 시스템** - Phase 1 진행중
- **기술 스택**: FastAPI, Docker, PostgreSQL, Redis, WSL
- **개발 환경**: "Windows에서 편집, WSL에서 실행" 방식
- **의존성 관리**: uv + pyproject.toml (requirements.txt 대체)
- **API 상태**: 
  - ✅ Gateway: `http://[WSL_IP]:8000/docs` (Swagger UI)
  - 🔄 Recommendation Engine: 투자 타이밍 분석 로직 구현 중
  - ❌ Finance API: 외부 금융 API 연동 필요
  - ❌ News Crawler: 뉴스 수집 및 감정 분석 필요

### 📋 **다음 단계 계획**

#### **Phase 1: 핵심 API 구현 (우선순위)**
1. **투자 타이밍 추천 로직** - 기술적 지표 기반 분석 알고리즘
2. **자산 가격 조회** - 외부 금융 API 연동 (Yahoo Finance, Alpha Vantage 등)
3. **뉴스 크롤링** - BeautifulSoup/Selenium을 활용한 뉴스 수집

#### **Phase 2-4: 고급 기능**
- 머신러닝 모델 및 예측 알고리즘
- Django 웹 인터페이스 및 사용자 관리
- 보안 시스템 (JWT 토큰 기반)
- 모니터링 및 로깅 시스템

---

## 주요 폴더 및 파일 구조

- **pkg_py/** : 시스템/자동화/데이터/AI/멀티미디어를 위한 핵심 Python 유틸리티
  - **functions_split/** : 윈도우/프로세스/네트워크/파일/자동화/번역/크롤링 등을 위한 수많은 단일 목적 스크립트
  - **system_object/** : 상태 관리, 파일/디렉토리/인코딩/색상/키맵 및 기타 시스템 객체를 위한 유틸리티
  - **refactor/** : 코드 자동화, 리팩토링, 모듈/파일 이름 변경, 메타 프로그래밍을 위한 도구
  - **workspace/** : 워크스페이스 관리 및 통합 실행/상태 제어
  - **독립 실행 스크립트** : 프로세스/윈도우/네트워크/멀티미디어/자동화/테스트/배포를 위한 다양한 스크립트
- **pkg_finance_invest_assist/** : **🆕 MSA 투자 자문 시스템** (최신 프로젝트)
  - **api_gateway/** : FastAPI 기반 API Gateway
  - **investment_advisor/** : 투자 추천 엔진
  - **market_data/** : 금융 데이터 API 클라이언트
  - **news_analyzer/** : 뉴스 크롤링 서비스
  - **shared/** : 공통 설정 및 데이터베이스 모듈
  - **deployment/** : Docker Compose 및 Nginx 설정
- **pkg_windows/** : **🆕 Windows 시스템 자동화 도구** (최신 추가)
  - **ensure_pk_system_enabled.py** : UV, FZF, Python 가상환경 자동 설치 및 설정
  - **Windows 레지스트리 관리** : 환경변수 설정 및 PATH 구성
  - **시스템 자동화** : 데스크톱 바로가기 생성, AutoRun 등록
- **tests/** : pytest 기반 단위/통합 테스트
- **docker-compose.yaml, *.Dockerfile** : Docker 기반 실행/배포 환경
- **pyproject.toml** : 프로젝트 메타데이터, 의존성, 빌드/패키징 설정
- **기타** : 다양한 데이터/미디어/문서 패키지 디렉토리 (`pkg_csv`, `pkg_json`, `pkg_mp3` 등 — 게시 시 주의)

---

## 주요 기능

- **시스템/OS 관리** : 프로세스/윈도우/네트워크/환경 관리, 백업/복원, 자동화
- **데이터 처리** : CSV, JSON, XLSX, 이미지, 사운드, 비디오 등 지원
- **멀티미디어** : YouTube 다운로드, 비디오/오디오 처리, 이미지 변환 등
- **네트워크/웹** : Cloudflare, Selenium, Playwright, FastAPI 등과의 통합
- **AI/NLP** : ChatGPT, Konlpy, OCR, 음성인식 등
- **자동화/유틸리티** : 배치 파일/디렉토리/이름 변경, 핫키, GUI, tmux, venv, Docker 등
- **테스트/배포** : pytest 기반 테스트, Git/Docker 자동화, 배포 스크립트
- **🆕 MSA 아키텍처** : Docker 오케스트레이션을 통한 마이크로서비스 기반 투자 자문 시스템
- **🆕 Windows 자동화** : UV, FZF 설치, 환경변수 설정, 시스템 구성 자동화

---

## 주요 모듈/스크립트 예시

- **functions_split/**  
  - 윈도우/프로세스 제어, 파일/디렉토리 관리, 번역, 크롤링, 자동화, 스크린샷, 네트워킹, 데이터 변환 등
- **system_object/**  
  - 시스템 상태 관리, 파일/디렉토리/인코딩/색상/키맵 유틸리티
- **refactor/**  
  - 코드 자동화, 함수/모듈 분할, 배치 이름 변경, 메타 프로그래밍
- **workspace/**  
  - 워크스페이스 통합, 실행/상태 관리
- **🆕 pkg_finance_invest_assist/**  
  - MSA 투자 자문 시스템: API Gateway, 추천 엔진, 금융 데이터, 뉴스 크롤링
- **🆕 pkg_windows/**  
  - Windows 시스템 자동화: UV/FZF 설치, 환경변수 설정, 레지스트리 관리

---

## 설치 및 사용법

### 빠른 시작 (Windows)
1. **설치 스크립트 실행**:
   ```cmd
   cd pk_system
   ensure_pk_system_enabled.cmd
   ```
   이 스크립트는 다음을 수행합니다:
   - uv 패키지 관리자 설치 및 구성
   - 퍼지 검색을 위한 fzf 설치
   - Python 가상 환경 설정
   - PATH 환경 변수 구성
   - 데스크톱 바로가기 생성
   - Business Demo 디렉토리 자동 생성

### 수동 설치
1. Python 3.12+ 환경을 준비합니다.
2. [uv](https://github.com/astral-sh/uv)를 사용하여 의존성을 설치합니다 (권장):
   ```bash
   # uv가 설치되지 않은 경우 설치
   pip install uv

   # pyproject.toml에 정의된 모든 의존성 설치
   uv pip install -e .
   ```
   - 이 프로젝트는 기존 venv/pip 대신 uv를 패키지 및 의존성 관리자로 사용합니다.
   - 설치 및 실행 시 uv를 사용해야 합니다.
3. (선택사항) Docker 환경  
   *Docker 기반 오케스트레이션 (docker-compose)은 개발 중이며 아직 지원되지 않습니다.*

### 🆕 **Windows 시스템 자동화 (최신 기능)**

#### **자동 설치 및 설정**
```cmd
# Windows에서 시스템 자동화 실행
cd pk_system
python pkg_windows/ensure_pk_system_enabled.py
```

이 스크립트는 다음을 자동으로 수행합니다:
- **UV 패키지 관리자** 설치 및 검증
- **FZF 퍼지 검색 도구** 설치 및 검증
- **Python 가상환경** 설정 및 PATH 구성
- **Business Demo 디렉토리** 자동 생성
- **환경변수 설정** (`D_BUSINESS_DEMO` 포함)
- **데스크톱 바로가기** 생성
- **AutoRun 등록** (명령 프롬프트 자동 실행)

#### **설정 확인**
```cmd
# 설치된 도구들 확인
uv --version
fzf --version
python --version

# 환경변수 확인
echo %PATH%
echo %D_BUSINESS_DEMO%
```

### 🆕 **MSA 투자 자문 시스템 실행 (WSL 환경)**

#### **1. WSL 환경 설정**
```bash
# WSL에서 프로젝트 디렉토리로 이동
cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist

# Docker 권한 설정
sudo usermod -aG docker $USER
newgrp docker
```

#### **2. MSA 서비스 실행**
```bash
# 모든 서비스 시작 (PostgreSQL, Redis, Gateway, 추천 엔진 등)
./scripts/docker_uv_sync.sh

# 또는 개별 서비스 테스트
./scripts/wsl_quick_test.sh
```

#### **3. API 테스트**
```bash
# WSL IP 확인
wsl hostname -I

# Windows 브라우저에서 Swagger UI 접속
explorer.exe http://[WSL_IP]:8000/docs
```

---

## 테스트

- pytest 기반 테스트는 `tests/` 폴더와 `pk_test_tests.py` 같은 스크립트에서 제공됩니다
- 예시:
  ```bash
  pytest tests/
  ```

### 🆕 **Windows 시스템 자동화 테스트**
```cmd
# 시스템 설정 확인
python pkg_windows/ensure_pk_system_enabled.py

# 개별 도구 테스트
uv --version
fzf --version
```

### 🆕 **MSA API 테스트**
```bash
# API Gateway 상태 확인
curl "http://[WSL_IP]:8000/"

# 투자 타이밍 추천 테스트 (구현 중)
curl "http://[WSL_IP]:8000/api/v1/recommend/invest-timing?asset_name=삼성전자"
```

---

## 프로젝트 구조 및 명명 규칙

### 파일 명명 규칙
- **`pk_` 접두사 파일**: 호출 전용 래퍼 함수
  - **`pkg_py/`에서**: 주요 진입점 래퍼 (예: `pk_ensure_chatGPT_responded.py`)
  - **`functions_split/`에서**: 내부 유틸리티 래퍼
  - 예시: `pkg_py/pk_ensure_chatGPT_responded.py` → `functions_split/ensure_chatGPT_responded()` 호출
- **`ensure_` 접두사 파일**: 실제 함수 구현
  - **위치**: 반드시 `functions_split/` 폴더에 있어야 함
  - 예시: `functions_split/ensure_chatGPT_responded.py` → `ensure_chatGPT_responded()` 함수 포함
- **함수 명명**: 함수는 `ensure_` 패턴으로 시작해야 함

### 함수 명명 패턴
이 프로젝트는 일관성과 명확성을 위해 세 가지 주요 함수 명명 패턴을 적극적으로 사용합니다:

#### **`ensure_` 패턴** - 보장된 실행
- **목적**: 특정 상태나 조건이 달성되도록 보장
- **동작**: 원하는 결과를 보장하기 위해 작업 수행
- **예시**:
  - `ensure_youtube_cookies_available()` - YouTube 쿠키가 준비되도록 보장
  - `ensure_potplayer_started()` - PotPlayer가 실행되도록 보장
  - `ensure_printed()` - 출력이 표시되도록 보장
  - `ensure_colorama_initialized_once()` - colorama가 초기화되도록 보장

#### **`get_` 패턴** - 데이터 검색
- **목적**: 부작용 없이 데이터를 검색하거나 계산
- **동작**: 시스템 상태를 수정하지 않고 값 반환
- **예시**:
  - `get_youtube_video_metadata()` - 비디오 정보 검색
  - `get_image_names_from_tasklist()` - 프로세스 목록 가져오기
  - `get_values_from_historical_file_routine()` - 히스토리 데이터 읽기
  - `get_nx()` - 다음 식별자 가져오기

#### **`set_` 패턴** - 상태 구성
- **목적**: 시스템 상태 구성 또는 수정
- **동작**: 설정 변경 또는 상태 업데이트
- **예시**:
  - `set_window_title()` - 윈도우 제목 변경
  - `set_environment_variables()` - 환경 구성
  - `set_database_values()` - 데이터베이스 항목 업데이트

#### **패턴 사용 가이드라인**
- **`ensure_`**: 함수가 성공하거나 실패를 우아하게 처리해야 할 때 사용
- **`get_`**: 부작용이 없는 순수 데이터 검색 함수에 사용
- **`set_`**: 시스템 상태나 구성을 명시적으로 수정할 때 사용
- **일관성**: 모든 새 함수에서 이 패턴 유지
- **명확성**: 패턴이 즉시 함수의 목적과 동작을 나타냄

### 디렉토리 구조
```
pkg_py/
├── functions_split/          # 핵심 함수 구현
│   ├── ensure_*.py          # 실제 함수 구현
│   ├── pk_*.py             # 내부 유틸리티 래퍼
│   └── other_*.py          # 유틸리티 함수
├── pk_*.py                 # 주요 진입점 래퍼
├── system_object/           # 시스템 상태 관리
├── refactor/               # 코드 자동화 도구
└── workspace/              # 워크스페이스 관리

🆕 pkg_finance_invest_assist/  # MSA 투자 자문 시스템
├── api_gateway/                # API Gateway (FastAPI)
├── investment_advisor/         # 투자 추천 엔진
├── market_data/               # 금융 데이터 API
├── news_analyzer/             # 뉴스 크롤링 서비스
├── shared/                    # 공통 모듈
├── deployment/                # Docker 설정
└── scripts/                   # 실행 스크립트

🆕 pkg_windows/  # Windows 시스템 자동화 도구
├── ensure_pk_system_enabled.py  # 자동 설치 및 설정
├── windows_registry_manager.py # 레지스트리 관리
└── system_automation.py       # 시스템 구성 자동화
```

### 설치 진입점
- **주요 설치**: `ensure_pk_system_enabled.cmd` (Windows)
- **자동화된 설정**: uv, fzf, Python venv 설치 및 PATH 구성
- **데스크톱 바로가기**: 쉬운 접근을 위한 런처 바로가기 생성

### 파일 구성 예시
```
# 주요 진입점 (pkg_py/)
pkg_py/pk_ensure_chatGPT_responded.py
├── pk_ensure_chatGPT_responded()  # 주요 래퍼 함수
├── ask_simple_question()          # 편의 함수
└── ask_with_custom_prompt()       # 추가 유틸리티

# 실제 구현 (functions_split/)
pkg_py/functions_split/ensure_chatGPT_responded.py
├── ensure_chatGPT_responded()     # 핵심 구현 (ensure_ 패턴)
├── get_chat_history()             # 데이터 검색 (get_ 패턴)
└── set_chat_settings()            # 구성 (set_ 패턴)

# functions_split/의 패턴 예시
pkg_py/functions_split/
├── ensure_youtube_cookies_available.py    # 보장된 실행
├── get_youtube_video_metadata.py          # 데이터 검색
├── set_window_title.py                    # 상태 구성
├── ensure_potplayer_started.py            # 보장된 실행
├── get_image_names_from_tasklist.py       # 데이터 검색
└── set_environment_variables.py           # 상태 구성

🆕 # MSA 투자 자문 시스템 예시
pkg_finance_invest_assist/
├── api_gateway/main.py               # API Gateway (FastAPI)
├── investment_advisor/main.py         # 투자 추천 서비스
├── market_data/main.py               # 금융 데이터 서비스
├── news_analyzer/main.py             # 뉴스 크롤링 서비스
└── shared/config.py                  # 공통 설정

🆕 # Windows 시스템 자동화 예시
pkg_windows/
├── ensure_pk_system_enabled.py        # 자동 설치 및 설정
├── windows_registry_manager.py       # 레지스트리 관리
└── system_automation.py              # 시스템 구성 자동화
```

## 개발/기여

### 개발 환경
- **IDE**: AI 기반 지원이 가능한 [Cursor](https://cursor.sh/)
- **AI 어시스턴트**: 코드 생성 및 디버깅을 위한 [ChatGPT](https://chat.openai.com/)
- **워크플로우**: 빠른 프로토타이핑을 위한 AI 강화 반복적 개발
- **🆕 MSA 개발**: "Windows에서 편집, WSL에서 실행" 방식

### 개발 가이드라인
- 각 주요 기능에 대해 `pkg_py/`의 스크립트 참조
- 의존성 및 환경 설정을 위해 `pyproject.toml` 참조
- 필요에 따라 자동화/배포/테스트 스크립트 사용
- 새 함수에 대해 위의 명명 규칙 준수
- **🆕 MSA 가이드라인**: 
  - 각 마이크로서비스는 독립적으로 개발
  - API Gateway를 통한 통신
  - Docker Compose로 전체 환경 관리

### AI 강화 개발 과정
1. **🖥️ Cursor IDE**: AI 기반 코드 완성 및 리팩토링 사용
2. **🤖 ChatGPT**: 복잡한 로직, 디버깅, 최적화를 위한 AI 활용
3. **🧠 반복적 개발**: 인간의 전문성과 AI 기능 결합
4. **📝 코드 리뷰**: AI 지원 코드 리뷰 및 개선 제안
5. **🚀 빠른 프로토타이핑**: 기능 개발 가속화를 위한 AI 사용

### 모범 사례
- **인간 감독**: AI 생성 코드를 항상 검토하고 검증
- **테스트**: AI 지원 기능의 포괄적 테스트 보장
- **문서화**: AI 강화 구성 요소에 대한 명확한 문서 유지
- **버전 관리**: AI 지원 커밋과 함께 적절한 Git 워크플로우 사용
- **🆕 MSA 모범 사례**:
  - 각 서비스별 독립적인 테스트
  - API 문서화 (Swagger UI)
  - Docker 이미지 최적화
  - 환경별 설정 분리

---

## 라이선스

MIT (임시, 변경 가능)

---

## 참고사항 및 경고

- 게시 시 `.gitignore`를 사용하여 민감한 데이터, 자격 증명, 세션/로그/미디어/문서 파일, 내부/기밀 자료를 제외해야 합니다
- 자세한 기능/용어는 각 스크립트와 `pyproject.toml`을 참조하세요
- 릴리스/태그 관리 및 다중 환경 실행 (Docker, WSL, venv, uv 등) 지원
- **🆕 MSA 참고사항**: 
  - WSL IP 주소는 재시작 시 변경될 수 있음
  - Docker 컨테이너는 WSL 환경에서만 실행
  - Windows 브라우저에서 WSL IP로 접속 필요 