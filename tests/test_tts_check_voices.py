#!/usr/bin/env python3
"""
실제 사용 가능한 SAPI 음성 확인 테스트
"""

import subprocess
import time

def check_available_voices():
    """실제 사용 가능한 SAPI 음성 확인"""
    print("🔊 실제 사용 가능한 SAPI 음성 확인")
    print("=" * 50)
    
    try:
        # 방법 1: PowerShell로 음성 개수 확인
        result = subprocess.run([
            "powershell", "-Command",
            "Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $voices = $synth.GetVoices(); Write-Host \"총 음성 개수: $($voices.Count)\"; for($i=0; $i -lt $voices.Count; $i++) { $voice = $voices.Item($i); Write-Host \"[$i] $($voice.GetDescription())\" }"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 음성 목록:")
            print(result.stdout)
        else:
            print("❌ 음성 목록 가져오기 실패")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ 오류: {e}")

def test_each_voice():
    """각 음성을 개별적으로 테스트"""
    print("\n🔊 각 음성 개별 테스트")
    print("=" * 50)
    
    test_text = "안녕하세요, 음성 테스트입니다"
    
    # 음성 개수를 먼저 확인
    try:
        result = subprocess.run([
            "powershell", "-Command",
            "Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $voices = $synth.GetVoices(); Write-Host $voices.Count"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            voice_count = int(result.stdout.strip())
            print(f"총 음성 개수: {voice_count}")
            
            for i in range(voice_count):
                print(f"\n🔊 음성 {i} 테스트")
                
                try:
                    test_result = subprocess.run([
                        "powershell", "-Command",
                        f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $voices = $synth.GetVoices(); $synth.Voice = $voices.Item({i}); $synth.Rate = 1.2; $synth.Volume = 30; $synth.Speak('{test_text}')"
                    ], capture_output=True, text=True)
                    
                    if test_result.returncode == 0:
                        print(f"✅ 음성 {i} 성공")
                    else:
                        print(f"❌ 음성 {i} 실패")
                        
                except Exception as e:
                    print(f"❌ 음성 {i} 오류: {e}")
                
                time.sleep(2)
                
        else:
            print("❌ 음성 개수 확인 실패")
            
    except Exception as e:
        print(f"❌ 오류: {e}")

def test_default_voice():
    """기본 음성으로 테스트"""
    print("\n🔊 기본 음성 테스트")
    print("=" * 50)
    
    test_texts = [
        "안녕하세요, 기본 음성 테스트입니다",
        "볼륨 30%, 속도 1.2로 설정되었습니다",
        "헤드폰에서 잘 들리시나요?",
        "테스트가 완료되었습니다"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        
        try:
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Rate = 1.2; $synth.Volume = 30; $synth.Speak('{text}')"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ 테스트 {i} 성공")
            else:
                print(f"❌ 테스트 {i} 실패")
                
        except Exception as e:
            print(f"❌ 테스트 {i} 오류: {e}")
        
        time.sleep(2)
        print()

def main():
    """메인 함수"""
    print("🎧 실제 사용 가능한 음성 확인 테스트")
    print("=" * 60)
    
    # 1. 사용 가능한 음성 목록 확인
    check_available_voices()
    
    # 2. 각 음성 개별 테스트
    test_each_voice()
    
    # 3. 기본 음성 테스트
    test_default_voice()
    
    print("\n🎉 음성 확인 테스트 완료!")
    print("실제로 몇 개의 음성이 있는지 확인되었습니다!")

if __name__ == "__main__":
    main() 