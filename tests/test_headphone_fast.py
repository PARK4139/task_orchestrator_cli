#!/usr/bin/env python3
"""
헤드폰 빠른 속도 테스트
"""

from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def test_headphone_fast():
    """헤드폰에서 빠른 속도로 테스트"""
    print("🎧 헤드폰 빠른 속도 테스트")
    print("=" * 30)
    
    # 빠른 속도 설정
    config = VoiceConfig(
        name="헤드폰 빠른 테스트",
        rate=250,  # 빠른 속도
        volume=0.1,  # 10% 볼륨
        language="ko"
    )
    
    print("🎵 설정:")
    print(f"   속도: {config.rate} (빠름)")
    print(f"   볼륨: {config.volume * 100}%")
    print()
    
    # 간단한 단어들 테스트
    test_words = ["안녕", "테스트", "성공"]
    
    for word in test_words:
        print(f"🔊 테스트: '{word}'")
        ensure_spoken_hybrid(word, voice_config=config)
        print()
    
    print("✅ 헤드폰 테스트 완료!")

if __name__ == "__main__":
    test_headphone_fast() 