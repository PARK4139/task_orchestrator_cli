#!/usr/bin/env python3
"""
소리 디버깅 테스트
"""

import subprocess
import time
from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def check_audio_devices():
    """오디오 장치 확인"""
    print("🔍 오디오 장치 확인")
    print("=" * 30)
    
    try:
        result = subprocess.run([
            "powershell", "-Command", 
            "Get-WmiObject -Class Win32_SoundDevice | Select-Object Name, Status"
        ], capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("📋 오디오 장치:")
            print(result.stdout)
        else:
            print("❌ 오디오 장치 확인 실패")
            
    except Exception as e:
        print(f"❌ 오류: {e}")

def test_simple_tts():
    """간단한 TTS 테스트"""
    print("\n🔊 간단한 TTS 테스트")
    print("=" * 30)
    
    try:
        # 기본 설정으로 테스트
        config = VoiceConfig(
            name="디버그 테스트",
            rate=150,
            volume=0.5,  # 50%로 높임
            language="ko"
        )
        
        print("🎵 설정:")
        print(f"   속도: {config.rate}")
        print(f"   볼륨: {config.volume * 100}%")
        print()
        
        # 테스트
        test_text = "테스트"
        print(f"🔊 테스트: '{test_text}'")
        ensure_spoken_hybrid(test_text, voice_config=config)
        
        print("✅ TTS 테스트 완료")
        
    except Exception as e:
        print(f"❌ TTS 테스트 실패: {e}")

def test_windows_sapi():
    """Windows SAPI 직접 테스트"""
    print("\n🔊 Windows SAPI 직접 테스트")
    print("=" * 30)
    
    try:
        result = subprocess.run([
            "powershell", "-Command",
            "Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 0; $synth.Volume = 50; $synth.Speak('Windows SAPI 테스트')"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Windows SAPI 성공")
        else:
            print(f"❌ Windows SAPI 실패: {result.stderr}")
            
    except Exception as e:
        print(f"❌ Windows SAPI 오류: {e}")

def test_pyttsx3():
    """pyttsx3 직접 테스트"""
    print("\n🔊 pyttsx3 직접 테스트")
    print("=" * 30)
    
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.5)
        engine.say("pyttsx3 테스트")
        engine.runAndWait()
        print("✅ pyttsx3 성공")
        
    except Exception as e:
        print(f"❌ pyttsx3 실패: {e}")

def main():
    """메인 함수"""
    print("🔧 소리 디버깅 시작")
    print("=" * 50)
    
    # 1. 오디오 장치 확인
    check_audio_devices()
    
    # 2. 간단한 TTS 테스트
    test_simple_tts()
    
    # 3. Windows SAPI 테스트
    test_windows_sapi()
    
    # 4. pyttsx3 테스트
    test_pyttsx3()
    
    print("\n🔧 디버깅 완료!")

if __name__ == "__main__":
    main() 