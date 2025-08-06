'use client';

import { motion } from 'framer-motion';
import { 
  ZapIcon, 
  ShieldIcon, 
  ClockIcon,
  UsersIcon,
  TrendingUpIcon,
  HeartIcon,
  BrainIcon,
  RocketIcon
} from 'lucide-react';

const FeaturesSection = () => {
  const features = [
    {
      icon: ZapIcon,
      title: 'AI 전문 지식 불필요',
      description: '복잡한 AI 공부 없이도 전문가 수준의 결과물을 얻을 수 있습니다. 직관적인 인터페이스로 누구나 쉽게 사용 가능합니다.',
      color: 'text-yellow-500',
      bgColor: 'bg-yellow-50'
    },
    {
      icon: ClockIcon,
      title: '빠른 작업 처리',
      description: '수시간 걸리던 작업을 몇 분 만에 완료할 수 있습니다. 평균 85%의 업무 시간을 절약할 수 있습니다.',
      color: 'text-blue-500',
      bgColor: 'bg-blue-50'
    },
    {
      icon: ShieldIcon,
      title: '안전하고 신뢰할 수 있는',
      description: '엔터프라이즈급 보안 시스템으로 데이터를 보호합니다. GDPR 및 국내 개인정보보호법을 완벽 준수합니다.',
      color: 'text-green-500',
      bgColor: 'bg-green-50'
    },
    {
      icon: BrainIcon,
      title: '지능형 자동화',
      description: '머신러닝 기반의 스마트 알고리즘이 사용자의 패턴을 학습하여 점점 더 정확한 결과를 제공합니다.',
      color: 'text-purple-500',
      bgColor: 'bg-purple-50'
    },
    {
      icon: UsersIcon,
      title: '팀 협업 지원',
      description: '개인부터 대기업까지 모든 규모의 팀을 지원합니다. 실시간 협업과 권한 관리 기능을 제공합니다.',
      color: 'text-pink-500',
      bgColor: 'bg-pink-50'
    },
    {
      icon: TrendingUpIcon,
      title: '지속적인 성장',
      description: '매월 새로운 AI 기능이 추가됩니다. 고객 피드백을 바탕으로 지속적으로 발전하는 서비스입니다.',
      color: 'text-orange-500',
      bgColor: 'bg-orange-50'
    }
  ];

  const stats = [
    {
      icon: RocketIcon,
      number: '2,000+',
      label: '활성 사용자',
      description: '전 세계 사용자들이 현사AI를 활용하고 있습니다'
    },
    {
      icon: HeartIcon,
      number: '98%',
      label: '고객 만족도',
      description: '대부분의 고객이 현사AI에 만족하고 있습니다'
    },
    {
      icon: ClockIcon,
      number: '85%',
      label: '시간 절약',
      description: '평균적으로 업무 시간을 크게 단축합니다'
    },
    {
      icon: TrendingUpIcon,
      number: '300%',
      label: '생산성 향상',
      description: '사용자들의 업무 생산성이 대폭 증가했습니다'
    }
  ];

  return (
    <section className="section-padding bg-white">
      <div className="container-custom">
        {/* 섹션 헤더 */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-20"
        >
          <h2 className="text-4xl md:text-5xl font-bold text-slate-800 mb-6">
            왜 현사AI인가?
          </h2>
          <p className="text-xl text-slate-600 max-w-3xl mx-auto leading-relaxed">
            현사AI만의 차별화된 특징들을 확인해보세요.<br />
            AI를 처음 사용하는 분들도 쉽고 안전하게 시작할 수 있습니다.
          </p>
        </motion.div>

        {/* 주요 특징들 */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-20">
          {features.map((feature, index) => {
            const IconComponent = feature.icon;
            
            return (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 50 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                className="group"
              >
                <div className="bg-white rounded-2xl p-8 shadow-sm border border-slate-100 hover:shadow-lg hover:border-slate-200 transition-all duration-300 h-full">
                  {/* 아이콘 */}
                  <div className={`w-16 h-16 ${feature.bgColor} rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300`}>
                    <IconComponent className={`w-8 h-8 ${feature.color}`} />
                  </div>

                  {/* 제목 */}
                  <h3 className="text-xl font-bold text-slate-800 mb-4">
                    {feature.title}
                  </h3>

                  {/* 설명 */}
                  <p className="text-slate-600 leading-relaxed">
                    {feature.description}
                  </p>
                </div>
              </motion.div>
            );
          })}
        </div>

        {/* 통계 섹션 */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="bg-gradient-to-br from-slate-50 to-blue-50 rounded-3xl p-12"
        >
          <div className="text-center mb-12">
            <h3 className="text-3xl font-bold text-slate-800 mb-4">
              숫자로 보는 현사AI
            </h3>
            <p className="text-slate-600 text-lg">
              현사AI가 만들어낸 실제 성과들을 확인해보세요
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {stats.map((stat, index) => {
              const IconComponent = stat.icon;
              
              return (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, scale: 0.8 }}
                  whileInView={{ opacity: 1, scale: 1 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.6, delay: index * 0.1 }}
                  className="text-center group"
                >
                  <div className="bg-white rounded-2xl p-6 shadow-sm hover:shadow-md transition-all duration-300 hover:-translate-y-1">
                    <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center mx-auto mb-4 group-hover:bg-blue-200 transition-colors">
                      <IconComponent className="w-6 h-6 text-blue-600" />
                    </div>
                    <div className="text-3xl font-bold text-slate-800 mb-2">
                      {stat.number}
                    </div>
                    <div className="text-lg font-semibold text-slate-700 mb-2">
                      {stat.label}
                    </div>
                    <div className="text-sm text-slate-500 leading-relaxed">
                      {stat.description}
                    </div>
                  </div>
                </motion.div>
              );
            })}
          </div>
        </motion.div>

        {/* 비교 섹션 */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="mt-20"
        >
          <div className="text-center mb-12">
            <h3 className="text-3xl font-bold text-slate-800 mb-4">
              기존 방식 vs 현사AI
            </h3>
            <p className="text-slate-600 text-lg">
              현사AI가 어떻게 업무 방식을 혁신하는지 비교해보세요
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            {/* 기존 방식 */}
            <div className="bg-red-50 rounded-2xl p-8 border-2 border-red-100">
              <h4 className="text-xl font-bold text-red-800 mb-6 flex items-center">
                <span className="w-6 h-6 bg-red-500 rounded-full flex items-center justify-center text-white text-sm mr-3">❌</span>
                기존 방식
              </h4>
              <ul className="space-y-4">
                <li className="flex items-start text-red-700">
                  <div className="w-2 h-2 bg-red-500 rounded-full mt-2 mr-3 flex-shrink-0" />
                  복잡한 AI 도구 학습에 수주~수개월 소요
                </li>
                <li className="flex items-start text-red-700">
                  <div className="w-2 h-2 bg-red-500 rounded-full mt-2 mr-3 flex-shrink-0" />
                  높은 학습 비용과 시행착오
                </li>
                <li className="flex items-start text-red-700">
                  <div className="w-2 h-2 bg-red-500 rounded-full mt-2 mr-3 flex-shrink-0" />
                  불안정한 결과물과 긴 작업 시간
                </li>
                <li className="flex items-start text-red-700">
                  <div className="w-2 h-2 bg-red-500 rounded-full mt-2 mr-3 flex-shrink-0" />
                  개별 도구마다 다른 사용법
                </li>
              </ul>
            </div>

            {/* 현사AI 방식 */}
            <div className="bg-green-50 rounded-2xl p-8 border-2 border-green-100">
              <h4 className="text-xl font-bold text-green-800 mb-6 flex items-center">
                <span className="w-6 h-6 bg-green-500 rounded-full flex items-center justify-center text-white text-sm mr-3">✅</span>
                현사AI 방식
              </h4>
              <ul className="space-y-4">
                <li className="flex items-start text-green-700">
                  <div className="w-2 h-2 bg-green-500 rounded-full mt-2 mr-3 flex-shrink-0" />
                  5분 만에 시작, 즉시 전문가 수준 결과
                </li>
                <li className="flex items-start text-green-700">
                  <div className="w-2 h-2 bg-green-500 rounded-full mt-2 mr-3 flex-shrink-0" />
                  월 9,900원부터 시작하는 합리적 가격
                </li>
                <li className="flex items-start text-green-700">
                  <div className="w-2 h-2 bg-green-500 rounded-full mt-2 mr-3 flex-shrink-0" />
                  일관되고 고품질인 결과물 보장
                </li>
                <li className="flex items-start text-green-700">
                  <div className="w-2 h-2 bg-green-500 rounded-full mt-2 mr-3 flex-shrink-0" />
                  하나의 플랫폼에서 모든 AI 서비스 이용
                </li>
              </ul>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default FeaturesSection;