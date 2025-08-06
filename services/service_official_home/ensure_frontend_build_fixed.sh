#!/bin/bash

echo "🔧 프론트엔드 빌드 문제 해결..."

# 1. 기존 빌드 캐시 완전 삭제
echo "1️⃣ 빌드 캐시 삭제..."
docker system prune -f
docker builder prune -f

# 2. 이미지 완전 재빌드
echo "2️⃣ 프론트엔드 이미지 재빌드..."
docker-compose build official-home-frontend --no-cache

# 3. 컨테이너 실행
echo "3️⃣ 컨테이너 시작..."
docker-compose up official-home-frontend -d

echo "✅ 완료! http://localhost:3000 확인해보세요" 