# Service Official Home

현사AI 공식 홈페이지 서비스 - SEO 최적화된 랜딩 페이지

## 🎯 서비스 개요

**service_official_home_smart_person_ai**은 현사AI의 공식 홈페이지를 담당하는 독립 마이크로서비스입니다.

### 주요 역할
- 🏠 **SEO 최적화 랜딩 페이지**: 구글 검색 유입 최적화
- 🎨 **브랜딩 사이트**: 현사AI 가치 제안 및 서비스 소개
- 💼 **리드 생성**: 회원가입 유도, 뉴스레터 구독, 데모 요청
- 📞 **고객 지원**: 문의 접수 및 고객 소통

## 🏗️ 기술 스택

### Frontend (포트: 3000)
- **Next.js 14**: App Router, SSR/SSG 지원
- **TypeScript**: 타입 안전성
- **Tailwind CSS**: 유틸리티 퍼스트 CSS
- **Framer Motion**: 애니메이션
- **Lucide React**: 아이콘

### Backend (포트: 8030)
- **FastAPI**: 고성능 API 서버
- **Pydantic**: 데이터 검증
- **SQLAlchemy**: ORM (향후 추가)
- **Structlog**: 구조화된 로깅

## 📁 프로젝트 구조

```
service_official_home_smart_person_ai/
├── backend/
│   └── main.py                     # FastAPI 백엔드 API
├── frontend/
│   ├── app/
│   │   ├── layout.tsx              # 전역 레이아웃 (SEO 메타데이터)
│   │   ├── page.tsx                # 홈페이지
│   │   └── globals.css             # 전역 스타일
│   ├── components/
│   │   ├── sections/
│   │   │   ├── HeroSection.tsx     # 히어로 섹션
│   │   │   ├── ServicesSection.tsx # 서비스 소개
│   │   │   ├── FeaturesSection.tsx # 주요 특징
│   │   │   ├── PricingSection.tsx  # 가격 계획
│   │   │   ├── TestimonialsSection.tsx # 고객 후기
│   │   │   └── CTASection.tsx      # 마지막 CTA
│   │   └── layout/
│   │       └── Footer.tsx          # 푸터
│   ├── next.config.js              # Next.js 설정
│   ├── tailwind.config.js          # Tailwind 설정
│   ├── tsconfig.json               # TypeScript 설정
│   └── package.json                # 의존성
└── README.md                       # 이 파일
```

## 🚀 실행 방법

### 1. 백엔드 실행
```bash
cd service_official_home_smart_person_ai/backend
python main.py
# → http://localhost:8030
```

### 2. 프론트엔드 개발 서버
```bash
cd service_official_home_smart_person_ai/frontend
npm install
npm run dev
# → http://localhost:3000
```

### 3. 프로덕션 빌드
```bash
cd service_official_home_smart_person_ai/frontend
npm run build
npm start
```

## 🎨 주요 섹션

### 1. Hero Section
- 현사AI 브랜딩 메시지
- 핵심 가치 제안
- 주요 CTA 버튼

### 2. Services Section  
- 6개 마이크로서비스 소개
- 각 서비스별 특징 및 기능
- 인터랙티브 카드 UI

### 3. Features Section
- 현사AI만의 차별점
- 기존 방식 vs 현사AI 비교
- 주요 통계 및 성과

### 4. Pricing Section
- 3단계 구독 플랜 (베이직/프리미엄/프로)
- 각 플랜별 기능 비교
- 특별 혜택 안내

### 5. Testimonials Section
- 실제 고객 후기
- 업종별 성공 사례
- 구체적 성과 지표

### 6. CTA Section
- 최종 회원가입 유도
- 특별 런칭 혜택
- 긴급성 메시지

## 🔧 백엔드 API

### 주요 엔드포인트

```python
# 홈페이지 관련 API
GET  /                          # 서버 상태
GET  /health                    # 헬스체크
GET  /api/v1/services-overview  # 서비스 개요
GET  /api/v1/testimonials       # 고객 후기

# 리드 생성 API
POST /api/v1/contact            # 문의 접수
POST /api/v1/newsletter         # 뉴스레터 구독
POST /api/v1/demo-request       # 데모 요청
```

## 🎯 SEO 최적화

### 메타데이터
- **Title**: "현사AI - 현명한 사람들의 AI"  
- **Description**: AI 산출물 공급 서비스 소개
- **Keywords**: AI, 인공지능, 이미지 생성, 동화책, 업무 자동화
- **Open Graph**: 소셜 미디어 최적화
- **Twitter Cards**: 트위터 공유 최적화

### 기술적 SEO
- **구조화된 데이터**: JSON-LD 스키마
- **시맨틱 HTML**: 적절한 HTML5 태그 사용  
- **이미지 최적화**: WebP, AVIF 지원
- **성능 최적화**: Next.js 자동 최적화

## 📊 성능 지표

### 목표 지표
- **Lighthouse 점수**: 95+ (모든 항목)
- **First Contentful Paint**: < 1.5초
- **Largest Contentful Paint**: < 2.5초
- **Cumulative Layout Shift**: < 0.1

### SEO 목표
- **Google 검색 순위**: "AI 서비스" 키워드 상위 10위
- **유기 트래픽**: 월 10,000+ 방문자
- **전환율**: 방문자 대비 회원가입 5%+

## 🔄 배포 전략

### 개발 환경
- **프론트엔드**: Vercel (Next.js 최적화)
- **백엔드**: AWS EC2 또는 Railway
- **도메인**: www.smartpersonai.com

### 프로덕션 환경
- **CDN**: Cloudflare (전 세계 캐싱)
- **모니터링**: Google Analytics, Hotjar
- **A/B 테스트**: 주요 CTA 버튼 및 메시지

## 🤝 다른 서비스와의 연동

### API Gateway 연동
- 회원가입 → `service_api_gateway`
- 결제 페이지 → `service_payment`

### 백엔드 서비스 연동  
- 문의 데이터 → 공통 데이터베이스
- 뉴스레터 → 이메일 마케팅 도구

## 📈 향후 계획

### Phase 2 기능
- [ ] 다국어 지원 (영어)
- [ ] 블로그 시스템
- [ ] 라이브 채팅
- [ ] 고객 성공 사례 페이지

### Phase 3 기능  
- [ ] A/B 테스트 시스템
- [ ] 개인화된 콘텐츠
- [ ] 소셜 미디어 통합
- [ ] 웨비나/데모 예약 시스템

## 🛠️ 개발 가이드

### 새 섹션 추가
1. `components/sections/`에 새 컴포넌트 생성
2. `app/page.tsx`에 import 및 추가
3. 반응형 디자인 적용 (Tailwind CSS)
4. 애니메이션 추가 (Framer Motion)

### 스타일 가이드
- **색상**: Tailwind 기본 팔레트 + 브랜드 컬러
- **타이포그래피**: Inter 폰트 
- **간격**: Tailwind 스페이싱 시스템
- **애니메이션**: 자연스럽고 의미 있는 모션

현사AI 공식 홈페이지로 브랜드 가치를 효과적으로 전달하고 고객 전환을 극대화합니다! 🚀