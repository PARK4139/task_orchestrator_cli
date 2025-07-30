#!/usr/bin/env python3
"""
낮은 볼륨(20%)으로 TTS 테스트
"""

import time
from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def test_low_volume_tts():
    """낮은 볼륨으로 TTS 테스트"""
    print("🔊 낮은 볼륨(20%) TTS 테스트 시작")
    print("=" * 40)
    
    # 낮은 볼륨 음성 설정
    low_volume_config = VoiceConfig(
        name="낮은 볼륨 테스트",
        rate=150,  # 적당한 속도
        volume=0.2,  # 20% 볼륨
        language="ko"
    )
    
    # 테스트 텍스트들
    test_texts = [
        "안녕하세요, 낮은 볼륨 테스트입니다",
        "이제 소리가 적당한가요?",
        "볼륨이 20퍼센트로 설정되었습니다",
        "테스트가 완료되었습니다"
    ]
    
    print(f"🎵 음성 설정: {low_volume_config.name}")
    print(f"   속도: {low_volume_config.rate}")
    print(f"   볼륨: {low_volume_config.volume * 100}%")
    print(f"   언어: {low_volume_config.language}")
    print()
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        ensure_spoken_hybrid(text, voice_config=low_volume_config)
        time.sleep(1)  # 재생 간격
        print()
    
    print("✅ 낮은 볼륨 TTS 테스트 완료!")

def test_medium_volume_tts():
    """중간 볼륨(50%)으로 TTS 테스트"""
    print("\n🔊 중간 볼륨(50%) TTS 테스트")
    print("=" * 40)
    
    # 중간 볼륨 음성 설정
    medium_volume_config = VoiceConfig(
        name="중간 볼륨 테스트",
        rate=150,  # 적당한 속도
        volume=0.5,  # 50% 볼륨
        language="ko"
    )
    
    # 테스트 텍스트들
    test_texts = [
        "안녕하세요, 중간 볼륨 테스트입니다",
        "이 볼륨이 적당한가요?",
        "볼륨이 50퍼센트로 설정되었습니다",
        "테스트가 완료되었습니다"
    ]
    
    print(f"🎵 음성 설정: {medium_volume_config.name}")
    print(f"   속도: {medium_volume_config.rate}")
    print(f"   볼륨: {medium_volume_config.volume * 100}%")
    print(f"   언어: {medium_volume_config.language}")
    print()
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        ensure_spoken_hybrid(text, voice_config=medium_volume_config)
        time.sleep(1)  # 재생 간격
        print()
    
    print("✅ 중간 볼륨 TTS 테스트 완료!")

def test_custom_volume_tts():
    """사용자 지정 볼륨으로 TTS 테스트"""
    print("\n🔊 사용자 지정 볼륨 TTS 테스트")
    print("=" * 40)
    
    # 사용자가 원하는 볼륨 설정
    custom_volume = 0.3  # 30% 볼륨 (원하는 값으로 변경 가능)
    
    custom_volume_config = VoiceConfig(
        name="사용자 지정 볼륨 테스트",
        rate=150,  # 적당한 속도
        volume=custom_volume,  # 사용자 지정 볼륨
        language="ko"
    )
    
    # 테스트 텍스트들
    test_texts = [
        "안녕하세요, 사용자 지정 볼륨 테스트입니다",
        f"볼륨이 {custom_volume * 100}퍼센트로 설정되었습니다",
        "이 볼륨이 적당한가요?",
        "테스트가 완료되었습니다"
    ]
    
    print(f"🎵 음성 설정: {custom_volume_config.name}")
    print(f"   속도: {custom_volume_config.rate}")
    print(f"   볼륨: {custom_volume_config.volume * 100}%")
    print(f"   언어: {custom_volume_config.language}")
    print()
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        ensure_spoken_hybrid(text, voice_config=custom_volume_config)
        time.sleep(1)  # 재생 간격
        print()
    
    print("✅ 사용자 지정 볼륨 TTS 테스트 완료!")

def main():
    """메인 테스트 함수"""
    print("🎧 다양한 볼륨으로 TTS 테스트")
    print("=" * 50)
    
    # 1. 낮은 볼륨(20%) 테스트
    test_low_volume_tts()
    
    # 2. 중간 볼륨(50%) 테스트
    test_medium_volume_tts()
    
    # 3. 사용자 지정 볼륨(30%) 테스트
    test_custom_volume_tts()
    
    print("\n📋 볼륨 설정 가이드:")
    print("- 0.1 (10%): 매우 조용함")
    print("- 0.2 (20%): 조용함")
    print("- 0.3 (30%): 적당함")
    print("- 0.5 (50%): 보통")
    print("- 0.7 (70%): 약간 큼")
    print("- 0.9 (90%): 큼")
    print("- 1.0 (100%): 매우 큼")

if __name__ == "__main__":
    main() 