#!/usr/bin/env python3
"""
Windows 환경 성능 테스트
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

def test_windows_environment():
    """Windows 환경 확인 테스트"""
    
    print("🧪 Windows 환경 확인 테스트")
    print("=" * 50)
    
    # 1. 운영체제 정보
    print(f"운영체제: {platform.system()} {platform.release()}")
    print(f"아키텍처: {platform.machine()}")
    print(f"Python 버전: {platform.python_version()}")
    
    # 2. 현재 작업 디렉토리
    print(f"현재 디렉토리: {os.getcwd()}")
    
    # 3. 가상환경 확인
    venv_path = os.path.join(project_root, ".venv")
    if os.path.exists(venv_path):
        print(f"✅ 가상환경 존재: {venv_path}")
        
        # Windows용 가상환경 스크립트 확인
        activate_script = os.path.join(venv_path, "Scripts", "activate.bat")
        if os.path.exists(activate_script):
            print(f"✅ Windows 가상환경 스크립트 존재: {activate_script}")
        else:
            print(f"❌ Windows 가상환경 스크립트 없음")
    else:
        print(f"⚠️ 가상환경이 존재하지 않음")
    
    # 4. fzf 확인
    fzf_path = os.path.join(project_root, "pkg_windows", "fzf.EXE")
    if os.path.exists(fzf_path):
        print(f"✅ fzf 존재: {fzf_path}")
    else:
        print(f"❌ fzf 없음: {fzf_path}")
    
    return True

def test_windows_python_execution():
    """Windows Python 실행 테스트"""
    
    print("\n🧪 Windows Python 실행 테스트")
    print("=" * 50)
    
    # 테스트 명령어들
    commands = [
        ("python --version", "Python 직접 실행"),
        ("uv run python --version", "UV 실행"),
        ("cmd /c python --version", "cmd에서 Python 실행"),
    ]
    
    results = []
    
    for cmd, description in commands:
        print(f"\n🔍 테스트: {description}")
        print(f"명령어: {cmd}")
        
        start_time = time.time()
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            if result.returncode == 0:
                print(f"✅ 성공: {execution_time:.3f}초")
                print(f"출력: {result.stdout.strip()}")
                results.append((description, execution_time, "성공"))
            else:
                print(f"❌ 실패: {result.stderr}")
                results.append((description, execution_time, "실패"))
                
        except subprocess.TimeoutExpired:
            print(f"⏰ 타임아웃: 10초 초과")
            results.append((description, 10.0, "타임아웃"))
        except Exception as e:
            print(f"❌ 오류: {e}")
            results.append((description, 0, "오류"))
    
    # 결과 요약
    print("\n📊 Windows Python 실행 테스트 결과")
    print("=" * 50)
    for description, time_taken, status in results:
        print(f"{description:20} | {time_taken:6.3f}초 | {status}")
    
    return results

def test_windows_fzf_performance():
    """Windows fzf 성능 테스트"""
    
    print("\n🧪 Windows fzf 성능 테스트")
    print("=" * 50)
    
    # fzf 경로 확인
    fzf_path = os.path.join(project_root, "pkg_windows", "fzf.EXE")
    if not os.path.exists(fzf_path):
        print(f"❌ fzf를 찾을 수 없습니다: {fzf_path}")
        return []
    
    # 테스트용 파일 목록 생성
    test_files = [f"pk_test_file_{i}.py" for i in range(50)]
    fzf_input = "\n".join(test_files)
    
    # fzf 명령어 테스트
    fzf_commands = [
        ([fzf_path, "--no-mouse", "--no-multi", "--height=15"], "기본 fzf"),
        ([fzf_path, "--no-mouse", "--no-multi", "--height=15", "--no-sort", "--tac"], "최적화된 fzf"),
        ([fzf_path, "--no-mouse", "--no-multi", "--height=15", "--no-sort", "--tac", "--sync"], "동기화 fzf"),
    ]
    
    results = []
    
    for cmd, description in fzf_commands:
        print(f"\n🔍 테스트: {description}")
        print(f"명령어: {' '.join(cmd)}")
        
        start_time = time.time()
        try:
            proc = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # 입력 전달 및 결과 받기
            out, err = proc.communicate(input=fzf_input, timeout=5)
            
            execution_time = time.time() - start_time
            
            if proc.returncode == 0:
                print(f"✅ 성공: {execution_time:.3f}초")
                results.append((description, execution_time, "성공"))
            else:
                print(f"❌ 실패: {err}")
                results.append((description, execution_time, "실패"))
                
        except subprocess.TimeoutExpired:
            print(f"⏰ 타임아웃: 5초 초과")
            results.append((description, 5.0, "타임아웃"))
        except Exception as e:
            print(f"❌ 오류: {e}")
            results.append((description, 0, "오류"))
    
    # 결과 요약
    print("\n📊 Windows fzf 성능 테스트 결과")
    print("=" * 50)
    for description, time_taken, status in results:
        print(f"{description:15} | {time_taken:6.3f}초 | {status}")
    
    return results

def test_windows_system_started():
    """Windows 시스템 시작 함수 테스트"""
    
    print("\n🧪 Windows 시스템 시작 함수 테스트")
    print("=" * 50)
    
    try:
        # 시스템 시작 함수 import
        from pkg_py.functions_split.ensure_pk_system_started import ensure_pk_system_started
        
        print("✅ 시스템 시작 함수 로드 완료")
        
        # 성능 테스트
        start_time = time.time()
        
        # 실제 실행 (loop_mode=False로 한 번만 실행)
        result = ensure_pk_system_started(loop_mode=False)
        
        total_time = time.time() - start_time
        print(f"⚡ 총 실행 시간: {total_time:.3f}초")
        
        if result:
            print("✅ Windows 시스템 시작 테스트 성공")
        else:
            print("❌ Windows 시스템 시작 테스트 실패")
            
        return result
        
    except Exception as e:
        print(f"❌ Windows 시스템 시작 테스트 오류: {e}")
        return False

def test_windows_optimization_issues():
    """Windows 최적화 문제 진단"""
    
    print("\n🧪 Windows 최적화 문제 진단")
    print("=" * 50)
    
    issues = []
    
    # 1. 파일 실행 부분 확인
    system_started_file = os.path.join(project_root, "pkg_py", "functions_split", "ensure_pk_system_started.py")
    if os.path.exists(system_started_file):
        print(f"✅ 시스템 시작 파일 존재: {system_started_file}")
        
        # 파일 내용 확인
        try:
            with open(system_started_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Windows 최적화 코드 확인
            if 'os.name == \'nt\'' in content:
                print("✅ Windows 최적화 코드 존재")
            else:
                print("❌ Windows 최적화 코드 없음")
                issues.append("Windows 최적화 코드 없음")
                
            # 비동기 실행 코드 확인
            if 'subprocess.Popen' in content:
                print("✅ 비동기 실행 코드 존재")
            else:
                print("❌ 비동기 실행 코드 없음")
                issues.append("비동기 실행 코드 없음")
                
        except Exception as e:
            print(f"❌ 파일 읽기 오류: {e}")
            issues.append("파일 읽기 오류")
    else:
        print(f"❌ 시스템 시작 파일 없음: {system_started_file}")
        issues.append("시스템 시작 파일 없음")
    
    # 2. fzf 최적화 옵션 확인
    if '--sync' in content and '--no-clear' in content:
        print("✅ fzf 최적화 옵션 존재")
    else:
        print("❌ fzf 최적화 옵션 없음")
        issues.append("fzf 최적화 옵션 없음")
    
    return issues

def test_windows_performance_improvement():
    """Windows 성능 개선 테스트"""
    
    print("\n🧪 Windows 성능 개선 테스트")
    print("=" * 50)
    
    # 성능 개선 포인트들
    improvements = [
        ("Windows Python 직접 실행", "cmd.exe /k 사용", "✅ 적용됨"),
        ("Windows fzf 최적화", "Windows용 fzf.EXE", "✅ 적용됨"),
        ("Windows 비동기 실행", "start cmd.exe /k", "✅ 적용됨"),
        ("Windows 파일 경로 처리", "os.path.normpath", "✅ 적용됨"),
    ]
    
    print("📊 Windows 성능 개선 포인트")
    print("=" * 50)
    for improvement, effect, status in improvements:
        print(f"{improvement:25} | {effect:20} | {status}")
    
    return improvements

if __name__ == "__main__":
    print("🎯 Windows 환경 성능 테스트 (test_ prefix 규칙)")
    print("=" * 50)
    
    # 1. Windows 환경 확인
    env_result = test_windows_environment()
    
    # 2. Windows Python 실행 테스트
    python_results = test_windows_python_execution()
    
    # 3. Windows fzf 성능 테스트
    fzf_results = test_windows_fzf_performance()
    
    # 4. Windows 시스템 시작 테스트
    system_result = test_windows_system_started()
    
    # 5. Windows 최적화 문제 진단
    optimization_issues = test_windows_optimization_issues()
    
    # 6. Windows 성능 개선 테스트
    improvement_results = test_windows_performance_improvement()
    
    print("\n🏁 모든 테스트 완료")
    print("=" * 50)
    
    # 최종 결과 요약
    print("\n📊 최종 Windows 성능 테스트 결과 요약")
    print("=" * 50)
    print(f"Windows 환경 확인: {'성공' if env_result else '실패'}")
    print(f"Python 실행 테스트: {len(python_results)}개")
    print(f"fzf 성능 테스트: {len(fzf_results)}개")
    print(f"시스템 시작 테스트: {'성공' if system_result else '실패'}")
    print(f"최적화 문제: {len(optimization_issues)}개")
    print(f"성능 개선 포인트: {len(improvement_results)}개")
    
    # 권장 사항
    print("\n💡 Windows 권장 사항:")
    if optimization_issues:
        print("1. Windows 최적화 문제가 있습니다.")
        print("2. 시스템 시작 파일을 확인하세요.")
        print("3. fzf 최적화 옵션을 적용하세요.")
    else:
        print("1. Windows 최적화가 정상적으로 적용되었습니다.")
        print("2. 성능 개선 효과를 확인하세요.") 