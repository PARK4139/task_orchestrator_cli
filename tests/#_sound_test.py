#!/usr/bin/env python3
"""
소리 테스트
"""

from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def sound_test():
    """소리 테스트"""
    print("🔊 소리 테스트")
    print("=" * 30)
    
    # 소리 설정
    config = VoiceConfig(
        name="소리 테스트",
        rate=200,  # 적당한 속도
        volume=0.15,  # 15% 볼륨
        language="ko"
    )
    
    print("🎵 설정:")
    print(f"   속도: {config.rate}")
    print(f"   볼륨: {config.volume * 100}%")
    print()
    
    # 소리 테스트
    test_text = "소리 테스트"
    print(f"🔊 테스트: '{test_text}'")
    ensure_spoken_hybrid(test_text, voice_config=config)
    
    print("\n✅ 소리 테스트 완료!")

if __name__ == "__main__":
    sound_test() 