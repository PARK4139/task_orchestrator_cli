import { Metadata } from 'next';
import dynamic from 'next/dynamic';

// 상대 경로로 변경
const HeroSection = dynamic(() => import('../components/sections/HeroSection'));
const ServicesSection = dynamic(() => import('../components/sections/ServicesSection'));
const FeaturesSection = dynamic(() => import('../components/sections/FeaturesSection'));
const PricingSection = dynamic(() => import('../components/sections/PricingSection'));
const TestimonialsSection = dynamic(() => import('../components/sections/TestimonialsSection'));
const CTASection = dynamic(() => import('../components/sections/CTASection'));
const Footer = dynamic(() => import('../components/layout/Footer'));

export const metadata: Metadata = {
  title: '현사AI - 현명한 사람들의 AI',
  description: '마차를 끄는 마차시대의 현명한 마부는 자동차시대가 되자 자동차의 운전수가 되었다.',
};

export default function HomePage() {
  return (
    <main className="min-h-screen">
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
