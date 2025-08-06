#!/bin/bash

echo "🎪 ensure_design_showcase_unified.sh: 통합 디자인 쇼케이스!"
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

# 뉴모피즘 디자인 적용 함수
apply_neumorphism() {
    echo "🥚 뉴모피즘 디자인 적용 중..."
    
    cat > app/globals.css << 'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;

/* 뉴모피즘 베이스 스타일 */
@layer base {
  html {
    scroll-behavior: smooth;
  }
  
  body {
    @apply antialiased;
    background: #f0f0f3;
    color: #333;
  }
}

/* 🥚 뉴모피즘 컴포넌트 스타일 */
@layer components {
  /* 기본 뉴모피즘 효과 */
  .neuro-base {
    background: #f0f0f3;
    border-radius: 20px;
    box-shadow: 
      20px 20px 60px #bebebe,
      -20px -20px 60px #ffffff;
    border: none;
  }

  .neuro-inset {
    background: #f0f0f3;
    border-radius: 20px;
    box-shadow: 
      inset 20px 20px 60px #bebebe,
      inset -20px -20px 60px #ffffff;
  }

  .neuro-card {
    @apply neuro-base p-8;
    transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  }

  .neuro-card:hover {
    box-shadow: 
      25px 25px 75px #bebebe,
      -25px -25px 75px #ffffff;
    transform: translateY(-5px);
  }

  /* 뉴모피즘 버튼 */
  .neuro-btn {
    @apply neuro-base px-8 py-4 font-semibold;
    color: #666;
    transition: all 0.2s ease;
    cursor: pointer;
  }

  .neuro-btn:hover {
    box-shadow: 
      15px 15px 45px #bebebe,
      -15px -15px 45px #ffffff;
  }

  .neuro-btn:active {
    @apply neuro-inset;
  }

  .neuro-btn-primary {
    background: linear-gradient(145deg, #667eea, #764ba2);
    color: white;
    box-shadow: 
      20px 20px 60px #5a6fd8,
      -20px -20px 60px #7c8cfc;
  }

  /* 뉴모피즘 헤더 */
  .neuro-header {
    background: #f0f0f3;
    box-shadow: 
      0 10px 30px #bebebe,
      0 -10px 30px #ffffff;
    backdrop-filter: blur(10px);
  }

  /* 뉴모피즘 아이콘 */
  .neuro-icon {
    @apply neuro-base w-16 h-16 flex items-center justify-center;
    font-size: 24px;
  }

  .neuro-icon-small {
    @apply neuro-base w-12 h-12 flex items-center justify-center;
    font-size: 18px;
    border-radius: 12px;
    box-shadow: 
      10px 10px 30px #bebebe,
      -10px -10px 30px #ffffff;
  }

  /* 뉴모피즘 섹션 */
  .neuro-section {
    background: #f0f0f3;
    border-radius: 30px;
    box-shadow: 
      30px 30px 80px #bebebe,
      -30px -30px 80px #ffffff;
    margin: 2rem;
    padding: 3rem;
  }

  /* 뉴모피즘 텍스트 */
  .neuro-text {
    color: #666;
  }

  .neuro-text-muted {
    color: #999;
  }

  .neuro-text-gradient {
    background: linear-gradient(145deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
}
EOF

    echo "✅ 뉴모피즘 디자인 적용 완료!"
}

# 다크모드 디자인 적용 함수
apply_darkmode() {
    echo "🌙 다크모드 디자인 적용 중..."
    
    cat > app/globals.css << 'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;

/* 다크 모드 베이스 */
@layer base {
  html {
    scroll-behavior: smooth;
  }
  
  body {
    @apply antialiased;
    background: #0a0a0a;
    color: #ffffff;
  }
}

/* 🌙 다크 모드 컴포넌트 스타일 */
@layer components {
  /* 기본 다크 카드 */
  .dark-card {
    background: rgba(18, 18, 18, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 2rem;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
  }

  .dark-card:hover {
    background: rgba(25, 25, 25, 0.9);
    border-color: rgba(255, 255, 255, 0.2);
    transform: translateY(-4px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  }

  /* 다크 버튼 */
  .dark-btn {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: #ffffff;
    padding: 12px 32px;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
  }

  .dark-btn:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(255, 255, 255, 0.3);
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  }

  .dark-btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    color: white;
  }

  .dark-btn-primary:hover {
    background: linear-gradient(135deg, #7c8cff 0%, #8a5db8 100%);
    box-shadow: 0 15px 30px rgba(102, 126, 234, 0.3);
  }

  .dark-btn-secondary {
    background: rgba(255, 255, 255, 0.1);
    border: 2px solid rgba(255, 255, 255, 0.3);
    color: rgba(255, 255, 255, 0.9);
  }

  /* 다크 헤더 */
  .dark-header {
    background: rgba(10, 10, 10, 0.8);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(20px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
  }

  /* 다크 섹션 */
  .dark-section {
    background: rgba(15, 15, 15, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 24px;
    margin: 2rem;
    padding: 3rem;
    backdrop-filter: blur(10px);
  }

  /* 다크 아이콘 컨테이너 */
  .dark-icon {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
  }

  .dark-icon-small {
    @apply dark-icon;
    width: 48px;
    height: 48px;
    border-radius: 10px;
  }

  /* 다크 텍스트 */
  .dark-text {
    color: #ffffff;
  }

  .dark-text-muted {
    color: rgba(255, 255, 255, 0.7);
  }

  .dark-text-gradient {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
}
EOF

    echo "✅ 다크모드 디자인 적용 완료!"
}

# 그라데이션 메쉬 디자인 적용 함수
apply_gradient_mesh() {
    echo "🌈 그라데이션 메쉬 디자인 적용 중..."
    
    cat > app/globals.css << 'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;

/* 그라데이션 메쉬 베이스 */
@layer base {
  html {
    scroll-behavior: smooth;
  }
  
  body {
    @apply antialiased;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    color: #333;
  }
}

/* 🌈 그라데이션 메쉬 컴포넌트 */
@layer components {
  /* 메쉬 카드 */
  .mesh-card {
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 24px;
    padding: 2rem;
    transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    position: relative;
    overflow: hidden;
  }

  .mesh-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: conic-gradient(
      from 0deg,
      rgba(255, 255, 255, 0.1) 0deg,
      transparent 90deg,
      rgba(255, 255, 255, 0.1) 180deg,
      transparent 270deg,
      rgba(255, 255, 255, 0.1) 360deg
    );
    animation: rotate 20s linear infinite;
    z-index: -1;
  }

  .mesh-card:hover {
    background: rgba(255, 255, 255, 0.35);
    border-color: rgba(255, 255, 255, 0.5);
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.2);
  }

  /* 메쉬 버튼 */
  .mesh-btn {
    background: rgba(255, 255, 255, 0.2);
    border: 2px solid rgba(255, 255, 255, 0.3);
    color: #ffffff;
    padding: 12px 32px;
    border-radius: 16px;
    font-weight: 600;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
    position: relative;
    overflow: hidden;
  }

  .mesh-btn:hover {
    background: rgba(255, 255, 255, 0.3);
    border-color: rgba(255, 255, 255, 0.5);
    transform: translateY(-2px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
  }

  .mesh-btn-primary {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1));
    border: 2px solid rgba(255, 255, 255, 0.4);
    color: white;
    font-weight: 700;
  }

  /* 메쉬 헤더 */
  .mesh-header {
    background: rgba(255, 255, 255, 0.1);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(30px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  }

  /* 메쉬 섹션 */
  .mesh-section {
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 32px;
    margin: 2rem;
    padding: 3rem;
    backdrop-filter: blur(20px);
    position: relative;
    overflow: hidden;
  }

  /* 메쉬 아이콘 */
  .mesh-icon {
    background: rgba(255, 255, 255, 0.2);
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-radius: 16px;
    width: 64px;
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
  }

  .mesh-icon-small {
    @apply mesh-icon;
    width: 48px;
    height: 48px;
    border-radius: 12px;
  }

  /* 메쉬 텍스트 */
  .mesh-text {
    color: #ffffff;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  }

  .mesh-text-muted {
    color: rgba(255, 255, 255, 0.8);
  }

  .mesh-text-gradient {
    background: linear-gradient(135deg, #ffffff 0%, rgba(255, 255, 255, 0.7) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  @keyframes rotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
}
EOF

    echo "✅ 그라데이션 메쉬 디자인 적용 완료!"
}

# 3D 카드 디자인 적용 함수
apply_3d_cards() {
    echo "📦 3D 카드 디자인 적용 중..."
    
    cat > app/globals.css << 'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;

/* 3D 카드 베이스 */
@layer base {
  html {
    scroll-behavior: smooth;
  }
  
  body {
    @apply antialiased;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    perspective: 1000px;
    color: #333;
  }
}

/* 📦 3D 카드 컴포넌트 */
@layer components {
  /* 3D 컨테이너 */
  .card-3d-container {
    perspective: 1000px;
    transform-style: preserve-3d;
  }

  /* 기본 3D 카드 */
  .card-3d {
    background: rgba(255, 255, 255, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    padding: 2rem;
    transition: all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    transform-style: preserve-3d;
    box-shadow: 
      0 20px 40px rgba(0, 0, 0, 0.1),
      0 0 0 1px rgba(255, 255, 255, 0.5);
    position: relative;
  }

  .card-3d:hover {
    transform: rotateX(-10deg) rotateY(10deg) translateY(-20px);
    box-shadow: 
      0 40px 80px rgba(0, 0, 0, 0.2),
      0 0 0 1px rgba(255, 255, 255, 0.8);
  }

  /* 3D 틸트 효과 */
  .card-3d-tilt {
    @apply card-3d;
    transform-origin: center;
  }

  .card-3d-tilt:hover {
    transform: rotateX(-15deg) rotateY(-10deg) translateY(-25px);
  }

  /* 3D 플립 카드 */
  .card-3d-flip {
    @apply card-3d;
    transform-style: preserve-3d;
  }

  .card-3d-flip:hover {
    transform: rotateY(15deg) translateZ(30px);
  }

  /* 3D 플로팅 */
  .card-3d-float {
    @apply card-3d;
    animation: float3d 6s ease-in-out infinite;
  }

  /* 3D 버튼 */
  .btn-3d {
    background: linear-gradient(145deg, #ffffff, #e6e6e6);
    border: none;
    border-radius: 16px;
    padding: 16px 32px;
    font-weight: 600;
    color: #333;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    box-shadow: 
      0 10px 20px rgba(0, 0, 0, 0.1),
      inset 0 1px 0 rgba(255, 255, 255, 0.8);
    transform-style: preserve-3d;
    position: relative;
  }

  .btn-3d:hover {
    transform: translateY(-4px) rotateX(-10deg);
    box-shadow: 
      0 20px 40px rgba(0, 0, 0, 0.15),
      inset 0 1px 0 rgba(255, 255, 255, 0.9);
  }

  .btn-3d:active {
    transform: translateY(-2px) rotateX(-5deg);
    box-shadow: 
      0 10px 20px rgba(0, 0, 0, 0.1),
      inset 0 1px 0 rgba(255, 255, 255, 0.7);
  }

  .btn-3d-secondary {
    background: linear-gradient(145deg, #f8f9fa, #e9ecef);
    color: #6c757d;
  }

  /* 3D 헤더 */
  .header-3d {
    background: rgba(255, 255, 255, 0.95);
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(20px);
    box-shadow: 
      0 4px 16px rgba(0, 0, 0, 0.1),
      inset 0 1px 0 rgba(255, 255, 255, 0.8);
    transform-style: preserve-3d;
  }

  /* 3D 섹션 */
  .section-3d {
    background: rgba(255, 255, 255, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 24px;
    margin: 2rem;
    padding: 3rem;
    backdrop-filter: blur(10px);
    box-shadow: 
      0 20px 40px rgba(0, 0, 0, 0.1),
      inset 0 1px 0 rgba(255, 255, 255, 0.6);
    transform-style: preserve-3d;
  }

  /* 3D 아이콘 */
  .icon-3d {
    background: linear-gradient(145deg, #ffffff, #f0f0f0);
    border-radius: 16px;
    width: 64px;
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    box-shadow: 
      0 10px 20px rgba(0, 0, 0, 0.1),
      inset 0 1px 0 rgba(255, 255, 255, 0.8);
    transition: all 0.3s ease;
    transform-style: preserve-3d;
  }

  .icon-3d-small {
    @apply icon-3d;
    width: 48px;
    height: 48px;
    font-size: 18px;
    border-radius: 12px;
  }

  /* 3D 텍스트 효과 */
  .text-3d {
    color: #333;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .text-3d-muted {
    color: #6c757d;
  }

  .text-3d-gradient {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  /* 3D 그리드 */
  .grid-3d {
    display: grid;
    gap: 2rem;
    transform-style: preserve-3d;
  }

  /* 3D 애니메이션 */
  @keyframes float3d {
    0%, 100% { transform: translateY(0px) rotateX(0deg); }
    50% { transform: translateY(-20px) rotateX(-5deg); }
  }

  .card-3d-pulse {
    animation: pulse3d 2s ease-in-out infinite;
  }

  @keyframes pulse3d {
    0%, 100% { transform: scale(1) rotateY(0deg); }
    50% { transform: scale(1.05) rotateY(5deg); }
  }
}
EOF

    echo "✅ 3D 카드 디자인 적용 완료!"
}

# 엔터 키 입력 대기 함수
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

# 디자인 적용 함수
apply_design() {
    local design_func=$1
    local design_name=$2
    local emoji=$3
    local next_design=$4
    
    echo ""
    echo "🚀 $design_name $emoji 적용 중..."
    $design_func
    
    wait_for_enter "$design_name" "$emoji" "$next_design"
}

# 메인 쇼케이스 루프
cycle_count=1
echo "🎬 통합 디자인 쇼케이스 시작! (Cycle #$cycle_count)"

while true; do
    echo ""
    echo "🔄 === Cycle #$cycle_count 시작 ==="
    echo ""
    
    # 1️⃣ 뉴모피즘
    apply_design "apply_neumorphism" "뉴모피즘" "🥚" "미니멀 다크모드 🌙"
    
    # 2️⃣ 다크 모드  
    apply_design "apply_darkmode" "미니멀 다크모드" "🌙" "그라데이션 메쉬 🌈"
    
    # 3️⃣ 그라데이션 메쉬
    apply_design "apply_gradient_mesh" "그라데이션 메쉬" "🌈" "3D 카드 📦"
    
    # 4️⃣ 3D 카드
    apply_design "apply_3d_cards" "3D 카드" "📦" ""
    
    cycle_count=$((cycle_count + 1))
    echo ""
    echo "🎉 Cycle #$((cycle_count - 1)) 완료!"
    echo "🔄 다음 사이클로 이동합니다..."
    echo ""
done 