'use client';

import { motion } from 'framer-motion';
import { ArrowRightIcon, SparklesIcon, RocketIcon } from 'lucide-react';
import Link from 'next/link';

const CTASection = () => {
  return (
    <section className="section-padding bg-gradient-to-br from-blue-600 via-purple-600 to-blue-800 relative overflow-hidden">
      {/* 배경 패턴 */}
      <div className="absolute inset-0 bg-grid-pattern opacity-10" />
      
      {/* 플로팅 요소들 */}
      <div className="absolute top-20 left-10 w-20 h-20 bg-white/10 rounded-full animate-float" />
      <div className="absolute top-40 right-20 w-16 h-16 bg-white/5 rounded-full animate-float" style={{ animationDelay: '1s' }} />
      <div className="absolute bottom-20 left-1/4 w-12 h-12 bg-white/10 rounded-full animate-float" style={{ animationDelay: '2s' }} />

      <div className="container-custom relative z-10">
        <div className="max-w-4xl mx-auto text-center text-white">
          {/* 메인 헤딩 */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="mb-8"
          >
            <div className="inline-flex items-center space-x-2 px-4 py-2 bg-white/20 backdrop-blur-sm rounded-full text-sm font-medium mb-6">
              <RocketIcon className="w-4 h-4" />
              <span>지금 바로 시작하세요</span>
            </div>
            
            <h2 className="text-4xl md:text-6xl font-bold mb-6 leading-tight">
              AI 시대의 현명한 선택
            </h2>
            
            <p className="text-xl md:text-2xl leading-relaxed opacity-90 mb-8">
              현사AI와 함께 업무 혁신을 경험하고<br />
              <span className="font-semibold">AI 전문가</span>가 되어보세요
            </p>
          </motion.div>

          {/* 특별 혜택 강조 */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="bg-white/10 backdrop-blur-sm rounded-2xl p-8 mb-10"
          >
            <div className="flex items-center justify-center mb-4">
              <SparklesIcon className="w-6 h-6 mr-2" />
              <h3 className="text-2xl font-bold">특별 런칭 혜택</h3>
            </div>
            
            <div className="grid md:grid-cols-3 gap-6 text-center">
              <div>
                <div className="text-3xl font-bold mb-2">7일</div>
                <div className="text-sm opacity-80">무료 체험</div>
              </div>
              <div>
                <div className="text-3xl font-bold mb-2">50%</div>
                <div className="text-sm opacity-80">첫 달 할인</div>
              </div>
              <div>
                <div className="text-3xl font-bold mb-2">1:1</div>
                <div className="text-sm opacity-80">무료 컨설팅</div>
              </div>
            </div>
          </motion.div>

          {/* CTA 버튼들 */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.4 }}
            className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-8"
          >
            <Link
              href={process.env.NEXT_PUBLIC_APP_URL || 'http://localhost:8000'}
              className="group inline-flex items-center px-8 py-4 bg-white text-blue-600 font-semibold rounded-lg hover:bg-slate-50 transition-all duration-200 hover:scale-105 shadow-lg hover:shadow-xl"
            >
              <span>무료로 시작하기</span>
              <ArrowRightIcon className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </Link>

            <Link
              href="#demo"
              className="inline-flex items-center px-8 py-4 border-2 border-white/30 text-white font-semibold rounded-lg hover:bg-white/10 backdrop-blur-sm transition-all duration-200"
            >
              <span>데모 요청하기</span>
            </Link>
          </motion.div>

          {/* 추가 정보 */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.6 }}
            className="text-center"
          >
            <p className="text-white/80 mb-4">
              ✨ 신용카드 등록 없이 바로 시작 • 언제든지 취소 가능
            </p>
            
            <div className="flex flex-wrap justify-center items-center gap-6 text-sm text-white/60">
              <div className="flex items-center">
                <div className="w-2 h-2 bg-green-400 rounded-full mr-2 animate-pulse" />
                <span>24/7 자동 서비스</span>
              </div>
              <div className="flex items-center">
                <div className="w-2 h-2 bg-green-400 rounded-full mr-2 animate-pulse" />
                <span>한국어 완벽 지원</span>
              </div>
              <div className="flex items-center">
                <div className="w-2 h-2 bg-green-400 rounded-full mr-2 animate-pulse" />
                <span>모바일 최적화</span>
              </div>
            </div>
          </motion.div>

          {/* 긴급성 메시지 */}
          <motion.div
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.8 }}
            className="mt-12 p-4 bg-yellow-500/20 backdrop-blur-sm rounded-lg border border-yellow-400/30"
          >
            <p className="text-yellow-100 text-sm">
              🔥 <strong>런칭 특가는 이번 달까지!</strong> 놓치면 정가로 시작해야 합니다.
            </p>
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default CTASection;