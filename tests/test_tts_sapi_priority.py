#!/usr/bin/env python3
"""
SAPI 우선 사용 테스트
"""

from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def test_sapi_priority():
    """SAPI 우선 사용 테스트"""
    print("🔊 SAPI 우선 사용 테스트")
    print("=" * 40)
    
    # 기본 설정
    config = VoiceConfig(
        name="SAPI 우선 테스트",
        rate=150,
        volume=0.3,  # 30% 볼륨
        language="ko"
    )
    
    print("🎵 설정:")
    print(f"   속도: {config.rate}")
    print(f"   볼륨: {config.volume * 100}%")
    print("   우선순위: Windows SAPI → pyttsx3 → gTTS")
    print()
    
    # 테스트 텍스트들
    test_texts = [
        "안녕하세요, SAPI 우선 테스트입니다",
        "이제 SAPI가 먼저 시도됩니다",
        "헤드폰에서 들리나요?",
        "테스트가 완료되었습니다"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        ensure_spoken_hybrid(text, voice_config=config)
        print()
    
    print("✅ SAPI 우선 테스트 완료!")

def test_sapi_only():
    """SAPI만 강제 사용 테스트"""
    print("\n🔊 SAPI만 강제 사용 테스트")
    print("=" * 30)
    
    from pkg_py.functions_split.ensure_spoken_hybrid import _hybrid_tts
    
    test_texts = [
        "안녕하세요, SAPI만 사용 테스트입니다",
        "SAPI가 강제로 사용됩니다",
        "헤드폰에서 들리나요?",
        "테스트가 완료되었습니다"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        # SAPI만 강제 사용
        _hybrid_tts.speak(text, force_method="Windows SAPI")
        print()
    
    print("✅ SAPI만 사용 테스트 완료!")

def main():
    """메인 함수"""
    print("🎧 SAPI 우선 사용 테스트 시작")
    print("=" * 50)
    
    # 1. SAPI 우선 사용 테스트
    test_sapi_priority()
    
    # 2. SAPI만 강제 사용 테스트
    test_sapi_only()
    
    print("\n🎉 SAPI 우선 사용 테스트 완료!")
    print("이제 SAPI가 우선적으로 사용되어 헤드폰에서 소리가 들릴 것입니다!")

if __name__ == "__main__":
    main() 