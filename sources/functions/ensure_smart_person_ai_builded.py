"""
smart_person_ai 빌드 테스트 함수
"""
import subprocess
import os
import sys
import time
import json
import platform
from typing import Dict, List, Tuple, Optional
from pathlib import Path


def functions():
    """
    smart_person_ai 빌드 테스트를 실행하는 메인 함수
    """
    
    # 0️⃣ 플랫폼 체크
    if platform.system() != "Windows":
        # WSL / Linux 분기: 로컬에서 직접 Docker 명령 실행
        try:
            project_root = Path(__file__).resolve().parents[2]
            project_path = project_root / "pkg_finance_invest_assist"
            deploy_path = project_path / "deployment"

            print(f" Linux 환경 감지 – {platform.system()} / {platform.release()}")
            print(f" 프로젝트 경로: {project_path}")

            # .env 준비
            env_example = project_path / "env.example"
            env_file = project_path / ".env"
            if env_example.exists() and not env_file.exists():
                subprocess.run(["cp", str(env_example), str(env_file)], check=True)
                print(".env 파일 생성")

            # 필수 디렉토리 준비
            (project_path / "logs").mkdir(exist_ok=True)
            (deploy_path / "ssl").mkdir(parents=True, exist_ok=True)

            # Docker Compose 빌드 및 기동
            subprocess.run(["docker", "compose", "build"], cwd=str(deploy_path), check=True)
            subprocess.run(["docker", "compose", "up", "-d"], cwd=str(deploy_path), check=True)

            print("서비스 기동 대기 (15s)…")
            time.sleep(15)

            # 간단 헬스체크
            import requests
            try:
                r = requests.get("http://localhost:8000/health", timeout=10)
                ok = r.status_code == 200
            except Exception:
                ok = False

            # 종료 정리
            subprocess.run(["docker", "compose", "down"], cwd=str(deploy_path), check=True)

            if ok:
                print("빌드 + 헬스체크 성공")
                return True
            else:
                print("헬스체크 실패")
                return False

        except subprocess.CalledProcessError as e:
            print(f" Docker 단계 실패: {e}")
            return False
        except Exception as e:
            print(f" 예상치 못한 오류: {e}")
            return False

    # ---- 이하 Windows + WSL 원래 로직 ----
    def ensure_windows_environment_detected() -> bool:
        """Windows 환경 감지"""
        if platform.system() != "Windows":
            print("이 테스트는 Windows 환경에서만 실행 가능합니다.")
            return False
        print("Windows 환경 감지됨")
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
                print("WSL 환경 확인됨")
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
    
    def ensure_docker_compose_enabled() -> bool:
        """Docker Compose 설치 확인"""
        try:
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", "docker-compose --version"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=10
            )
            if result.returncode == 0:
                print(f" Docker Compose 설치 확인: {result.stdout.strip()}")
                return True
            else:
                print(f" Docker Compose 설치 확인 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f" Docker Compose 설치 확인 실패: {e}")
            return False
    
    def ensure_project_directory_accessed() -> bool:
        """프로젝트 디렉토리 접근 확인"""
        try:
            # 현재 사용자 경로로 수정
            user_path = os.path.expanduser("~")
            project_path = f"/mnt/c/Users/{os.path.basename(user_path)}/Downloads/task_orchestrator_cli/pkg_finance_invest_assist"
            
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
    
    def ensure_environment_setup() -> bool:
        """환경 설정"""
        try:
            user_path = os.path.expanduser("~")
            project_path = f"/mnt/c/Users/{os.path.basename(user_path)}/Downloads/task_orchestrator_cli/pkg_finance_invest_assist"
            
            # .env 파일 복사
            result1 = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                 f"cd {project_path} && cp env.example .env"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=10
            )
            
            # 필요한 디렉토리 생성
            result2 = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                 f"cd {project_path} && mkdir -p logs deployment/ssl"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=10
            )
            
            if result1.returncode == 0 and result2.returncode == 0:
                print("환경 설정 완료")
                return True
            else:
                print(f" 환경 설정 실패: {result1.stderr} {result2.stderr}")
                return False
        except Exception as e:
            print(f" 환경 설정 실패: {e}")
            return False
    
    def ensure_docker_containers_built() -> bool:
        """Docker 컨테이너 빌드"""
        try:
            user_path = os.path.expanduser("~")
            project_path = f"/mnt/c/Users/{os.path.basename(user_path)}/Downloads/task_orchestrator_cli/pkg_finance_invest_assist"
            
            print("Docker 컨테이너 빌드 시작...")
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                 f"cd {project_path}/deployment && docker-compose build --no-cache"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=300  # 5분 타임아웃
            )
            
            if result.returncode == 0:
                print("Docker 컨테이너 빌드 완료")
                return True
            else:
                print(f" Docker 컨테이너 빌드 실패: {result.stderr}")
                return False
        except subprocess.TimeoutExpired:
            print("Docker 컨테이너 빌드 시간 초과")
            return False
        except Exception as e:
            print(f" Docker 컨테이너 빌드 실패: {e}")
            return False
    
    def ensure_containers_started() -> bool:
        """컨테이너 시작"""
        try:
            user_path = os.path.expanduser("~")
            project_path = f"/mnt/c/Users/{os.path.basename(user_path)}/Downloads/task_orchestrator_cli/pkg_finance_invest_assist"
            
            print("컨테이너 시작 중...")
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                 f"cd {project_path}/deployment && docker-compose up -d"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=120  # 2분 타임아웃
            )
            
            if result.returncode == 0:
                print("컨테이너 시작 완료")
                return True
            else:
                print(f" 컨테이너 시작 실패: {result.stderr}")
                return False
        except subprocess.TimeoutExpired:
            print("컨테이너 시작 시간 초과")
            return False
        except Exception as e:
            print(f" 컨테이너 시작 실패: {e}")
            return False
    
    def ensure_containers_status_checked() -> Dict[str, str]:
        """컨테이너 상태 확인"""
        try:
            user_path = os.path.expanduser("~")
            project_path = f"/mnt/c/Users/{os.path.basename(user_path)}/Downloads/task_orchestrator_cli/pkg_finance_invest_assist"
            
            print("�� 컨테이너 상태 확인 중...")
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                 f"cd {project_path}/deployment && docker-compose ps"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=30
            )
            
            if result.returncode == 0:
                print("컨테이너 상태 확인 완료")
                return {"status": "success", "output": result.stdout}
            else:
                print(f" 컨테이너 상태 확인 실패: {result.stderr}")
                return {"status": "error", "output": result.stderr}
        except Exception as e:
            print(f" 컨테이너 상태 확인 실패: {e}")
            return {"status": "error", "output": str(e)}
    
    def ensure_services_health_checked() -> Dict[str, str]:
        """서비스 헬스체크"""
        try:
            print("서비스 헬스체크 중...")
            
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
                        ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                         f"curl -s -o /dev/null -w '%{{http_code}}' http://localhost:{port}/health"],
                        capture_output=True,
                        text=True,
                        encoding='utf-8',
                        errors='ignore',
                        timeout=10
                    )
                    
                    if result.returncode == 0 and result.stdout.strip() == "200":
                        health_results[service_name] = "healthy"
                        print(f" {service_name}: healthy")
                    else:
                        health_results[service_name] = "unhealthy"
                        print(f" {service_name}: unhealthy")
                except Exception as e:
                    health_results[service_name] = f"error: {str(e)}"
                    print(f"️ {service_name}: error - {e}")
            
            return health_results
        except Exception as e:
            print(f" 서비스 헬스체크 실패: {e}")
            return {"error": str(e)}
    
    def ensure_containers_cleaned_up() -> bool:
        """컨테이너 정리"""
        try:
            user_path = os.path.expanduser("~")
            project_path = f"/mnt/c/Users/{os.path.basename(user_path)}/Downloads/task_orchestrator_cli/pkg_finance_invest_assist"
            
            print("컨테이너 정리 중...")
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu-24.04", "-e", "bash", "-c", 
                 f"cd {project_path}/deployment && docker-compose down"],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=60
            )
            
            if result.returncode == 0:
                print("컨테이너 정리 완료")
                return True
            else:
                print(f" 컨테이너 정리 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f" 컨테이너 정리 실패: {e}")
            return False
    
    # 메인 실행 로직
    print("�� smart_person_ai 빌드 테스트 시작")
    print("=" * 60)
    
    # 0단계: Windows 환경 감지
    print("\n0️⃣ Windows 환경 감지 중...")
    if not ensure_windows_environment_detected():
        print("Windows 환경 감지 실패. 테스트를 중단합니다.")
        return False
    
    # 1단계: WSL 환경 확인
    print("\n1️⃣ WSL 환경 확인 중...")
    if not ensure_wsl_environment_checked():
        print("WSL 환경 확인 실패. 테스트를 중단합니다.")
        return False
    
    # 2단계: Docker 설치 확인
    print("\n2️⃣ Docker 설치 확인 중...")
    if not ensure_docker_enabled():
        print("Docker 설치 확인 실패. 테스트를 중단합니다.")
        return False
    
    # 3단계: Docker Compose 설치 확인
    print("\n3️⃣ Docker Compose 설치 확인 중...")
    if not ensure_docker_compose_enabled():
        print("Docker Compose 설치 확인 실패. 테스트를 중단합니다.")
        return False
    
    # 4단계: 프로젝트 디렉토리 접근 확인
    print("\n4️⃣ 프로젝트 디렉토리 접근 확인 중...")
    if not ensure_project_directory_accessed():
        print("프로젝트 디렉토리 접근 실패. 테스트를 중단합니다.")
        return False
    
    # 5단계: 환경 설정
    print("\n5️⃣ 환경 설정 중...")
    if not ensure_environment_setup():
        print("환경 설정 실패. 테스트를 중단합니다.")
        return False
    
    # 6단계: Docker 컨테이너 빌드
    print("\n6️⃣ Docker 컨테이너 빌드 중...")
    if not ensure_docker_containers_built():
        print("Docker 컨테이너 빌드 실패. 테스트를 중단합니다.")
        return False
    
    # 7단계: 컨테이너 시작
    print("\n7️⃣ 컨테이너 시작 중...")
    if not ensure_containers_started():
        print("컨테이너 시작 실패. 테스트를 중단합니다.")
        return False
    
    # 8단계: 컨테이너 상태 확인
    print("\n8️⃣ 컨테이너 상태 확인 중...")
    status_result = ensure_containers_status_checked()
    
    # 9단계: 서비스 헬스체크
    print("\n9️⃣ 서비스 헬스체크 중...")
    health_results = ensure_services_health_checked()
    
    # 10단계: 결과 요약
    print("\n" + "=" * 60)
    print("테스트 결과 요약")
    print("=" * 60)
    
    print("\n 컨테이너 상태:")
    if status_result.get("status") == "success":
        print(status_result.get("output", "상태 확인 실패"))
    else:
        print(f" 상태 확인 실패: {status_result.get('output', '알 수 없는 오류')}")
    
    print("\n�� 서비스 헬스체크 결과:")
    for service, status in health_results.items():
        if status == "healthy":
            status_icon = ""
        elif status == "unhealthy":
            status_icon = ""
        else:
            status_icon = "️"
        print(f"  {status_icon} {service}: {status}")
    
    # 11단계: 컨테이너 정리
    print("\n�� 컨테이너 정리 중...")
    ensure_containers_cleaned_up()
    
    print("\n�� smart_person_ai 빌드 테스트 완료!")
    return True


if __name__ == "__main__":
    functions() 