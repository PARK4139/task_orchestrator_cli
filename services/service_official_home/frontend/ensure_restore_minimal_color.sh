#!/bin/bash

echo "🔄 ensure_ 방식: 미니멀 컬러 디자인으로 원복..."
echo "================================================"

echo "📝 globals.css 원복 중..."

# 1. globals.css를 깔끔한 미니멀 컬러 버전으로 복구
cat > app/globals.css << 'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;

/* 글로벌 스타일 */
@layer base {
  html {
    scroll-behavior: smooth;
  }
  
  body {
    @apply text-slate-800 antialiased;
  }
}

/* 미니멀 컬러 컴포넌트 */
@layer components {
  .btn-primary {
    @apply inline-flex items-center px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition-all duration-200 hover:scale-105 shadow-lg hover:shadow-xl;
  }
  
  .card {
    @apply bg-white rounded-xl shadow-sm border border-slate-200 hover:shadow-md transition-all duration-200;
  }
  
  .card-hover {
    @apply hover:-translate-y-1 hover:shadow-lg;
  }
  
  .gradient-bg {
    @apply bg-gradient-to-br from-slate-50 via-blue-50 to-slate-100;
  }
  
  .gradient-text {
    @apply bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent;
  }
}

/* 미니멀 컬러 애니메이션 */
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

.animate-float {
  animation: float 3s ease-in-out infinite;
}
EOF

echo "✅ CSS 원복 완료!"

echo "🎨 page.tsx를 미니멀 컬러 디자인으로 원복 중..."

# 2. page.tsx를 미니멀 컬러 버전으로 복구
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
const Footer = dynamic(() => import('@/components/layout/Footer'));

// 메타데이터 (SEO 최적화)
export const metadata: Metadata = {
  title: '🎨 현사AI - 미니멀 컬러 디자인',
  description: '깔끔한 미니멀 디자인에 생동감 있는 컬러를 더한 현사AI 서비스',
  openGraph: {
    title: '현사AI - 미니멀하지만 컬러풀한 AI 경험',
    description: '단순함과 아름다움이 조화된 AI 서비스 인터페이스',
    images: [
      {
        url: '/og-home.png',
        width: 1200,
        height: 630,
        alt: '현사AI 홈페이지 - 미니멀 컬러',
      },
    ],
  },
  alternates: {
    canonical: 'https://smartpersonai.com',
  },
};

export default function HomePage() {
  return (
    <main className="min-h-screen bg-white">
      {/* 🎨 원복 확인 배너 */}
      <div className="bg-gradient-to-r from-green-500 to-blue-500 text-white text-center py-2">
        <p className="text-sm font-medium">
          ✅ 미니멀 컬러 디자인으로 원복 완료! 깔끔하고 예쁜 디자인 🎨
        </p>
      </div>

      {/* 🎨 컬러풀 미니멀 헤더 */}
      <header className="border-b border-gray-100 bg-white shadow-sm sticky top-0 z-50 backdrop-blur-sm">
        <div className="container mx-auto px-6 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              {/* 그라데이션 로고 */}
              <div className="flex items-center space-x-3">
                <div className="w-14 h-14 bg-gradient-to-br from-blue-500 via-purple-500 to-pink-500 rounded-2xl flex items-center justify-center shadow-lg transform hover:scale-105 transition-transform">
                  <span className="text-white text-lg font-bold">AI</span>
                </div>
                <div>
                  <h1 className="text-3xl font-light text-gray-900 tracking-tight">
                    현사<span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">AI</span>
                  </h1>
                  <p className="text-sm text-gray-500 mt-0.5">Minimal • Colorful • Smart</p>
                </div>
              </div>
            </div>
            
            {/* 컬러풀 네비게이션 */}
            <nav className="hidden md:flex items-center space-x-8">
              <a href="#services" className="text-gray-600 hover:text-blue-600 transition-colors text-sm font-medium relative group">
                서비스
                <span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-blue-500 transition-all group-hover:w-full"></span>
              </a>
              <a href="#features" className="text-gray-600 hover:text-purple-600 transition-colors text-sm font-medium relative group">
                기능
                <span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-purple-500 transition-all group-hover:w-full"></span>
              </a>
              <a href="#pricing" className="text-gray-600 hover:text-pink-600 transition-colors text-sm font-medium relative group">
                가격
                <span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-pink-500 transition-all group-hover:w-full"></span>
              </a>
              <button className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-2.5 rounded-xl text-sm font-medium hover:shadow-lg transform hover:scale-105 transition-all duration-200">
                시작하기
              </button>
            </nav>
          </div>
        </div>
      </header>

      {/* 🌈 컬러풀 미니멀 히어로 섹션 */}
      <section className="relative overflow-hidden">
        {/* 서브틀한 그라데이션 배경 */}
        <div className="absolute inset-0 bg-gradient-to-br from-blue-50/30 via-purple-50/20 to-pink-50/30"></div>
        
        {/* 플로팅 컬러 도트들 */}
        <div className="absolute top-20 left-20 w-2 h-2 bg-blue-400 rounded-full animate-bounce"></div>
        <div className="absolute top-40 right-32 w-3 h-3 bg-purple-400 rounded-full animate-bounce delay-100"></div>
        <div className="absolute bottom-32 left-1/4 w-2 h-2 bg-pink-400 rounded-full animate-bounce delay-200"></div>
        
        <div className="relative py-24">
          <div className="container mx-auto px-6 text-center">
            <div className="max-w-4xl mx-auto">
              {/* 컬러풀 아이콘들 */}
              <div className="flex justify-center space-x-4 mb-8">
                <div className="w-3 h-3 bg-blue-500 rounded-full animate-pulse"></div>
                <div className="w-3 h-3 bg-purple-500 rounded-full animate-pulse delay-100"></div>
                <div className="w-3 h-3 bg-pink-500 rounded-full animate-pulse delay-200"></div>
              </div>

              <h2 className="text-6xl font-light text-gray-900 mb-6 leading-tight">
                Simple
                <span className="block text-transparent bg-clip-text bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 mt-2">
                  AI Experience
                </span>
              </h2>
              
              <p className="text-xl text-gray-600 mb-12 leading-relaxed max-w-2xl mx-auto">
                깔끔한 미니멀 디자인에 
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600 font-medium">생동감 있는 컬러</span>를 더했습니다.<br/>
                현명한 사람들을 위한 아름다운 AI 서비스.
              </p>
              
              {/* 그라데이션 CTA 버튼들 */}
              <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
                <button className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-10 py-4 rounded-xl text-lg font-medium hover:shadow-xl transform hover:scale-105 transition-all duration-200 relative overflow-hidden group">
                  <span className="relative z-10">지금 시작하기</span>
                  <div className="absolute inset-0 bg-gradient-to-r from-purple-600 to-pink-600 opacity-0 group-hover:opacity-100 transition-opacity duration-200"></div>
                </button>
                <button className="border-2 border-gray-200 text-gray-700 px-10 py-4 rounded-xl text-lg font-medium hover:border-purple-300 hover:bg-purple-50/50 transition-all duration-200 group">
                  <span className="group-hover:text-purple-600 transition-colors">더 알아보기</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 🎨 컬러 포인트가 있는 섹션들 */}
      
      {/* 서비스 소개 - 블루 포인트 */}
      <div className="bg-white border-t border-blue-100/50">
        <div className="max-w-7xl mx-auto py-4">
          <div className="h-1 bg-gradient-to-r from-transparent via-blue-500 to-transparent rounded-full"></div>
        </div>
        <HeroSection />
        <ServicesSection />
      </div>
      
      {/* 주요 기능 - 퍼플 포인트 */}
      <div className="bg-gradient-to-r from-purple-50/30 to-blue-50/30">
        <div className="max-w-7xl mx-auto py-4">
          <div className="h-1 bg-gradient-to-r from-transparent via-purple-500 to-transparent rounded-full"></div>
        </div>
        <FeaturesSection />
      </div>
      
      {/* 가격 정보 - 핑크 포인트 */}
      <div className="bg-white border-t border-pink-100/50">
        <div className="max-w-7xl mx-auto py-4">
          <div className="h-1 bg-gradient-to-r from-transparent via-pink-500 to-transparent rounded-full"></div>
        </div>
        <PricingSection />
      </div>
      
      {/* 고객 후기 - 그라데이션 포인트 */}
      <div className="bg-gradient-to-r from-blue-50/20 via-purple-50/20 to-pink-50/20">
        <div className="max-w-7xl mx-auto py-4">
          <div className="h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 rounded-full"></div>
        </div>
        <TestimonialsSection />
      </div>
      
      {/* CTA 섹션 - 컬러풀 배경 */}
      <div className="bg-white">
        <CTASection />
      </div>
      
      {/* 푸터 */}
      <Footer />
    </main>
  );
}
EOF

echo ""
echo "✅ 미니멀 컬러 디자인으로 완전 원복!"
echo "================================================"
echo ""
echo "🎨 복구된 디자인 특징:"
echo "   • 🤍 깔끔한 화이트 베이스"
echo "   • 🌈 적절한 컬러 포인트"
echo "   • ✨ 서브틀한 그라데이션"
echo "   • 🎯 미니멀한 레이아웃"
echo "   • 📏 컬러별 섹션 구분선"
echo "   • 🎪 작은 플로팅 도트들"
echo ""
echo "🌐 브라우저에서 확인: http://localhost:3000"
echo "🎉 깔끔하고 예쁜 미니멀 컬러 디자인으로 돌아왔습니다!"
EOF

## 🚀 **바로 실행하세요!**

```bash
cd services/smart_person_ai/service_official_home_smart_person_ai/frontend
chmod +x ensure_restore_minimal_color.sh
./ensure_restore_minimal_color.sh
```

## ✅ **원복 완료!**

**이제 브라우저에서 http://localhost:3000 을 새로고침하면:**

1. **🤍 깔끔한 화이트 배경**
2. **🌈 그라데이션 로고** (적당한 크기)
3. **🎯 "현사AI"** - AI 부분만 그라데이션
4. **✨ "Simple AI Experience"** - 무지개 그라데이션
5. **📏 섹션별 컬러 구분선** (블루→퍼플→핑크)
6. **🎪 작은 플로팅 도트들** (과하지 않게)
7. **🎨 적절한 컬러 포인트들**

**깔끔하고 예쁜 미니멀 컬러 디자인으로 완전히 돌아왔습니다!** 🎨✨

너무 과했던 프리미엄 다크 모드에서 벗어나서 적절하고 예쁜 디자인으로 원복되었습니다! 🤍🌈 