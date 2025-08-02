#!/usr/bin/env python3
"""
Test script for ensure_spoken function with gTTS support for Korean
"""

import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_spoken import ensure_spoken
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.map_massages import PkMessages2025

def test_ensure_spoken_gtts():
    """Test ensure_spoken function with gTTS for Korean text"""
    print(f"🎧 {PkMessages2025.AUDIO_TEST}")
    print("=" * 50)
    
    # Test Korean text (should use gTTS)
    korean_texts = [
        "안녕하세요, gTTS 테스트입니다",
        "한국어 음성 합성 테스트",
        "현재 시간은 오후 3시입니다"
    ]
    
    print("🇰🇷 한국어 텍스트 테스트 (gTTS 사용)")
    for i, text in enumerate(korean_texts, 1):
        print(f"테스트 {i}: {text}")
        try:
            ensure_spoken(text)
            print(f"✅ {PkMessages2025.AUDIO_TEST_SUCCESS} {i}")
        except Exception as e:
            print(f"❌ {PkMessages2025.AUDIO_TEST_FAILED} {i}: {e}")
        print()
    
    # Test English text (should use ElevenLabs)
    english_texts = [
        "Hello, this is a test",
        "English text-to-speech test",
        "Current time is 3 PM"
    ]
    
    print("🇺🇸 영어 텍스트 테스트 (ElevenLabs 사용)")
    for i, text in enumerate(english_texts, 1):
        print(f"테스트 {i}: {text}")
        try:
            ensure_spoken(text)
            print(f"✅ {PkMessages2025.AUDIO_TEST_SUCCESS} {i}")
        except Exception as e:
            print(f"❌ {PkMessages2025.AUDIO_TEST_FAILED} {i}: {e}")
        print()
    
    print(f"🎉 {PkMessages2025.TEST_COMPLETE}!")

def main():
    """Main function"""
    print(f"🎧 {PkMessages2025.AUDIO_TEST}")
    print("=" * 60)
    
    # Test ensure_spoken with gTTS support
    test_ensure_spoken_gtts()

if __name__ == "__main__":
    main() 