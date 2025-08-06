"""
D_PROJECT wrapper for paramiko를 사용해서 WSL에 Docker 설치
"""
import sys
from pathlib import Path

# 프로젝트 루트 경로 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pkg_py.functions_split.ensure_docker_installed_in_wsl_via_paramiko import ensure_docker_installed_in_wsl_via_paramiko


def ensure_docker_installed_in_wsl_via_paramiko():
    print("paramiko를 사용해서 WSL에 Docker 설치 루틴 실행")
    print("=" * 60)

    try:
        # ensure_docker_installed_in_wsl_via_paramiko 함수 실행
        result = ensure_docker_installed_in_wsl_via_paramiko()

        if result:
            print("\n✅ D_PROJECT: Docker 설치 성공적으로 완료!")
            return True
        else:
            print("\n❌ D_PROJECT: Docker 설치 실패!")
            return False

    except Exception as e:
        print(f"\n❌ D_PROJECT: Docker 설치 중 오류 발생: {str(e)}")
        return False


if __name__ == "__main__":
    ensure_docker_installed_in_wsl_via_paramiko() 


    