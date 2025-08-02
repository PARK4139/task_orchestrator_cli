"""
fin_service 컨테이너 빌드 테스트 실행 스크립트
"""
import sys
import os
from pathlib import Path

# 프로젝트 루트 경로 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pkg_py.workspace.pk_ensure_fin_service_container_build_tested import D_PROJECT


def main():
    """
    메인 실행 함수
    """
    print("🚀 fin_service 컨테이너 빌드 테스트 시작")
    print("=" * 60)
    
    # D_PROJECT 함수 실행
    success = D_PROJECT()
    
    if success:
        print("\n🎉 모든 테스트가 성공적으로 완료되었습니다!")
        return 0
    else:
        print("\n💥 테스트 중 오류가 발생했습니다.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code) 