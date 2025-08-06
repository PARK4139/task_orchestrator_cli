# Smart Person AI 하이브리드 프론트엔드 아키텍처

## 🎯 최적 솔루션: 단계별 접근

### Phase 1: MVP (Vite + React + TypeScript) ⚡
**목표**: 빠른 출시 및 검증
```
services/smart_person_ai/
├── frontend/                    # 메인 웹앱 (Vite)
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Dashboard.tsx    # 로그인 후 서비스
│   │   │   ├── AIImage.tsx      # AI 이미지 생성
│   │   │   ├── Payment.tsx      # 결제 시스템
│   │   │   └── ...
│   │   └── ...
│   └── vite.config.ts
```

**장점:**
- 2-3주만에 MVP 완성 가능
- 팀 온보딩 쉬움
- FastAPI와 완벽 연동
- PWA로 모바일 앱 경험

### Phase 2: 마케팅 사이트 추가 (Next.js) 🚀
**목표**: SEO 최적화된 마케팅 사이트
```
services/smart_person_ai/
├── frontend/                    # 메인 웹앱 (Vite)
├── marketing/                   # 마케팅 사이트 (Next.js)
│   ├── app/
│   │   ├── page.tsx            # 홈페이지 (SEO 최적화)
│   │   ├── pricing/page.tsx    # 가격 페이지
│   │   ├── features/page.tsx   # 기능 소개
│   │   └── blog/               # 블로그 (SEO)
│   └── next.config.js
```

**도메인 분리:**
- `app.smartpersonai.com` → Vite 웹앱 (로그인 후 서비스)
- `www.smartpersonai.com` → Next.js 마케팅 (SEO 최적화)

## 📊 단계별 개발 계획

### Phase 1 (1-2개월): Vite 웹앱
- [x] 기본 UI/UX 구축
- [x] 6개 마이크로서비스 연동
- [x] 결제 시스템 구현
- [x] PWA 설정 (모바일 최적화)

### Phase 2 (1개월): Next.js 마케팅
- [ ] SEO 최적화된 홈페이지
- [ ] 블로그 시스템 (콘텐츠 마케팅)
- [ ] 구글 애널리틱스 연동

### Phase 3 (선택): 통합 또는 분리 유지
- 옵션 A: Next.js로 전체 통합 (복잡)
- 옵션 B: 분리 유지 (추천) - 각각의 장점 활용