#!/bin/bash

echo "🔍 ensure_ 방식: 컨테이너 상태 체크..."
echo "================================================"

# 컨테이너 실행 상태 확인
if docker ps | grep -q "frontend-production-success"; then
    echo "✅ 컨테이너 실행 중"
    
    # 웹 서비스 응답 확인
    if curl -f http://localhost:3000 > /dev/null 2>&1; then
        echo "🌐 웹 서비스 정상 응답"
        echo "🎉 재빌드 불필요! 현재 상태 완벽함"
        
        # 간단한 상태 정보
        echo ""
        echo "📊 현재 상태:"
        docker ps | grep frontend-production-success
        echo ""
        echo "🌐 접속: http://localhost:3000"
        
    else
        echo "❌ 웹 서비스 응답 없음"
        echo "🔄 재빌드 필요!"
        
        # 자동 재빌드 제안
        read -p "자동으로 재빌드하시겠습니까? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            ./ensure_production_build_success.sh
        fi
    fi
    
else
    echo "❌ 컨테이너 실행되지 않음"
    echo "🚀 재빌드 및 재시작 필요!"
    
    # 자동 재시작 제안
    read -p "자동으로 재빌드하시겠습니까? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        ./ensure_production_build_success.sh
    fi
fi 