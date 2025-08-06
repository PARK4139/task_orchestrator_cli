#!/bin/bash

echo "🎪 ensure_design_showcase_advanced.sh: 고급 디자인 쇼케이스!"
echo "=============================================================="

# 브라우저 자동 새로고침을 위한 Node.js 스크립트 생성
cat > design_showcase_server.js << 'EOF'
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3001;

// 간단한 웹 서버로 브라우저 자동 새로고침 신호 전송
const server = http.createServer((req, res) => {
  if (req.url === '/reload') {
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'Access-Control-Allow-Origin': '*'
    });
    
    // 클라이언트에게 새로고침 신호 전송
    res.write('data: reload\n\n');
    res.end();
  } else {
    res.writeHead(404);
    res.end();
  }
});

server.listen(PORT, () => {
  console.log(`🔄 자동 새로고침 서버가 포트 ${PORT}에서 실행 중...`);
});
EOF

# 브라우저 자동 새로고침 스크립트 주입
cat > browser_auto_reload.js << 'EOF'
// 브라우저 콘솔에서 실행할 자동 새로고침 스크립트
setInterval(() => {
  fetch('http://localhost:3001/reload')
    .then(() => {
      console.log('🔄 디자인 변경 감지, 페이지 새로고침...');
      window.location.reload();
    })
    .catch(() => {
      // 서버가 없으면 10초마다 자동 새로고침
      window.location.reload();
    });
}, 10000);

console.log('🎨 자동 디자인 쇼케이스 활성화! 10초마다 자동 새로고침됩니다.');
EOF

echo "📋 고급 쇼케이스 준비 완료!"
echo ""
echo "🎯 실행 방법:"
echo "   1. 개발 서버 시작: npm run dev"
echo "   2. 브라우저에서 http://localhost:3000 열기"
echo "   3. F12 → Console → browser_auto_reload.js 내용 복사 붙여넣기"
echo "   4. 이 스크립트 실행: ./ensure_design_showcase_advanced.sh"
echo ""

# Node.js 서버 백그라운드 실행
node design_showcase_server.js &
SERVER_PID=$!

echo "🚀 자동 새로고침 서버 시작됨 (PID: $SERVER_PID)"
echo ""

# 디자인 변경 함수
apply_design_with_signal() {
    local script_name=$1
    local design_name=$2
    local emoji=$3
    
    echo ""
    echo "🎨 $design_name $emoji 적용 중..."
    ./$script_name
    
    # 새로고침 신호 전송
    curl -s http://localhost:3001/reload > /dev/null 2>&1
    
    echo "✅ $design_name $emoji 적용 완료!"
    echo "⏰ 10초 대기 중..."
    
    # 카운트다운 표시
    for i in {10..1}; do
        echo -ne "\r⏱️  다음 디자인까지: ${i}초     "
        sleep 1
    done
    echo ""
}

# 종료 시 서버 정리
trap "kill $SERVER_PID 2>/dev/null; rm -f design_showcase_server.js browser_auto_reload.js; echo '🛑 쇼케이스 종료됨'" EXIT

# 디자인 쇼케이스 시작
cycle=1
echo "🎬 고급 디자인 쇼케이스 시작!"

while true; do
    echo ""
    echo "🔄 ===== Cycle #$cycle ===== "
    
    apply_design_with_signal "ensure_neumorphism_applied.sh" "뉴모피즘" "🥚"
    apply_design_with_signal "ensure_darkmode_applied.sh" "다크모드" "🌙"
    apply_design_with_signal "ensure_gradient_mesh_applied.sh" "그라데이션 메쉬" "🌈"
    apply_design_with_signal "ensure_3d_cards_applied.sh" "3D 카드" "📦"
    
    cycle=$((cycle + 1))
done 