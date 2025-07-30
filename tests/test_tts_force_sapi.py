#!/usr/bin/env python3
"""
SAPI 강제 사용 테스트
"""

import subprocess
import time

def force_sapi_test():
    """SAPI 강제 사용 테스트"""
    print("🔊 SAPI 강제 사용 테스트")
    print("=" * 40)
    
    test_texts = [
        "안녕하세요, SAPI 강제 사용 테스트입니다",
        "이제 SAPI만 사용합니다",
        "헤드폰에서 들리나요?",
        "테스트가 완료되었습니다"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        
        try:
            # SAPI 직접 호출 (강제 사용)
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 1.5; $synth.Volume = 30; $synth.Speak('{text}')"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ SAPI 강제 테스트 {i} 성공")
            else:
                print(f"❌ SAPI 강제 테스트 {i} 실패")
                print(f"오류: {result.stderr}")
                
        except Exception as e:
            print(f"❌ SAPI 강제 테스트 {i} 오류: {e}")
        
        time.sleep(2)  # 재생 간격
        print()
    
    print("✅ SAPI 강제 사용 테스트 완료!")

def test_sapi_with_different_volumes():
    """SAPI 다양한 볼륨 테스트"""
    print("\n🔊 SAPI 다양한 볼륨 테스트")
    print("=" * 40)
    
    volumes = [20, 30, 50, 70]  # SAPI 볼륨 (0-100)
    
    for volume in volumes:
        print(f"🔊 볼륨 {volume}% 테스트")
        
        try:
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 1.5; $synth.Volume = {volume}; $synth.Speak('볼륨 {volume}퍼센트 테스트입니다')"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ 볼륨 {volume}% 성공")
            else:
                print(f"❌ 볼륨 {volume}% 실패")
                
        except Exception as e:
            print(f"❌ 볼륨 {volume}% 오류: {e}")
        
        time.sleep(2)
        print()

def test_sapi_with_different_speeds():
    """SAPI 다양한 속도 테스트"""
    print("\n🔊 SAPI 다양한 속도 테스트")
    print("=" * 40)
    
    speeds = [0.5, 1.0, 1.5, 2.0]  # SAPI 속도
    
    for speed in speeds:
        print(f"🔊 속도 {speed} 테스트")
        
        try:
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = {speed}; $synth.Volume = 30; $synth.Speak('속도 {speed} 테스트입니다')"
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
    print("🎧 SAPI 강제 사용 테스트 시작")
    print("=" * 50)
    
    # 1. SAPI 강제 사용 테스트
    force_sapi_test()
    
    # 2. SAPI 다양한 볼륨 테스트
    test_sapi_with_different_volumes()
    
    # 3. SAPI 다양한 속도 테스트
    test_sapi_with_different_speeds()
    
    print("\n🎉 SAPI 강제 사용 테스트 완료!")
    print("어떤 볼륨과 속도에서 헤드폰에서 소리가 들렸는지 알려주세요!")

if __name__ == "__main__":
    main() 