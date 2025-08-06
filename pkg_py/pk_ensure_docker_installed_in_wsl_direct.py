"""
D_PROJECT wrapper for WSL 내부에서 직접 Docker 설치
"""
import sys
import platform
from pathlib import Path

# 프로젝트 루트 경로 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pkg_py.functions_split.ensure_docker_installed_in_wsl_direct import ensure_docker_installed_in_wsl_direct


def pk_ensure_docker_installed_in_wsl_direct():
    print("WSL 내부에서 직접 Docker 설치 루틴 실행")
    print("=" * 60)

    # Windows 환경 확인
    if platform.system() != "Windows":
        print("❌ 이 루틴은 Windows 환경에서만 실행 가능합니다.")
        print("💡 Windows 환경에서 WSL을 사용하여 Docker를 설치하세요.")
        return False

    print("💡 Windows 환경 감지됨")
    print(" WSL 환경에서 Docker 설치를 시작합니다.")
    print("=" * 50)

    try:
        # ensure_docker_installed_in_wsl_direct 함수 실행
        result = ensure_docker_installed_in_wsl_direct()

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
    pk_ensure_docker_installed_in_wsl_direct() 