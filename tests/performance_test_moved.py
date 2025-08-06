#!/usr/bin/env python3
"""
성능 개선 테스트 스크립트
"""

import os
import sys
import time
import subprocess

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def test_uv_performance():
    """uv run python 성능 테스트"""
    
    print("🧪 uv run python 성능 테스트")
    print("=" * 50)
    
    # 테스트할 명령어들
    commands = [
        "uv run python -c \"print('Hello from uv!')\"",
        "python -c \"print('Hello from python!')\"",
    ]
    
    results = {}
    
    for cmd in commands:
        print(f"\n📊 테스트 중: {cmd}")
        
        start_time = time.time()
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            end_time = time.time()
            
            execution_time = end_time - start_time
            results[cmd] = {
                'time': execution_time,
                'success': result.returncode == 0,
                'output': result.stdout.strip(),
                'error': result.stderr.strip()
            }
            
            print(f"⏱️  실행 시간: {execution_time:.3f}초")
            print(f"✅ 성공: {result.returncode == 0}")
            if result.stdout.strip():
                print(f"📤 출력: {result.stdout.strip()}")
            if result.stderr.strip():
                print(f"❌ 에러: {result.stderr.strip()}")
                
        except subprocess.TimeoutExpired:
            print("⏰ 타임아웃 (30초)")
            results[cmd] = {'time': 30.0, 'success': False, 'timeout': True}
        except Exception as e:
            print(f"❌ 예외 발생: {e}")
            results[cmd] = {'time': 0, 'success': False, 'error': str(e)}
    
    print("\n📈 성능 비교 결과")
    print("=" * 50)
    
    for cmd, result in results.items():
        status = "✅" if result.get('success', False) else "❌"
        print(f"{status} {cmd}: {result.get('time', 0):.3f}초")
    
    return results

def test_python_imports():
    """Python 모듈 import 성능 테스트"""
    
    print("\n🧪 Python import 성능 테스트")
    print("=" * 50)
    
    import_tests = [
        "import sys",
        "import os", 
        "import time",
        "from pkg_py.functions_split.ensure_printed import ensure_printed"
    ]
    
    for test_import in import_tests:
        print(f"\n📊 테스트 중: {test_import}")
        
        start_time = time.time()
        try:
            exec(test_import)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"⏱️  import 시간: {execution_time:.6f}초")
        except Exception as e:
            print(f"❌ import 실패: {e}")

def test_file_operations():
    """파일 작업 성능 테스트"""
    
    print("\n🧪 파일 작업 성능 테스트")
    print("=" * 50)
    
    # 테스트 파일 생성
    test_file = "temp_performance_test.txt"
    test_content = "테스트 내용\n" * 1000
    
    # 파일 쓰기 테스트
    print("📝 파일 쓰기 테스트")
    start_time = time.time()
    try:
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(test_content)
        end_time = time.time()
        write_time = end_time - start_time
        print(f"⏱️  쓰기 시간: {write_time:.6f}초")
    except Exception as e:
        print(f"❌ 쓰기 실패: {e}")
        return
    
    # 파일 읽기 테스트
    print("📖 파일 읽기 테스트")
    start_time = time.time()
    try:
        with open(test_file, 'r', encoding='utf-8') as f:
            content = f.read()
        end_time = time.time()
        read_time = end_time - start_time
        print(f"⏱️  읽기 시간: {read_time:.6f}초")
        print(f"📊 읽은 데이터 크기: {len(content)} 문자")
    except Exception as e:
        print(f"❌ 읽기 실패: {e}")
    
    # 정리
    try:
        os.remove(test_file)
        print("🧹 테스트 파일 정리 완료")
    except Exception as e:
        print(f"⚠️  파일 정리 실패: {e}")

def test_system_info():
    """시스템 정보 출력"""
    
    print("\n🖥️  시스템 정보")
    print("=" * 50)
    
    print(f"🐍 Python 버전: {sys.version}")
    print(f"💻 플랫폼: {sys.platform}")
    print(f"📁 현재 작업 디렉토리: {os.getcwd()}")
    print(f"🔍 Python 실행 경로: {sys.executable}")
    
    # uv 버전 확인
    try:
        result = subprocess.run("uv --version", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"📦 uv 버전: {result.stdout.strip()}")
        else:
            print("❌ uv 버전 확인 실패")
    except Exception as e:
        print(f"❌ uv 버전 확인 중 오류: {e}")

def main():
    """메인 테스트 함수"""
    
    print("🚀 성능 테스트 시작")
    print("=" * 70)
    
    # 시스템 정보 출력
    test_system_info()
    
    # uv vs python 성능 테스트
    uv_results = test_uv_performance()
    
    # import 성능 테스트
    test_python_imports()
    
    # 파일 작업 성능 테스트  
    test_file_operations()
    
    print("\n🎉 모든 성능 테스트 완료")
    print("=" * 70)
    
    return uv_results

if __name__ == "__main__":
    main()