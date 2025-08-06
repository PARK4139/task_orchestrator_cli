#!/bin/bash

# WSL에서 Finance Investment Assistant 빠른 테스트 스크립트

echo "🚀 WSL에서 Finance Investment Assistant 빠른 테스트를 시작합니다..."
echo ""

# 현재 디렉토리 확인
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt 파일을 찾을 수 없습니다."
    echo "프로젝트 루트 디렉토리에서 실행해주세요."
    exit 1
fi

# Python 버전 확인
echo "🐍 Python 버전 확인..."
python3 --version

# 가상환경 생성 및 활성화
echo "📦 가상환경 설정 중..."
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

# 간단한 API 테스트 (Docker 없이)
echo "🧪 간단한 API 테스트를 시작합니다..."

# Gateway만 실행하여 테스트
echo "🚪 API Gateway 시작 중..."
cd gateway
uvicorn main:app --host 0.0.0.0 --port 8000 --reload > ../logs/gateway_test.log 2>&1 &
GATEWAY_PID=$!
cd ..

# 잠시 대기
sleep 3

echo "✅ API Gateway가 시작되었습니다!"
echo "📊 서비스 URL: http://localhost:8000"
echo "📚 API 문서: http://localhost:8000/docs"
echo ""

# 기본 테스트
echo "🧪 기본 API 테스트..."
curl -s http://localhost:8000/ | jq . || echo "API Gateway에 연결할 수 없습니다."

echo ""
echo "💡 테스트 예시:"
echo "  - 브라우저에서 http://localhost:8000/docs 접속"
echo "  - curl 'http://localhost:8000/api/v1/recommend/invest-timing?asset_name=삼성전자'"
echo ""

echo "🔄 API Gateway가 실행 중입니다. Ctrl+C로 중지할 수 있습니다."
echo "PID: $GATEWAY_PID"

# 대기
wait 