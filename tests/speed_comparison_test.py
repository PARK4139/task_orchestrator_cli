#!/usr/bin/env python3
"""
속도 비교 테스트 스크립트 (업데이트된 버전)
"""

import sys
import os
import time
import statistics
from pkg_py.functions_split.ensure_printed import ensure_printed

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def test_lightning():
    """초경량 버전 테스트 (가장 빠름)"""
    try:
        from pkg_py.functions_split.ensure_pk_system_started_lightning import ensure_pk_system_started_lightning
        
        start_time = time.time()
        
        # 실제 실행 없이 함수 호출만 테스트 (loop_mode=False로 설정)
        result = ensure_pk_system_started_lightning(loop_mode=False)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        return execution_time, result
        
    except Exception as e:
        ensure_printed(f"❌ 초경량 버전 테스트 실패: {e}", print_color='red')
        return None, None

def test_ultra_fast():
    """초고속 버전 테스트"""
    try:
        from pkg_py.functions_split.ensure_pk_system_started_ultra_fast import ensure_pk_system_started_ultra_fast
        
        start_time = time.time()
        
        # 실제 실행 없이 함수 호출만 테스트 (loop_mode=False로 설정)
        result = ensure_pk_system_started_ultra_fast(loop_mode=False)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        return execution_time, result
        
    except Exception as e:
        ensure_printed(f"❌ 초고속 버전 테스트 실패: {e}", print_color='red')
        return None, None

def test_direct_optimized():
    """직접 최적화 함수 테스트"""
    try:
        from pkg_py.functions_split.ensure_pk_system_started_optimized import ensure_pk_system_started_optimized
        
        start_time = time.time()
        
        # 실제 실행 없이 함수 호출만 테스트 (loop_mode=False로 설정)
        result = ensure_pk_system_started_optimized(loop_mode=False)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        return execution_time, result
        
    except Exception as e:
        ensure_printed(f"❌ 직접 최적화 함수 테스트 실패: {e}", print_color='red')
        return None, None

def test_macro_optimized():
    """매크로를 통한 최적화 함수 테스트"""
    try:
        from pkg_py.functions_split.ensure_pk_system_started_macro import ensure_pk_system_started_with_optimized
        
        start_time = time.time()
        
        # 실제 실행 없이 함수 호출만 테스트 (loop_mode=False로 설정)
        result = ensure_pk_system_started_with_optimized(loop_mode=False)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        return execution_time, result
        
    except Exception as e:
        ensure_printed(f"❌ 매크로 최적화 함수 테스트 실패: {e}", print_color='red')
        return None, None

def run_speed_comparison_test(iterations=5):
    """속도 비교 테스트 실행"""
    ensure_printed(f"🚀 속도 비교 테스트 시작 (총 {iterations}회)", print_color='green')
    
    lightning_times = []
    ultra_fast_times = []
    direct_times = []
    macro_times = []
    
    for i in range(iterations):
        ensure_printed(f"\n📊 테스트 {i+1}/{iterations}", print_color='cyan')
        
        # 초경량 버전 테스트 (가장 빠름)
        ensure_printed(f"⚡ 초경량 버전 테스트 중...", print_color='blue')
        lightning_time, lightning_result = test_lightning()
        
        if lightning_time is not None:
            lightning_times.append(lightning_time)
            ensure_printed(f"✅ 초경량 버전: {lightning_time:.4f}초", print_color='green')
        else:
            ensure_printed(f"❌ 초경량 버전 테스트 실패", print_color='red')
        
        # 초고속 버전 테스트
        ensure_printed(f"🚀 초고속 버전 테스트 중...", print_color='blue')
        ultra_fast_time, ultra_fast_result = test_ultra_fast()
        
        if ultra_fast_time is not None:
            ultra_fast_times.append(ultra_fast_time)
            ensure_printed(f"✅ 초고속 버전: {ultra_fast_time:.4f}초", print_color='green')
        else:
            ensure_printed(f"❌ 초고속 버전 테스트 실패", print_color='red')
        
        # 직접 최적화 함수 테스트
        ensure_printed(f"🔧 직접 최적화 함수 테스트 중...", print_color='blue')
        direct_time, direct_result = test_direct_optimized()
        
        if direct_time is not None:
            direct_times.append(direct_time)
            ensure_printed(f"✅ 직접 최적화: {direct_time:.4f}초", print_color='green')
        else:
            ensure_printed(f"❌ 직접 최적화 테스트 실패", print_color='red')
        
        # 매크로 최적화 함수 테스트
        ensure_printed(f"🔧 매크로 최적화 함수 테스트 중...", print_color='blue')
        macro_time, macro_result = test_macro_optimized()
        
        if macro_time is not None:
            macro_times.append(macro_time)
            ensure_printed(f"✅ 매크로 최적화: {macro_time:.4f}초", print_color='green')
        else:
            ensure_printed(f"❌ 매크로 최적화 테스트 실패", print_color='red')
        
        # 잠시 대기 (테스트 간 간격)
        time.sleep(0.5)
    
    return lightning_times, ultra_fast_times, direct_times, macro_times

def analyze_results(lightning_times, ultra_fast_times, direct_times, macro_times):
    """결과 분석 및 출력"""
    ensure_printed(f"\n📊 테스트 결과 분석", print_color='cyan')
    
    results = []
    
    if lightning_times:
        lightning_avg = statistics.mean(lightning_times)
        lightning_std = statistics.stdev(lightning_times) if len(lightning_times) > 1 else 0
        lightning_min = min(lightning_times)
        lightning_max = max(lightning_times)
        results.append(("초경량 버전", lightning_avg, lightning_std, lightning_min, lightning_max, lightning_times))
    
    if ultra_fast_times:
        ultra_fast_avg = statistics.mean(ultra_fast_times)
        ultra_fast_std = statistics.stdev(ultra_fast_times) if len(ultra_fast_times) > 1 else 0
        ultra_fast_min = min(ultra_fast_times)
        ultra_fast_max = max(ultra_fast_times)
        results.append(("초고속 버전", ultra_fast_avg, ultra_fast_std, ultra_fast_min, ultra_fast_max, ultra_fast_times))
    
    if direct_times:
        direct_avg = statistics.mean(direct_times)
        direct_std = statistics.stdev(direct_times) if len(direct_times) > 1 else 0
        direct_min = min(direct_times)
        direct_max = max(direct_times)
        results.append(("직접 최적화", direct_avg, direct_std, direct_min, direct_max, direct_times))
    
    if macro_times:
        macro_avg = statistics.mean(macro_times)
        macro_std = statistics.stdev(macro_times) if len(macro_times) > 1 else 0
        macro_min = min(macro_times)
        macro_max = max(macro_times)
        results.append(("매크로 최적화", macro_avg, macro_std, macro_min, macro_max, macro_times))
    
    if not results:
        ensure_printed(f"❌ 테스트 데이터가 부족합니다.", print_color='red')
        return
    
    # 결과 출력
    for name, avg, std, min_val, max_val, times in results:
        ensure_printed(f"\n📈 {name} 결과:", print_color='blue')
        ensure_printed(f"  • 평균: {avg:.4f}초", print_color='white')
        ensure_printed(f"  • 표준편차: {std:.4f}초", print_color='white')
        ensure_printed(f"  • 최소: {min_val:.4f}초", print_color='white')
        ensure_printed(f"  • 최대: {max_val:.4f}초", print_color='white')
        ensure_printed(f"  • 개별 결과: {[f'{t:.4f}' for t in times]}", print_color='cyan')
    
    # 성능 순위 결정
    results.sort(key=lambda x: x[1])  # 평균 시간으로 정렬
    
    ensure_printed(f"\n🏆 성능 순위:", print_color='cyan')
    for i, (name, avg, std, min_val, max_val, times) in enumerate(results, 1):
        if i == 1:
            ensure_printed(f"  🥇 {i}위: {name} ({avg:.4f}초) - 가장 빠름!", print_color='green')
        elif i == 2:
            ensure_printed(f"  🥈 {i}위: {name} ({avg:.4f}초)", print_color='yellow')
        elif i == 3:
            ensure_printed(f"  🥉 {i}위: {name} ({avg:.4f}초)", print_color='blue')
        else:
            ensure_printed(f"  {i}위: {name} ({avg:.4f}초)", print_color='white')
    
    # 가장 빠른 것과 가장 느린 것 비교
    if len(results) >= 2:
        fastest = results[0]
        slowest = results[-1]
        improvement = ((slowest[1] - fastest[1]) / slowest[1]) * 100
        ensure_printed(f"\n🚀 {fastest[0]}이 {slowest[0]}보다 {improvement:.1f}% 더 빠릅니다!", print_color='green')

def main():
    """메인 테스트 함수"""
    ensure_printed("🚀 속도 비교 테스트 시작", print_color='green')
    
    try:
        # 5회 테스트 실행
        lightning_times, ultra_fast_times, direct_times, macro_times = run_speed_comparison_test(iterations=5)
        
        # 결과 분석
        analyze_results(lightning_times, ultra_fast_times, direct_times, macro_times)
        
        ensure_printed(f"\n🎉 속도 비교 테스트 완료!", print_color='green')
        
    except Exception as e:
        ensure_printed(f"❌ 테스트 중 오류 발생: {e}", print_color='red')

if __name__ == "__main__":
    main() 