#!/bin/bash

echo "🎨 ensure_ 방식: 미니멀 컬러 테마 적용..."
echo "================================================"

# 위의 코드를 page.tsx에 적용
echo "📝 미니멀 컬러 디자인 적용 중..."

# 추가 CSS 클래스들을 globals.css에 추가
cat >> app/globals.css << 'EOF'

/* 🎨 미니멀 컬러 테마 전용 스타일 */

/* 컬러풀 호버 효과 */
.color-hover-blue:hover {
  @apply text-blue-600 scale-105;
  transition: all 0.2s ease;
}

.color-hover-purple:hover {
  @apply text-purple-600 scale-105;
  transition: all 0.2s ease;
}

.color-hover-pink:hover {
  @apply text-pink-600 scale-105;
  transition: all 0.2s ease;
}

/* 그라데이션 텍스트 애니메이션 */
@keyframes gradient-x {
  0%, 100% {
    background-size: 200% 200%;
    background-position: left center;
  }
  50% {
    background-size: 200% 200%;
    background-position: right center;
  }
}

.gradient-animate {
  animation: gradient-x 3s ease infinite;
}

/* 서브틀한 그림자 */
.minimal-shadow {
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
}

.minimal-shadow-lg {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

/* 컬러 포인트 라인 */
.color-divider-blue {
  background: linear-gradient(90deg, transparent, #3B82F6, transparent);
}

.color-divider-purple {
  background: linear-gradient(90deg, transparent, #8B5CF6, transparent);
}

.color-divider-pink {
  background: linear-gradient(90deg, transparent, #EC4899, transparent);
}

EOF

echo "✅ 미니멀 컬러 테마 적용 완료!"
echo "🌐 브라우저에서 확인: http://localhost:3000"
echo ""
echo "🎨 미니멀 컬러 테마 특징:"
echo "   • 🤍 깔끔한 미니멀 베이스"
echo "   • 🌈 생동감 있는 컬러 포인트"
echo "   • ✨ 서브틀한 애니메이션"
echo "   • 🎯 컬러별 섹션 구분" 