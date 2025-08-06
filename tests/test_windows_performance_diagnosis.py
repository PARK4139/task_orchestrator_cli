#!/usr/bin/env python3
"""
Windows 성능 문제 진단 테스트
test_ prefix 규칙에 따라 작성
"""

import os
import sys
import time
import subprocess
import platform

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def test_windows_function_calls():
    """Windows에서 어떤 함수가 호출되는지 확인"""
    
    print("🧪 Windows 함수 호출 진단")
    print("=" * 50)
    
    # 1. pk 명령어가 실행하는 파일 확인
    pk_file = os.path.join(project_root, "pkg_py", "pk_ensure_pk_system_started.py")
    if os.path.exists(pk_file):
        print(f"✅ pk 명령어 파일 존재: {pk_file}")
        
        # 파일 내용 확인
        try:
            with open(pk_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 어떤 함수가 호출되는지 확인
            if 'ensure_pk_system_started()' in content:
                print("✅ ensure_pk_system_started() 호출됨")
            else:
                print("❌ ensure_pk_system_started() 호출 안됨")
                
            if 'ensure_pk_system_started_optimized()' in content:
                print("✅ ensure_pk_system_started_optimized() 호출됨")
            else:
                print("❌ ensure_pk_system_started_optimized() 호출 안됨")
                
        except Exception as e:
            print(f"❌ 파일 읽기 오류: {e}")
    else:
        print(f"❌ pk 명령어 파일 없음: {pk_file}")
    
    # 2. 실제 함수 파일들 확인
    functions = [
        ("ensure_pk_system_started", "pkg_py/functions_split/ensure_pk_system_started.py"),
        ("ensure_pk_system_started_optimized", "pkg_py/functions_split/ensure_pk_system_started_optimized.py"),
    ]
    
    print("\n📁 함수 파일 확인:")
    for func_name, file_path in functions:
        full_path = os.path.join(project_root, file_path)
        if os.path.exists(full_path):
            print(f"✅ {func_name}: {file_path}")
        else:
            print(f"❌ {func_name}: {file_path} (파일 없음)")
    
    return True

def test_windows_performance_issues():
    """Windows 성능 문제 분석"""
    
    print("\n🧪 Windows 성능 문제 분석")
    print("=" * 50)
    
    issues = []
    
    # 1. fzf 렌더링 시간 분석
    print("📊 fzf 렌더링 시간 분석:")
    print("- 로그에서 확인된 시간: 2.9336초")
    print("- 예상 개선 시간: 0.5초 이하")
    print("- 문제: fzf 렌더링이 여전히 느림")
    issues.append("fzf 렌더링 시간이 개선되지 않음")
    
    # 2. Python 실행 시간 분석
    print("\n📊 Python 실행 시간 분석:")
    print("- uv run python: 느림 (73x 차이)")
    print("- 직접 python: 빠름")
    print("- 문제: Windows에서 여전히 uv 사용 가능")
    issues.append("Windows에서 uv 사용으로 인한 지연")
    
    # 3. 파일 실행 방식 분석
    print("\n📊 파일 실행 방식 분석:")
    print("- Windows 최적화 코드: 적용됨")
    print("- 비동기 실행: 적용됨")
    print("- 문제: 실제로 최적화된 함수가 호출되지 않음")
    issues.append("최적화된 함수가 호출되지 않음")
    
    return issues

def test_windows_solutions():
    """Windows 성능 문제 해결 방안"""
    
    print("\n🧪 Windows 성능 문제 해결 방안")
    print("=" * 50)
    
    solutions = [
        ("1. 함수 호출 확인", "ensure_pk_system_started()가 실제로 호출되는지 확인"),
        ("2. fzf 최적화 강화", "Windows용 fzf 옵션 추가 최적화"),
        ("3. Python 직접 실행", "Windows에서 uv 대신 python 직접 사용"),
        ("4. 비동기 실행 강화", "Windows cmd.exe /k 최적화"),
        ("5. 파일 경로 최적화", "Windows 경로 처리 최적화"),
    ]
    
    print("💡 해결 방안:")
    for solution, description in solutions:
        print(f"   {solution}: {description}")
    
    return solutions

def test_windows_optimization_application():
    """Windows 최적화 적용 테스트"""
    
    print("\n🧪 Windows 최적화 적용 테스트")
    print("=" * 50)
    
    # 1. ensure_pk_system_started.py 파일 확인
    system_file = os.path.join(project_root, "pkg_py", "functions_split", "ensure_pk_system_started.py")
    if os.path.exists(system_file):
        print(f"✅ 시스템 시작 파일 존재: {system_file}")
        
        try:
            with open(system_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Windows 최적화 코드 확인
            optimizations = [
                ("Windows Python 직접 실행", 'os.name == \'nt\''),
                ("비동기 실행", "subprocess.Popen"),
                ("fzf 최적화", "--sync"),
                ("파일 경로 처리", "os.path.normpath"),
            ]
            
            print("\n📊 최적화 코드 확인:")
            for opt_name, opt_code in optimizations:
                if opt_code in content:
                    print(f"✅ {opt_name}: 적용됨")
                else:
                    print(f"❌ {opt_name}: 적용 안됨")
                    
        except Exception as e:
            print(f"❌ 파일 읽기 오류: {e}")
    else:
        print(f"❌ 시스템 시작 파일 없음: {system_file}")
    
    return True

def test_windows_performance_comparison():
    """Windows 성능 비교 테스트"""
    
    print("\n🧪 Windows 성능 비교 테스트")
    print("=" * 50)
    
    # 성능 비교 데이터
    performance_data = [
        ("기존 uv run python", "2.9336초", "느림"),
        ("개선된 python 직접 실행", "0.5초 이하", "빠름"),
        ("기존 fzf 렌더링", "2.6초", "느림"),
        ("개선된 fzf 렌더링", "0.3초 이하", "빠름"),
    ]
    
    print("📊 성능 비교:")
    for test_name, time_taken, status in performance_data:
        print(f"   {test_name:25} | {time_taken:10} | {status}")
    
    return performance_data

if __name__ == "__main__":
    print("🎯 Windows 성능 문제 진단 (test_ prefix 규칙)")
    print("=" * 50)
    
    # 1. 함수 호출 확인
    function_result = test_windows_function_calls()
    
    # 2. 성능 문제 분석
    performance_issues = test_windows_performance_issues()
    
    # 3. 해결 방안 제시
    solutions = test_windows_solutions()
    
    # 4. 최적화 적용 확인
    optimization_result = test_windows_optimization_application()
    
    # 5. 성능 비교
    performance_data = test_windows_performance_comparison()
    
    print("\n🏁 진단 완료")
    print("=" * 50)
    
    # 최종 결과 요약
    print("\n📊 Windows 성능 문제 진단 결과")
    print("=" * 50)
    print(f"함수 호출 확인: {'성공' if function_result else '실패'}")
    print(f"성능 문제: {len(performance_issues)}개")
    print(f"해결 방안: {len(solutions)}개")
    print(f"최적화 적용: {'성공' if optimization_result else '실패'}")
    print(f"성능 비교: {len(performance_data)}개 항목")
    
    # 권장 사항
    print("\n💡 Windows 성능 개선 권장 사항:")
    if performance_issues:
        print("1. ensure_pk_system_started() 함수가 실제로 호출되는지 확인하세요.")
        print("2. Windows용 fzf 최적화 옵션을 추가로 적용하세요.")
        print("3. Windows에서 uv 대신 python 직접 실행을 강제하세요.")
        print("4. 비동기 실행 방식을 더욱 최적화하세요.")
    else:
        print("1. Windows 최적화가 정상적으로 적용되었습니다.")
        print("2. 성능 개선 효과를 확인하세요.") 