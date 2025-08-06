#!/bin/bash

echo "🥚 ensure_neumorphism_applied.sh: 뉴모피즘 디자인 적용..."
echo "========================================================"

echo "🎨 globals.css에 뉴모피즘 스타일 추가 중..."

# 뉴모피즘 스타일을 globals.css에 추가
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

  .neuro-btn-primary:hover {
    box-shadow: 
      25px 25px 75px #5a6fd8,
      -25px -25px 75px #7c8cfc;
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

  /* 뉴모피즘 입력 필드 */
  .neuro-input {
    @apply neuro-inset px-6 py-4 w-full;
    background: #f0f0f3;
    border: none;
    outline: none;
    color: #666;
  }

  .neuro-input::placeholder {
    color: #aaa;
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

  /* 소프트 그라데이션 */
  .neuro-gradient {
    background: linear-gradient(145deg, #f0f0f3, #cacaca);
  }

  .neuro-gradient-soft {
    background: linear-gradient(145deg, #667eea 0%, #764ba2 100%);
  }

  /* 뉴모피즘 텍스트 */
  .neuro-text {
    color: #666;
    text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
  }

  .neuro-text-dark {
    color: #333;
    text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.5);
  }

  .neuro-text-gradient {
    background: linear-gradient(145deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
}

/* 뉴모피즘 애니메이션 */
@keyframes neuro-float {
  0%, 100% { 
    transform: translateY(0px);
    box-shadow: 
      20px 20px 60px #bebebe,
      -20px -20px 60px #ffffff;
  }
  50% { 
    transform: translateY(-10px);
    box-shadow: 
      25px 30px 70px #bebebe,
      -25px -30px 70px #ffffff;
  }
}

.neuro-animate-float {
  animation: neuro-float 4s ease-in-out infinite;
}

/* 호버 펄스 효과 */
@keyframes neuro-pulse {
  0%, 100% {
    box-shadow: 
      20px 20px 60px #bebebe,
      -20px -20px 60px #ffffff;
  }
  50% {
    box-shadow: 
      30px 30px 80px #bebebe,
      -30px -30px 80px #ffffff;
  }
}

.neuro-pulse {
  animation: neuro-pulse 2s ease-in-out infinite;
}

/* 반응형 최적화 */
@media (max-width: 768px) {
  .neuro-card {
    border-radius: 15px;
    box-shadow: 
      15px 15px 45px #bebebe,
      -15px -15px 45px #ffffff;
  }
  
  .neuro-section {
    margin: 1rem;
    padding: 2rem;
    border-radius: 20px;
  }
}
EOF

echo "✅ 뉴모피즘 CSS 추가 완료!"

echo "🥚 page.tsx를 뉴모피즘 디자인으로 업데이트 중..."

# 뉴모피즘 page.tsx
cat > app/page.tsx << 'EOF'
import { Metadata } from 'next';
import dynamic from 'next/dynamic';

const HeroSection = dynamic(() => import('@/components/sections/HeroSection'));
const ServicesSection = dynamic(() => import('@/components/sections/ServicesSection'));
const FeaturesSection = dynamic(() => import('@/components/sections/FeaturesSection'));
const PricingSection = dynamic(() => import('@/components/sections/PricingSection'));
const TestimonialsSection = dynamic(() => import('@/components/sections/TestimonialsSection'));
const CTASection = dynamic(() => import('@/components/sections/CTASection'));
const Footer = dynamic(() => import('@/components/layout/Footer'));

export const metadata: Metadata = {
  title: '🥚 현사AI - 뉴모피즘 디자인',
  description: '소프트하고 촉감적인 뉴모피즘 UI로 만나는 현사AI - 포근한 입체감의 AI 서비스',
  openGraph: {
    title: '🥚 현사AI - 소프트한 뉴모피즘 경험',
    description: '🤍 부드럽고 따뜻한 뉴모피즘 디자인으로 만나는 AI 서비스',
  },
};

export default function NeumorphismHomePage() {
  return (
    <main className="min-h-screen" style={{ background: '#f0f0f3' }}>
      {/* 🥚 뉴모피즘 상태 확인 배너 */}
      <div className="neuro-gradient-soft text-center py-4 text-white shadow-lg">
        <p className="font-semibold">
          🥚 뉴모피즘 모드 활성화! 부드럽고 촉감적인 디자인을 경험해보세요 🤍
        </p>
      </div>

      {/* 🥚 뉴모피즘 헤더 */}
      <header className="neuro-header sticky top-0 z-50">
        <div className="container mx-auto px-6 py-6">
          <div className="flex items-center justify-between">
            {/* 소프트 로고 */}
            <div className="flex items-center space-x-6">
              <div className="neuro-icon neuro-animate-float">
                <span className="text-2xl font-bold neuro-text-gradient">AI</span>
              </div>
              <div>
                <h1 className="text-4xl font-light neuro-text-dark">
                  현사<span className="neuro-text-gradient font-bold">AI</span>
                </h1>
                <p className="text-sm neuro-text mt-1">Soft • Tactile • Warm</p>
              </div>
            </div>
            
            {/* 뉴모피즘 네비게이션 */}
            <nav className="hidden md:flex items-center space-x-8">
              <a href="#hero" className="neuro-text hover:text-purple-600 font-medium transition-colors">
                홈
              </a>
              <a href="#services" className="neuro-text hover:text-purple-600 font-medium transition-colors">
                서비스
              </a>
              <a href="#features" className="neuro-text hover:text-purple-600 font-medium transition-colors">
                기능
              </a>
              <a href="#pricing" className="neuro-text hover:text-purple-600 font-medium transition-colors">
                가격
              </a>
              <button className="neuro-btn-primary rounded-2xl">
                🚀 시작하기
              </button>
            </nav>
          </div>
        </div>
      </header>

      {/* 🥚 뉴모피즘 히어로 섹션 */}
      <section id="hero" className="py-20">
        <div className="container mx-auto px-6 text-center">
          <div className="neuro-card max-w-5xl mx-auto">
            {/* 소프트 브랜드 태그 */}
            <div className="inline-flex items-center space-x-3 neuro-inset px-6 py-3 rounded-full mb-12">
              <div className="w-3 h-3 neuro-gradient-soft rounded-full"></div>
              <span className="neuro-text font-medium">현명한 사람들의 AI</span>
            </div>

            {/* 메인 제목 */}
            <h2 className="text-6xl md:text-8xl font-light neuro-text-dark mb-8 leading-tight">
              <span className="block mb-4">부드러운</span>
              <span className="block neuro-text-gradient font-bold">
                AI 경험
              </span>
            </h2>
            
            {/* 부제목 */}
            <p className="text-xl md:text-2xl neuro-text mb-16 leading-relaxed max-w-3xl mx-auto">
              뉴모피즘 디자인으로 만나는 포근한 AI 서비스.<br/>
              <span className="neuro-text-dark font-semibold">소프트하고 따뜻한 촉감의 인터페이스.</span>
            </p>
            
            {/* 소프트 버튼들 */}
            <div className="flex flex-col sm:flex-row gap-8 justify-center items-center mb-16">
              <button className="neuro-btn-primary text-lg px-12 py-4">
                🚀 지금 시작하기
              </button>
              <button className="neuro-btn text-lg px-12 py-4">
                🔍 더 알아보기
              </button>
            </div>

            {/* 서비스 미리보기 */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
              <div className="neuro-card p-6 text-center">
                <div className="neuro-icon-small mx-auto mb-4">
                  <span>🎨</span>
                </div>
                <span className="neuro-text font-medium">AI 이미지</span>
              </div>
              <div className="neuro-card p-6 text-center">
                <div className="neuro-icon-small mx-auto mb-4">
                  <span>📚</span>
                </div>
                <span className="neuro-text font-medium">동화책</span>
              </div>
              <div className="neuro-card p-6 text-center">
                <div className="neuro-icon-small mx-auto mb-4">
                  <span>📊</span>
                </div>
                <span className="neuro-text font-medium">엑셀 자동화</span>
              </div>
              <div className="neuro-card p-6 text-center">
                <div className="neuro-icon-small mx-auto mb-4">
                  <span>🌐</span>
                </div>
                <span className="neuro-text font-medium">웹 크롤링</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 🥚 뉴모피즘 섹션들 */}
      <section id="services">
        <div className="neuro-section">
          <div className="text-center mb-12">
            <div className="inline-block neuro-inset px-8 py-4 rounded-2xl mb-6">
              <span className="neuro-text-gradient font-bold text-lg">🔵 주요 서비스</span>
            </div>
          </div>
          <ServicesSection />
        </div>
      </section>
      
      <section id="features">
        <div className="neuro-section">
          <div className="text-center mb-12">
            <div className="inline-block neuro-inset px-8 py-4 rounded-2xl mb-6">
              <span className="neuro-text-gradient font-bold text-lg">🟣 핵심 기능</span>
            </div>
          </div>
          <FeaturesSection />
        </div>
      </section>
      
      <section id="pricing">
        <div className="neuro-section">
          <div className="text-center mb-12">
            <div className="inline-block neuro-inset px-8 py-4 rounded-2xl mb-6">
              <span className="neuro-text-gradient font-bold text-lg">💎 가격 정보</span>
            </div>
          </div>
          <PricingSection />
        </div>
      </section>
      
      {/* 고객 후기 & CTA */}
      <section>
        <div className="neuro-section">
          <TestimonialsSection />
          <div className="mt-16">
            <CTASection />
          </div>
        </div>
      </section>
      
      {/* 뉴모피즘 푸터 */}
      <div className="neuro-header">
        <Footer />
      </div>
    </main>
  );
}
EOF

echo ""
echo "✅ 뉴모피즘 디자인 적용 완료!"
echo "=================================="
echo ""
echo "🥚 뉴모피즘 특징:"
echo "   • 🤍 소프트한 그림자 효과"
echo "   • 🎨 부드러운 입체감"
echo "   • 💫 촉감적인 인터랙션"
echo "   • 🌟 따뜻한 컬러 팔레트"
echo ""
echo "🌐 브라우저에서 확인: http://localhost:3000"
echo "🎉 포근한 뉴모피즘 디자인이 적용되었습니다!" 