# 🐧 WSL에서 Finance Investment Assistant API 실행 가이드

## 📋 사전 요구사항

### 1. WSL 설치 확인
```bash
wsl --list --verbose
```

### 2. Ubuntu WSL 설치 (권장)
```bash
wsl --install -d Ubuntu
```

## 🚀 빠른 시작

### 1단계: WSL 환경 설정
```bash
# WSL 터미널에서 실행
cd ~
wget https://raw.githubusercontent.com/your-repo/pkg_finance_invest_assist/main/scripts/setup_wsl.sh
chmod +x setup_wsl.sh
./setup_wsl.sh
```

### 2단계: 프로젝트 복사
```bash
# Windows 파일 시스템에서 WSL로 복사
cp -r /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist ~/projects/
cd ~/projects/pkg_finance_invest_assist
```

### 3단계: API 실행
```bash
# 실행 권한 부여
chmod +x scripts/*.sh

# API 실행
./scripts/run_api.sh
```

## 🛠️ 수동 설정 (선택사항)

### Python 환경 설정
```bash
# Python 3.11 설치
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev

# 가상환경 생성
python3 -m venv .venv
source .venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
```

### Docker 설치
```bash
# Docker 설치
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER

# WSL 재시작 후
docker --version
```

## 📊 서비스 포트

| 서비스 | 포트 | URL |
|--------|------|-----|
| API Gateway | 8000 | http://localhost:8000 |
| Recommendation Engine | 8001 | http://localhost:8001 |
| Finance API Client | 8002 | http://localhost:8002 |
| News Crawler | 8003 | http://localhost:8003 |

## 🧪 API 테스트

### 기본 테스트
```bash
# API Gateway 상태 확인
curl http://localhost:8000/

# 투자 타이밍 추천
curl "http://localhost:8000/api/v1/recommend/invest-timing?asset_name=삼성전자"

# 자산 가격 조회
curl "http://localhost:8000/api/v1/price/asset?asset_name=삼성전자"

# 뉴스 크롤링
curl "http://localhost:8000/api/v1/news/crawl?keywords=삼성전자,투자"
```

### 자동 테스트
```bash
./scripts/test_api.sh
```

## 📚 API 문서

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🛠️ 유용한 명령어

```bash
# 서비스 상태 확인
./scripts/status.sh

# 서비스 중지
./scripts/stop_api.sh

# 로그 확인
tail -f logs/gateway.log
tail -f logs/recommendation.log
tail -f logs/finance_api.log
tail -f logs/news_crawler.log

# Docker 서비스만 실행
cd infra
docker-compose up -d postgres redis
cd ..

# 개별 서비스 실행
cd gateway
uvicorn main:app --reload --port 8000
```

## 🔧 문제 해결

### 1. 포트 충돌
```bash
# 포트 사용 확인
sudo netstat -tulpn | grep :8000

# 프로세스 종료
sudo kill -9 <PID>
```

### 2. 권한 문제
```bash
# 스크립트 실행 권한
chmod +x scripts/*.sh

# Docker 권한
sudo usermod -aG docker $USER
newgrp docker
```

### 3. 의존성 문제
```bash
# 가상환경 재생성
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. Docker 문제
```bash
# Docker 서비스 재시작
sudo service docker restart

# 컨테이너 정리
docker system prune -a
```

## 🌐 브라우저에서 접근

WSL에서 실행된 API는 Windows 브라우저에서도 접근 가능합니다:

- http://localhost:8000/docs
- http://localhost:8001/docs
- http://localhost:8002/docs
- http://localhost:8003/docs

## 📝 개발 팁

### 1. 코드 수정 시 자동 재시작
FastAPI의 `--reload` 옵션으로 코드 수정 시 자동 재시작됩니다.

### 2. 로그 모니터링
```bash
# 실시간 로그 확인
tail -f logs/*.log

# 특정 서비스 로그
tail -f logs/gateway.log
```

### 3. 환경 변수 설정
```bash
# .env 파일 생성
cp env.example .env

# 환경 변수 수정
nano .env
```

## 🎯 다음 단계

1. **실제 금융 API 연동**: Yahoo Finance, Alpha Vantage 등
2. **데이터베이스 스키마 설계**: PostgreSQL 테이블 생성
3. **인증 시스템 추가**: JWT 토큰 기반 인증
4. **프론트엔드 개발**: React/Vue.js 웹 애플리케이션
5. **배포**: AWS EC2, Docker Swarm 등

## 📞 지원

문제가 발생하면 다음을 확인해주세요:

1. WSL 버전: `wsl --version`
2. Python 버전: `python3 --version`
3. Docker 버전: `docker --version`
4. 서비스 로그: `tail -f logs/*.log` 