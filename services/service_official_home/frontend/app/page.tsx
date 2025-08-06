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
      <div className="neuro-gradient-soft text-center py-4 text-white shadow-lg">
        <p className="font-semibold">
          🥚 뉴모피즘 모드 활성화! 부드럽고 촉감적인 디자인을 경험해보세요 🤍
        </p>
      </div>

      <header className="neuro-header sticky top-0 z-50">
        <div className="container mx-auto px-6 py-6">
          <div className="flex items-center justify-between">
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
            
            <nav className="hidden md:flex items-center space-x-8">
              <a href="#hero" className="neuro-text hover:text-purple-600 font-medium transition-colors">홈</a>
              <a href="#services" className="neuro-text hover:text-purple-600 font-medium transition-colors">서비스</a>
              <a href="#features" className="neuro-text hover:text-purple-600 font-medium transition-colors">기능</a>
              <a href="#pricing" className="neuro-text hover:text-purple-600 font-medium transition-colors">가격</a>
              <button className="neuro-btn-primary rounded-2xl">🚀 시작하기</button>
            </nav>
          </div>
        </div>
      </header>

      <section id="hero" className="py-20">
        <div className="container mx-auto px-6 text-center">
          <div className="neuro-card max-w-5xl mx-auto">
            <div className="inline-flex items-center space-x-3 neuro-inset px-6 py-3 rounded-full mb-12">
              <div className="w-3 h-3 neuro-gradient-soft rounded-full"></div>
              <span className="neuro-text font-medium">현명한 사람들의 AI</span>
            </div>

            <h2 className="text-6xl md:text-8xl font-light neuro-text-dark mb-8 leading-tight">
              <span className="block mb-4">부드러운</span>
              <span className="block neuro-text-gradient font-bold">AI 경험</span>
            </h2>
            
            <p className="text-xl md:text-2xl neuro-text mb-16 leading-relaxed max-w-3xl mx-auto">
              뉴모피즘 디자인으로 만나는 포근한 AI 서비스.<br/>
              <span className="neuro-text-dark font-semibold">소프트하고 따뜻한 촉감의 인터페이스.</span>
            </p>
            
            <div className="flex flex-col sm:flex-row gap-8 justify-center items-center mb-16">
              <button className="neuro-btn-primary text-lg px-12 py-4">🚀 지금 시작하기</button>
              <button className="neuro-btn text-lg px-12 py-4">🔍 더 알아보기</button>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
              <div className="neuro-card p-6 text-center">
                <div className="neuro-icon-small mx-auto mb-4"><span>🎨</span></div>
                <span className="neuro-text font-medium">AI 이미지</span>
              </div>
              <div className="neuro-card p-6 text-center">
                <div className="neuro-icon-small mx-auto mb-4"><span>📚</span></div>
                <span className="neuro-text font-medium">동화책</span>
              </div>
              <div className="neuro-card p-6 text-center">
                <div className="neuro-icon-small mx-auto mb-4"><span>📊</span></div>
                <span className="neuro-text font-medium">엑셀 자동화</span>
              </div>
              <div className="neuro-card p-6 text-center">
                <div className="neuro-icon-small mx-auto mb-4"><span>🌐</span></div>
                <span className="neuro-text font-medium">웹 크롤링</span>
              </div>
            </div>
          </div>
        </div>
      </section>

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
      
      <section>
        <div className="neuro-section">
          <TestimonialsSection />
          <div className="mt-16"><CTASection /></div>
        </div>
      </section>
      
      <div className="neuro-header">
        <Footer />
      </div>
    </main>
  );
}
