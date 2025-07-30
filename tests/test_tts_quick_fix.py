#!/usr/bin/env python3
"""
빠른 헤드폰 문제 해결 테스트
"""

import subprocess
import time

def check_audio_devices():
    """오디오 디바이스 확인"""
    print("🔊 오디오 디바이스 확인")
    print("=" * 40)
    
    try:
        result = subprocess.run([
            "powershell", "-Command",
            "Get-WmiObject -Class Win32_SoundDevice | Select-Object Name, Status"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 오디오 디바이스:")
            print(result.stdout)
        else:
            print("❌ 오디오 디바이스 확인 실패")
            
    except Exception as e:
        print(f"❌ 오류: {e}")

def test_sapi_direct():
    """SAPI 직접 테스트"""
    print("\n🔊 SAPI 직접 테스트")
    print("=" * 40)
    
    test_texts = [
        "안녕하세요, SAPI 직접 테스트입니다",
        "헤드폰에서 들리나요?",
        "볼륨 30%, 속도 1.2로 설정되었습니다"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        
        try:
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 1.2; $synth.Volume = 30; $synth.Speak('{text}')"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ SAPI 테스트 {i} 성공")
            else:
                print(f"❌ SAPI 테스트 {i} 실패")
                
        except Exception as e:
            print(f"❌ SAPI 테스트 {i} 오류: {e}")
        
        time.sleep(2)
        print()

def test_different_volumes():
    """다양한 볼륨 테스트"""
    print("\n🔊 다양한 볼륨 테스트")
    print("=" * 40)
    
    volumes = [20, 30, 50, 70]
    
    for volume in volumes:
        print(f"🔊 볼륨 {volume}% 테스트")
        
        try:
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 1.2; $synth.Volume = {volume}; $synth.Speak('볼륨 {volume}퍼센트 테스트입니다')"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ 볼륨 {volume}% 성공")
            else:
                print(f"❌ 볼륨 {volume}% 실패")
                
        except Exception as e:
            print(f"❌ 볼륨 {volume}% 오류: {e}")
        
        time.sleep(2)
        print()

def open_sound_settings():
    """소리 설정 열기"""
    print("\n🔊 Windows 소리 설정 열기")
    print("=" * 40)
    
    try:
        result = subprocess.run([
            "start", "ms-settings:sound"
        ], shell=True, capture_output=True, text=True)
        
        print("✅ Windows 소리 설정이 열렸습니다")
        print("다음 단계를 따라주세요:")
        print("1. '출력' 섹션에서 헤드폰을 찾으세요")
        print("2. 헤드폰을 '기본 장치'로 설정하세요")
        print("3. '기본 통신 장치'로도 설정하세요")
        print("4. 볼륨을 확인하세요")
        
    except Exception as e:
        print(f"❌ 소리 설정 열기 실패: {e}")

def main():
    """메인 함수"""
    print("🎧 빠른 헤드폰 문제 해결 테스트")
    print("=" * 50)
    
    # 1. 오디오 디바이스 확인
    check_audio_devices()
    
    # 2. SAPI 직접 테스트
    test_sapi_direct()
    
    # 3. 다양한 볼륨 테스트
    test_different_volumes()
    
    # 4. 소리 설정 열기
    open_sound_settings()
    
    print("\n🎉 빠른 해결 테스트 완료!")
    print("어떤 볼륨에서 헤드폰에서 소리가 들렸는지 알려주세요!")

if __name__ == "__main__":
    main() 