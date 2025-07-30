#!/usr/bin/env python3
"""
블루투스 헤드폰 TTS 진단 및 해결 스크립트
"""

import subprocess
import sys
import os

def check_audio_devices():
    """오디오 장치 확인"""
    print("🔍 오디오 장치 확인 중...")
    
    try:
        # Windows PowerShell 명령어로 오디오 장치 확인
        cmd = "Get-WmiObject -Class Win32_SoundDevice | Select-Object Name, Status"
        result = subprocess.run(["powershell", "-Command", cmd], 
                              capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("✅ 오디오 장치 목록:")
            print(result.stdout)
        else:
            print("❌ 오디오 장치 확인 실패")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ 오디오 장치 확인 오류: {e}")

def check_default_audio_device():
    """기본 오디오 장치 확인"""
    print("\n🔍 기본 오디오 장치 확인 중...")
    
    try:
        # Windows PowerShell 명령어로 기본 오디오 장치 확인
        cmd = """
        Add-Type -TypeDefinition @"
        using System.Runtime.InteropServices;
        public class AudioDevice {
            [DllImport("ole32.dll")]
            public static extern int CoCreateInstance(ref Guid rclsid, IntPtr pUnkOuter, uint dwClsContext, ref Guid riid, [MarshalAs(UnmanagedType.IUnknown)] out object ppv);
        }
"@
        $shell = New-Object -ComObject Shell.Application
        $shell.NameSpace(0x11).Items() | Where-Object {$_.Name -like "*audio*"} | ForEach-Object {$_.Name}
        """
        
        result = subprocess.run(["powershell", "-Command", cmd], 
                              capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("✅ 기본 오디오 장치:")
            print(result.stdout)
        else:
            print("❌ 기본 오디오 장치 확인 실패")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ 기본 오디오 장치 확인 오류: {e}")

def test_pyttsx3_with_device_selection():
    """pyttsx3로 특정 장치 선택 테스트"""
    print("\n🧪 pyttsx3 장치 선택 테스트")
    
    try:
        import pyttsx3
        
        # 엔진 초기화
        engine = pyttsx3.init()
        
        # 사용 가능한 드라이버 확인
        drivers = engine.getProperty('drivers')
        print(f"✅ 사용 가능한 드라이버: {drivers}")
        
        # 음성 목록 확인
        voices = engine.getProperty('voices')
        print(f"✅ 사용 가능한 음성: {len(voices)}개")
        
        # 현재 설정된 속성들 확인
        rate = engine.getProperty('rate')
        volume = engine.getProperty('volume')
        voice = engine.getProperty('voice')
        
        print(f"현재 설정:")
        print(f"  속도: {rate}")
        print(f"  볼륨: {volume}")
        print(f"  음성: {voice}")
        
        # 테스트 음성 재생
        test_text = "블루투스 헤드폰 테스트입니다"
        print(f"\n🔊 '{test_text}' 재생 중...")
        
        engine.say(test_text)
        engine.runAndWait()
        
        print("✅ pyttsx3 테스트 완료")
        return True
        
    except Exception as e:
        print(f"❌ pyttsx3 테스트 오류: {e}")
        return False

def test_windows_sapi_with_device():
    """Windows SAPI로 장치 선택 테스트"""
    print("\n🧪 Windows SAPI 장치 선택 테스트")
    
    try:
        import win32com.client
        
        # SAPI 스피커 생성
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        
        # 사용 가능한 오디오 출력 장치 확인
        audio_outputs = speaker.GetAudioOutputs()
        print(f"✅ 사용 가능한 오디오 출력 장치: {audio_outputs.Count}개")
        
        for i in range(audio_outputs.Count):
            output = audio_outputs.Item(i)
            print(f"  장치 {i+1}: {output.GetDescription()}")
        
        # 테스트 음성 재생
        test_text = "블루투스 헤드폰 SAPI 테스트입니다"
        print(f"\n🔊 '{test_text}' 재생 중...")
        
        speaker.Speak(test_text)
        
        print("✅ Windows SAPI 테스트 완료")
        return True
        
    except Exception as e:
        print(f"❌ Windows SAPI 테스트 오류: {e}")
        return False

def set_default_audio_device():
    """기본 오디오 장치 설정"""
    print("\n🔧 기본 오디오 장치 설정")
    
    try:
        # Windows 설정에서 오디오 장치 변경 안내
        print("Windows 설정에서 오디오 장치를 변경하려면:")
        print("1. Windows 설정 → 시스템 → 소리")
        print("2. 출력 장치에서 블루투스 헤드폰 선택")
        print("3. '기본 장치로 설정' 클릭")
        
        # 설정 앱 열기
        response = input("\n소리 설정을 열까요? (y/n): ")
        if response.lower() == 'y':
            subprocess.run(["ms-settings:sound"])
            print("✅ 소리 설정이 열렸습니다.")
        
    except Exception as e:
        print(f"❌ 설정 오류: {e}")

def test_bluetooth_specific():
    """블루투스 헤드폰 전용 테스트"""
    print("\n🎧 블루투스 헤드폰 전용 테스트")
    
    try:
        from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid
        
        # 블루투스 헤드폰용 음성 설정
        bt_voice_config = VoiceConfig(
            name="블루투스 헤드폰 음성",
            rate=150,  # 명확한 속도
            volume=1.0,  # 최대 볼륨
            language="ko"
        )
        
        test_texts = [
            "블루투스 헤드폰에서 들리시나요?",
            "이 음성이 블루투스 헤드폰에서 재생되고 있습니다",
            "볼륨을 확인해주세요"
        ]
        
        for i, text in enumerate(test_texts, 1):
            print(f"\n🔊 테스트 {i}: '{text}'")
            ensure_spoken_hybrid(text, voice_config=bt_voice_config)
        
        print("\n✅ 블루투스 헤드폰 테스트 완료")
        return True
        
    except Exception as e:
        print(f"❌ 블루투스 헤드폰 테스트 오류: {e}")
        return False

def main():
    """메인 진단 함수"""
    print("🎧 블루투스 헤드폰 TTS 진단 시작")
    print("=" * 50)
    
    # 1. 오디오 장치 확인
    check_audio_devices()
    
    # 2. 기본 오디오 장치 확인
    check_default_audio_device()
    
    # 3. pyttsx3 테스트
    test_pyttsx3_with_device_selection()
    
    # 4. Windows SAPI 테스트
    test_windows_sapi_with_device()
    
    # 5. 기본 오디오 장치 설정 안내
    set_default_audio_device()
    
    # 6. 블루투스 헤드폰 전용 테스트
    test_bluetooth_specific()
    
    print("\n📋 문제 해결 방법:")
    print("1. Windows 설정 → 시스템 → 소리에서 블루투스 헤드폰을 기본 장치로 설정")
    print("2. 블루투스 헤드폰의 볼륨이 충분한지 확인")
    print("3. 블루투스 헤드폰이 제대로 연결되어 있는지 확인")
    print("4. 다른 앱에서 소리가 나는지 확인")
    print("5. 블루투스 헤드폰을 재연결해보기")

if __name__ == "__main__":
    main() 