#!/usr/bin/env python3
"""
한글 앞부분 소리 문제 해결 테스트 스크립트
"""

import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_spoken import ensure_spoken
from pkg_py.functions_split.ensure_printed import ensure_printed

def test_korean_audio_fix():
    """한글 앞부분 소리 문제 해결 테스트"""
    print("🎧 한글 앞부분 소리 문제 해결 테스트")
    print("=" * 50)
    
    # 한글 텍스트 테스트 (앞부분 소리가 먹히는 문제가 있었던 텍스트들)
    korean_texts = [
        "안녕하세요",
        "한국어 음성 테스트",
        "앞부분 소리가 들리는지 확인",
        "현재 시간은 오후 3시입니다",
        "테스트 완료되었습니다"
    ]
    
    print("🇰🇷 한글 텍스트 TTS 테스트 (silent.mp3 적용)")
    for i, text in enumerate(korean_texts, 1):
        print(f"테스트 {i}: {text}")
        try:
            ensure_spoken(text)
            print(f"✅ 테스트 {i} 성공")
        except Exception as e:
            print(f"❌ 테스트 {i} 실패: {e}")
        print()
    
    print("🎉 테스트 완료!")

def main():
    """메인 함수"""
    test_korean_audio_fix()

if __name__ == "__main__":
    main() 