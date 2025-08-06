"""
WSL 환경에서 smart_person_ai 컨테이너 생성 확인 테스트
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
    WSL 환경에서 smart_person_ai 컨테이너 생성 확인 테스트를 실행하는 메인 함수
    """
    
    def ensure_windows_environment_detected() -> bool:
        """Windows 환경 감지"""
        if platform.system() != "Windows":
            print(" 이 테스트는 Windows 환경에서만 실행 가능합니다.")
            return False
        print(" Windows 환경 감지됨")
        return True
    
    def ensure_wsl_environment_checked() -> bool:
        """WSL 환경 확인"""
        try:
            # 인코딩 문제를 해결하기 위해 errors='ignore' 사용
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", "pwd"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=10
            )
            if result.returncode == 0:
                print(" WSL 환경 확인됨")
                return True
            else:
                print(f" WSL 환경 확인 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f" WSL 환경 확인 실패: {e}")
            return False
    
    def ensure_docker_enabled() -> bool:
        """Docker 설치 확인"""
        try:
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", "docker --version"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=10
            )
            if result.returncode == 0:
                print(f" Docker 설치 확인: {result.stdout.strip()}")
                return True
            else:
                print(f" Docker 설치 확인 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f" Docker 설치 확인 실패: {e}")
            return False
    
    def ensure_docker_daemon_running() -> bool:
        """Docker 데몬 실행 확인"""
        try:
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", "docker info"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=10
            )
            if result.returncode == 0:
                print(" Docker 데몬 실행 확인")
                return True
            else:
                print(f" Docker 데몬 실행 확인 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f" Docker 데몬 실행 확인 실패: {e}")
            return False
    
    def ensure_project_directory_accessed() -> bool:
        """프로젝트 디렉토리 접근 확인"""
        try:
            user_path = os.path.expanduser("~")
            project_path = f"/mnt/c/Users/{os.path.basename(user_path)}/Downloads/pk_system/pkg_finance_invest_assist"
            
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                 f"cd {project_path} && pwd"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=10
            )
            if result.returncode == 0:
                print(f" 프로젝트 디렉토리 접근 확인: {result.stdout.strip()}")
                return True
            else:
                print(f" 프로젝트 디렉토리 접근 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f" 프로젝트 디렉토리 접근 실패: {e}")
            return False
    
    def ensure_docker_images_exist() -> Dict[str, bool]:
        """Docker 이미지 존재 확인"""
        try:
            user_path = os.path.expanduser("~")
            project_path = f"/mnt/c/Users/{os.path.basename(user_path)}/Downloads/pk_system/pkg_finance_invest_assist"
            
            print("�� Docker 이미지 존재 확인 중...")
            
            expected_images = [
                "finance_api_gateway",
                "finance_investment_advisor", 
                "finance_market_data",
                "finance_news_analyzer"
            ]
            
            image_results = {}
            for image_name in expected_images:
                result = subprocess.run(
                    ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                     f"docker images | grep {image_name}"],
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    errors='ignore',
                    timeout=10
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    image_results[image_name] = True
                    print(f" {image_name}: 존재함")
                else:
                    image_results[image_name] = False
                    print(f" {image_name}: 존재하지 않음")
            
            return image_results
        except Exception as e:
            print(f" Docker 이미지 확인 실패: {e}")
            return {"error": str(e)}
    
    def ensure_docker_containers_exist() -> Dict[str, str]:
        """Docker 컨테이너 존재 확인"""
        try:
            user_path = os.path.expanduser("~")
            project_path = f"/mnt/c/Users/{os.path.basename(user_path)}/Downloads/pk_system/pkg_finance_invest_assist"
            
            print(" Docker 컨테이너 존재 확인 중...")
            
            expected_containers = [
                "finance_api_gateway",
                "finance_investment_advisor",
                "finance_market_data", 
                "finance_news_analyzer",
                "finance_nginx",
                "finance_db",
                "finance_redis"
            ]
            
            container_results = {}
            for container_name in expected_containers:
                result = subprocess.run(
                    ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                     f"docker ps -a | grep {container_name}"],
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    errors='ignore',
                    timeout=10
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    # 컨테이너 상태 확인
                    status_result = subprocess.run(
                        ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                         f"docker ps | grep {container_name}"],
                        capture_output=True,
                        text=True,
                        encoding='utf-8',
                        errors='ignore',
                        timeout=10
                    )
                    
                    if status_result.returncode == 0 and status_result.stdout.strip():
                        container_results[container_name] = "running"
                        print(f" {container_name}: 실행 중")
                    else:
                        container_results[container_name] = "stopped"
                        print(f"️ {container_name}: 중지됨")
                else:
                    container_results[container_name] = "not_found"
                    print(f" {container_name}: 존재하지 않음")
            
            return container_results
        except Exception as e:
            print(f" Docker 컨테이너 확인 실패: {e}")
            return {"error": str(e)}
    
    def ensure_network_exists() -> bool:
        """Docker 네트워크 존재 확인"""
        try:
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                 "docker network ls | grep finance_network"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=10
            )
            
            if result.returncode == 0 and result.stdout.strip():
                print(" finance_network 존재함")
                return True
            else:
                print(" finance_network 존재하지 않음")
                return False
        except Exception as e:
            print(f" Docker 네트워크 확인 실패: {e}")
            return False
    
    def ensure_volumes_exist() -> Dict[str, bool]:
        """Docker 볼륨 존재 확인"""
        try:
            print(" Docker 볼륨 존재 확인 중...")
            
            expected_volumes = [
                "finance_postgres_data"
            ]
            
            volume_results = {}
            for volume_name in expected_volumes:
                result = subprocess.run(
                    ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                     f"docker volume ls | grep {volume_name}"],
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    errors='ignore',
                    timeout=10
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    volume_results[volume_name] = True
                    print(f" {volume_name}: 존재함")
                else:
                    volume_results[volume_name] = False
                    print(f" {volume_name}: 존재하지 않음")
            
            return volume_results
        except Exception as e:
            print(f" Docker 볼륨 확인 실패: {e}")
            return {"error": str(e)}
    
    def ensure_services_accessible() -> Dict[str, str]:
        """서비스 접근성 확인"""
        try:
            print("�� 서비스 접근성 확인 중...")
            
            services = [
                ("API Gateway", "8000"),
                ("Investment Advisor", "8001"),
                ("Market Data", "8002"),
                ("News Analyzer", "8003"),
                ("Nginx", "80")
            ]
            
            accessibility_results = {}
            for service_name, port in services:
                try:
                    result = subprocess.run(
                        ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                         f"curl -s -o /dev/null -w '%{{http_code}}' http://localhost:{port}/health"],
                        capture_output=True,
                        text=True,
                        encoding='utf-8',
                        errors='ignore',
                        timeout=10
                    )
                    
                    if result.returncode == 0:
                        status_code = result.stdout.strip()
                        if status_code == "200":
                            accessibility_results[service_name] = "accessible"
                            print(f" {service_name}: 접근 가능")
                        else:
                            accessibility_results[service_name] = f"http_{status_code}"
                            print(f"️ {service_name}: HTTP {status_code}")
                    else:
                        accessibility_results[service_name] = "connection_failed"
                        print(f" {service_name}: 연결 실패")
                except Exception as e:
                    accessibility_results[service_name] = f"error: {str(e)}"
                    print(f" {service_name}: 오류 - {e}")
            
            return accessibility_results
        except Exception as e:
            print(f" 서비스 접근성 확인 실패: {e}")
            return {"error": str(e)}
    
    # 메인 실행 로직
    print(" WSL 환경에서 smart_person_ai 컨테이너 생성 확인 테스트 시작")
    print("=" * 60)
    
    # 0단계: Windows 환경 감지
    print("\n0️⃣ Windows 환경 감지 중...")
    if not ensure_windows_environment_detected():
        print(" Windows 환경 감지 실패. 테스트를 중단합니다.")
        return False
    
    # 1단계: WSL 환경 확인
    print("\n1️⃣ WSL 환경 확인 중...")
    if not ensure_wsl_environment_checked():
        print(" WSL 환경 확인 실패. 테스트를 중단합니다.")
        return False
    
    # 2단계: Docker 설치 확인
    print("\n2️⃣ Docker 설치 확인 중...")
    if not ensure_docker_enabled():
        print(" Docker 설치 확인 실패. 테스트를 중단합니다.")
        return False
    
    # 3단계: Docker 데몬 실행 확인
    print("\n3️⃣ Docker 데몬 실행 확인 중...")
    if not ensure_docker_daemon_running():
        print(" Docker 데몬 실행 확인 실패. 테스트를 중단합니다.")
        return False
    
    # 4단계: 프로젝트 디렉토리 접근 확인
    print("\n4️⃣ 프로젝트 디렉토리 접근 확인 중...")
    if not ensure_project_directory_accessed():
        print(" 프로젝트 디렉토리 접근 실패. 테스트를 중단합니다.")
        return False
    
    # 5단계: Docker 이미지 존재 확인
    print("\n5️⃣ Docker 이미지 존재 확인 중...")
    image_results = ensure_docker_images_exist()
    
    # 6단계: Docker 컨테이너 존재 확인
    print("\n6️⃣ Docker 컨테이너 존재 확인 중...")
    container_results = ensure_docker_containers_exist()
    
    # 7단계: Docker 네트워크 존재 확인
    print("\n7️⃣ Docker 네트워크 존재 확인 중...")
    network_exists = ensure_network_exists()
    
    # 8단계: Docker 볼륨 존재 확인
    print("\n8️⃣ Docker 볼륨 존재 확인 중...")
    volume_results = ensure_volumes_exist()
    
    # 9단계: 서비스 접근성 확인
    print("\n9️⃣ 서비스 접근성 확인 중...")
    accessibility_results = ensure_services_accessible()
    
    # 10단계: 결과 요약
    print("\n" + "=" * 60)
    print(" 컨테이너 생성 확인 결과 요약")
    print("=" * 60)
    
    print("\n Docker 이미지 상태:")
    for image, exists in image_results.items():
        status_icon = "" if exists else ""
        print(f"  {status_icon} {image}: {'존재함' if exists else '존재하지 않음'}")
    
    print("\n�� Docker 컨테이너 상태:")
    for container, status in container_results.items():
        if status == "running":
            status_icon = ""
        elif status == "stopped":
            status_icon = "️"
        else:
            status_icon = ""
        print(f"  {status_icon} {container}: {status}")
    
    print(f"\n Docker 네트워크: {' 존재함' if network_exists else ' 존재하지 않음'}")
    
    print("\n Docker 볼륨 상태:")
    for volume, exists in volume_results.items():
        status_icon = "" if exists else ""
        print(f"  {status_icon} {volume}: {'존재함' if exists else '존재하지 않음'}")
    
    print("\n�� 서비스 접근성:")
    for service, status in accessibility_results.items():
        if status == "accessible":
            status_icon = ""
        elif status.startswith("http_"):
            status_icon = "️"
        else:
            status_icon = ""
        print(f"  {status_icon} {service}: {status}")
    
    # 성공/실패 판정
    all_images_exist = all(image_results.values()) if isinstance(image_results, dict) and "error" not in image_results else False
    all_containers_exist = all(status != "not_found" for status in container_results.values()) if isinstance(container_results, dict) and "error" not in container_results else False
    all_services_accessible = all(status == "accessible" for status in accessibility_results.values()) if isinstance(accessibility_results, dict) and "error" not in accessibility_results else False
    
    print("\n" + "=" * 60)
    if all_images_exist and all_containers_exist and network_exists and all_services_accessible:
        print(" 모든 컨테이너가 성공적으로 생성되었습니다!")
        return True
    else:
        print("️ 일부 컨테이너 생성에 문제가 있습니다.")
        return False


if __name__ == "__main__":
    function_split() 