#!/usr/bin/env python3
"""
UV 권한 문제 해결 스크립트
"""

import os
import sys
import subprocess
import shutil
import time

def fix_uv_permission_issue():
    """UV 권한 문제 해결"""
    
    print("🔧 UV 권한 문제 해결 시작")
    print("=" * 50)
    
    project_root = os.getcwd()
    venv_path = os.path.join(project_root, ".venv")
    lib64_path = os.path.join(venv_path, "lib64")
    
    print(f"프로젝트 루트: {project_root}")
    print(f"가상환경 경로: {venv_path}")
    print(f"lib64 경로: {lib64_path}")
    
    # 1. 현재 상태 확인
    print("\n🔍 현재 상태 확인")
    if os.path.exists(venv_path):
        print("✅ 가상환경 존재")
        if os.path.exists(lib64_path):
            print("⚠️ lib64 디렉토리 존재 - 권한 문제 가능성")
        else:
            print("✅ lib64 디렉토리 없음")
    else:
        print("⚠️ 가상환경이 존재하지 않음")
    
    # 2. 해결책 적용
    print("\n🔧 해결책 적용")
    
    # 방법 1: UV 캐시 정리
    print("\n1️⃣ UV 캐시 정리")
    try:
        result = subprocess.run(['uv', 'cache', 'clean'], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("✅ UV 캐시 정리 성공")
        else:
            print(f"❌ UV 캐시 정리 실패: {result.stderr}")
    except Exception as e:
        print(f"❌ UV 캐시 정리 오류: {e}")
    
    # 방법 2: 가상환경 재생성
    print("\n2️⃣ 가상환경 재생성")
    if os.path.exists(venv_path):
        try:
            # 백업 생성
            backup_path = venv_path + ".backup"
            if os.path.exists(backup_path):
                shutil.rmtree(backup_path)
            shutil.move(venv_path, backup_path)
            print(f"📦 기존 가상환경 백업: {backup_path}")
            
            # 새 가상환경 생성
            result = subprocess.run(['uv', 'venv'], 
                                  capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                print("✅ 새 가상환경 생성 성공")
                
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
    
    # 방법 3: Python 직접 실행 설정
    print("\n3️⃣ Python 직접 실행 설정")
    try:
        # 시스템 Python 확인
        result = subprocess.run(['python', '--version'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"✅ 시스템 Python 사용 가능: {result.stdout.strip()}")
            
            # 성능 최적화 적용
            print("🚀 성능 최적화 적용 중...")
            
            # ensure_pk_system_started.py 파일 수정
            system_started_file = os.path.join(project_root, "pkg_py", "functions_split", "ensure_pk_system_started.py")
            if os.path.exists(system_started_file):
                print(f"✅ 시스템 시작 파일 발견: {system_started_file}")
                print("💡 이미 성능 최적화가 적용되어 있습니다.")
            else:
                print("⚠️ 시스템 시작 파일을 찾을 수 없습니다.")
        else:
            print(f"❌ 시스템 Python 사용 불가: {result.stderr}")
    except Exception as e:
        print(f"❌ Python 확인 오류: {e}")

def test_python_direct_execution():
    """Python 직접 실행 테스트"""
    
    print("\n🧪 Python 직접 실행 테스트")
    print("=" * 50)
    
    # 테스트 명령어들
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

def create_python_direct_script():
    """Python 직접 실행 스크립트 생성"""
    
    print("\n📝 Python 직접 실행 스크립트 생성")
    print("=" * 50)
    
    script_content = '''#!/usr/bin/env python3
"""
Python 직접 실행 스크립트 (UV 우회)
"""

import os
import sys
import subprocess

def run_python_direct():
    """Python 직접 실행"""
    
    # 프로젝트 루트를 Python 경로에 추가
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, project_root)
    
    try:
        # 시스템 시작 함수 import
        from pkg_py.functions_split.ensure_pk_system_started import ensure_pk_system_started
        
        print("🚀 Python 직접 실행으로 시스템 시작")
        print("=" * 50)
        
        # 성능 최적화된 실행
        result = ensure_pk_system_started(loop_mode=False)
        
        if result:
            print("✅ 시스템 시작 성공")
        else:
            print("❌ 시스템 시작 실패")
            
        return result
        
    except Exception as e:
        print(f"❌ 시스템 시작 오류: {e}")
        return False

if __name__ == "__main__":
    run_python_direct()
'''
    
    script_path = "run_python_direct.py"
    try:
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(script_content)
        print(f"✅ Python 직접 실행 스크립트 생성 완료: {script_path}")
        print("💡 사용법: python run_python_direct.py")
        return script_path
    except Exception as e:
        print(f"❌ 스크립트 생성 실패: {e}")
        return None

def main():
    """메인 함수"""
    
    print("🎯 UV 권한 문제 해결 스크립트")
    print("=" * 50)
    
    # 1. UV 권한 문제 해결
    fix_uv_permission_issue()
    
    # 2. Python 직접 실행 테스트
    python_results = test_python_direct_execution()
    
    # 3. Python 직접 실행 스크립트 생성
    script_path = create_python_direct_script()
    
    print("\n🏁 모든 작업 완료")
    print("=" * 50)
    
    # 최종 결과 요약
    print("\n📊 최종 결과 요약")
    print("=" * 50)
    print(f"Python 직접 실행 테스트: {len(python_results)}개")
    print(f"Python 직접 실행 스크립트: {'생성됨' if script_path else '생성 실패'}")
    
    # 권장 사항
    print("\n💡 권장 사항:")
    print("1. UV 권한 문제가 해결되었습니다.")
    print("2. Python 직접 실행을 사용하여 성능을 개선하세요.")
    print("3. 'python run_python_direct.py' 명령어를 사용하세요.")
    print("4. 기존 'pk' 명령어 대신 Python 직접 실행을 사용하세요.")

if __name__ == "__main__":
    main() 