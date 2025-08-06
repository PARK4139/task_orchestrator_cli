# pk_system

A comprehensive Python 3.12+ toolkit for automation, system management, data processing, AI, and multimedia.

## 🚀 Latest Updates (2025-08-04)

### ✅ **New Features**
- **Windows System Automation**: UV/FZF auto-installation, environment setup
- **MSA Investment Advisory System**: FastAPI-based microservices architecture
- **AI-Enhanced Development**: Cursor IDE + ChatGPT integration
- **프로젝트 메모 시스템**: 체계적인 업무 관리 및 아이디어 정리

### 🎯 **Current Status**
- AI 기술개발팀 업무 수행 중
- 자율주행 시스템 개발 및 테스트
- 비즈니스 자동화 파이프라인 구축

---

# 📋 프로젝트 메모 및 채팅방 내용 정리

## 주요 업무 내용 요약

### 🏢 업무 관련 메모
- **AI 기술개발팀** 소속으로 자율주행 관련 업무 수행
- **영상처리제어기(NX/NO)** 개발 및 테스트 업무
- **카메라 시스템** 제작 및 캘리브레이션
- **Flash 이미지** 생성 및 배포 관리
- **Jetson 하드웨어** 플래시 및 테스트 자동화

### 🛠 기술 스택 및 도구
- **개발 환경**: Python, FastAPI, Docker, WSL, Ubuntu
- **AI/ML**: NVIDIA Jetson, TensorRT, Computer Vision
- **하드웨어**: Jetson Xavier/Orin, 카메라 시스템
- **도구**: Git, SVN, MSI 노트북, VNC, SSH

### 💼 비즈니스 아이디어
- **AI 산출물 공급업**: AI 이미지, 동화책, 자동화 도구 판매
- **커스텀 AI 파이프라인**: 업무 프로세스 분석 → 견적 → 데모 → 구매
- **업무 자동화 교육**: AI 도구 사용법 교육 서비스
- **구독 모델**: 월 5,555원 × 2,000명 = 1,000만원 목표

## 🏗 시스템 아키텍처 설계

### 마이크로서비스 구조
```
├── services_controller (pk_system container)
│   ├── 중앙집중식 서비스 제어
│   ├── 응급상황 대응 시스템
│   └── CLI 기반 명령어 인터페이스
├── public_service_container
│   ├── 트래픽 분산 라우팅
│   ├── 로그인 게이트웨이
│   └── FastAPI 백엔드
├── public_database_container
│   └── PostgreSQL
├── private_service_container
│   └── 비즈니스 로직 서버
└── private_database_container
    └── PostgreSQL
```

### 하드웨어 환경
- **Server1**: NVIDIA Jetson AGX Xavier
- **Server2**: AWS EC2 / Ubuntu 24.04
- **Container**: Docker 기반 4개 컨테이너 구성
- **Deployment**: 점진적 확장 가능한 구조
- **Security**: Conway's Law 기반 조직 구조 반영

## 📊 데이터 및 프로세스 관리

### 매장 관리 프로세스 (수도코드)
```python
# 주방업무 프로세스
if 주방업무수행자.새식자재_구매:
    if 주방업무수행자.손질:
        주방업무수행자.조리()

# 홀업무 프로세스  
if 고객.주문(키오스크):
    고객.결제(키오스크)
    
if 호출벨.울림(주문비상대응):
    홀업무수행자.출동()
```

### 메모 관리 전략
- `pk_memo_working.pk`: 현재 진행 중인 TODO 항목
- `pk_memo_how.pk`: 완료된 작업 및 방법론
- 모든 작업은 텍스트 형태로 상세 기록
- 정기적인 백업 및 아카이빙

## 🔧 개발 도구 및 설정

### AI 코드베이스 관리
- **Cursor + Claude Sonnet 4**: AI 기반 코딩
- **Auto-run 모드**: 자동 테스트 실행
- **버전 관리**: v6.py 기준, 이전 버전은 `# ` prefix로 관리

### 테스트 환경
```bash
# pytest 설정
pytest --maxfail=1 --disable-warnings -v
pytest -s -v tests/test_function_cmd_to_os.py
```

### WSL 환경 설정
```bash
# UV 가상환경 설정
cd ~/Downloads/pk_system
uv venv .venv_linux
source .venv_linux/bin/activate
uv sync --active
```

## 🎯 프로젝트 목표 및 계획

### 단기 목표
1. **pk_system** 기능 최적화
2. **비즈니스 데모** 완성
3. **투자 보조 시스템** 개발
4. **자동화 파이프라인** 구축

### 장기 비전
- AI 기반 업무 자동화 플랫폼 구축
- B2C 구독 서비스 런칭  
- 글로벌 확장 (네이버/카카오 클라우드 → AWS Seoul)
- Conway's Law 기반 조직 구조 최적화

## 📈 수익 모델

### 현재 계획
- **AI 산출물 판매**: 이미지, 동화책, 자동화 도구
- **커스텀 파이프라인**: 건당 500만원
- **교육 서비스**: 업무 자동화 교육
- **구독 서비스**: 월 구독료 기반

### 목표 매출
- 2,000명 × 월 5,555원 = 월 1,000만원
- 연간 1.2억원 매출 목표

## 🏥 건강 관리

### 식단 관리
- 아침: 블루베리 + 그릭요거트 + 견과류
- 점심: 야채 + 계란국 + 밥 (소주잔 크기)
- 간헐적 단식 실천

### 운동 계획
- 풀업/데드리프트: 12회 3세트
- 바벨로우
- 필라테스 동작 포함

## 🛍 구매 계획 및 물품 관리

### 업무용 구매 목록
- DC 파워서플라이 (OPE-3020S)
- 카메라 제작 소모품 (실리콘, 실린지, 지퍼팩)
- 서랍장 (철재, 2단)
- 시작실 가구 선정

### 개인 구매 목록
- 유니클로 에어리즘 티셔츠 (화이트 S/M/L)
- 카시오 시계 LTP-V007L-7B1
- 커스텀어클락 티셔츠
- 큐라덴 전동 음파칫솔

## 🎮 개인 프로젝트

### 유튜브 콘텐츠 제작
- **채널명**: "우울남의 이상한 브이로그"
- **목표**: 하루 10개 채널에 5개 영상 업로드
- **파이프라인**: 기획 → 촬영 → 편집 → 자막 → 업로드

### 게임/스토리 아이디어
- 알파인 인디안 종족
- 우울남 캐릭터 시리즈
- 힐링 게임 컨셉

## 📝 메모 작성 규칙

### 태그 시스템
- `[TODO]`: 해야 할 일
- `[how]`: 방법론 및 완료된 작업  
- `[done]`: 완료된 작업
- `[archived]`: 보관된 내용

### 구분선 사용
```
_________________________________________________________________
```
각 메모 섹션은 위 구분선으로 분리

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.12+
- UV package manager
- Docker (optional)

### Quick Start
```bash
# Clone the repository
git clone https://github.com/your-username/pk_system.git
cd pk_system

# Setup virtual environment
uv venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate     # Windows

# Install dependencies
uv sync

# Run the system
python run.py
```

### Windows Setup
```batch
# Run the Windows setup script
ensure_pk_system_enabled_windows.bat
```

### Linux Setup
```bash
# Run the Linux setup script
./ensure_python_venv_setup.sh
```

## 📚 Documentation

- **Korean README**: [README_KOREAN.md](README_KOREAN.md)
- **English README**: [README_ENGLISH.md](README_ENGLISH.md)
- **Dictionary**: [dictionary.md](dictionary.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*이 문서는 pk_memo_working.pk와 pk_memo_how.pk 파일의 내용을 요약하고 정리한 것입니다. 지속적으로 업데이트하여 프로젝트의 진행 상황과 아이디어를 체계적으로 관리하고 있습니다.*