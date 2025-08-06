"""
Finance Investment Assistant 컨테이너 통합 테스트 실행 스크립트
"""
import sys
import inspect
from pathlib import Path

# 프로젝트 루트 경로 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pkg_py.pk_ensure_smart_person_ai_container_build_tested import ensure_smart_person_ai_container_builded_at_wsl


def main():
    """
    메인 실행 함수
    """
    # 현재 함수명을 동적으로 가져오기
    func_n = inspect.currentframe().f_code.co_name
    
    print("🚀 Finance Investment Assistant 컨테이너 통합 테스트 시작")
    print("=" * 60)
    
    # 컨테이너 통합 테스트 함수 실행
    success = ensure_smart_person_ai_container_builded_at_wsl()
    
    if success:
        print(f"\n🎉 {func_n} 함수가 성공적으로 완료되었습니다!")
        return 0
    else:
        print(f"\n💥 {func_n} 함수 실행 중 오류가 발생했습니다.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code) 