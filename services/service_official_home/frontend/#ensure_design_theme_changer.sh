#!/bin/bash

echo "🎨 ensure_ 방식: 디자인 테마 체인저..."
echo "================================================"

THEME="$1"

if [ -z "$THEME" ]; then
    echo "🎯 사용 가능한 디자인 테마:"
    echo "1. gradient   - 모던 그라데이션 (현재)"
    echo "2. minimal    - 미니멀 클린"
    echo "3. cyberpunk  - 사이버펑크 AI"
    echo "4. nature     - 네이처 소프트"
    echo "5. premium    - 프리미엄 다크"
    echo ""
    echo "사용법: ./ensure_design_theme_changer.sh [테마명]"
    echo "예시: ./ensure_design_theme_changer.sh minimal"
    exit 1
fi

echo "🎨 '$THEME' 테마로 변경 중..."

case $THEME in
    "gradient")
        echo "🌈 모던 그라데이션 테마 적용..."
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
  title: '🌈 현사AI - 모던 그라데이션 디자인',
  description: '아름다운 그라데이션으로 표현한 AI 서비스',
};

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50">
      {/* 그라데이션 헤더 */}
      <div className="bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 text-white text-center py-4">
        <div className="container mx-auto">
          <h1 className="text-2xl font-bold">🌈 모던 그라데이션 테마</h1>
          <p className="text-blue-100">부드럽고 생동감 있는 디자인</p>
        </div>
      </div>
      
      <HeroSection />
      <ServicesSection />
      <FeaturesSection />
      <PricingSection />
      <TestimonialsSection />
      <CTASection />
      <Footer />
    </main>
  );
}
EOF
        ;;
        
    "minimal")
        echo "🤍 미니멀 클린 테마 적용..."
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
  title: '🤍 현사AI - 미니멀 클린 디자인',
  description: '깔끔하고 단순한 미니멀 디자인',
};

export default function HomePage() {
  return (
    <main className="min-h-screen bg-white">
      {/* 미니멀 헤더 */}
      <div className="border-b border-gray-100 bg-white shadow-sm">
        <div className="container mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-light text-gray-900">현사AI</h1>
              <p className="text-sm text-gray-500 mt-1">미니멀 클린 디자인</p>
            </div>
            <div className="w-12 h-12 bg-gray-900 rounded-full flex items-center justify-center">
              <span className="text-white text-xl">AI</span>
            </div>
          </div>
        </div>
      </div>
      
      <div className="bg-gray-50">
        <HeroSection />
      </div>
      <ServicesSection />
      <div className="bg-gray-50">
        <FeaturesSection />
      </div>
      <PricingSection />
      <div className="bg-gray-50">
        <TestimonialsSection />
      </div>
      <CTASection />
      <Footer />
    </main>
  );
}
EOF
        ;;
        
    "cyberpunk")
        echo "🟣 사이버펑크 AI 테마 적용..."
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
  title: '🤖 현사AI - 사이버펑크 디자인',
  description: '미래적이고 테크한 사이버펑크 스타일',
};

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gray-900">
      {/* 사이버펑크 헤더 */}
      <div className="bg-gradient-to-r from-purple-900 via-blue-900 to-indigo-900 border-b-2 border-cyan-400">
        <div className="container mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-purple-400">
                🤖 현사AI
              </h1>
              <p className="text-cyan-300 mt-1 font-mono">CYBERPUNK.MODE.ACTIVATED</p>
            </div>
            <div className="relative">
              <div className="w-16 h-16 bg-gradient-to-r from-cyan-500 to-purple-500 rounded-lg flex items-center justify-center animate-pulse">
                <span className="text-black text-2xl font-bold">AI</span>
              </div>
              <div className="absolute -top-1 -right-1 w-4 h-4 bg-cyan-400 rounded-full animate-ping"></div>
            </div>
          </div>
        </div>
      </div>
      
      {/* 네온 그리드 배경 */}
      <div className="bg-gray-900 relative overflow-hidden">
        <div className="absolute inset-0 opacity-10">
          <div className="grid grid-cols-8 gap-4 h-full">
            {Array.from({length: 64}).map((_, i) => (
              <div key={i} className="border border-cyan-500"></div>
            ))}
          </div>
        </div>
        
        <HeroSection />
      </div>
      
      <div className="bg-black border-t border-cyan-400">
        <ServicesSection />
      </div>
      <div className="bg-gray-900">
        <FeaturesSection />
      </div>
      <div className="bg-black border-t border-purple-400">
        <PricingSection />
      </div>
      <div className="bg-gray-900">
        <TestimonialsSection />
      </div>
      <div className="bg-gradient-to-r from-purple-900 to-cyan-900">
        <CTASection />
      </div>
      <Footer />
    </main>
  );
}
EOF
        ;;
        
    "nature")
        echo "🌿 네이처 소프트 테마 적용..."
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
  title: '🌿 현사AI - 네이처 소프트 디자인',
  description: '자연스럽고 편안한 친환경 디자인',
};

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-green-50 via-emerald-50 to-teal-50">
      {/* 네이처 헤더 */}
      <div className="bg-gradient-to-r from-green-600 via-emerald-600 to-teal-600 text-white">
        <div className="container mx-auto px-4 py-8">
          <div className="text-center">
            <h1 className="text-4xl font-bold mb-2">🌿 현사AI</h1>
            <p className="text-green-100 text-lg">자연과 기술의 조화</p>
            <div className="flex justify-center mt-4 space-x-2">
              <span className="text-2xl animate-bounce">🌱</span>
              <span className="text-2xl animate-bounce delay-100">🍃</span>
              <span className="text-2xl animate-bounce delay-200">🌿</span>
            </div>
          </div>
        </div>
      </div>
      
      <HeroSection />
      
      <div className="bg-white">
        <ServicesSection />
      </div>
      
      <div className="bg-gradient-to-r from-green-100 to-emerald-100">
        <FeaturesSection />
      </div>
      
      <div className="bg-white">
        <PricingSection />
      </div>
      
      <div className="bg-gradient-to-r from-teal-100 to-green-100">
        <TestimonialsSection />
      </div>
      
      <div className="bg-gradient-to-r from-green-600 to-emerald-600">
        <CTASection />
      </div>
      
      <Footer />
    </main>
  );
}
EOF
        ;;
        
    "premium")
        echo "⚫ 프리미엄 다크 테마 적용..."
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
  title: '✨ 현사AI - 프리미엄 다크 디자인',
  description: '고급스럽고 세련된 프리미엄 다크 테마',
};

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gray-900">
      {/* 프리미엄 헤더 */}
      <div className="bg-gradient-to-r from-gray-900 via-black to-gray-900 border-b border-yellow-500">
        <div className="container mx-auto px-4 py-8">
          <div className="text-center">
            <h1 className="text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 via-yellow-500 to-yellow-600">
              현사AI
            </h1>
            <p className="text-gray-300 text-xl mt-2">Premium AI Experience</p>
            <div className="flex justify-center mt-4">
              <div className="w-24 h-1 bg-gradient-to-r from-yellow-400 to-yellow-600 rounded-full"></div>
            </div>
          </div>
        </div>
      </div>
      
      <div className="bg-gray-900">
        <HeroSection />
      </div>
      
      <div className="bg-black border-t border-gray-800">
        <ServicesSection />
      </div>
      
      <div className="bg-gray-900 border-t border-gray-800">
        <FeaturesSection />
      </div>
      
      <div className="bg-black border-t border-gray-800">
        <PricingSection />
      </div>
      
      <div className="bg-gray-900 border-t border-gray-800">
        <TestimonialsSection />
      </div>
      
      <div className="bg-gradient-to-r from-yellow-600 via-yellow-500 to-yellow-400">
        <CTASection />
      </div>
      
      <Footer />
    </main>
  );
}
EOF
        ;;
        
    *)
        echo "❌ 알 수 없는 테마: $THEME"
        echo "사용 가능한 테마: gradient, minimal, cyberpunk, nature, premium"
        exit 1
        ;;
esac

echo "✅ '$THEME' 테마 적용 완료!"
echo "🌐 브라우저에서 변경 사항을 확인하세요: http://localhost:3000"
echo "🔄 다른 테마를 시도해보려면:"
echo "   ./ensure_design_theme_changer.sh [테마명]" 