'use client';

import { motion } from 'framer-motion';
import { ArrowRightIcon, SparklesIcon } from 'lucide-react';
import Link from 'next/link';

const HeroSection = () => {
  return (
    <section className="relative min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-50 via-blue-50 to-slate-100 overflow-hidden">
      {/* 배경 패턴 */}
      <div className="absolute inset-0 opacity-5">
        <div className="absolute inset-0" style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23000000' fill-opacity='0.1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`,
        }} />
      </div>

      <div className="relative z-10 max-w-6xl mx-auto px-4 py-20 text-center">
        {/* 브랜드 로고 */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="mb-8"
        >
          <div className="inline-flex items-center space-x-2 px-4 py-2 bg-blue-100 text-blue-800 rounded-full text-sm font-medium">
            <SparklesIcon className="w-4 h-4" />
            <span>현명한 사람들의 AI</span>
          </div>
        </motion.div>

        {/* 메인 제목 */}
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="text-5xl md:text-7xl font-bold text-slate-800 mb-6"
        >
          현사AI
        </motion.h1>

        {/* 부제목 */}
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="text-xl md:text-2xl text-slate-600 mb-8 max-w-4xl mx-auto leading-relaxed"
        >
          AI를 모르는 사람들과 AI 공부가 귀찮은 사람들을 위한<br />
          <span className="text-blue-600 font-semibold">AI 산출물 공급 서비스</span>
        </motion.p>

        {/* 핵심 메시지 */}
        <motion.blockquote
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.6 }}
          className="text-lg md:text-xl text-slate-500 italic mb-12 max-w-5xl mx-auto leading-relaxed"
        >
          "마차를 끄는 마차시대의 현명한 마부는 자동차시대가 되자 자동차의 운전수가 되었다.<br />
          <span className="text-slate-700 font-medium">AI 시대의 현명한 사람들은 AI 사용자가 될 것을 나는 믿는다.</span>"
        </motion.blockquote>

        {/* CTA 버튼들 */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.8 }}
          className="flex flex-col sm:flex-row gap-4 justify-center items-center"
        >
          <Link
            href={process.env.NEXT_PUBLIC_APP_URL || 'http://localhost:8000'}
            className="group inline-flex items-center px-8 py-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-all duration-200 hover:scale-105 shadow-lg hover:shadow-xl"
          >
            <span className="font-semibold">지금 시작하기</span>
            <ArrowRightIcon className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" />
          </Link>

          <Link
            href="#services"
            className="inline-flex items-center px-8 py-4 border-2 border-slate-300 text-slate-700 rounded-lg hover:bg-slate-50 transition-all duration-200 hover:border-slate-400"
          >
            <span className="font-semibold">서비스 둘러보기</span>
          </Link>
        </motion.div>

        {/* 주요 수치 */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 1.0 }}
          className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-2xl mx-auto"
        >
          <div className="text-center">
            <div className="text-3xl font-bold text-blue-600 mb-2">6개</div>
            <div className="text-slate-600">AI 서비스</div>
          </div>
          <div className="text-center">
            <div className="text-3xl font-bold text-blue-600 mb-2">24/7</div>
            <div className="text-slate-600">자동 처리</div>
          </div>
          <div className="text-center">
            <div className="text-3xl font-bold text-blue-600 mb-2">90%</div>
            <div className="text-slate-600">시간 절약</div>
          </div>
        </motion.div>
      </div>

      {/* 스크롤 인디케이터 */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.6, delay: 1.2 }}
        className="absolute bottom-8 left-1/2 transform -translate-x-1/2"
      >
        <div className="flex flex-col items-center space-y-2 text-slate-400">
          <span className="text-sm">스크롤해서 더 보기</span>
          <motion.div
            animate={{ y: [0, 8, 0] }}
            transition={{ repeat: Infinity, duration: 1.5 }}
            className="w-6 h-10 border-2 border-slate-300 rounded-full flex justify-center"
          >
            <div className="w-1 h-3 bg-slate-300 rounded-full mt-2" />
          </motion.div>
        </div>
      </motion.div>
    </section>
  );
};

export default HeroSection;