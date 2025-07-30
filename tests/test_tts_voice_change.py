#!/usr/bin/env python3
"""
목소리 변경 테스트
"""

import subprocess
import time

def get_available_voices():
    """사용 가능한 SAPI 음성 목록 가져오기"""
    print("🔊 사용 가능한 SAPI 음성 목록")
    print("=" * 40)
    
    try:
        result = subprocess.run([
            "powershell", "-Command",
            "Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $voices = $synth.GetVoices(); for($i=0; $i -lt $voices.Count; $i++) { $voice = $voices.Item($i); Write-Host \"[$i] $($voice.GetDescription())\" }"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 사용 가능한 음성:")
            print(result.stdout)
        else:
            print("❌ 음성 목록 가져오기 실패")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ 오류: {e}")

def test_different_voices():
    """다양한 음성으로 테스트"""
    print("\n🔊 다양한 음성 테스트")
    print("=" * 40)
    
    test_text = "안녕하세요, 음성 변경 테스트입니다"
    
    # 음성 인덱스별 테스트 (0, 1, 2, 3)
    for voice_index in range(4):  # 최대 4개 음성 테스트
        print(f"🔊 음성 {voice_index} 테스트")
        
        try:
            result = subprocess.run([
                "powershell", "-Command",
                f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $voices = $synth.GetVoices(); if($voices.Count -gt {voice_index}) {{ $synth.Voice = $voices.Item({voice_index}); $synth.Rate = 1.2; $synth.Volume = 30; $synth.Speak('{test_text}') }} else {{ Write-Host '음성 {voice_index} 없음' }}"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ 음성 {voice_index} 성공")
            else:
                print(f"❌ 음성 {voice_index} 실패")
                if "음성" in result.stdout:
                    print(f"   {result.stdout.strip()}")
                
        except Exception as e:
            print(f"❌ 음성 {voice_index} 오류: {e}")
        
        time.sleep(2)
        print()

def test_voice_with_settings():
    """설정된 볼륨/속도로 음성 테스트"""
    print("\n🔊 설정된 볼륨/속도로 음성 테스트")
    print("=" * 40)
    
    test_texts = [
        "안녕하세요, 볼륨 30% 속도 1.2 테스트입니다",
        "이제 새로운 설정으로 음성이 재생됩니다",
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
    print("🎧 목소리 변경 테스트 시작")
    print("=" * 50)
    
    # 1. 사용 가능한 음성 목록 확인
    get_available_voices()
    
    # 2. 다양한 음성 테스트
    test_different_voices()
    
    # 3. 설정된 볼륨/속도로 테스트
    test_voice_with_settings()
    
    print("\n🎉 목소리 변경 테스트 완료!")
    print("어떤 음성이 가장 마음에 드시는지 알려주세요!")

if __name__ == "__main__":
    main() 