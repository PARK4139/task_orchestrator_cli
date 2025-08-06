#!/bin/bash

echo "🎨 ensure_design_showcase_hotreload.sh: 디자인 쇼케이스 인터랙티브 모드!"
echo "=================================================================="
echo ""
echo "🔄 4가지 디자인을 엔터 키로 수동 전환합니다:"
echo "   1️⃣ 뉴모피즘 (Neumorphism) 🥚"
echo "   2️⃣ 미니멀 다크모드 (Dark Mode) 🌙" 
echo "   3️⃣ 그라데이션 메쉬 (Gradient Mesh) 🌈"
echo "   4️⃣ 3D 카드 (3D Cards) 📦"
echo ""
echo "⌨️  엔터 키를 누르면 다음 디자인으로 전환"
echo "🌐 브라우저: http://localhost:3000"
echo "⏹️  중단하려면 Ctrl+C"
echo ""

# 함수 정의
wait_for_enter() {
    local design_name=$1
    local emoji=$2
    local next_design=$3
    
    echo ""
    echo "🎯 현재 디자인: $design_name $emoji"
    echo "=================================================="
    echo ""
    echo "👀 브라우저에서 디자인을 확인해보세요!"
    echo ""
    if [ -n "$next_design" ]; then
        echo "⏭️  다음: $next_design"
        echo "⌨️  엔터 키를 눌러서 다음 디자인으로 이동하세요..."
    else
        echo "🔄 엔터 키를 눌러서 다음 사이클을 시작하세요..."
    fi
    echo ""
    
    read -r -p "👉 Press Enter to continue... "
    echo ""
}

apply_design() {
    local script_name=$1
    local design_name=$2
    local emoji=$3
    local next_design=$4
    
    echo ""
    echo "🚀 $design_name $emoji 적용 중..."
    ./$script_name
    echo "✅ $design_name $emoji 적용 완료!"
    
    wait_for_enter "$design_name" "$emoji" "$next_design"
}

# 무한 루프로 디자인 순환
cycle_count=1
echo "🎬 디자인 쇼케이스 시작! (Cycle #$cycle_count)"

while true; do
    echo ""
    echo "🔄 === Cycle #$cycle_count 시작 ==="
    echo ""
    
    # 1️⃣ 뉴모피즘
    apply_design "ensure_neumorphism_applied.sh" "뉴모피즘" "🥚" "미니멀 다크모드 🌙"
    
    # 2️⃣ 다크 모드  
    apply_design "ensure_darkmode_applied.sh" "미니멀 다크모드" "🌙" "그라데이션 메쉬 🌈"
    
    # 3️⃣ 그라데이션 메쉬
    apply_design "ensure_gradient_mesh_applied.sh" "그라데이션 메쉬" "🌈" "3D 카드 📦"
    
    # 4️⃣ 3D 카드
    apply_design "ensure_3d_cards_applied.sh" "3D 카드" "📦" ""
    
    cycle_count=$((cycle_count + 1))
    echo ""
    echo "🎉 Cycle #$((cycle_count - 1)) 완료!"
    echo "🔄 다음 사이클로 이동합니다..."
    echo ""
done 