#!/usr/bin/env python3
"""
간단한 TTS 테스트 - "안녕하세요"만
"""

from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def test_simple_tts():
    """간단한 TTS 테스트"""
    print("🔊 간단한 TTS 테스트")
    print("=" * 30)
    
    # 10% 볼륨 설정
    config = VoiceConfig(
        name="간단 테스트",
        rate=150,
        volume=0.1,  # 10% 볼륨
        language="ko"
    )
    
    print("🎵 음성 설정:")
    print(f"   볼륨: {config.volume * 100}%")
    print(f"   속도: {config.rate}")
    print()
    
    # 간단한 테스트
    print("🔊 테스트: '안녕하세요'")
    ensure_spoken_hybrid("안녕하세요", voice_config=config)
    
    print("\n✅ 테스트 완료!")

if __name__ == "__main__":
    test_simple_tts() 