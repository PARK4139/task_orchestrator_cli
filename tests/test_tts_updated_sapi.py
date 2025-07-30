#!/usr/bin/env python3
"""
수정된 SAPI 설정 테스트
"""

from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def test_updated_sapi():
    """수정된 SAPI 설정 테스트"""
    print("🔊 수정된 SAPI 설정 테스트")
    print("=" * 40)
    
    # 기본 설정으로 테스트
    config = VoiceConfig(
        name="수정된 SAPI 테스트",
        rate=150,
        volume=0.3,  # 30% 볼륨
        language="ko"
    )
    
    print("🎵 설정:")
    print(f"   속도: {config.rate}")
    print(f"   볼륨: {config.volume * 100}%")
    print("   SAPI 속도: 1.5 (실패시 1.0)")
    print("   SAPI 볼륨: 30%")
    print()
    
    # 테스트 텍스트들
    test_texts = [
        "안녕하세요, 수정된 SAPI 테스트입니다",
        "속도가 1.5로 설정되었습니다",
        "볼륨이 30퍼센트로 설정되었습니다",
        "헤드폰에서 들리나요?",
        "테스트가 완료되었습니다"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        ensure_spoken_hybrid(text, voice_config=config)
        print()
    
    print("✅ 수정된 SAPI 테스트 완료!")

def test_sapi_priority():
    """SAPI 우선 테스트"""
    print("\n🔊 SAPI 우선 테스트")
    print("=" * 30)
    
    # SAPI만 강제 사용
    config = VoiceConfig(
        name="SAPI 우선 테스트",
        rate=150,
        volume=0.3,
        language="ko"
    )
    
    test_text = "SAPI 우선 테스트입니다"
    print(f"🔊 테스트: '{test_text}'")
    
    # SAPI 강제 사용
    from pkg_py.functions_split.ensure_spoken_hybrid import _hybrid_tts
    _hybrid_tts.speak(test_text, force_method="Windows SAPI")
    
    print("✅ SAPI 우선 테스트 완료!")

def main():
    """메인 함수"""
    print("🎧 수정된 SAPI 설정 테스트 시작")
    print("=" * 50)
    
    # 1. 수정된 SAPI 설정 테스트
    test_updated_sapi()
    
    # 2. SAPI 우선 테스트
    test_sapi_priority()
    
    print("\n🎉 수정된 SAPI 테스트 완료!")
    print("SAPI 속도 1.5와 볼륨 30%가 적용되었습니다!")

if __name__ == "__main__":
    main() 