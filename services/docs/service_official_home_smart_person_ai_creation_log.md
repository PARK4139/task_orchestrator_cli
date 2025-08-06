# Service Official Home 생성 로그

## 📅 개발 일지: 2024년 현사AI 공식 홈페이지 구축

### 🎯 프로젝트 개요
- **서비스명**: service_official_home_smart_person_ai
- **목적**: 현사AI 공식 홈페이지 - SEO 최적화된 랜딩 페이지
- **아키텍처**: 독립 마이크로서비스 (Frontend: Next.js, Backend: FastAPI)
- **포트**: Frontend 3000, Backend 8030

---

## 🚀 개발 진행 과정

### Phase 1: 기술 스택 결정
**사용자 질문**: "Vite + Typescript + Next.js 면 어때?"

**기술적 이슈 발견**:
- Vite와 Next.js는 **함께 사용할 수 없음** (둘 다 빌드 시스템)
- Vite: 빌드 도구 (Create React App 대체)
- Next.js: 완전한 풀스택 프레임워크 (자체 빌드 시스템 포함)

**비교 분석 결과**:
```
올바른 선택지:
✅ Option 1: Vite + React + TypeScript    (일반 웹앱용)
✅ Option 2: Next.js + TypeScript         (SEO 중요한 사이트용)
❌ 불가능: Vite + Next.js                (충돌)
```

**최종 결정**: **Next.js + TypeScript** 
- 이유: 공식 홈페이지는 SEO 최적화가 핵심
- 구글 검색 유입, 마케팅 랜딩 페이지 역할

### Phase 2: 서비스 설계
**사용자 요청**: "service_official_home_smart_person_ai 부터 만들자. frontend, backend 만들고 현사AI의 메인 페이지를 여기에 만들면 될것 같아"

**설계 방향**:
- 별도 마이크로서비스로 분리
- 역할: SEO 최적화, 브랜딩, 리드 생성, 서비스 소개
- 메인 애플리케이션과 독립적 운영

**서비스 구조**:
```
service_official_home_smart_person_ai/
├── frontend/           # Next.js (포트 3000)
├── backend/           # FastAPI (포트 8030)  
├── scripts/          # 개발 도구
└── README.md         # 서비스 문서
```

### Phase 3: 프론트엔드 구축 (Next.js 14)

**주요 컴포넌트 개발**:
1. **HeroSection**: 브랜딩 메시지 + 핵심 CTA
2. **ServicesSection**: 6개 AI 서비스 소개
3. **FeaturesSection**: 차별점, 기존 방식 vs 현사AI 비교
4. **PricingSection**: 3단계 구독 플랜 (베이직/프리미엄/프로)
5. **TestimonialsSection**: 고객 성공 사례 + 통계
6. **CTASection**: 최종 회원가입 유도 + 특별 혜택

**기술 스택**:
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- Framer Motion (애니메이션)
- Lucide React (아이콘)

**SEO 최적화**:
```typescript
// 메타데이터 최적화
export const metadata: Metadata = {
  title: '현사AI - 현명한 사람들의 AI',
  description: 'AI를 모르는 사람들과 AI 공부가 귀찮은 사람들을 위한 AI 산출물 공급 서비스',
  keywords: ['AI', '인공지능', '이미지 생성', '동화책', '업무 자동화'],
  openGraph: { /* 소셜 미디어 최적화 */ },
  // 구조화된 데이터 (JSON-LD)
}
```

### Phase 4: 백엔드 구축 (FastAPI)

**주요 API 엔드포인트**:
```python
POST /api/v1/contact          # 문의 접수
POST /api/v1/newsletter       # 뉴스레터 구독  
POST /api/v1/demo-request     # 데모 요청
GET  /api/v1/services-overview # 서비스 개요
GET  /api/v1/testimonials     # 고객 후기
```

**핵심 기능**:
- 리드 생성 (문의, 뉴스레터, 데모 요청)
- 백그라운드 이메일 발송
- 서비스 데이터 제공
- 헬스체크 및 모니터링

### Phase 5: 인프라 및 통합

**Docker 설정**:
- Frontend: Next.js standalone build
- Backend: Python 3.12 + FastAPI
- 개발/프로덕션 환경 분리

**개발 도구**:
```python
# scripts/dev.py - 통합 개발 서버
python scripts/dev.py                # 전체 실행
python scripts/dev.py --frontend     # 프론트엔드만
python scripts/dev.py --backend      # 백엔드만
```

**메인 프로젝트 통합**:
1. `docker-compose.yml`에 2개 서비스 추가
2. `nginx.conf`에 라우팅 설정
3. `README.md`에 서비스 정보 추가

**Nginx 라우팅**:
```nginx
location / {
    # 홈페이지가 최우선 (/)
    proxy_pass http://official_home_frontend;
}

location /app/ {
    # 메인 애플리케이션 (/app/)
    proxy_pass http://api_gateway/;
}

location /home-api/ {
    # 홈페이지 API (/home-api/)
    proxy_pass http://official_home_backend;
}
```

---

## 📊 개발 성과

### ✅ 완성된 기능
- [x] SEO 최적화 랜딩 페이지 (6개 섹션)
- [x] 반응형 디자인 + PWA 준비
- [x] 백엔드 API (문의, 뉴스레터, 데모)
- [x] Docker 컨테이너화
- [x] 메인 프로젝트 통합
- [x] 개발 도구 및 스크립트

### 🎯 주요 특징
1. **완전한 SEO 최적화**
   - 구조화된 데이터 (JSON-LD)
   - Open Graph + Twitter Cards  
   - 한국어 최적화 메타데이터

2. **전문적인 디자인**
   - 현사AI 브랜딩 일관성
   - 인터랙티브 애니메이션
   - 모바일 퍼스트 반응형

3. **비즈니스 최적화**
   - 리드 생성 폼들
   - 가격 계획 명확 표시  
   - 고객 후기 및 성과 지표

4. **마이크로서비스 통합**
   - 독립적인 홈페이지 서비스
   - API Gateway와 연동
   - 결제 시스템 연결

### 📈 성능 목표
- **Lighthouse 점수**: 95+ (모든 항목)
- **SEO 목표**: "AI 서비스" 키워드 상위 10위  
- **전환율**: 방문자 대비 회원가입 5%+

### 🌐 서비스 엔드포인트
- **홈페이지**: http://localhost:3000
- **홈페이지 API**: http://localhost:8030
- **API 문서**: http://localhost:8030/docs

---

## 🔄 아키텍처 결정 배경

### 왜 별도 마이크로서비스로 분리했나?

1. **도메인 분리**: 마케팅 사이트 vs 서비스 애플리케이션
2. **기술 최적화**: SEO 최적화 vs 사용자 경험 최적화
3. **배포 전략**: 정적 사이트 vs 동적 애플리케이션
4. **팀 분업**: 마케팅팀 vs 개발팀

### 하이브리드 프론트엔드 전략

**현재 구조**:
- `www.smartpersonai.com` → Next.js 홈페이지 (SEO 최적화)
- `app.smartpersonai.com` → Vite 웹앱 (사용자 서비스)

**장점**:
- 각 용도에 최적화된 기술 스택
- 독립적인 개발/배포 가능
- 성능과 SEO 두 마리 토끼

---

## 🎉 결론

**service_official_home_smart_person_ai**은 현사AI의 완전한 공식 홈페이지로서:

1. **기술적 완성도**: Next.js + FastAPI 마이크로서비스
2. **비즈니스 가치**: SEO 최적화 + 리드 생성
3. **확장 가능성**: 독립적인 서비스로 유지보수 용이
4. **통합 운영**: 메인 프로젝트와 완벽 연동

현사AI 브랜드의 온라인 관문 역할을 충실히 수행할 수 있는 전문적인 홈페이지가 완성되었습니다.

---

## 📚 관련 문서
- [service_official_home_smart_person_ai/README.md](../service_official_home_smart_person_ai/README.md)
- [frontend_technology_decision.md](./frontend_technology_decision.md) 
- [comparison-vite-vs-nextjs.md](../service_official_home_smart_person_ai/comparison-vite-vs-nextjs.md)