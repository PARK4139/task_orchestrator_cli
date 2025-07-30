#!/usr/bin/env python3
"""
헤드폰 디버깅 테스트
"""

import subprocess
import time

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

def test_sapi_direct():
    """SAPI 직접 테스트"""
    print("\n🔊 SAPI 직접 테스트")
    print("=" * 30)
    
    test_texts = [
        "안녕하세요, SAPI 직접 테스트입니다",
        "헤드폰에서 들리나요?",
        "테스트가 완료되었습니다"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        
        try:
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 1.5; $synth.Volume = 30; $synth.Speak('{text}')"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ SAPI 테스트 {i} 성공")
            else:
                print(f"❌ SAPI 테스트 {i} 실패")
                print(f"오류: {result.stderr}")
                
        except Exception as e:
            print(f"❌ SAPI 테스트 {i} 오류: {e}")
        
        time.sleep(2)
        print()

def test_pyttsx3_direct():
    """pyttsx3 직접 테스트"""
    print("\n🔊 pyttsx3 직접 테스트")
    print("=" * 30)
    
    try:
        import pyttsx3
        
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.3)
        
        test_texts = [
            "안녕하세요, pyttsx3 직접 테스트입니다",
            "헤드폰에서 들리나요?",
            "테스트가 완료되었습니다"
        ]
        
        for i, text in enumerate(test_texts, 1):
            print(f"🔊 테스트 {i}: '{text}'")
            engine.say(text)
            engine.runAndWait()
            time.sleep(2)
            print()
        
        print("✅ pyttsx3 직접 테스트 완료!")
        
    except Exception as e:
        print(f"❌ pyttsx3 실패: {e}")

def test_hybrid_tts():
    """하이브리드 TTS 테스트"""
    print("\n🔊 하이브리드 TTS 테스트")
    print("=" * 30)
    
    try:
        from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid
        
        config = VoiceConfig(
            name="헤드폰 디버그 테스트",
            rate=150,
            volume=0.5,  # 50%로 높임
            language="ko"
        )
        
        test_texts = [
            "안녕하세요, 하이브리드 테스트입니다",
            "헤드폰에서 들리나요?",
            "테스트가 완료되었습니다"
        ]
        
        for i, text in enumerate(test_texts, 1):
            print(f"🔊 테스트 {i}: '{text}'")
            ensure_spoken_hybrid(text, voice_config=config)
            time.sleep(2)
            print()
        
        print("✅ 하이브리드 TTS 테스트 완료!")
        
    except Exception as e:
        print(f"❌ 하이브리드 TTS 실패: {e}")

def open_sound_settings():
    """소리 설정 열기"""
    print("\n⚙️ Windows 소리 설정을 열어드립니다...")
    
    try:
        subprocess.run(["start", "ms-settings:sound"], shell=True)
        print("✅ Windows 소리 설정이 열렸습니다.")
        print("\n📋 다음 단계를 따라해주세요:")
        print("1. '출력' 섹션에서 '헤드폰(2- QCY H3 ANC HEADSET)' 선택")
        print("2. '기본 장치로 설정' 클릭")
        print("3. '기본 통신 장치로 설정' 클릭")
        print("4. 볼륨을 100%로 설정")
        print("5. 다른 장치들(LG HDR WQHD, Realtek 등) 비활성화")
        
    except Exception as e:
        print(f"❌ 소리 설정 열기 실패: {e}")

def main():
    """메인 함수"""
    print("🎧 헤드폰 디버깅 시작")
    print("=" * 50)
    
    # 1. 오디오 장치 확인
    check_audio_devices()
    
    # 2. SAPI 직접 테스트
    test_sapi_direct()
    
    # 3. pyttsx3 직접 테스트
    test_pyttsx3_direct()
    
    # 4. 하이브리드 TTS 테스트
    test_hybrid_tts()
    
    # 5. Windows 소리 설정 열기
    open_sound_settings()
    
    print("\n🔧 헤드폰 디버깅 완료!")
    print("어떤 테스트에서 소리가 들렸는지 알려주세요!")

if __name__ == "__main__":
    main() 