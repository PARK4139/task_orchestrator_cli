#!/bin/bash

echo "🔥 Official Home MSA - 개발모드 + 핫리로드 통합 실행..."
echo "================================================"

# 1️⃣ 기존 컨테이너 정리
echo "🧹 기존 컨테이너 정리 중..."
docker stop official-home-frontend official-home-backend 2>/dev/null || true
docker rm official-home-frontend official-home-backend 2>/dev/null || true
docker stop frontend-dev-hotreload 2>/dev/null || true
docker rm frontend-dev-hotreload 2>/dev/null || true

# 2️⃣ 백엔드 개발 모드 시작
echo ""
echo "🔧 백엔드 개발 모드 시작..."
cd backend

# 백엔드 의존성 확인 및 설치
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt 파일이 없습니다."
    exit 1
fi

# 백엔드 컨테이너 빌드 및 실행
echo "📦 백엔드 컨테이너 빌드 중..."
docker build -t official-home-backend-dev .

echo "🚀 백엔드 개발 서버 시작..."
docker run -d \
  --name official-home-backend \
  -p 8030:8030 \
  -v $(pwd):/app \
  -e PYTHONPATH=/app \
  -e DEBUG=true \
  official-home-backend-dev

cd ..

# 3️⃣ 프론트엔드 개발 모드 시작
echo ""
echo "🎨 프론트엔드 개발 모드 시작..."
cd frontend

# 프론트엔드 의존성 확인
if [ ! -f "package.json" ]; then
    echo "❌ package.json 파일이 없습니다."
    exit 1
fi

# 개발용 이미지 빌드
echo "📦 프론트엔드 개발 이미지 빌드 중..."
if ! docker images | grep -q "official-home-frontend-dev"; then
    docker build -f Dockerfile.dev -t official-home-frontend-dev . --no-cache
else
    echo "✅ 개발용 이미지 존재"
fi

# 프론트엔드 개발 컨테이너 실행 (핫리로드)
echo "🚀 프론트엔드 개발 서버 시작 (핫리로드)..."
docker run -d \
  --name official-home-frontend \
  -p 3000:3000 \
  -v $(pwd):/app \
  -v /app/node_modules \
  -v /app/.next \
  -e NODE_ENV=development \
  -e CHOKIDAR_USEPOLLING=true \
  -e WATCHPACK_POLLING=true \
  official-home-frontend-dev

cd ..

# 4️⃣ 서비스 상태 확인 및 헬스체크
echo ""
echo "⏳ 서비스 시작 대기 중..."
sleep 10

# 백엔드 헬스체크
echo "🔍 백엔드 상태 확인..."
if curl -f http://localhost:8030/health > /dev/null 2>&1; then
    echo "✅ 백엔드 서비스 정상 실행 (포트: 8030)"
else
    echo "⚠️ 백엔드 서비스 응답 대기 중..."
    echo "📋 백엔드 로그: docker logs official-home-backend"
fi

# 프론트엔드 헬스체크
echo "🔍 프론트엔드 상태 확인..."
if curl -f http://localhost:3000 > /dev/null 2>&1; then
    echo "✅ 프론트엔드 서비스 정상 실행 (포트: 3000)"
else
    echo "⚠️ 프론트엔드 서비스 응답 대기 중..."
    echo "📋 프론트엔드 로그: docker logs official-home-frontend"
fi

# 5️⃣ 컨테이너 상태 표시
echo ""
echo "📊 실행 중인 컨테이너:"
docker ps | grep -E "(official-home-frontend|official-home-backend)"

# 6️⃣ 개발 모드 정보 출력
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔥 Official Home MSA - 개발모드 활성화!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🌐 프론트엔드: http://localhost:3000"
echo "🔧 백엔드 API: http://localhost:8030"
echo "📋 실시간 로그:"
echo "   프론트엔드: docker logs -f official-home-frontend"
echo "   백엔드: docker logs -f official-home-backend"
echo "🛑 중지: docker stop official-home-frontend official-home-backend"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

echo ""
echo "🎯 개발 모드 설정 완료!" 