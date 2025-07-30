#!/bin/bash

# Docker + uv sync 개발 환경 스크립트

echo "🐳 Docker + uv sync 개발 환경을 시작합니다..."
echo ""

# 현재 디렉토리 확인
if [ ! -f "pyproject.toml" ]; then
    echo "❌ pyproject.toml 파일을 찾을 수 없습니다."
    echo "프로젝트 루트 디렉토리에서 실행해주세요."
    exit 1
fi

# Docker 상태 확인
echo "🔍 Docker 상태 확인 중..."
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker가 실행되지 않았습니다."
    echo "Docker Desktop을 시작해주세요."
    exit 1
fi

# 기존 컨테이너 정리
echo "🧹 기존 컨테이너 정리 중..."
docker-compose -f deployment/docker-compose.yml down

# 데이터베이스 서비스 시작
echo "🗄️ 데이터베이스 서비스 시작 중..."
cd deployment
docker-compose up -d postgres redis
cd ..

# 잠시 대기
sleep 5

# API 서비스 빌드 및 시작 (uv sync 사용)
echo "🏗️ API 서비스 빌드 중 (uv sync 사용)..."
cd deployment
docker-compose build api_gateway
docker-compose up -d api_gateway
cd ..

# 서비스 상태 확인
echo "📊 서비스 상태 확인 중..."
sleep 3
docker-compose -f deployment/docker-compose.yml ps

echo ""
echo "✅ Docker + uv sync 개발 환경이 시작되었습니다!"
echo ""
echo "📊 서비스 URL:"
echo "  - API Gateway: http://localhost:8000"
echo "  - Swagger UI: http://localhost:8000/docs"
echo ""
echo "🛠️ 유용한 명령어:"
echo "  - 로그 확인: docker-compose -f deployment/docker-compose.yml logs api_gateway"
echo "  - 서비스 중지: docker-compose -f deployment/docker-compose.yml down"
echo "  - 서비스 재시작: docker-compose -f deployment/docker-compose.yml restart api_gateway"
echo ""
echo "🧪 테스트 예시:"
echo "  curl http://localhost:8000/"
echo "  curl 'http://localhost:8000/api/v1/recommend/invest-timing?asset_name=삼성전자'"
echo ""
echo "🚀 uv sync 장점:"
echo "  - 자동 의존성 관리"
echo "  - lock 파일로 재현 가능한 빌드"
echo "  - 더 빠른 의존성 설치"
echo "  - 현대적인 Python 패키지 관리" 