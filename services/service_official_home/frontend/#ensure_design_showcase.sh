#!/bin/bash

echo "🎨 ensure_ 방식: 디자인 쇼케이스 자동 데모..."
echo "================================================"

THEMES=("gradient" "minimal" "cyberpunk" "nature" "premium")

echo "🚀 5가지 테마를 순차적으로 시연합니다!"
echo "각 테마마다 10초간 표시됩니다."
echo "브라우저에서 http://localhost:3000 을 열어두세요!"

read -p "시작하려면 Enter를 누르세요..." -r

for theme in "${THEMES[@]}"; do
    echo ""
    echo "🎨 현재 테마: $theme"
    ./ensure_design_theme_changer.sh $theme
    
    echo "⏰ 10초 대기 중... (Ctrl+C로 중단 가능)"
    for i in {10..1}; do
        echo -ne "\r   $i초 남음..."
        sleep 1
    done
    echo ""
done

echo ""
echo "🎉 모든 테마 시연 완료!"
echo "🎯 원하는 테마를 선택하세요:"
echo "   ./ensure_design_theme_changer.sh [테마명]" 