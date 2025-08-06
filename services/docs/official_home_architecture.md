# Service Official Home - 아키텍처 설계서

## 🏠 서비스 개요

**service_official_home_smart_person_ai**은 현사AI의 공식 홈페이지를 담당하는 독립 마이크로서비스입니다.

### 핵심 목표
- 🎯 **SEO 최적화**: 구글 검색 유입 극대화
- 🎨 **브랜딩**: 현사AI 가치 제안 전달
- 💼 **리드 생성**: 잠재 고객 → 실제 고객 전환
- 📞 **고객 소통**: 문의, 데모 요청, 뉴스레터

---

## 🏗️ 시스템 아키텍처

### 전체 구조도

```mermaid
graph TB
    subgraph "🌐 Client Layer"
        A[Web Browser]
        B[Mobile Browser]
        C[Search Engine Bots]
    end
    
    subgraph "🔀 Load Balancer"
        D[Nginx<br/>Port 80/443]
    end
    
    subgraph "🏠 Official Home Service"
        E[Next.js Frontend<br/>Port 3000]
        F[FastAPI Backend<br/>Port 8030]
    end
    
    subgraph "🌐 Main Application"  
        G[API Gateway<br/>Port 8000]
        H[Other Services...]
    end
    
    subgraph "🗄️ Data Layer"
        I[(PostgreSQL)]
        J[(Redis)]
    end
    
    A --> D
    B --> D  
    C --> D
    D --> E
    E --> F
    F --> I
    F --> J
    D --> G
```

### 서비스 간 통신

```mermaid
sequenceDiagram
    participant U as User
    participant N as Nginx
    participant FE as Next.js Frontend
    participant BE as FastAPI Backend
    participant AG as API Gateway
    participant DB as Database
    
    Note over U,DB: 홈페이지 방문 시나리오
    U->>N: GET /
    N->>FE: 라우팅
    FE->>BE: GET /api/v1/services-overview
    BE->>DB: 서비스 데이터 조회
    DB-->>BE: 데이터 반환
    BE-->>FE: JSON 응답
    FE-->>N: HTML 페이지
    N-->>U: 최종 페이지
    
    Note over U,DB: 회원가입 시나리오  
    U->>FE: 회원가입 버튼 클릭
    FE->>AG: POST /api/v1/auth/register
    AG-->>FE: 회원가입 완료
    FE-->>U: 대시보드로 리다이렉트
```

---

## 🎨 프론트엔드 아키텍처 (Next.js 14)

### 디렉토리 구조

```
frontend/
├── app/                        # App Router (Next.js 14)
│   ├── layout.tsx              # 전역 레이아웃 + SEO 메타데이터
│   ├── page.tsx                # 홈페이지 (/
│   ├── globals.css             # 전역 스타일
│   └── not-found.tsx           # 404 페이지
├── components/
│   ├── sections/               # 페이지 섹션들
│   │   ├── HeroSection.tsx     # 히어로 섹션
│   │   ├── ServicesSection.tsx # 서비스 소개
│   │   ├── FeaturesSection.tsx # 주요 특징
│   │   ├── PricingSection.tsx  # 가격 계획
│   │   ├── TestimonialsSection.tsx # 고객 후기
│   │   └── CTASection.tsx      # Call-to-Action
│   └── layout/
│       └── Footer.tsx          # 푸터
├── lib/                        # 유틸리티 함수
├── types/                      # TypeScript 타입 정의
└── public/                     # 정적 자산
    ├── images/
    ├── icons/
    └── manifest.json           # PWA 설정
```

### 핵심 컴포넌트

#### 1. HeroSection - 첫인상 결정
```typescript
const HeroSection = () => {
  return (
    <section className="hero-gradient min-h-screen">
      {/* 브랜딩 메시지 */}
      <h1>현사AI - 현명한 사람들의 AI</h1>
      
      {/* 핵심 가치 제안 */}
      <p>AI를 모르는 사람들을 위한 AI 산출물 공급 서비스</p>
      
      {/* 명언 */}
      <blockquote>
        "AI 시대의 현명한 사람들은 AI 사용자가 될 것을 나는 믿는다."
      </blockquote>
      
      {/* CTA 버튼 */}
      <Link href="/app">지금 시작하기</Link>
      <Link href="#services">서비스 둘러보기</Link>
    </section>
  );
};
```

#### 2. ServicesSection - 6개 AI 서비스 소개
```typescript
const services = [
  {
    id: 'ai_image',
    name: 'AI 이미지 생성',
    description: 'Stable Diffusion으로 고품질 이미지 생성',
    icon: ImageIcon,
    features: ['다양한 스타일', '고화질 생성', '빠른 처리']
  },
  // ... 나머지 5개 서비스
];
```

#### 3. PricingSection - 구독 플랜
```typescript
const pricingPlans = [
  {
    name: '베이직',
    price: 9900,
    tokens: 100,
    features: ['AI 이미지 생성', '기본 엑셀 자동화', '이메일 지원']
  },
  {
    name: '프리미엄', 
    price: 19900,
    tokens: 500,
    popular: true,
    features: ['모든 베이직 기능', 'AI 동화책', '웹 크롤링', '우선 지원']
  },
  {
    name: '프로',
    price: 49900, 
    tokens: 2000,
    features: ['무제한 사용', '커스텀 파이프라인', '전화 지원', 'SLA 보장']
  }
];
```

### SEO 최적화 전략

#### 메타데이터 설정
```typescript
// app/layout.tsx
export const metadata: Metadata = {
  title: {
    default: '현사AI - 현명한 사람들의 AI',
    template: '%s | 현사AI'
  },
  description: 'AI를 모르는 사람들과 AI 공부가 귀찮은 사람들을 위한 AI 산출물 공급 서비스',
  keywords: ['AI', '인공지능', '이미지 생성', '동화책', '업무 자동화', '현사AI'],
  
  // Open Graph (Facebook, LinkedIn)
  openGraph: {
    type: 'website',
    locale: 'ko_KR',
    url: 'https://smartpersonai.com',
    title: '현사AI - 현명한 사람들의 AI',
    description: 'AI 시대의 현명한 사람들은 AI 사용자가 될 것을 나는 믿는다.',
    siteName: '현사AI',
    images: [{
      url: '/og-image.png',
      width: 1200,
      height: 630,
      alt: '현사AI 공식 홈페이지'
    }]
  },
  
  // Twitter Cards
  twitter: {
    card: 'summary_large_image',
    title: '현사AI - 현명한 사람들의 AI',
    description: 'AI를 쉽고 빠르게 활용할 수 있는 모든 서비스',
    images: ['/twitter-image.png']
  },
  
  // 검색 로봇 설정
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large', 
      'max-snippet': -1
    }
  }
};
```

#### 구조화된 데이터 (JSON-LD)
```typescript
const organizationSchema = {
  '@context': 'https://schema.org',
  '@type': 'Organization',
  name: '현사AI',
  alternateName: 'Smart Person AI',
  url: 'https://smartpersonai.com',
  logo: 'https://smartpersonai.com/logo.png',
  description: 'AI를 모르는 사람들을 위한 AI 산출물 공급 서비스',
  sameAs: [
    'https://twitter.com/smartpersonai',
    'https://linkedin.com/company/smartpersonai'
  ],
  contactPoint: {
    '@type': 'ContactPoint', 
    telephone: '+82-10-0000-0000',
    contactType: 'customer service'
  }
};
```

---

## ⚡ 백엔드 아키텍처 (FastAPI)

### API 엔드포인트 설계

```python
# main.py
app = FastAPI(
    title="현사AI - Official Home Backend",
    description="공식 홈페이지 백엔드 API",
    version="0.1.0"
)

# 주요 엔드포인트
@app.get("/")                          # 서버 상태
@app.get("/health")                    # 헬스체크
@app.get("/api/v1/services-overview")  # 서비스 개요
@app.get("/api/v1/testimonials")       # 고객 후기

@app.post("/api/v1/contact")           # 문의 접수
@app.post("/api/v1/newsletter")        # 뉴스레터 구독
@app.post("/api/v1/demo-request")      # 데모 요청
```

### 데이터 모델

```python
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class ContactRequest(BaseModel):
    name: str
    email: EmailStr
    company: Optional[str] = None
    message: str
    service_interest: Optional[List[str]] = []

class NewsletterRequest(BaseModel):
    email: EmailStr
    interests: Optional[List[str]] = []

class DemoRequest(BaseModel):
    name: str
    email: EmailStr
    company: Optional[str] = None
    preferred_time: Optional[str] = None
    service_interest: str
```

### 백그라운드 작업 처리

```python
from fastapi import BackgroundTasks

@app.post("/api/v1/contact")
async def submit_contact(
    request: ContactRequest,
    background_tasks: BackgroundTasks
):
    # 문의 데이터 저장
    contact_id = save_contact(request)
    
    # 백그라운드에서 이메일 발송
    background_tasks.add_task(
        send_contact_notification,
        contact_id, request.email
    )
    
    return {"status": "success", "contact_id": contact_id}

async def send_contact_notification(contact_id: str, email: str):
    """백그라운드에서 실행되는 이메일 알림"""
    # 실제 이메일 발송 로직
    logger.info(f"Contact notification sent: {contact_id}")
```

---

## 🐳 배포 및 인프라

### Docker 설정

#### Frontend Dockerfile
```dockerfile
# Next.js 프로덕션 빌드
FROM node:18-alpine AS base

FROM base AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM base AS builder  
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
ENV NEXT_TELEMETRY_DISABLED 1
RUN npm run build

FROM base AS runner
WORKDIR /app
ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs
EXPOSE 3000
ENV PORT 3000

CMD ["node", "server.js"]
```

#### Backend Dockerfile
```dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8030

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8030"]
```

### Docker Compose 통합

```yaml
# docker-compose.yml (메인 프로젝트)
services:
  # 공식 홈페이지 백엔드
  official_home_backend:
    build:
      context: ./service_official_home_smart_person_ai/backend
      dockerfile: Dockerfile
    container_name: smart_ai_official_home_backend
    ports:
      - "8030:8030"
    environment:
      - DEBUG=false
      - DATABASE_URL=postgresql://smart_user:smart_password@postgres:5432/smart_person_ai
      - REDIS_URL=redis://redis:6379
    depends_on:
      - postgres
      - redis
    networks:
      - smart_ai_network

  # 공식 홈페이지 프론트엔드
  official_home_frontend:
    build:
      context: ./service_official_home_smart_person_ai/frontend
      dockerfile: Dockerfile
    container_name: smart_ai_official_home_frontend
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - NEXT_PUBLIC_API_URL=http://official_home_backend:8030
      - NEXT_PUBLIC_APP_URL=http://api_gateway:8000
    depends_on:
      - official_home_backend
    networks:
      - smart_ai_network
```

### Nginx 라우팅

```nginx
# nginx.conf
server {
    listen 80;
    server_name smartpersonai.com www.smartpersonai.com;
    
    # 홈페이지 (최우선 라우팅)
    location / {
        proxy_pass http://official_home_frontend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Next.js HMR 지원
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_cache_bypass $http_upgrade;
    }

    # 홈페이지 백엔드 API
    location /home-api/ {
        rewrite ^/home-api/(.*) /$1 break;
        proxy_pass http://official_home_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # 메인 애플리케이션
    location /app/ {
        proxy_pass http://api_gateway/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---

## 🚀 개발 도구 및 스크립트

### 통합 개발 스크립트

```python
# scripts/dev.py
#!/usr/bin/env python3
"""
현사AI 공식 홈페이지 개발 서버 실행 스크립트
"""

def run_backend():
    """백엔드 서버 실행"""
    backend_dir = PROJECT_ROOT / "backend"
    process = subprocess.Popen([
        sys.executable, "-m", "uvicorn", 
        "main:app", 
        "--host", "0.0.0.0", 
        "--port", "8030", 
        "--reload"
    ], cwd=backend_dir)
    return process

def run_frontend():
    """프론트엔드 개발 서버 실행"""
    frontend_dir = PROJECT_ROOT / "frontend"
    env = os.environ.copy()
    env['NEXT_PUBLIC_API_URL'] = 'http://localhost:8030'
    env['NEXT_PUBLIC_APP_URL'] = 'http://localhost:8000'
    
    process = subprocess.Popen([
        "npm", "run", "dev"
    ], cwd=frontend_dir, env=env)
    return process

# 사용법:
# python scripts/dev.py           # 전체 실행
# python scripts/dev.py --backend # 백엔드만
# python scripts/dev.py --frontend # 프론트엔드만
```

---

## 📊 성능 최적화

### 프론트엔드 최적화

#### 1. Next.js 최적화 설정
```javascript
// next.config.js
const nextConfig = {
  // 성능 최적화
  experimental: {
    optimizePackageImports: ['lucide-react'],
  },
  
  // 이미지 최적화
  images: {
    domains: ['localhost', 'smartpersonai.com'],
    formats: ['image/webp', 'image/avif'],
  },
  
  // 정적 최적화
  output: 'standalone',
  
  // 보안 헤더
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          { key: 'X-Frame-Options', value: 'DENY' },
          { key: 'X-Content-Type-Options', value: 'nosniff' },
          { key: 'Referrer-Policy', value: 'origin-when-cross-origin' }
        ]
      }
    ];
  }
};
```

#### 2. 컴포넌트 동적 로딩
```typescript
// app/page.tsx
import dynamic from 'next/dynamic';

// 컴포넌트 지연 로딩 (성능 최적화)
const HeroSection = dynamic(() => import('@/components/sections/HeroSection'));
const ServicesSection = dynamic(() => import('@/components/sections/ServicesSection'));
const PricingSection = dynamic(() => import('@/components/sections/PricingSection'));
```

#### 3. 이미지 최적화
```typescript
import Image from 'next/image';

// Next.js 최적화된 이미지
<Image
  src="/hero-image.png"
  alt="현사AI 메인 이미지"
  width={1200}
  height={630}
  priority // LCP 최적화
  placeholder="blur" // 로딩 경험 개선
/>
```

### 백엔드 최적화

#### 1. 응답 캐싱
```python
from functools import lru_cache

@lru_cache(maxsize=128)
@app.get("/api/v1/services-overview")
async def get_services_overview():
    """서비스 개요 - 캐싱 적용"""
    return services_data

@lru_cache(maxsize=64)  
@app.get("/api/v1/testimonials")
async def get_testimonials():
    """고객 후기 - 캐싱 적용"""
    return testimonials_data
```

#### 2. 데이터베이스 최적화
```python
# 연결 풀링
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True
)
```

---

## 📈 모니터링 및 분석

### 성능 지표

#### 프론트엔드 성과 목표
- **Lighthouse 점수**: 95+ (Performance, Accessibility, Best Practices, SEO)
- **First Contentful Paint**: < 1.5초
- **Largest Contentful Paint**: < 2.5초  
- **Cumulative Layout Shift**: < 0.1
- **Time to Interactive**: < 3.5초

#### 백엔드 성과 목표
- **응답 시간**: 평균 < 200ms
- **처리량**: 1000 req/s
- **가용성**: 99.9% 업타임
- **에러율**: < 0.1%

### SEO 성과 목표

```javascript
const seoTargets = {
  organicTraffic: {
    target: "월 10,000+ 방문자",
    timeline: "6개월 내"
  },
  
  keywordRanking: {
    "AI 서비스": "상위 10위",
    "AI 이미지 생성": "상위 5위", 
    "AI 동화책": "상위 3위",
    "엑셀 자동화": "상위 5위"
  },
  
  conversionRate: {
    target: "방문자 대비 5% 회원가입",
    newsletter: "2% 뉴스레터 구독",
    demo: "1% 데모 요청"
  }
};
```

### 분석 도구 통합

#### Google Analytics 4
```typescript
// app/layout.tsx
{process.env.NODE_ENV === 'production' && (
  <>
    <script
      async
      src={`https://www.googletagmanager.com/gtag/js?id=${process.env.NEXT_PUBLIC_GA_ID}`}
    />
    <script
      dangerouslySetInnerHTML={{
        __html: `
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', '${process.env.NEXT_PUBLIC_GA_ID}');
        `,
      }}
    />
  </>
)}
```

---

## 🔮 향후 확장 계획

### Phase 2 기능 (2024 Q2)
- [ ] **다국어 지원**: 영어 버전 추가
- [ ] **블로그 시스템**: 콘텐츠 마케팅 강화
- [ ] **라이브 채팅**: 실시간 고객 지원
- [ ] **고객 성공 사례**: 전용 페이지

### Phase 3 기능 (2024 Q3)  
- [ ] **A/B 테스트**: 전환율 최적화
- [ ] **개인화**: 방문자별 맞춤 콘텐츠
- [ ] **소셜 미디어**: 자동 콘텐츠 배포
- [ ] **웨비나**: 온라인 데모 시스템

### 기술 부채 해소 (지속적)
- [ ] **성능 최적화**: Core Web Vitals 개선
- [ ] **접근성**: WCAG 2.1 AA 준수
- [ ] **보안**: 정기 보안 감사
- [ ] **모니터링**: 실시간 알람 시스템

---

## 🎯 결론

**service_official_home_smart_person_ai**은 현사AI의 디지털 관문으로서:

1. **기술적 우수성**: Next.js + FastAPI 조합으로 최고의 성능과 SEO
2. **비즈니스 가치**: 브랜드 인지도 향상 + 리드 생성 + 고객 전환
3. **확장 가능성**: 모듈형 아키텍처로 지속적인 개선 가능
4. **운영 효율성**: 자동화된 배포 + 모니터링으로 안정적 서비스

현사AI가 AI 시장에서 독보적인 위치를 확립할 수 있도록 돕는 핵심 인프라로 자리잡을 것입니다.

---

## 📚 관련 문서
- [Service Official Home README](../service_official_home_smart_person_ai/README.md)
- [Frontend Technology Decision](./frontend_technology_decision.md)
- [Service Creation Log](./service_official_home_smart_person_ai_creation_log.md)
- [Main Project README](../README.md)