#!/usr/bin/env python3
"""
블루투스 헤드폰에서 적당한 볼륨으로 TTS 재생
"""

import subprocess
import time
from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid

def check_bluetooth_device():
    """블루투스 헤드폰 장치 확인"""
    print("🔍 블루투스 헤드폰 장치 확인 중...")
    
    try:
        # PowerShell로 오디오 장치 확인
        result = subprocess.run([
            "powershell", "-Command", 
            "Get-WmiObject -Class Win32_SoundDevice | Select-Object Name, Status"
        ], capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("📋 오디오 장치 목록:")
            print(result.stdout)
        else:
            print("❌ 오디오 장치 확인 실패")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ 오디오 장치 확인 중 오류: {e}")

def set_bluetooth_as_default():
    """블루투스 헤드폰을 기본 장치로 설정"""
    print("\n🎧 블루투스 헤드폰을 기본 장치로 설정 중...")
    
    try:
        # PowerShell로 기본 오디오 장치 설정
        commands = [
            # 기본 장치로 설정
            "powershell -Command \"$device = Get-WmiObject -Class Win32_SoundDevice | Where-Object {$_.Name -like '*QCY*' -or $_.Name -like '*헤드폰*'}; if ($device) { Write-Host 'Found device:' $device.Name }\"",
            
            # Windows SAPI로 블루투스 장치 선택
            "powershell -Command \"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $voices = $synth.GetInstalledVoices(); Write-Host 'Available voices:' $voices.Count\""
        ]
        
        for cmd in commands:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
            print(f"명령어 실행: {cmd[:50]}...")
            if result.returncode == 0:
                print(f"✅ 성공: {result.stdout.strip()}")
            else:
                print(f"❌ 실패: {result.stderr.strip()}")
                
    except Exception as e:
        print(f"❌ 블루투스 설정 중 오류: {e}")

def test_bluetooth_with_volume():
    """적당한 볼륨으로 블루투스 헤드폰 테스트"""
    print("\n🔊 블루투스 헤드폰에서 적당한 볼륨 테스트")
    print("=" * 50)
    
    # 적당한 볼륨 설정 (20%)
    bluetooth_config = VoiceConfig(
        name="블루투스 헤드폰 테스트",
        rate=150,  # 적당한 속도
        volume=0.2,  # 20% 볼륨
        language="ko"
    )
    
    test_texts = [
        "안녕하세요, 블루투스 헤드폰 테스트입니다",
        "이제 헤드폰에서 소리가 들리나요?",
        "볼륨이 20퍼센트로 설정되었습니다",
        "블루투스 연결이 정상인지 확인해주세요"
    ]
    
    print(f"🎵 음성 설정: {bluetooth_config.name}")
    print(f"   속도: {bluetooth_config.rate}")
    print(f"   볼륨: {bluetooth_config.volume * 100}%")
    print(f"   언어: {bluetooth_config.language}")
    print()
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        ensure_spoken_hybrid(text, voice_config=bluetooth_config)
        time.sleep(2)  # 재생 간격
        print()

def test_different_volumes():
    """다양한 볼륨으로 테스트"""
    print("\n🔊 다양한 볼륨으로 블루투스 테스트")
    print("=" * 50)
    
    volumes = [0.1, 0.2, 0.3, 0.5]  # 10%, 20%, 30%, 50%
    
    for volume in volumes:
        print(f"\n🎵 볼륨 {volume * 100}% 테스트")
        print("-" * 30)
        
        config = VoiceConfig(
            name=f"볼륨 {volume * 100}% 테스트",
            rate=150,
            volume=volume,
            language="ko"
        )
        
        test_text = f"볼륨이 {volume * 100}퍼센트입니다. 헤드폰에서 들리나요?"
        print(f"🔊 테스트: '{test_text}'")
        ensure_spoken_hybrid(test_text, voice_config=config)
        time.sleep(3)  # 재생 간격

def open_windows_sound_settings():
    """Windows 소리 설정 열기"""
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

def check_bluetooth_connection():
    """블루투스 연결 상태 확인"""
    print("\n🔍 블루투스 연결 상태 확인 중...")
    
    try:
        # 블루투스 장치 상태 확인
        result = subprocess.run([
            "powershell", "-Command",
            "Get-PnpDevice | Where-Object {$_.FriendlyName -like '*QCY*' -or $_.FriendlyName -like '*헤드폰*'} | Select-Object FriendlyName, Status"
        ], capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("📋 블루투스 장치 상태:")
            print(result.stdout)
        else:
            print("❌ 블루투스 장치 확인 실패")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ 블루투스 확인 중 오류: {e}")

def main():
    """메인 함수"""
    print("🎧 블루투스 헤드폰 TTS 문제 해결")
    print("=" * 50)
    
    # 1. 블루투스 장치 확인
    check_bluetooth_device()
    
    # 2. 블루투스 연결 상태 확인
    check_bluetooth_connection()
    
    # 3. 블루투스를 기본 장치로 설정
    set_bluetooth_as_default()
    
    # 4. 적당한 볼륨으로 테스트
    test_bluetooth_with_volume()
    
    # 5. 다양한 볼륨으로 테스트
    test_different_volumes()
    
    # 6. Windows 소리 설정 열기
    open_windows_sound_settings()
    
    print("\n✅ 모든 테스트 완료!")
    print("🎧 헤드폰에서 소리가 들리지 않으면 Windows 소리 설정을 확인해주세요.")

if __name__ == "__main__":
    main() 