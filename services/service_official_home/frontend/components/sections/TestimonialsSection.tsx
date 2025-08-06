'use client';

import { motion } from 'framer-motion';
import { StarIcon, QuoteIcon } from 'lucide-react';

const TestimonialsSection = () => {
  const testimonials = [
    {
      name: '김영희 대표',
      company: '크리에이티브 스튜디오',
      role: 'UI/UX 디자이너',
      service: 'AI 이미지 생성',
      content: '마케팅 이미지 제작 시간이 90% 단축되었습니다. 이제 하루에 10개 이상의 다양한 컨셉을 만들 수 있어서 클라이언트들이 정말 만족해하고 있어요. 현사AI 덕분에 업무 효율성이 엄청나게 향상되었습니다.',
      rating: 5,
      image: '/testimonials/kim-younghee.jpg',
      results: [
        '작업 시간 90% 단축',
        '일일 산출물 10배 증가',
        '클라이언트 만족도 95%'
      ]
    },
    {
      name: '박민수 팀장',
      company: '데이터 컨설팅',
      role: '데이터 분석가',
      service: '엑셀 자동화',
      content: '매월 3일 걸리던 보고서 작업이 30분으로 줄었습니다. 복잡한 데이터 정리부터 차트 생성까지 모든 과정이 자동화되어서 이제 분석에만 집중할 수 있게 되었어요. 정말 혁신적인 서비스입니다.',
      rating: 5,
      image: '/testimonials/park-minsu.jpg',
      results: [
        '보고서 작업 시간 94% 단축',
        '데이터 정확도 99% 향상',
        '월 120시간 절약'
      ]
    },
    {
      name: '이수진 원장',
      company: '햇살 어린이집',
      role: '교육 전문가',
      service: 'AI 동화책',
      content: '아이들이 정말 좋아해요! 매일 새로운 동화책을 만들어줄 수 있어서 아이들의 상상력과 창의력이 정말 많이 늘었습니다. 부모님들도 집에서 활용하고 싶다고 문의가 계속 들어오고 있어요.',
      rating: 5,
      image: '/testimonials/lee-sujin.jpg',
      results: [
        '일일 동화책 제작 20편',
        '아동 참여도 85% 증가',
        '학부모 만족도 98%'
      ]
    },
    {
      name: '정호철 대표',
      company: '투자 정보 서비스',
      role: '금융 분석가',
      service: '웹 크롤링',
      content: '실시간 주가와 뉴스 데이터를 자동으로 수집하고 분석해주니까 정말 편해요. 24시간 모니터링이 가능해져서 중요한 투자 기회를 놓치지 않을 수 있게 되었습니다. ROI가 300% 이상 증가했어요.',
      rating: 5,
      image: '/testimonials/jung-hocheol.jpg',
      results: [
        '데이터 수집 자동화 100%',
        'ROI 300% 증가',
        '24/7 모니터링 가능'
      ]
    },
    {
      name: '최미영 매니저',
      company: '스타트업 A',
      role: '마케팅 매니저',
      service: '통합 서비스',
      content: '현사AI의 모든 서비스를 활용하고 있는데, 정말 업무 혁신이 일어났어요. 이미지 제작, 콘텐츠 작성, 데이터 분석까지 모든 걸 AI가 도와주니 마케팅 성과가 2배 이상 향상되었습니다.',
      rating: 5,
      image: '/testimonials/choi-miyoung.jpg',
      results: [
        '마케팅 성과 200% 향상',
        '콘텐츠 제작 시간 80% 단축',
        '팀 생산성 150% 증가'
      ]
    },
    {
      name: '한지원 CEO',
      company: 'E-Commerce B',
      role: '온라인 쇼핑몰 운영',
      service: 'AI 이미지 + 엑셀 자동화',
      content: '상품 이미지 생성과 재고 관리가 완전히 자동화되어서 매출이 3배 늘었습니다. 특히 시즌별 상품 이미지를 빠르게 만들 수 있어서 트렌드에 맞춰 빠르게 대응할 수 있게 되었어요.',
      rating: 5,
      image: '/testimonials/han-jiwon.jpg',
      results: [
        '매출 300% 증가',
        '상품 출시 시간 70% 단축',
        '운영 효율성 5배 향상'
      ]
    }
  ];

  return (
    <section className="section-padding bg-slate-50">
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
            고객 성공 사례
          </h2>
          <p className="text-xl text-slate-600 max-w-3xl mx-auto leading-relaxed">
            현사AI와 함께 업무를 혁신한 고객들의 실제 경험담을 확인해보세요.
          </p>
        </motion.div>

        {/* 후기 그리드 */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {testimonials.map((testimonial, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              className="bg-white rounded-2xl p-8 shadow-sm hover:shadow-lg transition-all duration-300 hover:-translate-y-1"
            >
              {/* 인용 아이콘 */}
              <div className="flex justify-between items-start mb-6">
                <QuoteIcon className="w-8 h-8 text-blue-200" />
                <div className="flex">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <StarIcon key={i} className="w-5 h-5 text-yellow-500 fill-current" />
                  ))}
                </div>
              </div>

              {/* 후기 내용 */}
              <blockquote className="text-slate-700 mb-6 leading-relaxed">
                "{testimonial.content}"
              </blockquote>

              {/* 성과 지표 */}
              <div className="mb-6">
                <h4 className="text-sm font-semibold text-slate-800 mb-3">주요 성과</h4>
                <div className="space-y-2">
                  {testimonial.results.map((result, idx) => (
                    <div key={idx} className="flex items-center text-sm">
                      <div className="w-2 h-2 bg-green-500 rounded-full mr-3" />
                      <span className="text-slate-600">{result}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* 고객 정보 */}
              <div className="flex items-center">
                <div className="w-12 h-12 bg-gradient-to-br from-blue-400 to-purple-500 rounded-full flex items-center justify-center mr-4">
                  <span className="text-white font-semibold text-lg">
                    {testimonial.name.charAt(0)}
                  </span>
                </div>
                <div>
                  <div className="font-semibold text-slate-800">
                    {testimonial.name}
                  </div>
                  <div className="text-sm text-slate-500">
                    {testimonial.role} · {testimonial.company}
                  </div>
                  <div className="text-xs text-blue-600 mt-1">
                    {testimonial.service} 활용
                  </div>
                </div>
              </div>
            </motion.div>
          ))}
        </div>

        {/* 통계 섹션 */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="mt-16 bg-white rounded-2xl p-8 shadow-sm"
        >
          <h3 className="text-2xl font-bold text-center text-slate-800 mb-8">
            현사AI가 만든 변화
          </h3>
          <div className="grid md:grid-cols-4 gap-8 text-center">
            <div>
              <div className="text-4xl font-bold text-blue-600 mb-2">2,000+</div>
              <div className="text-slate-600">만족한 고객</div>
            </div>
            <div>
              <div className="text-4xl font-bold text-green-600 mb-2">85%</div>
              <div className="text-slate-600">평균 업무 시간 단축</div>
            </div>
            <div>
              <div className="text-4xl font-bold text-purple-600 mb-2">300%</div>
              <div className="text-slate-600">평균 생산성 향상</div>
            </div>
            <div>
              <div className="text-4xl font-bold text-orange-600 mb-2">98%</div>
              <div className="text-slate-600">고객 만족도</div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default TestimonialsSection;