#!/usr/bin/env python3
"""
Windows에서 fzf 명령어 실행 테스트
"""

import sys
import os

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_fzf_windows_compatible import (
    run_fzf_windows_safe,
    run_fzf_windows_interactive,
    is_fzf_available,
    get_fzf_version
)

def test_fzf_windows():
    """Windows에서 fzf 실행 테스트"""
    print("🔍 fzf 사용 가능 여부 확인...")
    
    if not is_fzf_available():
        print("❌ fzf가 설치되지 않았습니다.")
        return False
    
    version = get_fzf_version()
    print(f"✅ fzf 버전: {version}")
    
    # 테스트 데이터
    test_data = """file1.txt
file2.txt
file3.txt
test_file.py
example.py
sample.txt"""
    
    print("\n🧪 Windows 호환 fzf 테스트 시작...")
    
    # 방법 1: 안전한 실행 테스트
    print("\n1️⃣ 안전한 실행 테스트:")
    result = run_fzf_windows_safe(test_data)
    if result:
        print(f"✅ 선택된 파일: {result}")
    else:
        print("❌ 선택되지 않음")
    
    # 방법 2: 대화형 실행 테스트
    print("\n2️⃣ 대화형 실행 테스트:")
    returncode, stdout, stderr = run_fzf_windows_interactive(test_data)
    print(f"Return code: {returncode}")
    print(f"Output: {stdout}")
    if stderr:
        print(f"Error: {stderr}")
    
    return True

if __name__ == "__main__":
    test_fzf_windows()