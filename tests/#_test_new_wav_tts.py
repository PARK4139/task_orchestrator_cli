#!/usr/bin/env python3
"""
새로운 WAV TTS 생성 테스트 스크립트
"""

import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_spoken import ensure_spoken
from pkg_py.functions_split.ensure_printed import ensure_printed

def test_new_wav_tts():
    """새로운 WAV TTS 생성 테스트"""
    print("🎵 새로운 WAV TTS 생성 테스트")
    print("=" * 40)
    
    # 새로운 텍스트들 (아직 생성되지 않은 것들)
    new_texts = [
        "새로운 음성 테스트입니다",
        "WAV 포맷으로 저장됩니다",
        "고품질 음성입니다"
    ]
    
    for i, text in enumerate(new_texts, 1):
        print(f"테스트 {i}: {text}")
        try:
            # 새로운 TTS 생성 (WAV로 저장됨)
            ensure_spoken(text)
            print(f"✅ 테스트 {i} 완료")
        except Exception as e:
            print(f"❌ 테스트 {i} 실패: {e}")
        print()
    
    print("🎉 테스트 완료!")

if __name__ == "__main__":
    test_new_wav_tts() 