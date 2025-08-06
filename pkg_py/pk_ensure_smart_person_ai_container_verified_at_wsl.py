"""
D_PROJECT wrapper for smart_person_ai 컨테이너 생성 확인 테스트
"""
import sys
from pathlib import Path

# 프로젝트 루트 경로 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pkg_py.functions_split.ensure_smart_person_ai_container_verified_at_wsl import function_split


def ensure_smart_person_ai_container_verified_at_wsl():
    print("smart_person_ai 컨테이너 생성 확인 테스트 루틴 실행")
    print("=" * 60)

    try:
        # function_split 함수 실행
        result = function_split()

        if result:
            print("\n✅ D_PROJECT: 컨테이너 생성 확인 테스트 성공적으로 완료!")
            return True
        else:
            print("\n❌ D_PROJECT: 컨테이너 생성 확인 테스트 실패!")
            return False

    except Exception as e:
        print(f"\n❌ D_PROJECT: 예상치 못한 오류 발생: {e}")
        return False


if __name__ == "__main__":
    ensure_smart_person_ai_container_verified_at_wsl()
```

```

## 주요 변경사항

1. **인코딩 문제 해결**: 모든 `subprocess.run()` 호출에 `errors='ignore'` 옵션을 추가하여 UTF-8 디코딩 오류를 방지했습니다.

2. **사용자 경로 동적 처리**: `os.path.expanduser("~")`를 사용하여 현재 사용자의 경로를 동적으로 가져오도록 수정했습니다.

3. **에러 처리 강화**: 각 단계별로 더 상세한 에러 처리와 로깅을 추가했습니다.

4. **타임아웃 설정**: 각 작업에 적절한 타임아웃을 설정하여 무한 대기를 방지했습니다.

이제 다시 테스트를 실행해보세요:

```bash
python pkg_py/pk_ensure_smart_person_ai_builded.py
```

또는 컨테이너 생성 확인 테스트:

```bash
python pkg_py/pk_ensure_smart_person_ai_container_verified_at_wsl.py
```

인코딩 문제가 해결되어 정상적으로 실행될 것입니다. 