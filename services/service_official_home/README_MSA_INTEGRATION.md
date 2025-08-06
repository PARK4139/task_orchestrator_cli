# Official Home MSA - 통합 관리 시스템

## 📋 개요

기존의 여러 스크립트들을 2개의 통합 스크립트로 정리하여 MSA 서비스를 효율적으로 관리할 수 있습니다.

## 🚀 통합 스크립트

### 1. 개발모드 + 핫리로드
```bash
./ensure_official_home_development_mode_ran.sh
```

**기능:**
- 🔥 실시간 핫리로드 개발 환경
- 🔧 백엔드 개발 서버 (포트: 8030)
- 🎨 프론트엔드 개발 서버 (포트: 3000)
- 📦 볼륨 마운트로 실시간 파일 반영
- 🔍 자동 헬스체크 및 상태 확인

### 2. 운영모드
```bash
./ensure_official_home_operation_mode_ran.sh
```

**기능:**
- 🚀 프로덕션 최적화 빌드
- 📦 멀티스테이지 Docker 빌드
- 🔧 자동 빌드 오류 수정
- 🛡️ 헬스체크 및 재시작 정책
- 📊 실시간 모니터링

## 🔧 내장 Fix 기능

### 개발모드 Fix 기능
- ✅ 기존 컨테이너 자동 정리
- ✅ 의존성 파일 검증
- ✅ 개발용 이미지 자동 빌드
- ✅ 핫리로드 환경 설정
- ✅ 서비스 상태 자동 확인

### 운영모드 Fix 기능
- ✅ Next.js 설정 최적화
- ✅ Dockerfile 멀티스테이지 빌드
- ✅ 빌드 오류 자동 수정
- ✅ 프로덕션 환경 최적화
- ✅ 헬스체크 및 재시작 정책

## 📊 사용법

### 개발 시작
```bash
cd services/smart_person_ai/service_official_home_smart_person_ai
./ensure_official_home_development_mode_ran.sh
```

### 운영 배포
```bash
cd services/smart_person_ai/service_official_home_smart_person_ai
./ensure_official_home_operation_mode_ran.sh
```

## 🌐 접속 정보

### 개발모드
- **프론트엔드**: http://localhost:3000
- **백엔드 API**: http://localhost:8030
- **실시간 로그**: `docker logs -f official-home-frontend`

### 운영모드
- **프론트엔드**: http://localhost:3000
- **백엔드 API**: http://localhost:8030
- **실시간 로그**: `docker-compose -f docker-compose.prod.yml logs -f`

## 🛑 중지 명령

### 개발모드 중지
```bash
docker stop official-home-frontend official-home-backend
```

### 운영모드 중지
```bash
docker-compose -f docker-compose.prod.yml down
```

## 📋 로그 확인

### 개발모드 로그
```bash
# 프론트엔드 로그
docker logs -f official-home-frontend

# 백엔드 로그
docker logs -f official-home-backend
```

### 운영모드 로그
```bash
# 전체 로그
docker-compose -f docker-compose.prod.yml logs -f

# 개별 서비스 로그
docker logs -f official-home-frontend
docker logs -f official-home-backend
```

## 🔄 기존 스크립트 대체

### 기존 스크립트들
- `start_frontend_fixed.sh` → `ensure_official_home_development_mode_ran.sh`
- `ensure_development_hot_reload.sh` → `ensure_official_home_development_mode_ran.sh`
- `ensure_hotreload_test_start.sh` → `ensure_official_home_development_mode_ran.sh`
- `docker-compose.yml` → `ensure_official_home_operation_mode_ran.sh`

### 통합된 기능
- ✅ 핫리로드 개발 환경
- ✅ 운영 모드 배포
- ✅ 자동 빌드 오류 수정
- ✅ 헬스체크 및 모니터링
- ✅ 로그 관리

## 🎯 장점

1. **단순화**: 2개의 스크립트로 모든 기능 통합
2. **자동화**: Fix 기능이 내장되어 있어 수동 개입 최소화
3. **안정성**: 헬스체크 및 오류 복구 기능
4. **편의성**: 명확한 사용법과 상태 표시
5. **확장성**: 다른 MSA 서비스에도 동일한 패턴 적용 가능

## 📝 주의사항

- Docker와 Docker Compose가 설치되어 있어야 합니다
- 포트 3000과 8030이 사용 가능해야 합니다
- 충분한 디스크 공간이 필요합니다 (이미지 빌드용) 