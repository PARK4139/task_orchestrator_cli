#!/bin/bash

echo "🔄 ensure_ 방식: 안정적인 컨텐츠 구조로 복구..."
echo "================================================"

echo "📝 기본 page.tsx 구조로 되돌리는 중..."

# 1. 기본 컨텐츠 구조로 page.tsx 복구
cat > app/page.tsx << 'EOF'
import { Metadata } from 'next';
import dynamic from 'next/dynamic';

// 컴포넌트 동적 로딩 (성능 최적화)
const HeroSection = dynamic(() => import('@/components/sections/HeroSection'));
const ServicesSection = dynamic(() => import('@/components/sections/ServicesSection'));
const FeaturesSection = dynamic(() => import('@/components/sections/FeaturesSection'));
const PricingSection = dynamic(() => import('@/components/sections/PricingSection'));
const TestimonialsSection = dynamic(() => import('@/components/sections/TestimonialsSection'));
const CTASection = dynamic(() => import('@/components/sections/CTASection'));

export const metadata: Metadata = {
  title: '현사AI - 현명한 사람들의 AI 서비스',
  description: '개인 맞춤형 AI 솔루션을 통해 일상과 비즈니스를 혁신하세요. 이미지 생성, 동화책 제작, 엑셀 자동화 등 다양한 서비스를 제공합니다.',
  keywords: '현사AI, AI 서비스, 인공지능, 개인 맞춤형 AI, 이미지 생성, 동화책 제작, 엑셀 자동화',
  openGraph: {
    title: '현사AI - 현명한 사람들의 AI 서비스',
    description: '개인 맞춤형 AI 솔루션으로 일상과 비즈니스를 혁신하세요',
    url: 'https://hyeonsa-ai.com',
    siteName: '현사AI',
    images: [{
      url: 'https://hyeonsa-ai.com/og-image.jpg',
      width: 1200,
      height: 630,
    }],
    locale: 'ko_KR',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: '현사AI - 현명한 사람들의 AI 서비스',
    description: '개인 맞춤형 AI 솔루션으로 일상과 비즈니스를 혁신하세요',
    images: ['https://hyeonsa-ai.com/twitter-image.jpg'],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
};

export default function HomePage() {
  return (
    <main className="min-h-screen">
      {/* 🎯 글래스모피즘 확인 배너 */}
      <div className="fixed top-0 left-0 right-0 z-50 glass-banner text-center py-3">
        <p className="text-lg font-bold text-white drop-shadow-lg">
          🔮 글래스모피즘 디자인 적용 완료! 투명하고 우아한 디자인을 확인하세요 ✨
        </p>
      </div>
      
      {/* 각 섹션들 */}
      <div className="pt-16">
        <HeroSection />
        <ServicesSection />
        <FeaturesSection />
        <PricingSection />
        <TestimonialsSection />
        <CTASection />
      </div>
    </main>
  );
}
EOF

echo "✅ 기본 컨텐츠 구조 복구 완료!"

# 2. 글래스모피즘 CSS 적용
echo "🔮 글래스모피즘 CSS 스타일 적용 중..."

cat > app/globals.css << 'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* 🔮 글래스모피즘 베이스 스타일 */
@layer base {
  html {
    scroll-behavior: smooth;
  }
  
  body {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
    background-size: 300% 300%;
    animation: gradientShift 15s ease infinite;
    min-height: 100vh;
  }
  
  @keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
}

/* 🔮 글래스모피즘 컴포넌트 */
@layer components {
  
  /* 기본 글래스 카드 */
  .glass-card {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  }
  
  /* 강한 글래스 효과 */
  .glass-strong {
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 25px;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
  }
  
  /* 부드러운 글래스 효과 */
  .glass-soft {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  }
  
  /* 글래스 버튼 */
  .glass-btn {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 50px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  }
  
  .glass-btn:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
  }
  
  /* 글래스 배너 */
  .glass-banner {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    animation: bannerGlow 3s ease-in-out infinite alternate;
  }
  
  @keyframes bannerGlow {
    0% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.2); }
    100% { box-shadow: 0 0 40px rgba(255, 255, 255, 0.4); }
  }
  
  /* 플로팅 애니메이션 */
  .glass-floating {
    animation: glassFloat 6s ease-in-out infinite;
  }
  
  @keyframes glassFloat {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    33% { transform: translateY(-15px) rotate(1deg); }
    66% { transform: translateY(-8px) rotate(-1deg); }
  }
  
  /* 호버 효과 */
  .glass-hover {
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }
  
  .glass-hover:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
    background: rgba(255, 255, 255, 0.25);
  }
  
  /* 텍스트 글래스 효과 */
  .glass-text {
    color: white;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    font-weight: 600;
  }
  
  /* 그라데이션 텍스트 (글래스모피즘과 조화) */
  .glass-gradient-text {
    background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.6) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
  }
  
  /* 네비게이션 글래스 */
  .glass-nav {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  }
  
  /* 모바일 반응형 */
  @media (max-width: 768px) {
    .glass-card, .glass-strong, .glass-soft {
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
    }
  }
}

/* 🌟 유틸리티 클래스 */
@layer utilities {
  .text-glass {
    @apply text-white drop-shadow-lg;
  }
  
  .bg-glass-light {
    background: rgba(255, 255, 255, 0.1);
  }
  
  .bg-glass-medium {
    background: rgba(255, 255, 255, 0.2);
  }
  
  .bg-glass-strong {
    background: rgba(255, 255, 255, 0.3);
  }
}
EOF

echo "✅ 글래스모피즘 CSS 적용 완료!"
echo ""
echo "🔮 글래스모피즘 디자인 적용 완료!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🌐 브라우저에서 http://localhost:3000 확인하세요!"
echo "✨ 투명하고 우아한 글래스모피즘 디자인을 경험해보세요!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" 