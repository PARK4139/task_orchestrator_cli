#!/usr/bin/env python3
"""
빠른 음성 테스트 스크립트
"""

from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def test_fast_voice():
    """빠른 음성으로 테스트"""
    print("🚀 빠른 음성 테스트 시작")
    print("=" * 40)
    
    # 빠른 음성 설정
    fast_voice_config = VoiceConfig(
        name="빠른 음성",
        rate=200,  # 빠른 속도
        volume=0.9,  # 높은 볼륨
        language="ko"
    )
    
    # 테스트 텍스트들
    test_texts = [
        "안녕하세요, 빠른 음성 테스트입니다",
        "이것은 빠른 속도로 재생되는 음성입니다",
        "속도가 빨라서 더 효율적으로 들을 수 있습니다",
        "테스트가 완료되었습니다"
    ]
    
    print(f"🎵 음성 설정: {fast_voice_config.name}")
    print(f"   속도: {fast_voice_config.rate}")
    print(f"   볼륨: {fast_voice_config.volume}")
    print(f"   언어: {fast_voice_config.language}")
    print()
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        ensure_spoken_hybrid(text, voice_config=fast_voice_config)
        print()
    
    print("✅ 빠른 음성 테스트 완료!")

if __name__ == "__main__":
    test_fast_voice() 