#!/bin/bash

echo "🚀 프론트엔드 컨테이너 올바른 실행..."
echo "================================================"

# 현재 위치에서 실행 (service_official_home_smart_person_ai 디렉토리)
echo "📍 현재 위치: $(pwd)"

echo ""
echo "1️⃣ 기존 컨테이너 정리..."
docker-compose down

echo ""
echo "2️⃣ 프로덕션 프론트엔드 시작..."
docker-compose up official-home-frontend -d

echo ""
echo "3️⃣ 컨테이너 상태 확인..."
sleep 3
docker-compose ps

echo ""
echo "4️⃣ 실시간 로그 확인..."
docker-compose logs --tail=10 official-home-frontend

echo ""
echo "✅ 프론트엔드 실행 완료!"
echo "🌐 접속 URL: http://localhost:3000"
echo "📋 로그 실시간 보기: docker-compose logs -f official-home-frontend"
echo "🛑 중지하기: docker-compose down official-home-frontend" 