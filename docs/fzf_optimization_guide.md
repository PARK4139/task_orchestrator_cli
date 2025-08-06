# fzf 최적화 기능 가이드

## 개요

`ensure_pk_system_started()` 함수의 fzf 기능을 최적화하여 다음과 같은 기능들을 제공합니다:

1. **점진적 배치 로딩**: 파일을 50개씩 배치로 나누어 fzf에 실시간 공급
2. **비동기 처리**: 파일 스캔과 UI 렌더링을 동시에 처리
3. **스마트 적응형 로딩**: 파일 수에 따라 자동으로 최적화 방식 선택

## 최적화 모드

### 1. Traditional (기존) 모드
- 기존 `ensure_pk_system_started()` 함수와 동일한 동작
- 모든 파일을 한 번에 로딩
- 안정적이고 검증된 방식

### 2. Optimized (비동기 최적화) 모드
- 비동기 처리로 UI 블로킹 방지
- 스마트 적응형 로딩 (파일 수 ≥ 100개일 때 점진적 로딩)
- 50개씩 배치로 점진적 로딩
- 백그라운드에서 추가 배치 로딩

### 3. Progressive (점진적 로딩) 모드
- 실제 fzf reload 기능 활용
- 즉시 UI 표시 후 점진적 배치 로딩
- Ctrl+N: 다음 배치, Ctrl+P: 이전 배치
- 가장 진보된 최적화 방식

### 4. Auto (자동 선택) 모드
- 사용 가능한 최고 수준의 최적화 자동 선택
- Progressive → Optimized → Traditional 순서로 선택

## 사용법

### 기본 사용법

```python
from pkg_py.functions_split.ensure_pk_system_started_macro import ensure_pk_system_started_macro

# 자동 최적화 모드 (권장)
ensure_pk_system_started_macro(optimization_mode="auto")

# 특정 모드 지정
ensure_pk_system_started_macro(optimization_mode="progressive")
ensure_pk_system_started_macro(optimization_mode="optimized")
ensure_pk_system_started_macro(optimization_mode="traditional")
```

### 편의 함수들

```python
from pkg_py.functions_split.ensure_pk_system_started_macro import (
    ensure_pk_system_started_as_fallback,
    ensure_pk_system_started_with_progressive,
    ensure_pk_system_started_with_optimized,
    ensure_pk_system_started_with_traditional
)

# 자동 선택
ensure_pk_system_started_as_fallback()

# 특정 모드
ensure_pk_system_started_with_progressive()
ensure_pk_system_started_with_optimized()
ensure_pk_system_started_with_traditional()
```

### 사용 가능한 모드 확인

```python
from pkg_py.functions_split.ensure_pk_system_started_macro import (
    get_available_optimization_modes,
    print_optimization_info
)

# 사용 가능한 모드 목록
modes = get_available_optimization_modes()
print(f"사용 가능한 모드: {modes}")

# 최적화 정보 출력
print_optimization_info()
```

## 성능 특징

### 파일 수별 최적화 동작

| 파일 수 | 동작 방식 | 설명 |
|---------|-----------|------|
| < 100개 | 기존 방식 | 모든 파일을 한 번에 로딩 |
| ≥ 100개 | 점진적 로딩 | 50개씩 배치로 점진적 로딩 |

### 성능 개선 효과

1. **UI 응답성 향상**: 즉시 UI 표시로 사용자 경험 개선
2. **메모리 사용량 최적화**: 배치 단위 로딩으로 메모리 효율성 증대
3. **대용량 파일 목록 처리**: 수백 개 파일도 부드럽게 처리
4. **비동기 처리**: 백그라운드 로딩으로 UI 블로킹 방지

## 기술적 세부사항

### 점진적 배치 로딩

```python
class ProgressiveFzfOptimizer:
    def __init__(self, file_list, batch_size=50):
        self.batch_size = batch_size  # 기본 50개씩 배치
        self.total_files = len(file_list)
    
    def should_use_progressive_loading(self):
        return self.total_files >= 100  # 100개 이상일 때 활성화
    
    def get_initial_batch(self):
        return self.display_names[:self.batch_size]  # 첫 50개
    
    def get_next_batch(self):
        # 다음 50개 배치 반환
        start = (self.current_batch + 1) * self.batch_size
        end = min(start + self.batch_size, self.total_files)
        return self.display_names[start:end]
```

### 비동기 처리

```python
class AsyncFzfProcessor:
    async def prepare_fzf_data_async(self):
        """비동기로 fzf 데이터 준비"""
        def prepare_data():
            return "\n".join(display_names)
        
        with ThreadPoolExecutor() as executor:
            return await loop.run_in_executor(executor, prepare_data)
```

### 스마트 적응형 로딩

```python
def should_use_progressive_loading(self):
    """파일 수에 따라 점진적 로딩 여부 결정"""
    return self.total_files >= 100  # 임계값: 100개
```

## 테스트

### 테스트 실행

```bash
# 테스트 스크립트 실행
python tests/test_fzf_optimization.py
```

### 테스트 항목

1. **최적화 모드 테스트**: 모든 모드의 정상 동작 확인
2. **점진적 로딩 테스트**: 배치 로딩 기능 검증
3. **비동기 최적화 테스트**: 비동기 처리 기능 검증
4. **성능 비교 테스트**: 기존 vs 최적화 성능 비교

## 문제 해결

### 일반적인 문제들

1. **Import 오류**
   ```
   ❌ 최적화된 버전을 찾을 수 없습니다.
   ```
   - 해결: 필요한 모듈이 올바르게 설치되었는지 확인

2. **fzf 실행 오류**
   ```
   ❌ fzf를 찾을 수 없습니다. 자동완성 모드를 사용합니다.
   ```
   - 해결: fzf가 시스템에 설치되어 있는지 확인

3. **성능 문제**
   - 파일 수가 적은 경우 (< 100개): 기존 방식이 더 빠를 수 있음
   - 대용량 파일 목록: 점진적 로딩 모드 권장

### 디버깅

```python
# 디버그 정보 출력
from pkg_py.functions_split.ensure_pk_system_started_macro import print_optimization_info
print_optimization_info()

# 사용 가능한 모드 확인
from pkg_py.functions_split.ensure_pk_system_started_macro import get_available_optimization_modes
modes = get_available_optimization_modes()
print(f"Available modes: {modes}")
```

## 마이그레이션 가이드

### 기존 코드에서 최적화 버전으로 전환

**기존 코드:**
```python
from pkg_py.functions_split.ensure_pk_system_started import ensure_pk_system_started

# 기존 방식
ensure_pk_system_started()
```

**최적화된 코드:**
```python
from pkg_py.functions_split.ensure_pk_system_started_macro import ensure_pk_system_started_macro

# 자동 최적화 (권장)
ensure_pk_system_started_macro(optimization_mode="auto")

# 또는 기존과 동일한 동작
ensure_pk_system_started_macro(optimization_mode="traditional")
```

## 향후 계획

1. **더 정교한 적응형 로딩**: 시스템 성능에 따른 동적 임계값 조정
2. **캐싱 기능**: 자주 사용되는 파일 목록 캐싱
3. **사용자 설정**: 개인별 최적화 설정 저장
4. **성능 모니터링**: 실시간 성능 지표 수집

## 라이선스

이 최적화 기능은 기존 프로젝트와 동일한 라이선스를 따릅니다. 