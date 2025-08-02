#!/usr/bin/env python3
"""
간단한 TTS 테스트 스크립트
"""

import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_spoken import ensure_spoken
from pkg_py.functions_split.ensure_printed import ensure_printed

def test_simple_tts():
    """간단한 TTS 테스트"""
    print("🎧 간단한 TTS 테스트")
    print("=" * 30)
    
    # 테스트할 텍스트들
    test_texts = [
        "안녕하세요",
        "테스트입니다",
        "소리가 들리나요?"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"테스트 {i}: {text}")
        try:
            ensure_spoken(text)
            print(f"✅ 테스트 {i} 완료")
        except Exception as e:
            print(f"❌ 테스트 {i} 실패: {e}")
        print()
    
    print("🎉 테스트 완료!")

if __name__ == "__main__":
    test_simple_tts() 