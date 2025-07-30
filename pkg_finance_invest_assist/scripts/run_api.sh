#!/bin/bash

# WSL에서 Finance Investment Assistant API 실행 스크립트

set -e

echo "🚀 Finance Investment Assistant API를 시작합니다..."

# 현재 디렉토리 확인
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt 파일을 찾을 수 없습니다."
    echo "프로젝트 루트 디렉토리에서 실행해주세요."
    exit 1
fi

# 환경 변수 설정
export DATABASE_URL="postgresql://finance_user:finance_password@localhost:5432/finance_db"
export REDIS_URL="redis://localhost:6379"

# 가상환경 생성 및 활성화
echo "🐍 Python 가상환경 설정 중..."
if [ ! -d ".venv" ]; then
    echo "가상환경을 생성합니다..."
    python3 -m venv .venv
fi

source .venv/bin/activate

# 의존성 설치
echo "📦 의존성 설치 중..."
pip install --upgrade pip
pip install -r requirements.txt

# 로그 디렉토리 생성
mkdir -p logs

# Docker 서비스 시작 (백그라운드)
echo "🐳 Docker 서비스 시작 중..."
if command -v docker-compose &> /dev/null; then
    cd infra
    docker-compose up -d postgres redis
    cd ..
    echo "✅ PostgreSQL과 Redis가 시작되었습니다."
else
    echo "⚠️  Docker Compose가 설치되지 않았습니다."
    echo "Docker 없이 API만 실행합니다."
fi

# API 서비스 실행
echo "🌐 API 서비스들을 시작합니다..."

# API Gateway 실행 (백그라운드)
echo "🚪 API Gateway 시작 중..."
cd gateway
uvicorn main:app --host 0.0.0.0 --port 8000 --reload > ../logs/gateway.log 2>&1 &
GATEWAY_PID=$!
cd ..

# Recommendation Engine 실행 (백그라운드)
echo "🧠 Recommendation Engine 시작 중..."
cd recommend-engine
uvicorn main:app --host 0.0.0.0 --port 8001 --reload > ../logs/recommendation.log 2>&1 &
RECOMMENDATION_PID=$!
cd ..

# Finance API Client 실행 (백그라운드)
echo "💰 Finance API Client 시작 중..."
cd finance-api-client
uvicorn main:app --host 0.0.0.0 --port 8002 --reload > ../logs/finance_api.log 2>&1 &
FINANCE_API_PID=$!
cd ..

# News Crawler 실행 (백그라운드)
echo "📰 News Crawler 시작 중..."
cd news-crawler
uvicorn main:app --host 0.0.0.0 --port 8003 --reload > ../logs/news_crawler.log 2>&1 &
NEWS_CRAWLER_PID=$!
cd ..

# PID 파일 저장
echo $GATEWAY_PID > logs/gateway.pid
echo $RECOMMENDATION_PID > logs/recommendation.pid
echo $FINANCE_API_PID > logs/finance_api.pid
echo $NEWS_CRAWLER_PID > logs/news_crawler.pid

# 서비스 상태 확인
echo "⏳ 서비스 시작 대기 중..."
sleep 5

echo "✅ 모든 API 서비스가 시작되었습니다!"
echo ""
echo "📊 서비스 URL:"
echo "  - API Gateway: http://localhost:8000"
echo "  - Recommendation Engine: http://localhost:8001"
echo "  - Finance API Client: http://localhost:8002"
echo "  - News Crawler: http://localhost:8003"
echo ""
echo "📚 API 문서:"
echo "  - Swagger UI: http://localhost:8000/docs"
echo "  - ReDoc: http://localhost:8000/redoc"
echo ""
echo "🛠️  유용한 명령어:"
echo "  - 로그 확인: tail -f logs/*.log"
echo "  - 서비스 중지: ./scripts/stop_api.sh"
echo "  - 상태 확인: ./scripts/status.sh"
echo ""
echo "💡 테스트 예시:"
echo "  curl 'http://localhost:8000/api/v1/recommend/invest-timing?asset_name=삼성전자'"
echo "  curl 'http://localhost:8000/api/v1/price/asset?asset_name=삼성전자'"
echo "  curl 'http://localhost:8000/api/v1/news/crawl?keywords=삼성전자,투자'"

# 대기
echo ""
echo "🔄 API 서비스가 실행 중입니다. Ctrl+C로 중지할 수 있습니다."
wait 