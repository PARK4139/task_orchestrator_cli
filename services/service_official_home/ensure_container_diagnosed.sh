cd services/smart_person_ai

# 진단 스크립트 생성 및 실행
cat > diagnose_frontend.sh << 'EOF'
#!/bin/bash

echo "🔍 프론트엔드 도커 컨테이너 문제 진단 시작..."
echo "================================================"

cd "$(dirname "$0")"

echo "1️⃣ 현재 실행 중인 컨테이너 확인:"
docker ps | grep -E "(smart_ai|frontend)" || echo "❌ 실행 중인 프론트엔드 컨테이너 없음"

echo ""
echo "2️⃣ 종료된 컨테이너 확인:"
docker ps -a | grep -E "(smart_ai|frontend)" || echo "❌ 프론트엔드 컨테이너 기록 없음"

echo ""
echo "3️⃣ 최근 컨테이너 로그 확인:"
if docker ps -a | grep -q "smart_ai_official_home_frontend"; then
    echo "📋 프론트엔드 컨테이너 로그:"
    docker logs --tail=20 smart_ai_official_home_frontend
else
    echo "❌ 프론트엔드 컨테이너를 찾을 수 없습니다"
fi

echo ""
echo "4️⃣ Docker Compose 서비스 상태:"
docker-compose ps official_home_frontend || echo "❌ Docker Compose 서비스 정보 없음"

echo ""
echo "5️⃣ 포트 3000 사용 확인:"
netstat -tlnp | grep :3000 || echo "ℹ️ 포트 3000이 비어있음"

echo ""
echo "6️⃣ Docker 이미지 확인:"
docker images | grep -E "(smart_ai|frontend|node)" || echo "❌ 관련 Docker 이미지 없음"

echo ""
echo "7️⃣ Docker Compose 파일 유효성 확인:"
docker-compose config --quiet && echo "✅ docker-compose.yml 파일 유효" || echo "❌ docker-compose.yml 파일 오류"

echo ""
echo "8️⃣ 디스크 공간 확인:"
df -h | head -2

echo ""
echo "9️⃣ Docker 데몬 상태 확인:"
docker version --format '{{.Server.Version}}' && echo "✅ Docker 데몬 실행 중" || echo "❌ Docker 데몬 문제"

echo ""
echo "================================================"
echo "🛠️ 문제 해결을 위한 권장 단계:"
echo "1. 컨테이너 재시작: docker-compose up official_home_frontend --force-recreate"
echo "2. 이미지 재빌드: docker-compose build official_home_frontend"  
echo "3. 전체 재시작: docker-compose down && docker-compose up -d"
EOF

chmod +x diagnose_frontend.sh
./diagnose_frontend.sh