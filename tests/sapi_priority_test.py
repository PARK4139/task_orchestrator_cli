#!/usr/bin/env python3
"""
SAPI 우선 TTS 테스트
"""

import subprocess
import time

def test_sapi_priority():
    """SAPI 우선 테스트"""
    print("🔊 SAPI 우선 TTS 테스트")
    print("=" * 40)
    
    # SAPI 직접 사용
    test_texts = [
        "안녕하세요",
        "SAPI 테스트입니다",
        "헤드폰에서 들리나요?",
        "테스트 완료"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 SAPI 테스트 {i}: '{text}'")
        
        try:
            # SAPI 직접 호출
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
        
        time.sleep(2)  # 재생 간격
        print()
    
    print("✅ SAPI 우선 테스트 완료!")

def test_sapi_with_volume():
    """SAPI 볼륨 테스트"""
    print("\n🔊 SAPI 볼륨 테스트")
    print("=" * 30)
    
    volumes = [10, 20, 30, 50]  # SAPI 볼륨 (0-100)
    
    for volume in volumes:
        print(f"🔊 볼륨 {volume}% 테스트")
        
        try:
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 0; $synth.Volume = {volume}; $synth.Speak('볼륨 {volume}퍼센트 테스트')"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ 볼륨 {volume}% 성공")
            else:
                print(f"❌ 볼륨 {volume}% 실패")
                
        except Exception as e:
            print(f"❌ 볼륨 {volume}% 오류: {e}")
        
        time.sleep(2)
        print()

def test_sapi_with_speed():
    """SAPI 속도 테스트"""
    print("\n🔊 SAPI 속도 테스트")
    print("=" * 30)
    
    speeds = [-2, -1, 0, 1, 2]  # SAPI 속도 (-10 to 10)
    
    for speed in speeds:
        print(f"🔊 속도 {speed} 테스트")
        
        try:
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = {speed}; $synth.Volume = 30; $synth.Speak('속도 {speed} 테스트')"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ 속도 {speed} 성공")
            else:
                print(f"❌ 속도 {speed} 실패")
                
        except Exception as e:
            print(f"❌ 속도 {speed} 오류: {e}")
        
        time.sleep(2)
        print()

def main():
    """메인 함수"""
    print("🎧 SAPI 우선 TTS 테스트 시작")
    print("=" * 50)
    
    # 1. SAPI 우선 테스트
    test_sapi_priority()
    
    # 2. SAPI 볼륨 테스트
    test_sapi_with_volume()
    
    # 3. SAPI 속도 테스트
    test_sapi_with_speed()
    
    print("\n🎉 SAPI 테스트 완료!")
    print("SAPI가 헤드폰에서 잘 들린다면 이 방법을 사용하세요!")

if __name__ == "__main__":
    main() 