#!/bin/bash

echo "🚀 Official Home MSA - 운영모드 통합 실행..."
echo "================================================"

# 1️⃣ 기존 컨테이너 정리
echo "🧹 기존 컨테이너 정리 중..."
docker-compose down 2>/dev/null || true
docker stop official-home-frontend official-home-backend 2>/dev/null || true
docker rm official-home-frontend official-home-backend 2>/dev/null || true

# 2️⃣ 운영용 이미지 빌드
echo ""
echo "📦 운영용 이미지 빌드 중..."

# 백엔드 운영용 이미지 빌드
echo "🔧 백엔드 운영용 이미지 빌드..."
cd backend
docker build -t official-home-backend-prod .
cd ..

# 프론트엔드 운영용 이미지 빌드
echo "🎨 프론트엔드 운영용 이미지 빌드..."
cd frontend

# 빌드 오류 수정 로직
echo "🔧 프론트엔드 빌드 최적화 중..."
if [ -f "next.config.js" ]; then
    # Next.js 설정 최적화
    sed -i 's/experimental: {/experimental: {\n    outputFileTracingRoot: undefined,/g' next.config.js 2>/dev/null || true
fi

# Dockerfile 최적화
if [ -f "Dockerfile" ]; then
    # 멀티스테이지 빌드 최적화
    cat > Dockerfile.prod << 'EOF'
FROM node:18-alpine AS base

# Install dependencies only when needed
FROM base AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app

# Install dependencies based on the preferred package manager
COPY package.json package-lock.json* ./
RUN npm ci --only=production

# Rebuild the source code only when needed
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Next.js collects completely anonymous telemetry data about general usage.
# Learn more here: https://nextjs.org/telemetry
# Uncomment the following line in case you want to disable telemetry during the build.
ENV NEXT_TELEMETRY_DISABLED 1

RUN npm run build

# Production image, copy all the files and run next
FROM base AS runner
WORKDIR /app

ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public

# Set the correct permission for prerender cache
RUN mkdir .next
RUN chown nextjs:nodejs .next

# Automatically leverage output traces to reduce image size
# https://nextjs.org/docs/advanced-features/output-file-tracing
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT 3000
ENV HOSTNAME "0.0.0.0"

CMD ["node", "server.js"]
EOF
fi

# 운영용 이미지 빌드
docker build -f Dockerfile.prod -t official-home-frontend-prod .

cd ..

# 3️⃣ Docker Compose로 운영 모드 시작
echo ""
echo "🚀 운영 모드 서비스 시작..."
cat > docker-compose.prod.yml << 'EOF'
version: '3.8'

services:
  # 백엔드 API (운영)
  official-home-backend:
    image: official-home-backend-prod
    ports:
      - "8030:8030"
    environment:
      - NODE_ENV=production
      - DEBUG=false
      - LOG_LEVEL=info
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8030/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    restart: unless-stopped

  # 프론트엔드 (운영)
  official-home-frontend:
    image: official-home-frontend-prod
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - NEXT_PUBLIC_API_URL=http://official-home-backend:8030
      - NEXT_PUBLIC_APP_URL=http://localhost:3000
    depends_on:
      official-home-backend:
        condition: service_healthy
    restart: unless-stopped
EOF

# 운영 모드 시작
docker-compose -f docker-compose.prod.yml up -d

# 4️⃣ 서비스 상태 확인 및 헬스체크
echo ""
echo "⏳ 서비스 시작 대기 중..."
sleep 15

# 백엔드 헬스체크
echo "🔍 백엔드 상태 확인..."
for i in {1..5}; do
    if curl -f http://localhost:8030/health > /dev/null 2>&1; then
        echo "✅ 백엔드 서비스 정상 실행 (포트: 8030)"
        break
    else
        echo "⏳ 백엔드 서비스 시작 대기 중... ($i/5)"
        sleep 3
    fi
done

# 프론트엔드 헬스체크
echo "🔍 프론트엔드 상태 확인..."
for i in {1..5}; do
    if curl -f http://localhost:3000 > /dev/null 2>&1; then
        echo "✅ 프론트엔드 서비스 정상 실행 (포트: 3000)"
        break
    else
        echo "⏳ 프론트엔드 서비스 시작 대기 중... ($i/5)"
        sleep 3
    fi
done

# 5️⃣ 컨테이너 상태 표시
echo ""
echo "📊 실행 중인 컨테이너:"
docker ps | grep -E "(official-home-frontend|official-home-backend)"

# 6️⃣ 운영 모드 정보 출력
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 Official Home MSA - 운영모드 활성화!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🌐 프론트엔드: http://localhost:3000"
echo "🔧 백엔드 API: http://localhost:8030"
echo "📋 실시간 로그:"
echo "   전체: docker-compose -f docker-compose.prod.yml logs -f"
echo "   프론트엔드: docker logs -f official-home-frontend"
echo "   백엔드: docker logs -f official-home-backend"
echo "🛑 중지: docker-compose -f docker-compose.prod.yml down"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

echo ""
echo "🎯 운영 모드 설정 완료!" 