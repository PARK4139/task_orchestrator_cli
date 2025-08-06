#!/bin/bash

# API 서비스 중지 스크립트

echo "🛑 API 서비스를 중지합니다..."

# PID 파일에서 프로세스 ID 읽기
if [ -f "logs/gateway.pid" ]; then
    GATEWAY_PID=$(cat logs/gateway.pid)
    if kill -0 $GATEWAY_PID 2>/dev/null; then
        echo "🚪 API Gateway 중지 중..."
        kill $GATEWAY_PID
        rm logs/gateway.pid
    fi
fi

if [ -f "logs/recommendation.pid" ]; then
    RECOMMENDATION_PID=$(cat logs/recommendation.pid)
    if kill -0 $RECOMMENDATION_PID 2>/dev/null; then
        echo "🧠 Recommendation Engine 중지 중..."
        kill $RECOMMENDATION_PID
        rm logs/recommendation.pid
    fi
fi

if [ -f "logs/finance_api.pid" ]; then
    FINANCE_API_PID=$(cat logs/finance_api.pid)
    if kill -0 $FINANCE_API_PID 2>/dev/null; then
        echo "💰 Finance API Client 중지 중..."
        kill $FINANCE_API_PID
        rm logs/finance_api.pid
    fi
fi

if [ -f "logs/news_crawler.pid" ]; then
    NEWS_CRAWLER_PID=$(cat logs/news_crawler.pid)
    if kill -0 $NEWS_CRAWLER_PID 2>/dev/null; then
        echo "📰 News Crawler 중지 중..."
        kill $NEWS_CRAWLER_PID
        rm logs/news_crawler.pid
    fi
fi

# Docker 서비스 중지
if command -v docker-compose &> /dev/null; then
    echo "🐳 Docker 서비스 중지 중..."
    cd infra
    docker-compose down
    cd ..
fi

echo "✅ 모든 API 서비스가 중지되었습니다." 