import { Metadata } from 'next';
import dynamic from 'next/dynamic';

// 기존 컴포넌트 재사용 [[memory:5052747]]
const HeroSection = dynamic(() => import('@/components/sections/HeroSection'));
const ServicesSection = dynamic(() => import('@/components/sections/ServicesSection'));
const FeaturesSection = dynamic(() => import('@/components/sections/FeaturesSection'));
const PricingSection = dynamic(() => import('@/components/sections/PricingSection'));
const TestimonialsSection = dynamic(() => import('@/components/sections/TestimonialsSection'));
const CTASection = dynamic(() => import('@/components/sections/CTASection'));
const Footer = dynamic(() => import('@/components/layout/Footer'));

export const metadata: Metadata = {
  title: '✨ 현사AI - 글래스모피즘 디자인',
  description: '투명하고 세련된 글래스모피즘 UI로 만나는 현사AI 서비스',
  openGraph: {
    title: '✨ 현사AI - 글래스모피즘 경험',
    description: '🔮 투명함과 깊이감이 어우러진 미래형 AI 인터페이스',
  },
};

export default function GlassmorphismPage() {
  return (
    <main className="min-h-screen relative overflow-hidden">
      {/* 🌌 글래스모피즘 배경 레이어 */}
      <div className="fixed inset-0 z-0">
        {/* 그라데이션 배경 */}
        <div className="absolute inset-0 bg-gradient-to-br from-blue-400/20 via-purple-400/20 to-pink-400/20"></div>
        
        {/* 플로팅 글래스 오브젝트들 */}
        <div className="absolute top-20 left-20 w-32 h-32 glass-layer-1 rounded-full animate-float"></div>
        <div className="absolute top-40 right-32 w-24 h-24 glass-layer-2 rounded-lg rotate-45 animate-bounce-subtle"></div>
        <div className="absolute bottom-32 left-1/3 w-20 h-20 glass-layer-3 rounded-full animate-pulse"></div>
        
        {/* 배경 패턴 */}
        <div className="absolute inset-0 bg-grid-pattern opacity-20"></div>
      </div>

      {/* 🔮 글래스모피즘 헤더 */}
      <header className="glass-neon-gradient sticky top-0 z-50 border-b border-white/10">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            {/* 글래스 로고 */}
            <div className="flex items-center space-x-3">
              <div className="glass-depth-card w-12 h-12 flex items-center justify-center">
                <span className="text-white font-bold text-lg">AI</span>
              </div>
              <h1 className="text-2xl font-light text-white glass-text-frosted">
                현사<span className="gradient-animate bg-gradient-to-r from-blue-300 to-pink-300 bg-clip-text text-transparent">AI</span>
              </h1>
            </div>
            
            {/* 글래스 네비게이션 */}
            <nav className="hidden md:flex items-center space-x-6">
              <a href="#services" className="glass-dynamic px-4 py-2 rounded-lg text-white/90 hover:text-white">
                서비스
              </a>
              <a href="#features" className="glass-dynamic px-4 py-2 rounded-lg text-white/90 hover:text-white">
                기능
              </a>
              <a href="#pricing" className="glass-dynamic px-4 py-2 rounded-lg text-white/90 hover:text-white">
                가격
              </a>
              <button className="glass-neon-gradient px-6 py-2 rounded-xl text-white font-semibold hover:scale-105 transition-transform">
                ✨ 시작하기
              </button>
            </nav>
          </div>
        </div>
      </header>

      {/* 🌟 글래스모피즘 히어로 섹션 */}
      <section className="relative z-10 section-padding">
        <div className="container-custom text-center">
          <div className="glass-depth-card p-16 mb-12">
            <h2 className="text-6xl font-light text-white mb-6 glass-text-frosted">
              투명한 <span className="gradient-animate bg-gradient-to-r from-blue-300 via-purple-300 to-pink-300 bg-clip-text text-transparent">AI 경험</span>
            </h2>
            <p className="text-xl text-white/80 mb-8 max-w-2xl mx-auto leading-relaxed">
              글래스모피즘 디자인으로 만나는 차세대 AI 서비스.<br/>
              투명함 속에서 피어나는 무한한 가능성.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button className="glass-neon-blue px-8 py-4 rounded-2xl text-white font-semibold hover:scale-105 transition-all">
                🚀 지금 시작하기
              </button>
              <button className="glass-frosted px-8 py-4 rounded-2xl text-white/90 border border-white/20 hover:bg-white/10 transition-all">
                🔍 더 알아보기
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* 🔮 글래스 섹션들 - 기존 컴포넌트 래핑 */}
      <div className="glass-layer-1 relative z-10">
        <div className="glass-card-classic m-8 p-8 rounded-3xl">
          <HeroSection />
        </div>
      </div>
      
      <div className="glass-layer-2 relative z-10">
        <div className="glass-neon-purple m-8 p-8 rounded-3xl">
          <ServicesSection />
        </div>
      </div>
      
      <div className="glass-layer-3 relative z-10">
        <div className="glass-frosted m-8 p-8 rounded-3xl">
          <FeaturesSection />
        </div>
      </div>
      
      {/* 기존 섹션들 계속... */}
      <div className="relative z-10">
        <div className="glass-dynamic m-8 p-8 rounded-3xl">
          <PricingSection />
          <TestimonialsSection />
          <CTASection />
        </div>
      </div>
      
      <Footer />
    </main>
  );
} 