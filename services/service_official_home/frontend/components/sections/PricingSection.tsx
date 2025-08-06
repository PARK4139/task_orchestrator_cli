'use client';

import { motion } from 'framer-motion';
import { CheckIcon, StarIcon } from 'lucide-react';
import Link from 'next/link';

const PricingSection = () => {
  const pricingPlans = [
    {
      name: '베이직',
      price: 9900,
      tokens: 100,
      description: 'AI를 처음 사용하는 개인 사용자에게 최적',
      features: [
        'AI 이미지 생성 (월 50개)',
        '기본 엑셀 자동화',
        '이메일 지원',
        '기본 템플릿 제공',
        '커뮤니티 액세스'
      ],
      notIncluded: [
        'AI 동화책 생성',
        '웹 크롤링',
        '우선 지원'
      ],
      popular: false,
      color: 'border-slate-200',
      buttonStyle: 'btn-outline'
    },
    {
      name: '프리미엄',
      price: 19900,
      tokens: 500,
      description: '소상공인과 전문가를 위한 완전한 솔루션',
      features: [
        'AI 이미지 생성 (월 250개)',
        'AI 동화책 생성 (월 20편)',
        '고급 엑셀 자동화',
        '웹 크롤링 서비스',
        '우선 이메일 지원',
        '고급 템플릿',
        '커스텀 스타일',
        'API 액세스'
      ],
      notIncluded: [
        '전화 지원',
        'SLA 보장'
      ],
      popular: true,
      color: 'border-blue-500',
      buttonStyle: 'btn-primary'
    },
    {
      name: '프로',
      price: 49900,
      tokens: 2000,
      description: '기업과 팀을 위한 무제한 AI 서비스',
      features: [
        '무제한 AI 이미지 생성',
        '무제한 AI 동화책 생성',
        '전문 엑셀 자동화',
        '고급 웹 크롤링',
        '커스텀 파이프라인',
        '전화 + 이메일 지원',
        'SLA 보장',
        '전용 계정 매니저',
        '팀 협업 도구',
        'API 무제한',
        '데이터 우선순위 처리'
      ],
      notIncluded: [],
      popular: false,
      color: 'border-purple-500',
      buttonStyle: 'btn-secondary'
    }
  ];

  return (
    <section id="pricing" className="section-padding gradient-bg">
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
            합리적인 가격 계획
          </h2>
          <p className="text-xl text-slate-600 max-w-3xl mx-auto leading-relaxed">
            월 9,900원부터 시작하는 현사AI 구독 서비스.<br />
            필요에 따라 언제든지 업그레이드하거나 다운그레이드할 수 있습니다.
          </p>
        </motion.div>

        {/* 가격 카드들 */}
        <div className="grid md:grid-cols-3 gap-8 max-w-7xl mx-auto">
          {pricingPlans.map((plan, index) => (
            <motion.div
              key={plan.name}
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.2 }}
              className={`relative bg-white rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 ${
                plan.popular ? 'scale-105 shadow-glow' : 'hover:scale-105'
              }`}
            >
              {/* 인기 배지 */}
              {plan.popular && (
                <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
                  <div className="bg-blue-600 text-white px-6 py-2 rounded-full text-sm font-semibold flex items-center">
                    <StarIcon className="w-4 h-4 mr-1" />
                    가장 인기
                  </div>
                </div>
              )}

              <div className={`p-8 border-2 ${plan.color} rounded-2xl h-full flex flex-col`}>
                {/* 플랜 정보 */}
                <div className="text-center mb-8">
                  <h3 className="text-2xl font-bold text-slate-800 mb-2">
                    {plan.name}
                  </h3>
                  <p className="text-slate-600 mb-4">
                    {plan.description}
                  </p>
                  <div className="mb-4">
                    <span className="text-4xl font-bold text-slate-800">
                      {plan.price.toLocaleString()}원
                    </span>
                    <span className="text-slate-500 ml-2">/월</span>
                  </div>
                  <div className="text-sm text-slate-500 mb-6">
                    월 {plan.tokens}토큰 제공
                  </div>
                </div>

                {/* 기능 목록 */}
                <div className="flex-1 mb-8">
                  <div className="space-y-4">
                    {plan.features.map((feature, idx) => (
                      <div key={idx} className="flex items-start">
                        <CheckIcon className="w-5 h-5 text-green-500 mr-3 mt-0.5 flex-shrink-0" />
                        <span className="text-slate-700">{feature}</span>
                      </div>
                    ))}
                    {plan.notIncluded.map((feature, idx) => (
                      <div key={idx} className="flex items-start opacity-50">
                        <div className="w-5 h-5 mr-3 mt-0.5 flex-shrink-0 flex items-center justify-center">
                          <div className="w-3 h-0.5 bg-slate-400 rounded" />
                        </div>
                        <span className="text-slate-500 line-through">{feature}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* CTA 버튼 */}
                <Link
                  href={`${process.env.NEXT_PUBLIC_APP_URL}/payment?plan=${plan.name.toLowerCase()}`}
                  className={`w-full text-center ${plan.buttonStyle} justify-center`}
                >
                  {plan.name} 시작하기
                </Link>
              </div>
            </motion.div>
          ))}
        </div>

        {/* 추가 정보 */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.8 }}
          className="text-center mt-16"
        >
          <div className="bg-white/80 backdrop-blur-sm rounded-2xl p-8 max-w-4xl mx-auto">
            <h3 className="text-2xl font-bold text-slate-800 mb-4">
              💡 현사AI만의 특별한 혜택
            </h3>
            <div className="grid md:grid-cols-3 gap-6 text-center">
              <div>
                <div className="text-3xl mb-2">🔄</div>
                <h4 className="font-semibold text-slate-800 mb-2">언제든 변경</h4>
                <p className="text-sm text-slate-600">
                  플랜은 언제든지 변경 가능합니다. 위약금이나 수수료 없이 자유롭게 조정하세요.
                </p>
              </div>
              <div>
                <div className="text-3xl mb-2">💸</div>
                <h4 className="font-semibold text-slate-800 mb-2">7일 무료 체험</h4>
                <p className="text-sm text-slate-600">
                  모든 플랜을 7일간 무료로 체험해보세요. 만족하지 않으면 100% 환불해드립니다.
                </p>
              </div>
              <div>
                <div className="text-3xl mb-2">🎯</div>
                <h4 className="font-semibold text-slate-800 mb-2">맞춤형 지원</h4>
                <p className="text-sm text-slate-600">
                  각 플랜에 따라 차별화된 지원을 제공합니다. 성공적인 AI 활용을 도와드립니다.
                </p>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default PricingSection;