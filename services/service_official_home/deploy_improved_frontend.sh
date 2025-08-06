#!/bin/bash

echo "🚀 개선된 프론트엔드 빌드 및 배포 시작..."
echo "================================================"

cd "$(dirname "$0")"

# 1. 기존 리소스 정리
echo "1️⃣ 기존 컨테이너 및 이미지 정리..."
docker-compose down official-home-frontend
docker rmi $(docker images | grep "service_official_home_smart_person_ai-official-home-frontend" | awk '{print $3}') 2>/dev/null || echo "기존 이미지 없음"

# 2. 개선된 Dockerfile로 빌드
echo "2️⃣ 개선된 Dockerfile로 빌드 중..."
cd frontend
docker build -f Dockerfile.fixed -t smart-ai-frontend-improved:latest . --no-cache

# 3. 빌드 성공 확인
if [ $? -eq 0 ]; then
    echo "✅ 빌드 성공!"
    
    # 4. 컨테이너 실행
    echo "3️⃣ 개선된 컨테이너 실행..."
    docker run -d \
        --name smart_ai_frontend_improved \
        -p 3000:3000 \
        -e NODE_ENV=production \
        -e NEXT_PUBLIC_API_URL=http://localhost:8030 \
        -e NEXT_PUBLIC_APP_URL=http://localhost:3000 \
        smart-ai-frontend-improved:latest
    
    echo "4️⃣ 컨테이너 상태 확인..."
    sleep 3
    docker ps | grep smart_ai_frontend_improved
    
    echo "5️⃣ 로그 확인..."
    docker logs --tail=10 smart_ai_frontend_improved
    
    echo ""
    echo "✅ 배포 완료!"
    echo "🌐 접속 URL: http://localhost:3000"
    echo "📋 실시간 로그: docker logs -f smart_ai_frontend_improved"
    echo "🛑 중지: docker stop smart_ai_frontend_improved"
    
else
    echo "❌ 빌드 실패! 로그를 확인해주세요."
    echo "🔍 상세 디버깅을 위해 다음 명령어를 실행하세요:"
    echo "docker build -f Dockerfile.fixed -t debug-build . --progress=plain"
fi 