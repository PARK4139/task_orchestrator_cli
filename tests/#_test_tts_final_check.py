#!/usr/bin/env python3
"""
최종 TTS 확인 테스트
"""

from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def final_tts_check():
    """최종 TTS 확인"""
    print("🔊 최종 TTS 확인")
    print("=" * 30)
    
    # 최적 설정
    config = VoiceConfig(
        name="최종 확인",
        rate=150,
        volume=0.3,  # 30% 볼륨
        language="ko"
    )
    
    print("🎵 설정:")
    print(f"   속도: {config.rate}")
    print(f"   볼륨: {config.volume * 100}%")
    print("   우선순위: Windows SAPI → pyttsx3 → gTTS")
    print()
    
    # 테스트
    test_text = "안녕하세요, 최종 확인 테스트입니다"
    print(f"🔊 테스트: '{test_text}'")
    ensure_spoken_hybrid(test_text, voice_config=config)
    
    print("\n✅ 최종 확인 완료!")
    print("헤드폰에서 소리가 들렸다면 TTS가 정상 작동합니다!")

if __name__ == "__main__":
    final_tts_check() 