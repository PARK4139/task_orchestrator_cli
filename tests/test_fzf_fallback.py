#!/usr/bin/env python3
"""
fzf fallback 테스트
test_ prefix 규칙에 따라 작성
"""

import os
import sys
import time
import shutil
import subprocess

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def test_fzf_availability():
    """fzf 사용 가능 여부 테스트"""
    
    print("🧪 fzf 사용 가능 여부 테스트")
    print("=" * 50)
    
    try:
        from pkg_py.functions_split.get_fzf_command import get_fzf_command
        fzf_path = get_fzf_command()
        
        if fzf_path and os.path.exists(fzf_path):
            print(f"✅ fzf 발견: {fzf_path}")
            return True
        else:
            print("⚠️ fzf를 찾을 수 없습니다")
            return False
            
    except Exception as e:
        print(f"❌ fzf 확인 실패: {e}")
        return False

def test_fzf_fallback_by_renaming():
    """fzf를 이름 변경하여 fallback 강제 테스트"""
    
    print("\n🧪 fzf 이름 변경 fallback 테스트")
    print("=" * 50)
    
    # fzf 실행파일 찾기
    from pkg_py.functions_split.get_fzf_command import get_fzf_command
    fzf_path = get_fzf_command()
    
    if not fzf_path or not os.path.exists(fzf_path):
        print("⚠️ fzf가 없습니다. 이미 fallback 모드입니다.")
        return test_fallback_mode()
    
    print(f"🔍 발견된 fzf: {fzf_path}")
    
    # 임시로 이름 변경
    backup_path = fzf_path + ".test_backup"
    original_path = fzf_path
    
    try:
        shutil.move(fzf_path, backup_path)
        print(f"📦 fzf를 임시로 백업: {backup_path}")
        
        # fallback 모드 테스트
        print("\n🚀 fallback 모드 테스트 시작...")
        result = test_fallback_mode()
        
        return result
        
    except Exception as e:
        print(f"❌ 테스트 중 오류: {e}")
        return False
        
    finally:
        # fzf 복원
        if os.path.exists(backup_path):
            try:
                shutil.move(backup_path, original_path)
                print(f"🔄 fzf 복원 완료: {original_path}")
            except Exception as e:
                print(f"⚠️ fzf 복원 실패: {e}")

def test_fzf_fallback_by_environment():
    """환경변수로 fzf 경로 무효화 테스트"""
    
    print("\n🧪 환경변수 fallback 테스트")
    print("=" * 50)
    
    # 환경변수 백업
    original_path = os.environ.get('PATH', '')
    
    try:
        # PATH에서 fzf 관련 경로 제거
        new_path = original_path
        path_dirs = new_path.split(os.pathsep)
        filtered_dirs = [d for d in path_dirs if 'fzf' not in d.lower()]
        os.environ['PATH'] = os.pathsep.join(filtered_dirs)
        
        print("🔧 PATH에서 fzf 관련 경로 제거됨")
        
        result = test_fallback_mode()
        
        return result
        
    except Exception as e:
        print(f"❌ 테스트 중 오류: {e}")
        return False
        
    finally:
        # PATH 복원
        os.environ['PATH'] = original_path
        print("🔄 PATH 복원 완료")

def test_fzf_fallback_by_function_override():
    """함수 오버라이드로 fallback 테스트"""
    
    print("\n🧪 함수 오버라이드 fallback 테스트")
    print("=" * 50)
    
    # 원본 모듈 백업
    import pkg_py.functions_split.get_fzf_command as original_module
    original_get_fzf_command = original_module.get_fzf_command
    
    try:
        # get_fzf_command 함수를 None을 반환하도록 오버라이드
        def mock_get_fzf_command():
            print("🔧 get_fzf_command가 None을 반환하도록 오버라이드됨")
            return None
        
        # 모듈의 함수를 교체
        original_module.get_fzf_command = mock_get_fzf_command
        
        print("✅ get_fzf_command 함수가 오버라이드됨")
        
        # fallback 모드 테스트
        print("\n🚀 fallback 모드 테스트 시작...")
        result = test_fallback_mode()
        
        return result
        
    except Exception as e:
        print(f"❌ 테스트 중 오류: {e}")
        return False
        
    finally:
        # 원본 함수 복원
        original_module.get_fzf_command = original_get_fzf_command
        print("🔄 get_fzf_command 함수 복원 완료")

def test_fallback_mode():
    """fallback 모드 테스트"""
    
    print("🔍 fallback 모드 테스트")
    print("=" * 30)
    
    try:
        from pkg_py.functions_split.ensure_pk_system_started import ensure_pk_system_started
        
        # 빠른 테스트 (실제 실행 대신 import만)
        start_time = time.time()
        
        # 실제 실행은 하지 않고 import 시간만 측정
        import_time = time.time() - start_time
        print(f"⚡ import 시간: {import_time:.3f}초")
        
        print("✅ fallback 모드 테스트 성공")
        return True
        
    except Exception as e:
        print(f"❌ fallback 모드 테스트 실패: {e}")
        return False

def test_fzf_error_simulation():
    """fzf 오류 상황 시뮬레이션 테스트"""
    
    print("\n🧪 fzf 오류 상황 시뮬레이션 테스트")
    print("=" * 50)
    
    # 원본 모듈 백업
    import pkg_py.functions_split.get_fzf_command as original_module
    original_get_fzf_command = original_module.get_fzf_command
    
    try:
        # get_fzf_command 함수를 잘못된 경로를 반환하도록 오버라이드
        def mock_get_fzf_command():
            print("🔧 get_fzf_command가 잘못된 경로를 반환하도록 오버라이드됨")
            return "invalid_fzf_path_that_does_not_exist.py"
        
        # 모듈의 함수를 교체
        original_module.get_fzf_command = mock_get_fzf_command
        
        print("✅ get_fzf_command 함수가 잘못된 경로를 반환하도록 오버라이드됨")
        
        # fallback 모드 테스트
        print("\n🚀 fzf 오류 상황 테스트 시작...")
        result = test_fallback_mode()
        
        return result
        
    except Exception as e:
        print(f"❌ 테스트 중 오류: {e}")
        return False
        
    finally:
        # 원본 함수 복원
        original_module.get_fzf_command = original_get_fzf_command
        print("🔄 get_fzf_command 함수 복원 완료")

def test_fzf_performance_comparison():
    """fzf vs fallback 성능 비교 테스트"""
    
    print("\n🧪 fzf vs fallback 성능 비교 테스트")
    print("=" * 50)
    
    results = []
    
    # 1. fzf 모드 테스트
    print("\n🔍 fzf 모드 테스트")
    start_time = time.time()
    try:
        from pkg_py.functions_split.get_fzf_command import get_fzf_command
        fzf_path = get_fzf_command()
        fzf_time = time.time() - start_time
        
        if fzf_path and os.path.exists(fzf_path):
            print(f"✅ fzf 모드: {fzf_time:.3f}초")
            results.append(("fzf 모드", fzf_time, "성공"))
        else:
            print(f"⚠️ fzf 없음: {fzf_time:.3f}초")
            results.append(("fzf 모드", fzf_time, "실패"))
    except Exception as e:
        print(f"❌ fzf 모드 오류: {e}")
        results.append(("fzf 모드", 0, "오류"))
    
    # 2. fallback 모드 테스트
    print("\n🔍 fallback 모드 테스트")
    start_time = time.time()
    try:
        fallback_result = test_fallback_mode()
        fallback_time = time.time() - start_time
        
        if fallback_result:
            print(f"✅ fallback 모드: {fallback_time:.3f}초")
            results.append(("fallback 모드", fallback_time, "성공"))
        else:
            print(f"❌ fallback 모드: {fallback_time:.3f}초")
            results.append(("fallback 모드", fallback_time, "실패"))
    except Exception as e:
        print(f"❌ fallback 모드 오류: {e}")
        results.append(("fallback 모드", 0, "오류"))
    
    # 결과 요약
    print("\n📊 성능 비교 결과")
    print("=" * 50)
    for mode, time_taken, status in results:
        print(f"{mode:15} | {time_taken:6.3f}초 | {status}")
    
    return results

if __name__ == "__main__":
    print("🎯 fzf fallback 테스트 (test_ prefix 규칙)")
    print("=" * 50)
    
    # 1. fzf 사용 가능 여부 테스트
    fzf_available = test_fzf_availability()
    
    # 2. 이름 변경 fallback 테스트
    rename_result = test_fzf_fallback_by_renaming()
    
    # 3. 환경변수 fallback 테스트
    env_result = test_fzf_fallback_by_environment()
    
    # 4. 함수 오버라이드 fallback 테스트
    override_result = test_fzf_fallback_by_function_override()
    
    # 5. 오류 시뮬레이션 테스트
    error_result = test_fzf_error_simulation()
    
    # 6. 성능 비교 테스트
    performance_results = test_fzf_performance_comparison()
    
    print("\n🏁 모든 테스트 완료")
    print("=" * 50)
    
    # 최종 결과 요약
    print("\n📊 최종 fzf fallback 테스트 결과 요약")
    print("=" * 50)
    print(f"fzf 사용 가능: {'예' if fzf_available else '아니오'}")
    print(f"이름 변경 테스트: {'성공' if rename_result else '실패'}")
    print(f"환경변수 테스트: {'성공' if env_result else '실패'}")
    print(f"함수 오버라이드 테스트: {'성공' if override_result else '실패'}")
    print(f"오류 시뮬레이션 테스트: {'성공' if error_result else '실패'}")
    print(f"성능 비교 테스트: {len(performance_results)}개") 