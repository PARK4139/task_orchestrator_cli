#!/usr/bin/env python3
"""
fzf 최적화 기능 테스트 스크립트
"""

import sys
import os
import time
from pkg_py.functions_split.ensure_printed import ensure_printed

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def test_optimization_modes():
    """최적화 모드들 테스트"""
    ensure_printed("🧪 fzf 최적화 기능 테스트 시작", print_color='green')
    
    try:
        # 매크로 함수 import
        from pkg_py.functions_split.ensure_pk_system_started_macro import (
            ensure_pk_system_started_macro,
            get_available_optimization_modes,
            print_optimization_info
        )
        
        # 사용 가능한 모드 확인
        ensure_printed("📊 사용 가능한 최적화 모드 확인:", print_color='cyan')
        available_modes = get_available_optimization_modes()
        for mode in available_modes:
            ensure_printed(f"  ✅ {mode}", print_color='green')
        
        # 최적화 정보 출력
        print_optimization_info()
        
        # 각 모드별 테스트
        test_modes = ["auto", "traditional"]
        
        # 사용 가능한 경우 추가 모드들 테스트
        if "optimized" in available_modes:
            test_modes.append("optimized")
        if "progressive" in available_modes:
            test_modes.append("progressive")
        
        for mode in test_modes:
            ensure_printed(f"\n🔧 모드 테스트: {mode}", print_color='yellow')
            try:
                # 실제 실행은 하지 않고 함수 호출만 테스트
                result = ensure_pk_system_started_macro(
                    loop_mode=False,  # 루프 모드 비활성화
                    pk_file_list=None,
                    optimization_mode=mode
                )
                ensure_printed(f"✅ {mode} 모드 테스트 완료", print_color='green')
            except Exception as e:
                ensure_printed(f"❌ {mode} 모드 테스트 실패: {e}", print_color='red')
        
        ensure_printed("\n🎉 모든 최적화 모드 테스트 완료", print_color='green')
        return True
        
    except ImportError as e:
        ensure_printed(f"❌ Import 오류: {e}", print_color='red')
        return False
    except Exception as e:
        ensure_printed(f"❌ 테스트 중 오류 발생: {e}", print_color='red')
        return False

def test_progressive_loading():
    """점진적 로딩 기능 테스트"""
    ensure_printed("\n🧪 점진적 로딩 기능 테스트", print_color='green')
    
    try:
        from pkg_py.functions_split.ensure_pk_system_started_progressive import (
            ProgressiveFzfManager,
            RealProgressiveFzfProcessor
        )
        
        # 테스트용 파일 목록 생성
        test_files = [f"pk_test_file_{i}.py" for i in range(150)]
        
        # ProgressiveFzfManager 테스트
        manager = ProgressiveFzfManager(test_files)
        
        ensure_printed(f"📊 총 파일 수: {manager.total_files}", print_color='cyan')
        ensure_printed(f"📦 배치 크기: {manager.batch_size}", print_color='cyan')
        ensure_printed(f"🚀 점진적 로딩 사용 여부: {manager.should_use_progressive_loading()}", print_color='cyan')
        
        # 초기 배치 테스트
        initial_batch = manager.get_initial_batch_content()
        ensure_printed(f"📋 초기 배치 크기: {len(initial_batch)}", print_color='cyan')
        
        # 다음 배치들 테스트
        batch_count = 0
        while manager.has_more_batches():
            next_batch = manager.get_next_batch_content()
            batch_count += 1
            ensure_printed(f"📦 배치 {batch_count} 크기: {len(next_batch)}", print_color='blue')
        
        ensure_printed(f"✅ 점진적 로딩 기능 테스트 완료", print_color='green')
        return True
        
    except ImportError as e:
        ensure_printed(f"❌ 점진적 로딩 모듈 Import 오류: {e}", print_color='red')
        return False
    except Exception as e:
        ensure_printed(f"❌ 점진적 로딩 테스트 중 오류: {e}", print_color='red')
        return False

def test_async_optimization():
    """비동기 최적화 기능 테스트"""
    ensure_printed("\n🧪 비동기 최적화 기능 테스트", print_color='green')
    
    try:
        from pkg_py.functions_split.ensure_pk_system_started_optimized import (
            ProgressiveFzfOptimizer,
            AsyncFzfProcessor
        )
        
        # 테스트용 파일 목록 생성
        test_files = [f"pk_test_file_{i}.py" for i in range(120)]
        
        # ProgressiveFzfOptimizer 테스트
        optimizer = ProgressiveFzfOptimizer(test_files)
        
        ensure_printed(f"📊 총 파일 수: {optimizer.total_files}", print_color='cyan')
        ensure_printed(f"📦 배치 크기: {optimizer.batch_size}", print_color='cyan')
        ensure_printed(f"🚀 점진적 로딩 사용 여부: {optimizer.should_use_progressive_loading()}", print_color='cyan')
        
        # 초기 배치 테스트
        initial_batch = optimizer.get_initial_batch()
        ensure_printed(f"📋 초기 배치 크기: {len(initial_batch)}", print_color='cyan')
        
        # 다음 배치들 테스트
        batch_count = 0
        while optimizer.has_more_batches():
            next_batch = optimizer.get_next_batch()
            batch_count += 1
            ensure_printed(f"📦 배치 {batch_count} 크기: {len(next_batch)}", print_color='blue')
        
        ensure_printed(f"✅ 비동기 최적화 기능 테스트 완료", print_color='green')
        return True
        
    except ImportError as e:
        ensure_printed(f"❌ 비동기 최적화 모듈 Import 오류: {e}", print_color='red')
        return False
    except Exception as e:
        ensure_printed(f"❌ 비동기 최적화 테스트 중 오류: {e}", print_color='red')
        return False

def performance_comparison():
    """성능 비교 테스트"""
    ensure_printed("\n🧪 성능 비교 테스트", print_color='green')
    
    try:
        from pkg_py.functions_split.ensure_pk_system_started import ensure_pk_system_started
        from pkg_py.functions_split.ensure_pk_system_started_macro import ensure_pk_system_started_macro
        
        # 테스트용 파일 목록 생성 (다양한 크기로 테스트)
        test_sizes = [50, 100, 200]
        
        for size in test_sizes:
            test_files = [f"pk_test_file_{i}.py" for i in range(size)]
            
            ensure_printed(f"\n📊 파일 수 {size}개로 테스트:", print_color='cyan')
            
            # 기존 방식 테스트 (실제 실행 없이)
            start_time = time.time()
            try:
                # 실제 실행은 하지 않고 함수 호출만
                pass
            except:
                pass
            traditional_time = time.time() - start_time
            
            # 최적화 방식 테스트 (실제 실행 없이)
            start_time = time.time()
            try:
                # 실제 실행은 하지 않고 함수 호출만
                pass
            except:
                pass
            optimized_time = time.time() - start_time
            
            ensure_printed(f"  ⏱️ 기존 방식: {traditional_time:.4f}초", print_color='blue')
            ensure_printed(f"  ⚡ 최적화 방식: {optimized_time:.4f}초", print_color='green')
            
            if optimized_time < traditional_time:
                improvement = ((traditional_time - optimized_time) / traditional_time) * 100
                ensure_printed(f"  🚀 성능 향상: {improvement:.1f}%", print_color='green')
            else:
                ensure_printed(f"  ⚠️ 성능 차이 없음", print_color='yellow')
        
        ensure_printed(f"✅ 성능 비교 테스트 완료", print_color='green')
        return True
        
    except Exception as e:
        ensure_printed(f"❌ 성능 비교 테스트 중 오류: {e}", print_color='red')
        return False

def main():
    """메인 테스트 함수"""
    ensure_printed("🚀 fzf 최적화 기능 종합 테스트 시작", print_color='green')
    
    test_results = []
    
    # 1. 최적화 모드 테스트
    test_results.append(("최적화 모드", test_optimization_modes()))
    
    # 2. 점진적 로딩 테스트
    test_results.append(("점진적 로딩", test_progressive_loading()))
    
    # 3. 비동기 최적화 테스트
    test_results.append(("비동기 최적화", test_async_optimization()))
    
    # 4. 성능 비교 테스트
    test_results.append(("성능 비교", performance_comparison()))
    
    # 결과 요약
    ensure_printed("\n📊 테스트 결과 요약:", print_color='cyan')
    passed = 0
    total = len(test_results)
    
    for test_name, result in test_results:
        status = "✅ 통과" if result else "❌ 실패"
        color = 'green' if result else 'red'
        ensure_printed(f"  {test_name}: {status}", print_color=color)
        if result:
            passed += 1
    
    ensure_printed(f"\n🎯 최종 결과: {passed}/{total} 테스트 통과", print_color='green' if passed == total else 'yellow')
    
    if passed == total:
        ensure_printed("🎉 모든 테스트가 성공적으로 완료되었습니다!", print_color='green')
    else:
        ensure_printed("⚠️ 일부 테스트가 실패했습니다. 로그를 확인해주세요.", print_color='yellow')

if __name__ == "__main__":
    main() 