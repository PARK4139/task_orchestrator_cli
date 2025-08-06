#!/usr/bin/env python3
"""
UV 권한 문제 해결 테스트
test_ prefix 규칙에 따라 작성
"""

import os
import sys
import time
import subprocess
import shutil

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def test_uv_permission_issue():
    """UV 권한 문제 테스트"""
    
    print("🧪 UV 권한 문제 테스트")
    print("=" * 50)
    
    # 1. 현재 UV 환경 상태 확인
    print("\n🔍 현재 UV 환경 상태 확인")
    
    venv_path = os.path.join(project_root, ".venv")
    lib64_path = os.path.join(venv_path, "lib64")
    
    print(f"프로젝트 루트: {project_root}")
    print(f"가상환경 경로: {venv_path}")
    print(f"lib64 경로: {lib64_path}")
    
    # 2. 파일 존재 여부 확인
    issues = []
    
    if os.path.exists(venv_path):
        print(f"✅ 가상환경 존재: {venv_path}")
        
        if os.path.exists(lib64_path):
            print(f"⚠️ lib64 디렉토리 존재: {lib64_path}")
            
            # 권한 확인
            try:
                os.access(lib64_path, os.R_OK)
                print("✅ lib64 읽기 권한 있음")
            except Exception as e:
                print(f"❌ lib64 읽기 권한 없음: {e}")
                issues.append("lib64 읽기 권한 없음")
            
            try:
                os.access(lib64_path, os.W_OK)
                print("✅ lib64 쓰기 권한 있음")
            except Exception as e:
                print(f"❌ lib64 쓰기 권한 없음: {e}")
                issues.append("lib64 쓰기 권한 없음")
        else:
            print("✅ lib64 디렉토리 없음")
    else:
        print("⚠️ 가상환경이 존재하지 않음")
    
    return issues

def test_uv_cleanup_solutions():
    """UV 정리 해결책 테스트"""
    
    print("\n🧪 UV 정리 해결책 테스트")
    print("=" * 50)
    
    solutions = []
    
    # 1. UV 캐시 정리
    print("\n🔍 UV 캐시 정리 테스트")
    try:
        result = subprocess.run(['uv', 'cache', 'clean'], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("✅ UV 캐시 정리 성공")
            solutions.append("UV 캐시 정리")
        else:
            print(f"❌ UV 캐시 정리 실패: {result.stderr}")
    except Exception as e:
        print(f"❌ UV 캐시 정리 오류: {e}")
    
    # 2. 가상환경 재생성
    print("\n🔍 가상환경 재생성 테스트")
    venv_path = os.path.join(project_root, ".venv")
    
    if os.path.exists(venv_path):
        try:
            # 백업 생성
            backup_path = venv_path + ".backup"
            shutil.move(venv_path, backup_path)
            print(f"📦 기존 가상환경 백업: {backup_path}")
            
            # 새 가상환경 생성
            result = subprocess.run(['uv', 'venv'], 
                                  capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                print("✅ 새 가상환경 생성 성공")
                solutions.append("가상환경 재생성")
                
                # 백업 삭제
                try:
                    shutil.rmtree(backup_path)
                    print(f"🧹 백업 삭제 완료: {backup_path}")
                except Exception as e:
                    print(f"⚠️ 백업 삭제 실패: {e}")
            else:
                print(f"❌ 새 가상환경 생성 실패: {result.stderr}")
                # 백업 복원
                try:
                    shutil.move(backup_path, venv_path)
                    print(f"🔄 백업 복원 완료: {venv_path}")
                except Exception as e:
                    print(f"⚠️ 백업 복원 실패: {e}")
                    
        except Exception as e:
            print(f"❌ 가상환경 재생성 오류: {e}")
    else:
        print("⚠️ 가상환경이 존재하지 않아 재생성 불필요")
    
    return solutions

def test_python_direct_execution():
    """Python 직접 실행 테스트 (UV 우회)"""
    
    print("\n🧪 Python 직접 실행 테스트")
    print("=" * 50)
    
    # Python 직접 실행 테스트
    commands = [
        ("python --version", "Python 직접 실행"),
        ("python -c 'import sys; print(sys.executable)'", "Python 경로 확인"),
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
    print("\n📊 Python 직접 실행 테스트 결과")
    print("=" * 50)
    for description, time_taken, status in results:
        print(f"{description:20} | {time_taken:6.3f}초 | {status}")
    
    return results

def test_uv_alternative_solutions():
    """UV 대안 해결책 테스트"""
    
    print("\n🧪 UV 대안 해결책 테스트")
    print("=" * 50)
    
    alternatives = []
    
    # 1. 시스템 Python 사용
    print("\n🔍 시스템 Python 사용")
    try:
        result = subprocess.run(['python', '--version'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"✅ 시스템 Python 사용 가능: {result.stdout.strip()}")
            alternatives.append("시스템 Python 사용")
        else:
            print(f"❌ 시스템 Python 사용 불가: {result.stderr}")
    except Exception as e:
        print(f"❌ 시스템 Python 확인 오류: {e}")
    
    # 2. 가상환경 직접 생성
    print("\n🔍 가상환경 직접 생성")
    try:
        venv_path = os.path.join(project_root, "venv_direct")
        result = subprocess.run(['python', '-m', 'venv', venv_path], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(f"✅ 직접 가상환경 생성 성공: {venv_path}")
            alternatives.append("직접 가상환경 생성")
            
            # 정리
            try:
                shutil.rmtree(venv_path)
                print(f"🧹 직접 가상환경 정리 완료: {venv_path}")
            except Exception as e:
                print(f"⚠️ 직접 가상환경 정리 실패: {e}")
        else:
            print(f"❌ 직접 가상환경 생성 실패: {result.stderr}")
    except Exception as e:
        print(f"❌ 직접 가상환경 생성 오류: {e}")
    
    # 3. pip 직접 사용
    print("\n🔍 pip 직접 사용")
    try:
        result = subprocess.run(['pip', '--version'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"✅ pip 직접 사용 가능: {result.stdout.strip()}")
            alternatives.append("pip 직접 사용")
        else:
            print(f"❌ pip 직접 사용 불가: {result.stderr}")
    except Exception as e:
        print(f"❌ pip 확인 오류: {e}")
    
    return alternatives

def test_performance_comparison_with_alternatives():
    """대안들과의 성능 비교 테스트"""
    
    print("\n🧪 대안들과의 성능 비교 테스트")
    print("=" * 50)
    
    # 실행 방법들 비교
    execution_methods = [
        ("python --version", "Python 직접 실행"),
        ("uv run python --version", "UV 실행"),
        ("pip --version", "pip 직접 실행"),
    ]
    
    results = []
    
    for cmd, description in execution_methods:
        print(f"\n🔍 테스트: {description}")
        print(f"명령어: {cmd}")
        
        start_time = time.time()
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=15)
            execution_time = time.time() - start_time
            
            if result.returncode == 0:
                print(f"✅ 성공: {execution_time:.3f}초")
                results.append((description, execution_time, "성공"))
            else:
                print(f"❌ 실패: {result.stderr}")
                results.append((description, execution_time, "실패"))
                
        except subprocess.TimeoutExpired:
            print(f"⏰ 타임아웃: 15초 초과")
            results.append((description, 15.0, "타임아웃"))
        except Exception as e:
            print(f"❌ 오류: {e}")
            results.append((description, 0, "오류"))
    
    # 결과 요약
    print("\n📊 성능 비교 결과")
    print("=" * 50)
    for description, time_taken, status in results:
        print(f"{description:20} | {time_taken:6.3f}초 | {status}")
    
    return results

if __name__ == "__main__":
    print("🎯 UV 권한 문제 해결 테스트 (test_ prefix 규칙)")
    print("=" * 50)
    
    # 1. UV 권한 문제 테스트
    permission_issues = test_uv_permission_issue()
    
    # 2. UV 정리 해결책 테스트
    cleanup_solutions = test_uv_cleanup_solutions()
    
    # 3. Python 직접 실행 테스트
    python_results = test_python_direct_execution()
    
    # 4. UV 대안 해결책 테스트
    alternative_solutions = test_uv_alternative_solutions()
    
    # 5. 성능 비교 테스트
    performance_results = test_performance_comparison_with_alternatives()
    
    print("\n🏁 모든 테스트 완료")
    print("=" * 50)
    
    # 최종 결과 요약
    print("\n📊 최종 UV 권한 문제 해결 테스트 결과 요약")
    print("=" * 50)
    print(f"권한 문제: {len(permission_issues)}개")
    print(f"정리 해결책: {len(cleanup_solutions)}개")
    print(f"Python 직접 실행 테스트: {len(python_results)}개")
    print(f"대안 해결책: {len(alternative_solutions)}개")
    print(f"성능 비교 테스트: {len(performance_results)}개")
    
    # 권장 해결책
    print("\n💡 권장 해결책:")
    if permission_issues:
        print("1. UV 가상환경 권한 문제가 있습니다.")
        print("2. Python 직접 실행을 사용하세요.")
        print("3. UV 캐시를 정리하세요.")
    else:
        print("1. UV 환경이 정상입니다.")
        print("2. 성능 최적화를 위해 Python 직접 실행을 고려하세요.") 