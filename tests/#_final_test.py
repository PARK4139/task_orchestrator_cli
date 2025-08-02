#!/usr/bin/env python3
"""
최종 TTS 테스트
"""

from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def final_test():
    """최종 테스트"""
    print("🎧 최종 TTS 테스트")
    print("=" * 30)
    
    # 최적 설정
    config = VoiceConfig(
        name="최종 테스트",
        rate=250,  # 빠른 속도
        volume=0.1,  # 10% 볼륨
        language="ko"
    )
    
    print("🎵 설정:")
    print(f"   속도: {config.rate} (빠름)")
    print(f"   볼륨: {config.volume * 100}%")
    print()
    
    # 테스트
    test_text = "테스트 완료"
    print(f"🔊 테스트: '{test_text}'")
    ensure_spoken_hybrid(test_text, voice_config=config)
    
    print("\n✅ 최종 테스트 완료!")

if __name__ == "__main__":
    final_test() 