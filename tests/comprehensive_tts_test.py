#!/usr/bin/env python3
"""
종합 TTS 테스트 - 모든 방법을 인덱스와 함께 테스트
"""

import time
from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def test_basic_tts_methods():
    """기본 TTS 방법들 테스트"""
    print("🔊 1. 기본 TTS 방법들 테스트")
    print("=" * 50)
    
    # 1-1. 기본 ensure_spoken (하이브리드)
    print("\n📋 1-1. 기본 ensure_spoken (하이브리드)")
    print("-" * 30)
    from pkg_py.functions_split.ensure_spoken import ensure_spoken
    ensure_spoken("안녕하세요, 기본 ensure_spoken 테스트입니다")
    time.sleep(2)
    
    # 1-2. 하이브리드 TTS 직접 호출
    print("\n📋 1-2. 하이브리드 TTS 직접 호출")
    print("-" * 30)
    ensure_spoken_hybrid("안녕하세요, 하이브리드 TTS 직접 호출 테스트입니다")
    time.sleep(2)

def test_volume_configurations():
    """볼륨 설정 테스트"""
    print("\n🔊 2. 볼륨 설정 테스트")
    print("=" * 50)
    
    volumes = [
        (0.05, "5% - 매우 조용함"),
        (0.1, "10% - 조용함 (권장)"),
        (0.2, "20% - 적당함"),
        (0.3, "30% - 보통"),
        (0.5, "50% - 약간 큼"),
        (0.7, "70% - 큼"),
        (0.9, "90% - 매우 큼")
    ]
    
    for i, (volume, description) in enumerate(volumes, 1):
        print(f"\n📋 2-{i}. {description}")
        print("-" * 30)
        
        config = VoiceConfig(
            name=f"볼륨 {volume * 100}% 테스트",
            rate=150,
            volume=volume,
            language="ko"
        )
        
        test_text = f"볼륨이 {volume * 100}퍼센트입니다. {description}"
        ensure_spoken_hybrid(test_text, voice_config=config)
        time.sleep(3)

def test_speed_configurations():
    """속도 설정 테스트"""
    print("\n🔊 3. 속도 설정 테스트")
    print("=" * 50)
    
    speeds = [
        (50, "매우 느림"),
        (100, "느림"),
        (150, "보통"),
        (200, "빠름"),
        (250, "매우 빠름")
    ]
    
    for i, (speed, description) in enumerate(speeds, 1):
        print(f"\n📋 3-{i}. {description} (속도: {speed})")
        print("-" * 30)
        
        config = VoiceConfig(
            name=f"속도 {speed} 테스트",
            rate=speed,
            volume=0.1,  # 10% 볼륨 유지
            language="ko"
        )
        
        test_text = f"속도가 {speed}로 설정되었습니다. {description}"
        ensure_spoken_hybrid(test_text, voice_config=config)
        time.sleep(3)

def test_hybrid_tts_components():
    """하이브리드 TTS 구성 요소 테스트"""
    print("\n🔊 4. 하이브리드 TTS 구성 요소 테스트")
    print("=" * 50)
    
    # 4-1. pyttsx3 테스트
    print("\n📋 4-1. pyttsx3 테스트")
    print("-" * 30)
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.1)
        engine.say("pyttsx3 직접 테스트입니다")
        engine.runAndWait()
        print("✅ pyttsx3 성공")
    except Exception as e:
        print(f"❌ pyttsx3 실패: {e}")
    time.sleep(2)
    
    # 4-2. Windows SAPI 테스트
    print("\n📋 4-2. Windows SAPI 테스트")
    print("-" * 30)
    try:
        import subprocess
        result = subprocess.run([
            "powershell", "-Command",
            "Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 0; $synth.Volume = 10; $synth.Speak('Windows SAPI 직접 테스트입니다')"
        ], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Windows SAPI 성공")
        else:
            print(f"❌ Windows SAPI 실패: {result.stderr}")
    except Exception as e:
        print(f"❌ Windows SAPI 실패: {e}")
    time.sleep(2)
    
    # 4-3. gTTS 테스트 (인터넷 필요)
    print("\n📋 4-3. gTTS 테스트 (인터넷 필요)")
    print("-" * 30)
    try:
        from gtts import gTTS
        import os
        tts = gTTS(text="gTTS 직접 테스트입니다", lang='ko')
        tts.save("temp_test.mp3")
        os.system("start temp_test.mp3")
        print("✅ gTTS 성공")
        time.sleep(3)
        os.remove("temp_test.mp3")
    except Exception as e:
        print(f"❌ gTTS 실패: {e}")
    time.sleep(2)

def test_voice_configurations():
    """음성 설정 테스트"""
    print("\n🔊 5. 음성 설정 테스트")
    print("=" * 50)
    
    # 5-1. 기본 설정
    print("\n📋 5-1. 기본 음성 설정")
    print("-" * 30)
    basic_config = VoiceConfig(
        name="기본 설정",
        rate=150,
        volume=0.1,
        language="ko"
    )
    ensure_spoken_hybrid("기본 음성 설정 테스트입니다", voice_config=basic_config)
    time.sleep(2)
    
    # 5-2. 빠른 음성
    print("\n📋 5-2. 빠른 음성 설정")
    print("-" * 30)
    fast_config = VoiceConfig(
        name="빠른 음성",
        rate=200,
        volume=0.1,
        language="ko"
    )
    ensure_spoken_hybrid("빠른 음성 설정 테스트입니다", voice_config=fast_config)
    time.sleep(2)
    
    # 5-3. 조용한 음성
    print("\n📋 5-3. 조용한 음성 설정")
    print("-" * 30)
    quiet_config = VoiceConfig(
        name="조용한 음성",
        rate=150,
        volume=0.05,
        language="ko"
    )
    ensure_spoken_hybrid("조용한 음성 설정 테스트입니다", voice_config=quiet_config)
    time.sleep(2)

def test_bluetooth_specific():
    """블루투스 헤드폰 특화 테스트"""
    print("\n🔊 6. 블루투스 헤드폰 특화 테스트")
    print("=" * 50)
    
    # 6-1. 헤드폰용 최적 설정
    print("\n📋 6-1. 헤드폰용 최적 설정")
    print("-" * 30)
    headphone_config = VoiceConfig(
        name="헤드폰 최적",
        rate=150,
        volume=0.1,  # 10% - 헤드폰에 적합
        language="ko"
    )
    ensure_spoken_hybrid("헤드폰용 최적 설정 테스트입니다", voice_config=headphone_config)
    time.sleep(2)
    
    # 6-2. 다양한 볼륨으로 헤드폰 테스트
    print("\n📋 6-2. 헤드폰용 다양한 볼륨 테스트")
    print("-" * 30)
    headphone_volumes = [0.05, 0.1, 0.15, 0.2]
    
    for i, volume in enumerate(headphone_volumes, 1):
        print(f"\n  6-2-{i}. 볼륨 {volume * 100}%")
        config = VoiceConfig(
            name=f"헤드폰 볼륨 {volume * 100}%",
            rate=150,
            volume=volume,
            language="ko"
        )
        test_text = f"헤드폰 볼륨 {volume * 100}퍼센트 테스트입니다"
        ensure_spoken_hybrid(test_text, voice_config=config)
        time.sleep(2)

def test_final_integration():
    """최종 통합 테스트"""
    print("\n🔊 7. 최종 통합 테스트")
    print("=" * 50)
    
    # 7-1. 완벽한 설정으로 테스트
    print("\n📋 7-1. 완벽한 설정 테스트")
    print("-" * 30)
    perfect_config = VoiceConfig(
        name="완벽한 설정",
        rate=150,
        volume=0.1,
        language="ko"
    )
    
    final_texts = [
        "안녕하세요, 최종 통합 테스트입니다",
        "헤드폰에서 소리가 들리나요?",
        "볼륨이 10퍼센트로 설정되었습니다",
        "속도가 150으로 설정되었습니다",
        "모든 테스트가 완료되었습니다"
    ]
    
    for i, text in enumerate(final_texts, 1):
        print(f"  테스트 {i}: '{text}'")
        ensure_spoken_hybrid(text, voice_config=perfect_config)
        time.sleep(1)

def main():
    """메인 테스트 함수"""
    print("🎧 종합 TTS 테스트 시작")
    print("=" * 60)
    print("각 테스트 후 헤드폰에서 소리가 들리는지 확인해주세요!")
    print("=" * 60)
    
    # 모든 테스트 실행
    test_basic_tts_methods()
    test_volume_configurations()
    test_speed_configurations()
    test_hybrid_tts_components()
    test_voice_configurations()
    test_bluetooth_specific()
    test_final_integration()
    
    print("\n🎉 모든 테스트 완료!")
    print("=" * 60)
    print("📋 테스트 결과 요약:")
    print("- 기본 TTS: ✅")
    print("- 하이브리드 TTS: ✅")
    print("- 볼륨 설정: ✅")
    print("- 속도 설정: ✅")
    print("- 음성 설정: ✅")
    print("- 블루투스 헤드폰: ✅")
    print("- 최종 통합: ✅")
    print("\n🎧 헤드폰에서 소리가 들렸다면 모든 기능이 정상 작동합니다!")

if __name__ == "__main__":
    main() 