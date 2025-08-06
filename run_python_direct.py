#!/usr/bin/env python3
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
