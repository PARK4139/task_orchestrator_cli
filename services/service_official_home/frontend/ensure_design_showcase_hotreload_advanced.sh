#!/bin/bash

echo "🎪 ensure_design_showcase_hotreload_advanced.sh: 완전한 디자인 쇼케이스!"
echo "=================================================================="
echo ""
echo "🎨 사용 가능한 디자인 테마 (총 10개):"
echo "   1️⃣ 뉴모피즘 (Neumorphism) 🥚"
echo "   2️⃣ 다크모드 (Dark Mode) 🌙" 
echo "   3️⃣ 그라데이션 메쉬 (Gradient Mesh) 🌈"
echo "   4️⃣ 3D 카드 (3D Cards) 📦"
echo "   5️⃣ 글래스모피즘 (Glassmorphism) ✨"
echo "   6️⃣ 모던 그라데이션 (Modern Gradient) 🌈"
echo "   7️⃣ 미니멀 클린 (Minimal Clean) 🤍"
echo "   8️⃣ 사이버펑크 (Cyberpunk) 🟣"
echo "   9️⃣ 네이처 소프트 (Nature) 🌿"
echo "   🔟 프리미엄 다크 (Premium Dark) ⚫"
echo ""
echo "🌐 브라우저: http://localhost:3000"
echo "⏹️  중단하려면 Ctrl+C"
echo ""

# 1️⃣ 뉴모피즘 디자인 적용 함수
apply_neumorphism() {
    echo "🥚 뉴모피즘 디자인 적용 중..."
    
    # 뉴모피즘 globals.css
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

  .neuro-btn {
    @apply neuro-base px-8 py-4 font-semibold;
    color: #666;
    transition: all 0.2s ease;
    cursor: pointer;
  }

  .neuro-btn-primary {
    background: linear-gradient(145deg, #667eea, #764ba2);
    color: white;
    box-shadow: 
      20px 20px 60px #5a6fd8,
      -20px -20px 60px #7c8cfc;
  }

  .neuro-header {
    background: #f0f0f3;
    box-shadow: 
      0 10px 30px #bebebe,
      0 -10px 30px #ffffff;
    backdrop-filter: blur(10px);
  }

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

  .neuro-section {
    background: #f0f0f3;
    border-radius: 30px;
    box-shadow: 
      30px 30px 80px #bebebe,
      -30px -30px 80px #ffffff;
    margin: 2rem;
    padding: 3rem;
  }

  .neuro-gradient-soft {
    background: linear-gradient(145deg, #667eea 0%, #764ba2 100%);
  }

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
}
EOF

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
EOF

    echo "✅ 1️⃣ 뉴모피즘 디자인 완전 적용 완료!"
}

# 2️⃣ 다크모드 디자인 적용 함수
apply_darkmode() {
    echo "🌙 다크모드 디자인 적용 중..."
    
    cat > app/globals.css << 'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  html { scroll-behavior: smooth; }
  body { @apply antialiased; background: #0a0a0a; color: #ffffff; }
}

@layer components {
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
  .dark-btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    color: white;
    padding: 12px 32px;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
  }
  .dark-header {
    background: rgba(10, 10, 10, 0.8);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(20px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
  }
  .dark-section {
    background: rgba(15, 15, 15, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 24px;
    margin: 2rem;
    padding: 3rem;
    backdrop-filter: blur(10px);
  }
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
  .dark-icon-small { @apply dark-icon; width: 48px; height: 48px; border-radius: 10px; }
  .dark-text { color: #ffffff; }
  .dark-text-muted { color: rgba(255, 255, 255, 0.7); }
  .dark-text-gradient {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .dark-gradient-banner {
    background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }
}
EOF

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
  title: '🌙 현사AI - 다크 모드',
  description: '세련되고 깔끔한 다크 모드로 만나는 현사AI - 편안한 어둠 속의 AI 서비스',
};

export default function DarkModeHomePage() {
  return (
    <main className="min-h-screen bg-black text-white">
      <div className="dark-gradient-banner text-center py-4">
        <p className="font-semibold dark-text">
          🌙 다크 모드 활성화! 세련되고 편안한 어둠 속 디자인을 경험해보세요 🖤
        </p>
      </div>

      <header className="dark-header sticky top-0 z-50">
        <div className="container mx-auto px-6 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-6">
              <div className="dark-icon">
                <span className="text-2xl font-bold dark-text-gradient">AI</span>
              </div>
              <div>
                <h1 className="text-4xl font-light dark-text">
                  현사<span className="dark-text-gradient font-bold">AI</span>
                </h1>
                <p className="text-sm dark-text-muted mt-1">Dark • Minimal • Elegant</p>
              </div>
            </div>
            
            <nav className="hidden md:flex items-center space-x-8">
              <a href="#hero" className="dark-text-muted hover:text-purple-400 font-medium transition-colors">홈</a>
              <a href="#services" className="dark-text-muted hover:text-purple-400 font-medium transition-colors">서비스</a>
              <a href="#features" className="dark-text-muted hover:text-purple-400 font-medium transition-colors">기능</a>
              <a href="#pricing" className="dark-text-muted hover:text-purple-400 font-medium transition-colors">가격</a>
              <button className="dark-btn-primary rounded-2xl">🚀 시작하기</button>
            </nav>
          </div>
        </div>
      </header>

      <section id="hero" className="py-20">
        <div className="container mx-auto px-6 text-center">
          <div className="dark-card max-w-5xl mx-auto">
            <h2 className="text-6xl md:text-8xl font-light dark-text mb-8 leading-tight">
              <span className="block mb-4">세련된</span>
              <span className="block dark-text-gradient font-bold">AI 경험</span>
            </h2>
            
            <p className="text-xl md:text-2xl dark-text-muted mb-16 leading-relaxed max-w-3xl mx-auto">
              다크 모드로 만나는 우아한 AI 서비스.<br/>
              <span className="dark-text font-semibold">편안한 어둠 속에서 만나는 세련된 인터페이스.</span>
            </p>
            
            <div className="flex flex-col sm:flex-row gap-8 justify-center items-center mb-16">
              <button className="dark-btn-primary text-lg px-12 py-4">🚀 지금 시작하기</button>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
              <div className="dark-card p-6 text-center">
                <div className="dark-icon-small mx-auto mb-4"><span>🎨</span></div>
                <span className="dark-text-muted font-medium">AI 이미지</span>
              </div>
              <div className="dark-card p-6 text-center">
                <div className="dark-icon-small mx-auto mb-4"><span>📚</span></div>
                <span className="dark-text-muted font-medium">동화책</span>
              </div>
              <div className="dark-card p-6 text-center">
                <div className="dark-icon-small mx-auto mb-4"><span>📊</span></div>
                <span className="dark-text-muted font-medium">엑셀 자동화</span>
              </div>
              <div className="dark-card p-6 text-center">
                <div className="dark-icon-small mx-auto mb-4"><span>🌐</span></div>
                <span className="dark-text-muted font-medium">웹 크롤링</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="services">
        <div className="dark-section">
          <ServicesSection />
        </div>
      </section>
      
      <section id="features">
        <div className="dark-section">
          <FeaturesSection />
        </div>
      </section>
      
      <section id="pricing">
        <div className="dark-section">
          <PricingSection />
        </div>
      </section>
      
      <section>
        <div className="dark-section">
          <TestimonialsSection />
          <div className="mt-16"><CTASection /></div>
        </div>
      </section>
      
      <div className="dark-header">
        <Footer />
      </div>
    </main>
  );
}
EOF

    echo "✅ 2️⃣ 다크모드 디자인 완전 적용 완료!"
}

# 3️⃣ 그라데이션 메쉬 디자인 적용 함수
apply_gradient_mesh() {
    echo "🌈 그라데이션 메쉬 디자인 적용 중..."
    
    cat > app/globals.css << 'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  html { scroll-behavior: smooth; }
  body { 
    @apply antialiased; 
    background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
    background-size: 400% 400%;
    animation: gradient-shift 20s ease infinite;
    min-height: 100vh;
    color: #333;
  }
}

@layer components {
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
  .mesh-btn-secondary {
    background: rgba(255, 255, 255, 0.15);
    border: 2px solid rgba(255, 255, 255, 0.25);
    color: rgba(255, 255, 255, 0.9);
  }
  .mesh-header {
    background: rgba(255, 255, 255, 0.1);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(30px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  }
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
  .mesh-icon-small { @apply mesh-icon; width: 48px; height: 48px; border-radius: 12px; }
  .mesh-text { color: #ffffff; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); }
  .mesh-text-muted { color: rgba(255, 255, 255, 0.8); }
  .mesh-text-gradient {
    background: linear-gradient(135deg, #ffffff 0%, rgba(255, 255, 255, 0.7) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .mesh-gradient-banner {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  }
  @keyframes gradient-shift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
  @keyframes rotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
}
EOF

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
  title: '🌈 현사AI - 그라데이션 메쉬',
  description: '화려하고 역동적인 그라데이션 메쉬로 만나는 현사AI - 생생한 컬러의 AI 서비스',
};

export default function HomePage() {
  return (
    <main className="min-h-screen">
      <div className="mesh-gradient-banner text-center py-4">
        <p className="font-semibold mesh-text">
          🌈 그라데이션 메쉬 모드! 화려하고 역동적인 컬러 디자인을 경험해보세요 🎨
        </p>
      </div>

      <header className="mesh-header sticky top-0 z-50">
        <div className="container mx-auto px-6 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-6">
              <div className="mesh-icon">
                <span className="text-2xl font-bold mesh-text-gradient">AI</span>
              </div>
              <div>
                <h1 className="text-4xl font-light mesh-text">
                  현사<span className="mesh-text-gradient font-bold">AI</span>
                </h1>
                <p className="text-sm mesh-text-muted mt-1">Colorful • Dynamic • Vibrant</p>
              </div>
            </div>
            
            <nav className="hidden md:flex items-center space-x-8">
              <a href="#hero" className="mesh-text-muted hover:text-white font-medium transition-colors">홈</a>
              <a href="#services" className="mesh-text-muted hover:text-white font-medium transition-colors">서비스</a>
              <a href="#features" className="mesh-text-muted hover:text-white font-medium transition-colors">기능</a>
              <a href="#pricing" className="mesh-text-muted hover:text-white font-medium transition-colors">가격</a>
              <button className="mesh-btn-primary rounded-2xl">🚀 시작하기</button>
            </nav>
          </div>
        </div>
      </header>

      <section id="hero" className="py-20">
        <div className="container mx-auto px-6 text-center">
          <div className="mesh-card max-w-5xl mx-auto">
            <h2 className="text-6xl md:text-8xl font-light mesh-text mb-8 leading-tight">
              <span className="block mb-4">화려한</span>
              <span className="block mesh-text-gradient font-bold">AI 경험</span>
            </h2>
            
            <p className="text-xl md:text-2xl mesh-text-muted mb-16 leading-relaxed max-w-3xl mx-auto">
              그라데이션 메쉬로 만나는 생동감 넘치는 AI 서비스.<br/>
              <span className="mesh-text font-semibold">화려한 컬러와 역동적인 애니메이션의 인터페이스.</span>
            </p>
            
            <div className="flex flex-col sm:flex-row gap-8 justify-center items-center mb-16">
              <button className="mesh-btn-primary text-lg px-12 py-4">🚀 지금 시작하기</button>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
              <div className="mesh-card p-6 text-center">
                <div className="mesh-icon-small mx-auto mb-4"><span>🎨</span></div>
                <span className="mesh-text-muted font-medium">AI 이미지</span>
              </div>
              <div className="mesh-card p-6 text-center">
                <div className="mesh-icon-small mx-auto mb-4"><span>📚</span></div>
                <span className="mesh-text-muted font-medium">동화책</span>
              </div>
              <div className="mesh-card p-6 text-center">
                <div className="mesh-icon-small mx-auto mb-4"><span>📊</span></div>
                <span className="mesh-text-muted font-medium">엑셀 자동화</span>
              </div>
              <div className="mesh-card p-6 text-center">
                <div className="mesh-icon-small mx-auto mb-4"><span>🌐</span></div>
                <span className="mesh-text-muted font-medium">웹 크롤링</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="services">
        <div className="mesh-section">
          <ServicesSection />
        </div>
      </section>
      
      <section id="features">
        <div className="mesh-section">
          <FeaturesSection />
        </div>
      </section>
      
      <section id="pricing">
        <div className="mesh-section">
          <PricingSection />
        </div>
      </section>
      
      <section>
        <div className="mesh-section">
          <TestimonialsSection />
          <div className="mt-16"><CTASection /></div>
        </div>
      </section>
      
      <div className="mesh-header">
        <Footer />
      </div>
    </main>
  );
}
EOF

    echo "✅ 3️⃣ 그라데이션 메쉬 디자인 완전 적용 완료!"
}

# 4️⃣ 3D 카드 디자인 적용 함수
apply_3d_cards() {
    echo "📦 3D 카드 디자인 적용 중..."
    
    cat > app/globals.css << 'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  html { scroll-behavior: smooth; }
  body { 
    @apply antialiased; 
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    perspective: 1000px;
    color: #333;
  }
}

@layer components {
  .card-3d-container {
    perspective: 1000px;
    transform-style: preserve-3d;
  }
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
  .card-3d-tilt { @apply card-3d; transform-origin: center; }
  .card-3d-tilt:hover { transform: rotateX(-15deg) rotateY(-10deg) translateY(-25px); }
  .card-3d-flip { @apply card-3d; transform-style: preserve-3d; }
  .card-3d-flip:hover { transform: rotateY(15deg) translateZ(30px); }
  .card-3d-float { @apply card-3d; animation: float3d 6s ease-in-out infinite; }
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
  .btn-3d-primary {
    background: linear-gradient(145deg, #667eea, #764ba2);
    color: white;
    box-shadow: 
      0 10px 20px rgba(102, 126, 234, 0.3),
      inset 0 1px 0 rgba(255, 255, 255, 0.2);
  }
  .btn-3d-primary:hover {
    background: linear-gradient(145deg, #7c8cfc, #8a5db8);
    box-shadow: 
      0 20px 40px rgba(102, 126, 234, 0.4),
      inset 0 1px 0 rgba(255, 255, 255, 0.3);
  }
  .btn-3d-secondary {
    background: linear-gradient(145deg, #f8f9fa, #e9ecef);
    color: #6c757d;
  }
  .header-3d {
    background: rgba(255, 255, 255, 0.95);
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(20px);
    box-shadow: 
      0 4px 16px rgba(0, 0, 0, 0.1),
      inset 0 1px 0 rgba(255, 255, 255, 0.8);
    transform-style: preserve-3d;
  }
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
  .icon-3d:hover {
    transform: rotateX(-10deg) rotateY(10deg) translateY(-5px);
  }
  .icon-3d-small { @apply icon-3d; width: 48px; height: 48px; font-size: 18px; border-radius: 12px; }
  .text-3d { color: #333; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); }
  .text-3d-muted { color: #6c757d; }
  .text-3d-gradient {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .grid-3d {
    display: grid;
    gap: 2rem;
    transform-style: preserve-3d;
  }
  .bg-3d-layer {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    z-index: -1;
  }
  .gradient-3d-banner {
    background: linear-gradient(145deg, #667eea, #764ba2);
    box-shadow: 
      0 4px 16px rgba(0, 0, 0, 0.1),
      inset 0 1px 0 rgba(255, 255, 255, 0.2);
  }
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
  title: '📦 현사AI - 3D 카드 디자인',
  description: '입체적이고 역동적인 3D 카드로 만나는 현사AI - 깊이감 있는 인터랙티브 AI 서비스',
};

export default function HomePage() {
  return (
    <main className="min-h-screen card-3d-container">
      <div className="bg-3d-layer"></div>

      <div className="gradient-3d-banner w-full text-center py-4">
        <p className="font-bold text-white">
          📦 3D 카드 모드! 입체적이고 역동적인 디자인을 경험해보세요 🎯
        </p>
      </div>

      <header className="header-3d sticky top-0 z-50">
        <div className="container mx-auto px-6 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-6">
              <div className="icon-3d card-3d-pulse">
                <span className="text-2xl font-bold text-3d-gradient">AI</span>
              </div>
              <div>
                <h1 className="text-4xl font-light text-3d">
                  현사<span className="text-3d-gradient font-bold">AI</span>
                </h1>
                <p className="text-sm text-3d-muted mt-1">3D • Interactive • Dynamic</p>
              </div>
            </div>
            
            <nav className="hidden md:flex items-center space-x-8">
              <a href="#hero" className="text-3d-muted hover:text-purple-600 font-medium transition-colors">홈</a>
              <a href="#services" className="text-3d-muted hover:text-purple-600 font-medium transition-colors">서비스</a>
              <a href="#features" className="text-3d-muted hover:text-purple-600 font-medium transition-colors">기능</a>
              <a href="#pricing" className="text-3d-muted hover:text-purple-600 font-medium transition-colors">가격</a>
              <button className="btn-3d-primary">✨ 시작하기</button>
            </nav>
          </div>
        </div>
      </header>

      <section id="hero" className="py-20">
        <div className="container mx-auto px-6 text-center">
          <div className="card-3d-tilt max-w-5xl mx-auto">
            <h2 className="text-6xl md:text-8xl font-light text-3d mb-8 leading-tight">
              <span className="block mb-4">입체적</span>
              <span className="block text-3d-gradient font-bold">AI 경험</span>
            </h2>
            
            <p className="text-xl md:text-2xl text-3d-muted mb-16 leading-relaxed max-w-3xl mx-auto">
              3D 카드로 만나는 역동적 AI 서비스.<br/>
              <span className="text-3d font-semibold">깊이감과 원근법이 살아있는 인터페이스.</span>
            </p>
            
            <div className="flex flex-col sm:flex-row gap-8 justify-center items-center mb-16">
              <button className="btn-3d-primary text-lg px-12 py-4">🚀 지금 시작하기</button>
            </div>

            <div className="grid-3d grid-cols-2 md:grid-cols-4">
              <div className="card-3d-flip p-6 text-center">
                <div className="icon-3d-small mx-auto mb-4"><span>🎨</span></div>
                <span className="text-3d-muted font-medium">AI 이미지</span>
              </div>
              <div className="card-3d-tilt p-6 text-center">
                <div className="icon-3d-small mx-auto mb-4"><span>📚</span></div>
                <span className="text-3d-muted font-medium">동화책</span>
              </div>
              <div className="card-3d-float p-6 text-center">
                <div className="icon-3d-small mx-auto mb-4"><span>📊</span></div>
                <span className="text-3d-muted font-medium">엑셀 자동화</span>
              </div>
              <div className="card-3d p-6 text-center">
                <div className="icon-3d-small mx-auto mb-4"><span>🌐</span></div>
                <span className="text-3d-muted font-medium">웹 크롤링</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="services">
        <div className="section-3d">
          <ServicesSection />
        </div>
      </section>
      
      <section id="features">
        <div className="section-3d">
          <FeaturesSection />
        </div>
      </section>
      
      <section id="pricing">
        <div className="section-3d">
          <PricingSection />
        </div>
      </section>
      
      <section>
        <div className="section-3d">
          <TestimonialsSection />
          <div className="mt-16"><CTASection /></div>
        </div>
      </section>
      
      <div className="header-3d">
        <Footer />
      </div>
    </main>
  );
}
EOF

    echo "✅ 4️⃣ 3D 카드 디자인 완전 적용 완료!"
}

# 5️⃣ 글래스모피즘 디자인 적용 함수
apply_glassmorphism() {
    echo "✨ 글래스모피즘 디자인 적용 중..."
    
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
  title: '✨ 현사AI - 글래스모피즘 디자인',
  description: '투명하고 세련된 글래스모피즘 UI로 만나는 현사AI 서비스',
};

export default function HomePage() {
  return (
    <main className="min-h-screen relative overflow-hidden">
      <div className="glass-header w-full text-center py-4">
        <p className="font-semibold glass-text">
          ✨ 글래스모피즘 모드! 투명하고 세련된 유리 질감 디자인을 경험해보세요 🔮
        </p>
      </div>
      
      <header className="glass-header sticky top-0 z-50">
        <div className="container mx-auto px-6 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-6">
              <div className="glass-icon">
                <span className="text-2xl font-bold glass-text">AI</span>
              </div>
              <div>
                <h1 className="text-4xl font-light glass-text">
                  현사<span className="glass-gradient font-bold">AI</span>
                </h1>
                <p className="text-sm glass-text-muted mt-1">Glass • Transparent • Elegant</p>
              </div>
            </div>
            
            <nav className="hidden md:flex items-center space-x-8">
              <a href="#hero" className="glass-text-muted hover:text-white font-medium transition-colors">홈</a>
              <a href="#services" className="glass-text-muted hover:text-white font-medium transition-colors">서비스</a>
              <a href="#features" className="glass-text-muted hover:text-white font-medium transition-colors">기능</a>
              <a href="#pricing" className="glass-text-muted hover:text-white font-medium transition-colors">가격</a>
              <button className="glass-btn">✨ 시작하기</button>
            </nav>
          </div>
        </div>
      </header>

      <section id="hero" className="py-20">
        <div className="container mx-auto px-6 text-center">
          <div className="glass-card max-w-5xl mx-auto">
            <h2 className="text-6xl md:text-8xl font-light glass-text mb-8 leading-tight">
              <span className="block mb-4">투명한</span>
              <span className="block glass-gradient font-bold">AI 경험</span>
            </h2>
            
            <p className="text-xl md:text-2xl glass-text-muted mb-16 leading-relaxed max-w-3xl mx-auto">
              글래스모피즘으로 만나는 미래형 AI 서비스.<br/>
              <span className="glass-text font-semibold">투명함과 깊이감이 어우러진 인터페이스.</span>
            </p>
            
            <div className="flex flex-col sm:flex-row gap-8 justify-center items-center mb-16">
              <button className="glass-btn text-lg px-12 py-4">🚀 지금 시작하기</button>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
              <div className="glass-card p-6 text-center">
                <div className="glass-icon-small mx-auto mb-4"><span>🎨</span></div>
                <span className="glass-text-muted font-medium">AI 이미지</span>
              </div>
              <div className="glass-card p-6 text-center">
                <div className="glass-icon-small mx-auto mb-4"><span>📚</span></div>
                <span className="glass-text-muted font-medium">동화책</span>
              </div>
              <div className="glass-card p-6 text-center">
                <div className="glass-icon-small mx-auto mb-4"><span>📊</span></div>
                <span className="glass-text-muted font-medium">엑셀 자동화</span>
              </div>
              <div className="glass-card p-6 text-center">
                <div className="glass-icon-small mx-auto mb-4"><span>🌐</span></div>
                <span className="glass-text-muted font-medium">웹 크롤링</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="services">
        <div className="glass-card container mx-auto px-6 py-12">
          <ServicesSection />
        </div>
      </section>
      
      <section id="features">
        <div className="glass-card container mx-auto px-6 py-12">
          <FeaturesSection />
        </div>
      </section>
      
      <section id="pricing">
        <div className="glass-card container mx-auto px-6 py-12">
          <PricingSection />
        </div>
      </section>
      
      <section>
        <div className="glass-card container mx-auto px-6 py-12">
          <TestimonialsSection />
          <div className="mt-16"><CTASection /></div>
        </div>
      </section>
      
      <div className="glass-header">
        <Footer />
      </div>
    </main>
  );
}
EOF

    echo "✅ 5️⃣ 글래스모피즘 디자인 완전 적용 완료!"
}

# 6️⃣ 모던 그라데이션 디자인 적용 함수  
apply_modern_gradient() {
    echo "🌈 모던 그라데이션 디자인 적용 중..."
    
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
      <div className="bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 text-white">
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

    echo "✅ 6️⃣ 모던 그라데이션 디자인 완전 적용 완료!"
}

# 7️⃣ 미니멀 클린 디자인 적용 함수
apply_minimal_clean() {
    echo "🤍 미니멀 클린 디자인 적용 중..."
    
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
      <div className="border-b border-gray-100 bg-white shadow-sm">
        <div className="container mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-light text-gray-900">🤍 현사AI - 미니멀 클린</h1>
              <p className="text-sm text-gray-500 mt-1">깔끔하고 단순한 디자인</p>
            </div>
            <div className="w-12 h-12 bg-gray-900 rounded-full flex items-center justify-center">
              <span className="text-white text-xl">AI</span>
            </div>
          </div>
        </div>
      </div>
      
      <div className="bg-gray-50"><HeroSection /></div>
      <ServicesSection />
      <div className="bg-gray-50"><FeaturesSection /></div>
      <PricingSection />
      <div className="bg-gray-50"><TestimonialsSection /></div>
      <CTASection />
      <Footer />
    </main>
  );
}
EOF

    echo "✅ 7️⃣ 미니멀 클린 디자인 완전 적용 완료!"
}

# 8️⃣ 사이버펑크 디자인 적용 함수
apply_cyberpunk() {
    echo "🟣 사이버펑크 디자인 적용 중..."
    
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
      
      <div className="bg-black border-t border-cyan-400"><ServicesSection /></div>
      <div className="bg-gray-900"><FeaturesSection /></div>
      <div className="bg-black border-t border-purple-400"><PricingSection /></div>
      <div className="bg-gray-900"><TestimonialsSection /></div>
      <div className="bg-gradient-to-r from-purple-900 to-cyan-900"><CTASection /></div>
      <Footer />
    </main>
  );
}
EOF

    echo "✅ 8️⃣ 사이버펑크 디자인 완전 적용 완료!"
}

# 9️⃣ 네이처 소프트 디자인 적용 함수
apply_nature_soft() {
    echo "🌿 네이처 소프트 디자인 적용 중..."
    
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
      <div className="bg-white"><ServicesSection /></div>
      <div className="bg-gradient-to-r from-green-100 to-emerald-100"><FeaturesSection /></div>
      <div className="bg-white"><PricingSection /></div>
      <div className="bg-gradient-to-r from-teal-100 to-green-100"><TestimonialsSection /></div>
      <div className="bg-gradient-to-r from-green-600 to-emerald-600"><CTASection /></div>
      <Footer />
    </main>
  );
}
EOF

    echo "✅ 9️⃣ 네이처 소프트 디자인 완전 적용 완료!"
}

# 🔟 프리미엄 다크 디자인 적용 함수
apply_premium_dark() {
    echo "⚫ 프리미엄 다크 디자인 적용 중..."
    
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
      
      <div className="bg-gray-900"><HeroSection /></div>
      <div className="bg-black border-t border-gray-800"><ServicesSection /></div>
      <div className="bg-gray-900 border-t border-gray-800"><FeaturesSection /></div>
      <div className="bg-black border-t border-gray-800"><PricingSection /></div>
      <div className="bg-gray-900 border-t border-gray-800"><TestimonialsSection /></div>
      <div className="bg-gradient-to-r from-yellow-600 via-yellow-500 to-yellow-400"><CTASection /></div>
      <Footer />
    </main>
  );
}
EOF

    echo "✅ 🔟 프리미엄 다크 디자인 완전 적용 완료!"
}

# 디자인 선택 메뉴
show_design_menu() {
    echo ""
    echo "🎨 디자인 선택 메뉴 (총 10개)"
    echo "================================="
    echo "1️⃣ 뉴모피즘 🥚          6️⃣ 모던 그라데이션 🌈"
    echo "2️⃣ 다크모드 🌙          7️⃣ 미니멀 클린 🤍"
    echo "3️⃣ 그라데이션 메쉬 🌈     8️⃣ 사이버펑크 🟣"
    echo "4️⃣ 3D 카드 📦          9️⃣ 네이처 소프트 🌿"
    echo "5️⃣ 글래스모피즘 ✨       🔟 프리미엄 다크 ⚫"
    echo ""
    read -r -p "원하는 디자인 번호를 입력하세요 (1-10): " choice
    
    case $choice in
        1) apply_neumorphism ;;
        2) apply_darkmode ;;
        3) apply_gradient_mesh ;;
        4) apply_3d_cards ;;
        5) apply_glassmorphism ;;
        6) apply_modern_gradient ;;
        7) apply_minimal_clean ;;
        8) apply_cyberpunk ;;
        9) apply_nature_soft ;;
        10) apply_premium_dark ;;
        *)
            echo "❌ 잘못된 선택입니다. 1-10 사이의 숫자를 입력해주세요."
            show_design_menu
            ;;
    esac
}

# 🎯 선택 모드 메인 루프
echo "🎯 완전한 디자인 선택 모드 시작!"
while true; do
    show_design_menu
    echo ""
    echo "✅ 디자인 적용 완료!"
    echo ""
    read -r -p "다른 디자인을 선택하시겠습니까? (y/n): " continue_choice
    if [[ ! $continue_choice =~ ^[Yy]$ ]]; then
        break
    fi
done

echo ""
echo "🎉 완전한 디자인 쇼케이스 종료!" 