#!/usr/bin/env python3
"""
SAPI 속도 1.5 테스트
"""

import subprocess
import time

def test_sapi_speed_1_5():
    """SAPI 속도 1.5 테스트"""
    print("🔊 SAPI 속도 1.5 테스트")
    print("=" * 40)
    
    # SAPI 속도 1.5 테스트
    test_texts = [
        "안녕하세요, 속도 1.5 테스트입니다",
        "이제 헤드폰에서 들리나요?",
        "속도가 1.5로 설정되었습니다",
        "테스트가 완료되었습니다"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        
        try:
            # SAPI 속도 1.5로 설정
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 1.5; $synth.Volume = 30; $synth.Speak('{text}')"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ SAPI 속도 1.5 테스트 {i} 성공")
            else:
                print(f"❌ SAPI 속도 1.5 테스트 {i} 실패")
                print(f"오류: {result.stderr}")
                
        except Exception as e:
            print(f"❌ SAPI 속도 1.5 테스트 {i} 오류: {e}")
        
        time.sleep(2)  # 재생 간격
        print()
    
    print("✅ SAPI 속도 1.5 테스트 완료!")

def test_sapi_speed_1_0():
    """SAPI 속도 1.0 테스트 (대안)"""
    print("\n🔊 SAPI 속도 1.0 테스트 (대안)")
    print("=" * 40)
    
    # SAPI 속도 1.0 테스트
    test_texts = [
        "안녕하세요, 속도 1.0 테스트입니다",
        "이제 헤드폰에서 들리나요?",
        "속도가 1.0으로 설정되었습니다",
        "테스트가 완료되었습니다"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        
        try:
            # SAPI 속도 1.0으로 설정
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 1.0; $synth.Volume = 30; $synth.Speak('{text}')"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ SAPI 속도 1.0 테스트 {i} 성공")
            else:
                print(f"❌ SAPI 속도 1.0 테스트 {i} 실패")
                print(f"오류: {result.stderr}")
                
        except Exception as e:
            print(f"❌ SAPI 속도 1.0 테스트 {i} 오류: {e}")
        
        time.sleep(2)  # 재생 간격
        print()
    
    print("✅ SAPI 속도 1.0 테스트 완료!")

def test_sapi_speed_comparison():
    """SAPI 속도 비교 테스트"""
    print("\n🔊 SAPI 속도 비교 테스트")
    print("=" * 40)
    
    speeds = [0.5, 1.0, 1.5, 2.0]  # 테스트할 속도들
    
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
    print("🎧 SAPI 속도 테스트 시작")
    print("=" * 50)
    
    # 1. SAPI 속도 1.5 테스트
    test_sapi_speed_1_5()
    
    # 2. SAPI 속도 1.0 테스트 (대안)
    test_sapi_speed_1_0()
    
    # 3. SAPI 속도 비교 테스트
    test_sapi_speed_comparison()
    
    print("\n🎉 SAPI 속도 테스트 완료!")
    print("어떤 속도가 가장 적당한지 확인해주세요!")

if __name__ == "__main__":
    main() 