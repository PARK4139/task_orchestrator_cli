#!/bin/bash

echo "🎨 ensure_ 방식: 핫 리로드 테스트 가이드..."
echo "================================================"

echo "✅ 1단계: 개발 서버 실행 확인"
if docker ps | grep -q "frontend-dev-hotreload"; then
    echo "   ✅ 개발 컨테이너 실행 중"
else
    echo "   ❌ 개발 컨테이너 실행 필요"
    echo "   실행 명령: ./ensure_development_hot_reload.sh"
    exit 1
fi

echo ""
echo "✅ 2단계: 브라우저 접속 안내"
echo "   🌐 http://localhost:3000 접속하세요"
echo "   💡 브라우저를 화면 반쪽에 두고 에디터는 다른 반쪽에 두면 좋습니다"

echo ""
echo "✅ 3단계: 실시간 테스트 시나리오"
echo "   📝 app/page.tsx 파일을 열어보세요"
echo "   🎨 제목에 이모지나 텍스트를 추가해보세요"
echo "   ⚡ 저장하면 즉시 브라우저에 반영됩니다!"

echo ""
echo "✅ 4단계: 고급 테스트"
echo "   🎨 components/sections/HeroSection.tsx 수정"
echo "   🌈 Tailwind CSS 클래스 변경"
echo "   ⭐ 새로운 컴포넌트 추가"

echo ""
echo "✅ 5단계: 로그 모니터링"
echo "   📋 실시간 로그: docker logs -f frontend-dev-hotreload"
echo "   🔍 오류 발생 시 로그에서 즉시 확인 가능"

echo ""
echo "🔥 핫 리로드 테스트 포인트:"
echo "   • 파일 저장 시 1-2초 내 브라우저 반영"
echo "   • CSS 변경 시 전체 새로고침 없이 스타일만 업데이트"
echo "   • JavaScript 오류 시 화면에 오류 오버레이 표시"
echo "   • 컴포넌트 상태는 가능한 유지됨 (Fast Refresh)"

echo ""
echo "🎯 지금 바로 테스트해보세요!"
echo "1. 브라우저에서 http://localhost:3000 열기"
echo "2. app/page.tsx 파일 수정하기"
echo "3. 저장하고 실시간 반영 확인하기" 