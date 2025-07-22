# pk_system

## 프로젝트 개요

**pk_system**은 Python 3.12+ 기반의 멀티 유틸리티/자동화/시스템 관리/데이터 처리/AI/멀티미디어 통합 툴킷입니다.  
WSL, Docker, uv, venv 환경에서 동작하며, 다양한 파일 포맷, 시스템, 네트워크, 멀티미디어, 자연어처리, 자동화, 테스트, 배포 기능을 제공합니다.

---

## 주요 폴더 및 파일 구조

- **pkg_py/** : 핵심 Python 유틸리티 및 시스템/자동화/데이터/AI/멀티미디어 모듈
  - 다양한 단일 목적 스크립트 및 시스템 레이어별 모듈(`pk_system_object.*.py`)
  - 예: 파일/디렉터리 관리, Git/Docker/WSL/윈도우 자동화, Youtube/Cloudflare/ChatGPT 등
- **tests/** : 테스트 코드(단위/통합/기능 테스트)
- **project_release_server/**, **project_vpc_test/** : 배포/테스트 관련 프로젝트 구조(현재 코드 없음)
- **docs_README.md** : 간단한 프로젝트 정보 및 pyproject.toml 안내
- **pyproject.toml** : 프로젝트 메타 정보, 의존성, 빌드/패키징 설정
- **docker-compose.yaml, *.Dockerfile** : Docker 기반 실행/배포 환경
- **pk_push_project_to_github.py** : Git 자동 커밋/푸시/상태 관리 스크립트
- **기타** : 다양한 데이터/포맷별 패키지 디렉터리(`pkg_csv`, `pkg_json`, `pkg_mp3` 등)

---

## 주요 기능

- **시스템/OS 관리** : 백업, 복원, 프로세스/윈도우/네트워크/환경변수 관리, 자동화
- **데이터 처리** : CSV, JSON, XLSX, 이미지, 사운드, 동영상 등 다양한 포맷 지원
- **멀티미디어** : Youtube 다운로드, 영상/음성 처리, 이미지 변환 등
- **네트워크/웹** : Cloudflare, Selenium, Playwright, FastAPI 등 지원
- **AI/자연어처리** : ChatGPT, Konlpy, OCR, 음성인식 등
- **자동화/유틸리티** : 파일/디렉터리/이름 일괄변경, 핫키, GUI, tmux, venv, Docker 등
- **테스트/배포** : pytest 기반 테스트, Git/Docker 자동화, 배포 스크립트

---

## 설치 및 실행

1. Python 3.12+ 환경 준비
2. 의존성 설치
   ```bash
   pip install -r requirements.txt
   # 또는
   pip install -e .  # pyproject.toml 기반
   ```
3. (선택) Docker 환경
   ```bash
   docker-compose up --build
   ```

---

## 테스트

- `tests/` 폴더 및 `pk_test_tests.py` 등에서 pytest 기반 테스트 제공
- 예시:
  ```bash
  pytest tests/
  ```

---

## 개발/기여

- 주요 기능별로 `pkg_py/` 내 스크립트 참고
- 의존성 및 환경설정은 `pyproject.toml` 참고
- 자동화/배포/테스트 스크립트 활용 가능

---

## 라이선스

MIT (임시, 추후 변경 가능)

---

## 기타

- 상세 기능/용어는 각 스크립트 및 pyproject.toml 참고
- release/tag 관리 및 환경별 실행은 Docker, WSL, venv, uv 등 지원
