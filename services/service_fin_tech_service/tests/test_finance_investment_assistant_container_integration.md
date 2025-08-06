# Finance Investment Assistant 컨테이너 통합 테스트

이 프로젝트는 WSL 환경에서 Finance Investment Assistant 컨테이너 통합 테스트를 자동화하는 Python 코드입니다.

## 📁 파일 구조

```
pkg_py/
├── functions_split/
│   └── pk_ensure_smart_person_ai_container_build_tested.py  # 메인 함수
├── workspace/
│   ├── pk_ensure_smart_person_ai_container_build_tested.py  # 컨테이너 통합 테스트 wrapper
│   ├── test_finance_investment_assistant_container_integration.py  # 테스트 실행 스크립트
│   └── test_finance_investment_assistant_container_integration.md  # 이 파일
```

## 🚀 사용법

### 1. 직접 실행 (function_split)

```python
from pkg_py.functions_split.pk_ensure_smart_person_ai_container_build_tested import function_split

# 함수 실행
result = function_split()
```

### 2. 컨테이너 통합 테스트 wrapper 사용

```python
from pkg_py.pk_ensure_smart_person_ai_container_build_tested import ensure_smart_person_ai_container_builded_at_wsl

# wrapper 함수 실행
result = ensure_smart_person_ai_container_builded_at_wsl()
```

### 3. 테스트 스크립트 실행

```bash
# 프로젝트 루트에서 실행
python pkg_py/workspace/test_finance_investment_assistant_container_integration.py
```

## 🔧 테스트 단계

1. **WSL 환경 확인** - Ubuntu-24.04 접근 가능 여부 확인
2. **Docker 설치 확인** - Docker 및 Docker Compose 설치 상태 확인
3. **프로젝트 디렉토리 접근** - smart_person_ai 프로젝트 경로 접근 확인
4. **환경 설정** - .env 파일 복사 및 필요한 디렉토리 생성
5. **Docker 컨테이너 빌드** - 모든 서비스 컨테이너 빌드
6. **컨테이너 시작** - Docker Compose로 전체 스택 실행
7. **컨테이너 상태 확인** - 실행 중인 컨테이너 상태 확인
8. **서비스 헬스체크** - 각 서비스의 /health 엔드포인트 테스트
9. **결과 요약** - 테스트 결과 및 서비스 상태 출력
10. **컨테이너 정리** - 테스트 완료 후 컨테이너 정리

## 📊 테스트 대상 서비스

| 서비스 | 포트 | 설명 |
|--------|------|------|
| API Gateway | 8000 | 메인 API 게이트웨이 |
| Investment Advisor | 8001 | 투자 타이밍 추천 서비스 |
| Market Data | 8002 | 시장 데이터 서비스 |
| News Analyzer | 8003 | 뉴스 분석 서비스 |
| Nginx | 80 | 리버스 프록시 |

## ⚠️ 사전 요구사항

1. **WSL Ubuntu-24.04** 설치 및 설정
2. **Docker Desktop** 설치 (WSL 2 백엔드 활성화)
3. **Finance Investment Assistant 프로젝트** 경로: `/mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist`

## 🐛 문제 해결

### WSL 접근 문제
```bash
# WSL 배포판 목록 확인
wsl --list --verbose

# Ubuntu-24.04가 설치되어 있는지 확인
wsl -d Ubuntu-24.04 -e bash -c "echo 'WSL 접근 성공'"
```

### Docker 설치 문제
```bash
# Docker Desktop 설치 확인
docker --version
docker-compose --version
```

### 프로젝트 경로 문제
```bash
# 프로젝트 디렉토리 존재 확인
ls -la /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist
```

## 📝 로그 확인

테스트 실행 중 발생하는 오류는 다음 명령어로 확인할 수 있습니다:

```bash
# WSL에서 직접 실행
wsl -d Ubuntu-24.04 -e bash -c "cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist/deployment && docker-compose logs"
```

## 🔄 재실행

테스트를 다시 실행하려면:

```bash
# 컨테이너 정리
wsl -d Ubuntu-24.04 -e bash -c "cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist/deployment && docker-compose down"

# 테스트 재실행
python pkg_py/workspace/test_smart_person_ai_container_build.py
```

## 📈 성공 지표

- ✅ 모든 컨테이너가 성공적으로 빌드됨
- ✅ 모든 서비스가 정상적으로 시작됨
- ✅ 모든 헬스체크 엔드포인트가 응답함
- ✅ nginx 리버스 프록시가 정상 작동함

## 🎯 테스트 결과 예시

```
🚀 WSL 환경에서 smart_person_ai 컨테이너 빌드 테스트 시작
============================================================

1️⃣ WSL 환경 확인 중...
✅ WSL 환경 확인 완료

2️⃣ Docker 설치 확인 중...
✅ Docker 설치 확인: Docker version 24.0.7

3️⃣ Docker Compose 설치 확인 중...
✅ Docker Compose 설치 확인: docker-compose version 1.29.2

4️⃣ 프로젝트 디렉토리 접근 확인 중...
✅ 프로젝트 디렉토리 접근 확인: /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist

5️⃣ 환경 설정 중...
✅ 환경 설정 완료

6️⃣ Docker 컨테이너 빌드 중...
✅ Docker 컨테이너 빌드 완료

7️⃣ 컨테이너 시작 중...
✅ 컨테이너 시작 완료

8️⃣ 컨테이너 상태 확인 중...
✅ 컨테이너 상태 확인 완료

9️⃣ 서비스 헬스체크 중...
✅ API Gateway 헬스체크 성공
✅ Investment Advisor 헬스체크 성공
✅ Market Data 헬스체크 성공
✅ News Analyzer 헬스체크 성공
✅ Nginx 헬스체크 성공

============================================================
📊 테스트 결과 요약
============================================================

🔍 컨테이너 상태:
Name                    Command               State           Ports
--------------------------------------------------------------------------------
finance_api_gateway     uv run uvicorn api_ ...   Up      0.0.0.0:8000->8000/tcp
finance_investment_ ... uv run uvicorn inv ...   Up      0.0.0.0:8001->8001/tcp
finance_market_data     uv run uvicorn mar ...   Up      0.0.0.0:8002->8002/tcp
finance_news_analyzer   uv run uvicorn new ...   Up      0.0.0.0:8003->8003/tcp
finance_nginx           nginx -g daemon off;      Up      0.0.0.0:80->80/tcp

🏥 서비스 헬스체크 결과:
  ✅ API Gateway: healthy
  ✅ Investment Advisor: healthy
  ✅ Market Data: healthy
  ✅ News Analyzer: healthy
  ✅ Nginx: healthy

🧹 컨테이너 정리 중...
✅ 컨테이너 정리 완료

🎉 WSL 환경에서 smart_person_ai 컨테이너 빌드 테스트 완료!
``` 