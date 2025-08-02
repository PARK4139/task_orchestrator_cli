#!/usr/bin/env python3
"""
헤드폰에서 10% 볼륨으로 최종 TTS 테스트
"""

import time
from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def test_final_bluetooth_tts():
    """헤드폰에서 10% 볼륨으로 최종 테스트"""
    print("🎧 헤드폰에서 10% 볼륨 TTS 최종 테스트")
    print("=" * 50)
    
    # 10% 볼륨 설정
    final_config = VoiceConfig(
        name="헤드폰 최종 테스트",
        rate=150,  # 적당한 속도
        volume=0.1,  # 10% 볼륨
        language="ko"
    )
    
    # 간단한 테스트 텍스트들
    test_texts = [
        "안녕하세요, 헤드폰 테스트입니다",
        "이제 헤드폰에서 소리가 들리나요?",
        "볼륨이 10퍼센트로 설정되었습니다",
        "테스트가 완료되었습니다"
    ]
    
    print(f"🎵 음성 설정: {final_config.name}")
    print(f"   속도: {final_config.rate}")
    print(f"   볼륨: {final_config.volume * 100}%")
    print(f"   언어: {final_config.language}")
    print()
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        ensure_spoken_hybrid(text, voice_config=final_config)
        time.sleep(2)  # 재생 간격
        print()
    
    print("✅ 헤드폰 TTS 최종 테스트 완료!")
    print("🎧 헤드폰에서 소리가 들렸다면 정상 작동입니다!")

def test_quick_volume_check():
    """빠른 볼륨 체크"""
    print("\n🔊 빠른 볼륨 체크")
    print("=" * 30)
    
    volumes = [0.05, 0.1, 0.15]  # 5%, 10%, 15%
    
    for volume in volumes:
        print(f"\n🎵 볼륨 {volume * 100}% 테스트")
        print("-" * 25)
        
        config = VoiceConfig(
            name=f"볼륨 {volume * 100}% 체크",
            rate=150,
            volume=volume,
            language="ko"
        )
        
        test_text = f"볼륨이 {volume * 100}퍼센트입니다"
        print(f"🔊 테스트: '{test_text}'")
        ensure_spoken_hybrid(test_text, voice_config=config)
        time.sleep(3)  # 재생 간격

def main():
    """메인 함수"""
    print("🎧 헤드폰 TTS 최종 확인")
    print("=" * 50)
    
    # 1. 최종 테스트
    test_final_bluetooth_tts()
    
    # 2. 빠른 볼륨 체크
    test_quick_volume_check()
    
    print("\n📋 설정 완료!")
    print("- 볼륨: 10% (0.1)")
    print("- 속도: 150")
    print("- 언어: 한국어")
    print("- 출력: 블루투스 헤드폰")

if __name__ == "__main__":
    main() 