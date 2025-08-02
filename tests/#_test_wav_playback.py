#!/usr/bin/env python3
"""
WAV 파일 재생 테스트 스크립트
"""

import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_spoken import ensure_spoken
from pkg_py.functions_split.ensure_printed import ensure_printed

def test_wav_playback():
    """WAV 파일 재생 테스트"""
    print("🎵 WAV 파일 재생 테스트")
    print("=" * 30)
    
    # 테스트할 텍스트들 (이미 WAV로 저장된 것들)
    test_texts = [
        "안녕하세요",
        "테스트입니다"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"테스트 {i}: {text}")
        try:
            # 이미 WAV 파일이 있으므로 캐시에서 재생될 것입니다
            ensure_spoken(text)
            print(f"✅ 테스트 {i} 완료")
        except Exception as e:
            print(f"❌ 테스트 {i} 실패: {e}")
        print()
    
    print("🎉 테스트 완료!")

if __name__ == "__main__":
    test_wav_playback() 