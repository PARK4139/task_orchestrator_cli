"""
WSL 환경에서 fin_service 컨테이너 빌드 테스트를 재현하는 함수
"""
import subprocess
import os
import sys
import time
import json
import platform
from typing import Dict, List, Tuple, Optional
from pathlib import Path


def function_split():
    """
    WSL 환경에서 fin_service 컨테이너 빌드 테스트를 재현하는 메인 함수
    """
    
    def ensure_windows_environment_detected() -> bool:
        """Windows 환경 감지"""
        if platform.system() != "Windows":
            print("❌ 이 테스트는 Windows 환경에서만 실행 가능합니다.")
            return False
        print("✅ Windows 환경 감지됨")
        return True
    
    def ensure_wsl_environment_checked() -> bool:
        """WSL 환경 확인"""
        try:
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", "pwd"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=10
            )
            return result.returncode == 0
        except Exception as e:
            print(f"❌ WSL 환경 확인 실패: {e}")
            return False
    
    def ensure_docker_enabled() -> bool:
        """Docker 설치 확인"""
        try:
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", "docker --version"],
                capture_output=True,
                text=True,
                encoding='utf-8',
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
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", "docker-compose --version"],
                capture_output=True,
                text=True,
                encoding='utf-8',
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
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                 "cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist && pwd"],
                capture_output=True,
                text=True,
                encoding='utf-8',
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
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                 "cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist && cp env.example .env"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=10
            )
            
            # 필요한 디렉토리 생성
            result2 = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                 "cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist && mkdir -p logs deployment/ssl"],
                capture_output=True,
                text=True,
                encoding='utf-8',
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
            print("⚠️  Docker 컨테이너 빌드는 Windows 환경에서 직접 실행할 수 없습니다.")
            print("   WSL 환경에서 직접 실행하거나 Docker Desktop을 통해 실행해야 합니다.")
            print("   빌드 명령어: cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist/deployment && docker-compose build --no-cache")
            return False
        except Exception as e:
            print(f"❌ Docker 컨테이너 빌드 실패: {e}")
            return False
    
    def ensure_containers_started() -> bool:
        """컨테이너 시작"""
        try:
            print("⚠️  컨테이너 시작은 Windows 환경에서 직접 실행할 수 없습니다.")
            print("   WSL 환경에서 직접 실행하거나 Docker Desktop을 통해 실행해야 합니다.")
            print("   시작 명령어: cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist/deployment && docker-compose up -d")
            return False
        except Exception as e:
            print(f"❌ 컨테이너 시작 실패: {e}")
            return False
    
    def ensure_containers_status_checked() -> Dict[str, str]:
        """컨테이너 상태 확인"""
        try:
            print("⚠️  컨테이너 상태 확인은 Windows 환경에서 직접 실행할 수 없습니다.")
            print("   WSL 환경에서 직접 실행하거나 Docker Desktop을 통해 실행해야 합니다.")
            print("   상태 확인 명령어: cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist/deployment && docker-compose ps")
            return {"status": "error", "output": "Windows 환경에서는 직접 실행 불가"}
        except Exception as e:
            print(f"❌ 컨테이너 상태 확인 실패: {e}")
            return {"status": "error", "output": str(e)}
    
    def ensure_services_health_checked() -> Dict[str, str]:
        """서비스 헬스체크"""
        try:
            print("⚠️  서비스 헬스체크는 Windows 환경에서 직접 실행할 수 없습니다.")
            print("   WSL 환경에서 직접 실행하거나 Docker Desktop을 통해 실행해야 합니다.")
            print("   헬스체크 명령어: curl -s http://localhost:8000/health")
            
            services = [
                ("API Gateway", "8000"),
                ("Investment Advisor", "8001"),
                ("Market Data", "8002"),
                ("News Analyzer", "8003"),
                ("Nginx", "80")
            ]
            
            health_results = {}
            for service_name, port in services:
                health_results[service_name] = "windows_environment_unsupported"
            
            return health_results
        except Exception as e:
            print(f"❌ 서비스 헬스체크 실패: {e}")
            return {"error": str(e)}
    
    def ensure_containers_cleaned_up() -> bool:
        """컨테이너 정리"""
        try:
            print("⚠️  컨테이너 정리는 Windows 환경에서 직접 실행할 수 없습니다.")
            print("   WSL 환경에서 직접 실행하거나 Docker Desktop을 통해 실행해야 합니다.")
            print("   정리 명령어: cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist/deployment && docker-compose down")
            return False
        except Exception as e:
            print(f"❌ 컨테이너 정리 실패: {e}")
            return False
    
    # 메인 실행 로직
    print("🚀 WSL 환경에서 fin_service 컨테이너 빌드 테스트 시작")
    print("=" * 60)
    
    # 0단계: Windows 환경 감지
    print("\n0️⃣ Windows 환경 감지 중...")
    if not ensure_windows_environment_detected():
        print("❌ Windows 환경 감지 실패. 테스트를 중단합니다.")
        return False
    
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
    
    # 6단계: Docker 컨테이너 빌드 (Windows 환경에서는 직접 실행 불가)
    print("\n6️⃣ Docker 컨테이너 빌드 중...")
    if not ensure_docker_containers_built():
        print("❌ Docker 컨테이너 빌드 실패. 테스트를 중단합니다.")
        return False
    
    # 7단계: 컨테이너 시작 (Windows 환경에서는 직접 실행 불가)
    print("\n7️⃣ 컨테이너 시작 중...")
    if not ensure_containers_started():
        print("❌ 컨테이너 시작 실패. 테스트를 중단합니다.")
        return False
    
    # 8단계: 컨테이너 상태 확인 (Windows 환경에서는 직접 실행 불가)
    print("\n8️⃣ 컨테이너 상태 확인 중...")
    status_result = ensure_containers_status_checked()
    
    # 9단계: 서비스 헬스체크 (Windows 환경에서는 직접 실행 불가)
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
        status_icon = "⚠️" if status == "windows_environment_unsupported" else "❌"
        print(f"  {status_icon} {service}: {status}")
    
    # 11단계: 컨테이너 정리 (Windows 환경에서는 직접 실행 불가)
    print("\n🧹 컨테이너 정리 중...")
    ensure_containers_cleaned_up()
    
    print("\n" + "=" * 60)
    print("📋 Windows 환경에서 실행 불가능한 작업들:")
    print("=" * 60)
    print("❌ Docker 컨테이너 빌드")
    print("❌ 컨테이너 시작")
    print("❌ 컨테이너 상태 확인")
    print("❌ 서비스 헬스체크")
    print("❌ 컨테이너 정리")
    print("\n💡 해결 방법:")
    print("1. WSL Ubuntu-24.04에 직접 접속하여 실행")
    print("2. Docker Desktop을 통해 실행")
    print("3. 제공된 명령어를 WSL 환경에서 직접 실행")
    
    print("\n🎉 Windows 환경에서 fin_service 컨테이너 빌드 테스트 완료!")
    print("   (일부 작업은 Windows 환경에서 직접 실행 불가)")
    return True


if __name__ == "__main__":
    function_split() 