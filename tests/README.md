# Tests Directory

## 📁 파일 구조

### 유효한 테스트 파일들 (현재 사용 중)
- `test_base.py` - 테스트 프레임워크 기본 클래스들
- `test_runner.py` - 자동화된 테스트 실행기
- `test_simple_debug.py` - 기본 디버깅 테스트
- `test_pid_debug.py` - PID 디버깅 테스트
- `test_window_title_debug.py` - 윈도우 타이틀 디버깅 테스트
- `test_common_imports.py` - 공통 import 검증
- `comprehensive_tts_test.py` - TTS 통합 테스트

### 아카이브된 테스트 파일들 (더 이상 유효하지 않음)
- `#_test_*.py` - 50개 이상의 오래된/중복된 테스트 파일들

## 🧹 테스트 코드 정리 가이드라인

### 왜 이렇게 많은 테스트 파일이 있었나요?

**대부분의 테스트 파일들은 실제로 불필요했습니다:**

1. **개발 과정의 임시 코드들**
   - 디버깅 중 생성된 임시 파일들
   - 특정 문제 해결을 위한 일회성 테스트들
   - 마이그레이션 과정의 테스트 코드들

2. **중복된 기능 테스트들**
   - TTS 관련 20개 이상의 중복 테스트
   - 오디오 관련 10개 이상의 유사한 테스트
   - 같은 기능을 다른 방식으로 테스트한 코드들

3. **실제로 필요한 테스트는 소수**
   - 핵심 기능 검증용 테스트
   - 통합 테스트
   - 기본 import/환경 검증

### 🎯 테스트 작성 모범 사례

**새로운 테스트를 추가할 때 고려사항:**

1. **정말 필요한가?**
   - 기존 테스트로 충분한지 확인
   - 중복되지 않는 고유한 기능인지 검토

2. **테스트 범위**
   - 단위 테스트: 개별 함수/클래스 검증
   - 통합 테스트: 여러 컴포넌트 간 상호작용
   - E2E 테스트: 전체 워크플로우 검증

3. **테스트 명명 규칙**
   - `test_[기능명]_[시나리오].py`
   - 임시 테스트는 `temp_test_` 접두사 사용
   - 디버그용은 `debug_test_` 접두사 사용

4. **정기적인 정리**
   - 월 1회 테스트 파일 검토
   - 더 이상 유효하지 않은 테스트 아카이브
   - 중복 테스트 통합

### 📊 현재 테스트 상태

```
총 테스트 파일: 57개
├── 유효한 테스트: 7개 (12%)
├── 아카이브된 테스트: 50개 (88%)
└── 실제 사용 빈도: 낮음 (대부분 개발 중 임시 생성)
```

**결론**: 대부분의 테스트 코드는 개발 과정에서 생성된 임시 파일들이었으며, 실제로는 핵심 기능 검증을 위한 소수의 테스트만으로도 충분합니다.

## 🚀 사용법

### 1. 개별 테스트 실행

```bash
# dry_run 모드로 개별 테스트 실행
python test_simple_debug.py

# 실제 실행 모드로 테스트 실행 (test_base.py에서 dry_run=False로 변경)
python test_simple_debug.py
```

### 2. 자동화된 테스트 실행

```bash
# dry_run 모드로 모든 테스트 실행 (기본값)
python test_runner.py --dry-run

# 실제 실행 모드로 모든 테스트 실행
python test_runner.py --actual

# 특정 디렉토리의 테스트 실행
python test_runner.py --test-dir /path/to/tests

# 리포트 저장 없이 실행
python test_runner.py --dry-run --no-save-report
```

### 3. 테스트 리포트 확인

테스트 실행 후 자동으로 생성되는 리포트 파일들:
- `detailed_test_report_dry_run_YYYYMMDD_HHMMSS.txt` - 상세 리포트 (dry_run 모드)
- `detailed_test_report_actual_YYYYMMDD_HHMMSS.txt` - 상세 리포트 (실제 실행 모드)

## 🔍 Dry Run 기능

모든 테스트는 기본적으로 **dry_run 모드**로 실행됩니다:

### Dry Run 모드의 특징
- ✅ 실제 시스템에 영향을 주지 않음
- ✅ 빠른 실행 속도
- ✅ 안전한 테스트 환경
- ✅ 시뮬레이션된 결과 출력

### Dry Run에서 시뮬레이션되는 기능들
- `ensure_printed()` → 시뮬레이션된 출력
- `ensure_spoken_hybrid()` → 시뮬레이션된 TTS
- `time.sleep()` → 시뮬레이션된 대기
- Windows API 호출 → 시뮬레이션된 결과

## 📊 테스트 결과 해석

### 성공률 계산
```
성공률 = (통과한 테스트 수 / 총 테스트 수) × 100%
```

### 테스트 상태
- ✅ **PASS** - 테스트 성공
- ❌ **FAIL** - 테스트 실패
- ⚠️ **SKIP** - 테스트 건너뜀
- 🔄 **ERROR** - 테스트 실행 중 오류

## 🛠️ 새로운 테스트 추가하기

### 1. 기본 테스트 템플릿

```python
#!/usr/bin/env python3
"""
테스트 설명
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_base import DryRunMixin, run_test_with_dry_run

class YourTestClass(DryRunMixin):
    """테스트 클래스"""
    
    def __init__(self, dry_run: bool = True):
        super().__init__(dry_run)
    
    def test_your_function(self):
        """테스트 함수"""
        self.dry_run_print("테스트 시작", print_color="blue")
        
        if self.dry_run:
            self.dry_run_print("🔍 [DRY RUN] 시뮬레이션", print_color="blue")
        else:
            # 실제 테스트 로직
            pass
        
        self.dry_run_print("테스트 완료", print_color="green")

def test_your_function():
    """테스트 함수"""
    test_instance = YourTestClass(dry_run=True)
    test_instance.test_your_function()

if __name__ == "__main__":
    run_test_with_dry_run(test_your_function, "테스트 이름")
```

### 2. 파일명 규칙
- 테스트 파일: `test_*.py`
- 비활성화된 테스트: `#_test_*.py`

## 🔧 설정 및 커스터마이징

### DryRunMixin 클래스 사용법

```python
class YourTest(DryRunMixin):
    def __init__(self, dry_run: bool = True):
        super().__init__(dry_run)
    
    def your_test_method(self):
        # 출력 시뮬레이션
        self.dry_run_print("메시지", print_color="blue")
        
        # 함수 실행 시뮬레이션
        result = self.dry_run_execute(some_function, arg1, arg2)
        
        # 대기 시뮬레이션
        self.dry_run_sleep(2.0)
```

## 📝 주의사항

1. **기본적으로 dry_run 모드 사용**: 실제 시스템에 영향을 주지 않도록 기본값은 dry_run=True입니다.
2. **테스트 파일명**: `test_`로 시작하는 파일만 자동 테스트 실행기에 포함됩니다.
3. **Import 오류**: 일부 테스트에서 import 오류가 발생할 수 있지만, dry_run 모드에서는 안전하게 처리됩니다.
4. **리포트 저장**: 테스트 실행 후 자동으로 리포트가 저장됩니다.

## 🐛 문제 해결

### Import 오류
```
⚠️ 테스트 파일 로드 실패: test_file.py - import error
```
- dry_run 모드에서는 안전하게 처리됩니다.
- 실제 실행 시에는 해당 모듈이 올바르게 설치되어 있는지 확인하세요.

### 테스트 실패
```
❌ 테스트 실패: test_name - error message
```
- dry_run 모드에서는 시뮬레이션된 결과를 확인하세요.
- 실제 실행 시에는 상세한 오류 메시지를 확인하세요.

## 📞 지원

테스트 시스템에 문제가 있거나 개선 사항이 있으면 개발팀에 문의하세요. 