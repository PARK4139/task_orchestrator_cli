# FastAPI 백엔드 Dockerfile
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 업데이트 및 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python 의존성 설치
COPY ./service_official_home/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# shared 모듈 복사
COPY ./shared ./shared

# 애플리케이션 코드 복사
COPY ./service_official_home/backend .

# 환경 변수 설정
ENV PYTHONPATH=/app

# 포트 노출
EXPOSE 8030

# 헬스체크
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD curl -f http://localhost:8030/health || exit 1

# 애플리케이션 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8030", "--reload"]