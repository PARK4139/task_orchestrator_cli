#!/usr/bin/env python3
"""
성능 최적화 테스트 (프로젝트 루트에서 이동됨)
"""

import os
import sys
import time

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def test_performance_optimization():
    """성능 최적화 테스트"""
    
    print("🚀 성능 최적화 테스트 시작")
    print("=" * 50)
    
    try:
        # 기본 import 테스트
        print("📦 기본 모듈 import 테스트...")
        start_time = time.time()
        
        from pkg_py.functions_split.ensure_printed import ensure_printed
        from pkg_py.functions_split.get_nx import get_nx
        
        import_time = time.time() - start_time
        print(f"⏱️  Import 시간: {import_time:.3f}초")
        
        # 함수 실행 테스트
        print("\n🔧 함수 실행 테스트...")
        start_time = time.time()
        
        ensure_printed("테스트 메시지", print_color='green')
        test_file = __file__
        nx = get_nx(test_file)
        
        execution_time = time.time() - start_time
        print(f"⏱️  함수 실행 시간: {execution_time:.3f}초")
        print(f"📁 파일명 (nx): {nx}")
        
        # 시스템 정보
        print(f"\n💻 시스템 정보:")
        print(f"   🐍 Python: {sys.version.split()[0]}")
        print(f"   📁 작업 디렉토리: {os.getcwd()}")
        print(f"   🔍 스크립트 경로: {__file__}")
        
        print("\n✅ 성능 최적화 테스트 완료")
        return True
        
    except ImportError as e:
        print(f"❌ Import 오류: {e}")
        return False
    except Exception as e:
        print(f"❌ 실행 오류: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_uv_vs_python():
    """uv와 python 성능 비교"""
    
    print("\n🏁 uv vs python 성능 비교")
    print("=" * 50)
    
    import subprocess
    
    # 간단한 Python 코드 실행 테스트
    test_code = "print('Hello World'); import sys; print(f'Python: {sys.version.split()[0]}')"
    
    commands = [
        f'python -c "{test_code}"',
        f'uv run python -c "{test_code}"'
    ]
    
    for cmd in commands:
        print(f"\n📊 테스트: {cmd.split()[0]}")
        
        start_time = time.time()
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            execution_time = time.time() - start_time
            
            if result.returncode == 0:
                print(f"⏱️  실행 시간: {execution_time:.3f}초")
                print(f"📤 출력: {result.stdout.strip()}")
            else:
                print(f"❌ 실행 실패 (코드: {result.returncode})")
                if result.stderr:
                    print(f"❌ 에러: {result.stderr.strip()}")
                    
        except subprocess.TimeoutExpired:
            print("⏰ 타임아웃 (30초)")
        except Exception as e:
            print(f"❌ 예외: {e}")

if __name__ == "__main__":
    success = test_performance_optimization()
    test_uv_vs_python()
    
    if success:
        print("\n🎉 모든 테스트 성공!")
    else:
        print("\n❌ 일부 테스트 실패")
        sys.exit(1)