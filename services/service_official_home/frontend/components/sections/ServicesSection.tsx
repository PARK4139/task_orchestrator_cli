'use client';

import { motion } from 'framer-motion';
import { 
  ImageIcon, 
  BookOpenIcon, 
  FileSpreadsheetIcon,
  GlobeIcon
} from 'lucide-react';

const ServicesSection = () => {
  const services = [
    {
      id: 'ai_image',
      name: 'AI 이미지 생성',
      description: 'Stable Diffusion으로 고품질 이미지를 생성하세요. 다양한 스타일과 테마로 원하는 이미지를 빠르게 만들 수 있습니다.',
      icon: ImageIcon,
      color: 'bg-purple-500',
      gradient: 'from-purple-400 to-pink-400',
      features: ['다양한 스타일', '고화질 생성', '빠른 처리', '커스텀 프롬프트']
    },
    {
      id: 'ai_book',
      name: 'AI 동화책 생성',
      description: 'Claude AI로 창의적인 동화책을 만들어보세요. 교육적이면서도 재미있는 스토리를 자동으로 생성합니다.',
      icon: BookOpenIcon,
      color: 'bg-blue-500',
      gradient: 'from-blue-400 to-cyan-400',
      features: ['맞춤형 스토리', '연령별 최적화', '교육 콘텐츠', '일러스트 포함']
    },
    {
      id: 'excel_automation',
      name: '엑셀 자동화',
      description: '복잡한 엑셀 작업을 자동으로 처리합니다. 파일 병합, 데이터 분석, 차트 생성까지 한 번에.',
      icon: FileSpreadsheetIcon,
      color: 'bg-green-500',
      gradient: 'from-green-400 to-emerald-400',
      features: ['파일 병합', '데이터 분석', '차트 생성', '자동 보고서']
    },
    {
      id: 'web_crawler',
      name: '웹 크롤링',
      description: '주가, 뉴스 등 웹 데이터를 자동 수집합니다. 실시간 모니터링과 데이터 분석까지 제공합니다.',
      icon: GlobeIcon,
      color: 'bg-orange-500',
      gradient: 'from-orange-400 to-red-400',
      features: ['실시간 수집', '감정 분석', '데이터 정제', '알림 서비스']
    }
  ];

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2
      }
    }
  };

  const cardVariants = {
    hidden: { opacity: 0, y: 50 },
    visible: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.6,
        ease: "easeOut"
      }
    }
  };

  return (
    <section id="services" className="section-padding bg-white">
      <div className="container-custom">
        {/* 섹션 헤더 */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl md:text-5xl font-bold text-slate-800 mb-6">
            AI 서비스 라인업
          </h2>
          <p className="text-xl text-slate-600 max-w-3xl mx-auto leading-relaxed">
            현사AI의 6개 핵심 서비스로 당신의 업무와 창작 활동을 혁신하세요.
            복잡한 AI 지식 없이도 전문가 수준의 결과물을 얻을 수 있습니다.
          </p>
        </motion.div>

        {/* 서비스 카드들 */}
        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
          className="grid md:grid-cols-2 lg:grid-cols-4 gap-8"
        >
          {services.map((service, index) => {
            const IconComponent = service.icon;
            
            return (
              <motion.div
                key={service.id}
                variants={cardVariants}
                className="group relative"
              >
                {/* 카드 배경 그라디언트 */}
                <div className={`absolute inset-0 bg-gradient-to-br ${service.gradient} rounded-2xl opacity-0 group-hover:opacity-10 transition-opacity duration-300`} />
                
                {/* 메인 카드 */}
                <div className="relative card p-8 h-full hover:shadow-xl transition-all duration-300 group-hover:-translate-y-2">
                  {/* 아이콘 */}
                  <div className={`w-16 h-16 ${service.color} rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300`}>
                    <IconComponent className="w-8 h-8 text-white" />
                  </div>

                  {/* 제목 */}
                  <h3 className="text-xl font-bold text-slate-800 mb-4 group-hover:text-blue-600 transition-colors">
                    {service.name}
                  </h3>

                  {/* 설명 */}
                  <p className="text-slate-600 mb-6 leading-relaxed">
                    {service.description}
                  </p>

                  {/* 기능 목록 */}
                  <div className="space-y-2">
                    {service.features.map((feature, idx) => (
                      <div key={idx} className="flex items-center text-sm text-slate-500">
                        <div className="w-1.5 h-1.5 bg-blue-500 rounded-full mr-3" />
                        {feature}
                      </div>
                    ))}
                  </div>

                  {/* 호버 시 나타나는 더보기 버튼 */}
                  <div className="absolute bottom-8 left-8 right-8 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <button className="w-full py-2 text-blue-600 font-medium text-sm border border-blue-200 rounded-lg hover:bg-blue-50 transition-colors">
                      자세히 보기
                    </button>
                  </div>
                </div>
              </motion.div>
            );
          })}
        </motion.div>

        {/* 추가 서비스 예고 */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="text-center mt-16 p-8 bg-slate-50 rounded-2xl"
        >
          <h3 className="text-2xl font-bold text-slate-800 mb-4">
            더 많은 서비스가 준비 중입니다
          </h3>
          <p className="text-slate-600 mb-6">
            현사AI는 지속적으로 새로운 AI 서비스를 개발하고 있습니다.<br />
            곧 출시될 서비스들을 미리 만나보세요.
          </p>
          <div className="flex flex-wrap justify-center gap-4 text-sm">
            <span className="px-4 py-2 bg-white text-slate-600 rounded-full border">🎵 AI 음악 생성</span>
            <span className="px-4 py-2 bg-white text-slate-600 rounded-full border">📹 AI 영상 편집</span>
            <span className="px-4 py-2 bg-white text-slate-600 rounded-full border">💬 AI 챗봇 제작</span>
            <span className="px-4 py-2 bg-white text-slate-600 rounded-full border">📊 AI 데이터 분석</span>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default ServicesSection;