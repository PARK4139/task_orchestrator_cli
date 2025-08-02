#!/usr/bin/env python3
"""
간단한 오디오 테스트
"""

import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_spoken import ensure_spoken

def test_simple():
    """간단한 오디오 테스트"""
    print("🔊 간단한 오디오 테스트")
    print("=" * 30)
    
    # 이미 생성된 WAV 파일이 있는 텍스트로 테스트
    test_text = "안녕하세요"
    
    print(f"테스트: {test_text}")
    try:
        ensure_spoken(test_text)
        print("✅ 테스트 완료")
    except Exception as e:
        print(f"❌ 테스트 실패: {e}")

if __name__ == "__main__":
    test_simple() 