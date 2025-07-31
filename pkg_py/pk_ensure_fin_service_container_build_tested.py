"""
D_PROJECT wrapper for fin_service 컨테이너 빌드 테스트
"""
import sys
from pathlib import Path

# 프로젝트 루트 경로 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pkg_py.functions_split.pk_ensure_fin_service_container_build_tested import function_split


def D_PROJECT():
    """
    WSL 환경에서 fin_service 컨테이너 빌드 테스트를 실행하는 wrapper 함수
    """
    print("🔧 D_PROJECT: fin_service 컨테이너 빌드 테스트 실행")
    print("=" * 60)

    try:
        # function_split 함수 실행
        result = function_split()

        if result:
            print("\n✅ D_PROJECT: 테스트 성공적으로 완료!")
            return True
        else:
            print("\n❌ D_PROJECT: 테스트 실패!")
            return False

    except Exception as e:
        print(f"\n❌ D_PROJECT: 예상치 못한 오류 발생: {e}")
        return False


if __name__ == "__main__":
    D_PROJECT()
