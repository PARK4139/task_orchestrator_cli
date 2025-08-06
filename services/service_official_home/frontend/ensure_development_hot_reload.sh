#!/bin/bash

echo "🔥 ensure_ 방식: 개발 모드 실시간 핫 리로드 설정..."
echo "================================================"

# 1️⃣ 기존 프로덕션 컨테이너 정리
echo "🧹 기존 프로덕션 컨테이너 정리 중..."
docker stop frontend-production-success 2>/dev/null && echo "✅ 프로덕션 컨테이너 중지됨" || echo "ℹ️ 프로덕션 컨테이너 없음"
docker rm frontend-production-success 2>/dev/null && echo "✅ 프로덕션 컨테이너 제거됨" || echo "ℹ️ 제거할 컨테이너 없음"

# 기존 개발 컨테이너도 정리
docker stop frontend-dev-hotreload 2>/dev/null || true
docker rm frontend-dev-hotreload 2>/dev/null || true

# 2️⃣ 개발용 이미지 확인 및 빌드
echo ""
echo "🔨 개발용 Docker 이미지 준비 중..."
if ! docker images | grep -q "frontend-dev-fixed"; then
    echo "📦 개발용 이미지가 없습니다. 빌드 중..."
    docker build -f Dockerfile.dev -t frontend-dev-fixed . --no-cache
else
    echo "✅ 개발용 이미지 존재"
fi

# 3️⃣ 개발 모드 컨테이너 실행 (볼륨 마운트)
echo ""
echo "🚀 개발 모드 컨테이너 시작 (실시간 반영)..."
docker run -d \
  --name frontend-dev-hotreload \
  -p 3000:3000 \
  -v $(pwd):/app \
  -v /app/node_modules \
  -v /app/.next \
  -e NODE_ENV=development \
  -e CHOKIDAR_USEPOLLING=true \
  -e WATCHPACK_POLLING=true \
  frontend-dev-fixed

# 4️⃣ 시작 대기 및 헬스체크
echo ""
echo "⏳ 개발 서버 시작 대기 중..."
sleep 8

# 5️⃣ 상태 확인
if docker ps | grep -q "frontend-dev-hotreload"; then
    echo "✅ 개발 모드 컨테이너 실행 성공!"
    
    # 웹 서비스 확인
    echo "🌐 웹 서비스 확인 중..."
    sleep 5
    
    if curl -f http://localhost:3000 > /dev/null 2>&1; then
        echo "🎉 핫 리로드 개발 환경 준비 완료!"
        echo ""
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "🔥 실시간 핫 리로드 개발 모드 활성화!"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "🌐 접속 URL: http://localhost:3000"
        echo "📝 파일 수정 시 자동으로 브라우저 반영됩니다"
        echo "📋 실시간 로그: docker logs -f frontend-dev-hotreload"
        echo "🛑 중지: docker stop frontend-dev-hotreload"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        
        # 컨테이너 상태 표시
        echo ""
        echo "📊 컨테이너 상태:"
        docker ps | grep frontend-dev-hotreload
        
    else
        echo "⚠️ 웹 서비스 응답 대기 중... (조금 더 기다려주세요)"
        echo "📋 로그 확인: docker logs frontend-dev-hotreload"
    fi
else
    echo "❌ 컨테이너 실행 실패"
    echo "📋 로그 확인:"
    docker logs frontend-dev-hotreload 2>/dev/null || echo "로그 없음"
fi

echo ""
echo "🎯 개발 모드 설정 완료!" 