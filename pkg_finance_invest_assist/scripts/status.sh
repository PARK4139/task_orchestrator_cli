#!/bin/bash

# API 서비스 상태 확인 스크립트

echo "📊 API 서비스 상태를 확인합니다..."
echo ""

# 각 서비스의 상태 확인
services=(
    "gateway:8000:API Gateway"
    "recommendation:8001:Recommendation Engine"
    "finance_api:8002:Finance API Client"
    "news_crawler:8003:News Crawler"
)

for service in "${services[@]}"; do
    IFS=':' read -r name port description <<< "$service"
    
    if [ -f "logs/${name}.pid" ]; then
        PID=$(cat logs/${name}.pid)
        if kill -0 $PID 2>/dev/null; then
            echo "✅ $description (PID: $PID, Port: $port)"
        else
            echo "❌ $description (중지됨)"
        fi
    else
        echo "❌ $description (PID 파일 없음)"
    fi
done

echo ""
echo "🌐 서비스 URL:"
echo "  - API Gateway: http://localhost:8000"
echo "  - Recommendation Engine: http://localhost:8001"
echo "  - Finance API Client: http://localhost:8002"
echo "  - News Crawler: http://localhost:8003"

echo ""
echo "🐳 Docker 서비스 상태:"
if command -v docker-compose &> /dev/null; then
    cd infra
    docker-compose ps
    cd ..
else
    echo "Docker Compose가 설치되지 않았습니다."
fi

echo ""
echo "📝 최근 로그 (마지막 5줄):"
if [ -f "logs/gateway.log" ]; then
    echo "🚪 API Gateway:"
    tail -n 5 logs/gateway.log
    echo ""
fi 