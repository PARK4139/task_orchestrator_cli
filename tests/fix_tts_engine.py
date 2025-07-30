#!/usr/bin/env python3
"""
TTS 엔진 문제 해결
"""

import time
from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def test_tts_engine_fix():
    """TTS 엔진 문제 해결 테스트"""
    print("🔧 TTS 엔진 문제 해결")
    print("=" * 40)
    
    # 안정적인 설정
    config = VoiceConfig(
        name="엔진 수정 테스트",
        rate=150,  # 안정적인 속도
        volume=0.3,  # 30% 볼륨
        language="ko"
    )
    
    print("🎵 설정:")
    print(f"   속도: {config.rate}")
    print(f"   볼륨: {config.volume * 100}%")
    print()
    
    # 여러 번 테스트
    test_texts = ["첫번째", "두번째", "세번째"]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        ensure_spoken_hybrid(text, voice_config=config)
        time.sleep(2)  # 재생 간격
        print()
    
    print("✅ TTS 엔진 수정 완료!")

def test_single_engine():
    """단일 엔진 테스트"""
    print("\n🔊 단일 엔진 테스트")
    print("=" * 30)
    
    try:
        import pyttsx3
        
        # pyttsx3 직접 테스트
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.3)
        
        test_texts = ["엔진1", "엔진2", "엔진3"]
        
        for i, text in enumerate(test_texts, 1):
            print(f"🔊 pyttsx3 테스트 {i}: '{text}'")
            engine.say(text)
            engine.runAndWait()
            time.sleep(1)
            print()
        
        print("✅ pyttsx3 테스트 완료!")
        
    except Exception as e:
        print(f"❌ pyttsx3 실패: {e}")

def test_windows_sapi_direct():
    """Windows SAPI 직접 테스트"""
    print("\n🔊 Windows SAPI 직접 테스트")
    print("=" * 30)
    
    import subprocess
    
    test_texts = ["SAPI1", "SAPI2", "SAPI3"]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 SAPI 테스트 {i}: '{text}'")
        
        try:
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 0; $synth.Volume = 30; $synth.Speak('{text}')"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ SAPI {i} 성공")
            else:
                print(f"❌ SAPI {i} 실패")
                
        except Exception as e:
            print(f"❌ SAPI {i} 오류: {e}")
        
        time.sleep(1)
        print()

def main():
    """메인 함수"""
    print("🔧 TTS 엔진 문제 해결 시작")
    print("=" * 50)
    
    # 1. 하이브리드 TTS 테스트
    test_tts_engine_fix()
    
    # 2. 단일 엔진 테스트
    test_single_engine()
    
    # 3. Windows SAPI 직접 테스트
    test_windows_sapi_direct()
    
    print("\n🔧 엔진 문제 해결 완료!")

if __name__ == "__main__":
    main() 