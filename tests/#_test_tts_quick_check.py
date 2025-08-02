#!/usr/bin/env python3
"""
빠른 TTS 상태 확인
"""

import subprocess
import time

def quick_sapi_test():
    """빠른 SAPI 테스트"""
    print("🔊 빠른 SAPI 테스트")
    print("=" * 30)
    
    test_text = "안녕하세요, 빠른 테스트입니다"
    print(f"🔊 테스트: '{test_text}'")
    
    try:
        result = subprocess.run([
            "powershell", "-Command",
            f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 1.5; $synth.Volume = 30; $synth.Speak('{test_text}')"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ SAPI 성공")
        else:
            print(f"❌ SAPI 실패: {result.stderr}")
            
    except Exception as e:
        print(f"❌ SAPI 오류: {e}")

def quick_hybrid_test():
    """빠른 하이브리드 테스트"""
    print("\n🔊 빠른 하이브리드 테스트")
    print("=" * 30)
    
    try:
        from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid
        
        config = VoiceConfig(
            name="빠른 테스트",
            rate=150,
            volume=0.5,  # 50%로 높임
            language="ko"
        )
        
        test_text = "안녕하세요, 하이브리드 테스트입니다"
        print(f"🔊 테스트: '{test_text}'")
        ensure_spoken_hybrid(test_text, voice_config=config)
        
    except Exception as e:
        print(f"❌ 하이브리드 테스트 실패: {e}")

def check_audio_devices():
    """오디오 장치 확인"""
    print("\n🔍 오디오 장치 확인")
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
    print("🎧 빠른 TTS 상태 확인")
    print("=" * 50)
    
    # 1. 오디오 장치 확인
    check_audio_devices()
    
    # 2. 빠른 SAPI 테스트
    quick_sapi_test()
    
    # 3. 빠른 하이브리드 테스트
    quick_hybrid_test()
    
    # 4. Windows 소리 설정 열기
    open_sound_settings()
    
    print("\n🔧 빠른 확인 완료!")
    print("어떤 테스트에서 소리가 들렸는지 알려주세요!")

if __name__ == "__main__":
    main() 