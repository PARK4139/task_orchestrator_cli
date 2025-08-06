#!/usr/bin/env python3
"""
WSL에서 직접 실행하는 smart_person_ai 컨테이너 빌드 테스트
"""
import subprocess
import sys
import os
import platform
from typing import Dict, List, Tuple, Optional


def test_wsl_smart_person_ai_container_build():
    """
    WSL 환경에서 smart_person_ai 컨테이너 빌드 테스트
    """
    
    def ensure_wsl_environment_checked() -> bool:
        """WSL 환경 확인"""
        try:
            result = subprocess.run(
                ["pwd"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                print(f"✅ WSL 환경 확인: {result.stdout.strip()}")
                return True
            else:
                print(f"❌ WSL 환경 확인 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ WSL 환경 확인 실패: {e}")
            return False
    
    def ensure_docker_enabled() -> bool:
        """Docker 설치 확인"""
        try:
            result = subprocess.run(
                ["docker", "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                print(f"✅ Docker 설치 확인: {result.stdout.strip()}")
                return True
            else:
                print(f"❌ Docker 설치 확인 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ Docker 설치 확인 실패: {e}")
            return False
    
    def ensure_docker_compose_enabled() -> bool:
        """Docker Compose 설치 확인"""
        try:
            result = subprocess.run(
                ["docker-compose", "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                print(f"✅ Docker Compose 설치 확인: {result.stdout.strip()}")
                return True
            else:
                print(f"❌ Docker Compose 설치 확인 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ Docker Compose 설치 확인 실패: {e}")
            return False
    
    def ensure_project_directory_accessed() -> bool:
        """프로젝트 디렉토리 접근 확인"""
        try:
            result = subprocess.run(
                ["cd", "/mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist", "&&", "pwd"],
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                print(f"✅ 프로젝트 디렉토리 접근 확인: {result.stdout.strip()}")
                return True
            else:
                print(f"❌ 프로젝트 디렉토리 접근 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ 프로젝트 디렉토리 접근 실패: {e}")
            return False
    
    def ensure_environment_setup() -> bool:
        """환경 설정"""
        try:
            # .env 파일 복사
            result1 = subprocess.run(
                ["cd", "/mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist", "&&", "cp", "env.example", ".env"],
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            # 필요한 디렉토리 생성
            result2 = subprocess.run(
                ["cd", "/mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist", "&&", "mkdir", "-p", "logs", "deployment/ssl"],
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result1.returncode == 0 and result2.returncode == 0:
                print("✅ 환경 설정 완료")
                return True
            else:
                print(f"❌ 환경 설정 실패: {result1.stderr} {result2.stderr}")
                return False
        except Exception as e:
            print(f"❌ 환경 설정 실패: {e}")
            return False
    
    def ensure_docker_containers_built() -> bool:
        """Docker 컨테이너 빌드"""
        try:
            result = subprocess.run(
                ["cd", "/mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist/deployment", "&&", "docker-compose", "build", "--no-cache"],
                shell=True,
                capture_output=True,
                text=True,
                timeout=600  # 10분 타임아웃
            )
            
            if result.returncode == 0:
                print("✅ Docker 컨테이너 빌드 완료")
                return True
            else:
                print(f"❌ Docker 컨테이너 빌드 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ Docker 컨테이너 빌드 실패: {e}")
            return False
    
    def ensure_containers_started() -> bool:
        """컨테이너 시작"""
        try:
            result = subprocess.run(
                ["cd", "/mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist/deployment", "&&", "docker-compose", "up", "-d"],
                shell=True,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                print("✅ 컨테이너 시작 완료")
                return True
            else:
                print(f"❌ 컨테이너 시작 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ 컨테이너 시작 실패: {e}")
            return False
    
    def ensure_containers_status_checked() -> Dict[str, str]:
        """컨테이너 상태 확인"""
        try:
            result = subprocess.run(
                ["cd", "/mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist/deployment", "&&", "docker-compose", "ps"],
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                print("✅ 컨테이너 상태 확인 완료")
                print(result.stdout)
                return {"status": "success", "output": result.stdout}
            else:
                print(f"❌ 컨테이너 상태 확인 실패: {result.stderr}")
                return {"status": "error", "output": result.stderr}
        except Exception as e:
            print(f"❌ 컨테이너 상태 확인 실패: {e}")
            return {"status": "error", "output": str(e)}
    
    def ensure_services_health_checked() -> Dict[str, str]:
        """서비스 헬스체크"""
        services = [
            ("API Gateway", "8000"),
            ("Investment Advisor", "8001"),
            ("Market Data", "8002"),
            ("News Analyzer", "8003"),
            ("Nginx", "80")
        ]
        
        health_results = {}
        
        for service_name, port in services:
            try:
                result = subprocess.run(
                    ["curl", "-s", f"http://localhost:{port}/health"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    print(f"✅ {service_name} 헬스체크 성공")
                    health_results[service_name] = "healthy"
                else:
                    print(f"❌ {service_name} 헬스체크 실패")
                    health_results[service_name] = "unhealthy"
                    
            except Exception as e:
                print(f"❌ {service_name} 헬스체크 실패: {e}")
                health_results[service_name] = "error"
        
        return health_results
    
    def ensure_containers_cleaned_up() -> bool:
        """컨테이너 정리"""
        try:
            result = subprocess.run(
                ["cd", "/mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist/deployment", "&&", "docker-compose", "down"],
                shell=True,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                print("✅ 컨테이너 정리 완료")
                return True
            else:
                print(f"❌ 컨테이너 정리 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ 컨테이너 정리 실패: {e}")
            return False
    
    # 메인 실행 로직
    print("🚀 WSL 환경에서 smart_person_ai 컨테이너 빌드 테스트 시작")
    print("=" * 60)
    
    # 1단계: WSL 환경 확인
    print("\n1️⃣ WSL 환경 확인 중...")
    if not ensure_wsl_environment_checked():
        print("❌ WSL 환경 확인 실패. 테스트를 중단합니다.")
        return False
    
    # 2단계: Docker 설치 확인
    print("\n2️⃣ Docker 설치 확인 중...")
    if not ensure_docker_enabled():
        print("❌ Docker 설치 확인 실패. 테스트를 중단합니다.")
        return False
    
    # 3단계: Docker Compose 설치 확인
    print("\n3️⃣ Docker Compose 설치 확인 중...")
    if not ensure_docker_compose_enabled():
        print("❌ Docker Compose 설치 확인 실패. 테스트를 중단합니다.")
        return False
    
    # 4단계: 프로젝트 디렉토리 접근 확인
    print("\n4️⃣ 프로젝트 디렉토리 접근 확인 중...")
    if not ensure_project_directory_accessed():
        print("❌ 프로젝트 디렉토리 접근 실패. 테스트를 중단합니다.")
        return False
    
    # 5단계: 환경 설정
    print("\n5️⃣ 환경 설정 중...")
    if not ensure_environment_setup():
        print("❌ 환경 설정 실패. 테스트를 중단합니다.")
        return False
    
    # 6단계: Docker 컨테이너 빌드
    print("\n6️⃣ Docker 컨테이너 빌드 중...")
    if not ensure_docker_containers_built():
        print("❌ Docker 컨테이너 빌드 실패. 테스트를 중단합니다.")
        return False
    
    # 7단계: 컨테이너 시작
    print("\n7️⃣ 컨테이너 시작 중...")
    if not ensure_containers_started():
        print("❌ 컨테이너 시작 실패. 테스트를 중단합니다.")
        return False
    
    # 8단계: 컨테이너 상태 확인
    print("\n8️⃣ 컨테이너 상태 확인 중...")
    status_result = ensure_containers_status_checked()
    
    # 9단계: 서비스 헬스체크
    print("\n9️⃣ 서비스 헬스체크 중...")
    health_results = ensure_services_health_checked()
    
    # 10단계: 결과 요약
    print("\n" + "=" * 60)
    print("📊 테스트 결과 요약")
    print("=" * 60)
    
    print("\n🔍 컨테이너 상태:")
    print(status_result.get("output", "상태 확인 실패"))
    
    print("\n🏥 서비스 헬스체크 결과:")
    for service, status in health_results.items():
        status_icon = "✅" if status == "healthy" else "❌"
        print(f"  {status_icon} {service}: {status}")
    
    # 11단계: 컨테이너 정리 (선택사항)
    print("\n🧹 컨테이너 정리 중...")
    ensure_containers_cleaned_up()
    
    print("\n🎉 WSL 환경에서 smart_person_ai 컨테이너 빌드 테스트 완료!")
    return True


if __name__ == "__main__":
    success = test_wsl_smart_person_ai_container_build()
    if success:
        print("\n🎉 모든 테스트가 성공적으로 완료되었습니다!")
        sys.exit(0)
    else:
        print("\n💥 테스트 중 오류가 발생했습니다.")
        sys.exit(1) 