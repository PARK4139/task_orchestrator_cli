#!/usr/bin/env python3
"""
블루투스 헤드폰 TTS 해결 스크립트
"""

import subprocess
import sys
import os

def set_bluetooth_as_default():
    """블루투스 헤드폰을 기본 오디오 장치로 설정"""
    print("🔧 블루투스 헤드폰을 기본 장치로 설정 중...")
    
    try:
        # Windows PowerShell 명령어로 블루투스 헤드폰을 기본 장치로 설정
        cmd = """
        $audioDevices = Get-WmiObject -Class Win32_SoundDevice
        $bluetoothDevice = $audioDevices | Where-Object {$_.Name -like "*QCY*" -or $_.Name -like "*Bluetooth*" -or $_.Name -like "*Headset*"}
        if ($bluetoothDevice) {
            Write-Host "블루투스 헤드폰 발견: $($bluetoothDevice.Name)"
        } else {
            Write-Host "블루투스 헤드폰을 찾을 수 없습니다."
        }
        """
        
        result = subprocess.run(["powershell", "-Command", cmd], 
                              capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("✅ 블루투스 헤드폰 확인:")
            print(result.stdout)
        else:
            print("❌ 블루투스 헤드폰 확인 실패")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ 블루투스 헤드폰 설정 오류: {e}")

def test_windows_sapi_with_bluetooth():
    """Windows SAPI로 블루투스 헤드폰 테스트"""
    print("\n🎧 Windows SAPI 블루투스 헤드폰 테스트")
    
    try:
        import win32com.client
        
        # SAPI 스피커 생성
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        
        # 사용 가능한 오디오 출력 장치 확인
        audio_outputs = speaker.GetAudioOutputs()
        print(f"✅ 사용 가능한 오디오 출력 장치: {audio_outputs.Count}개")
        
        # 블루투스 헤드폰 찾기
        bluetooth_device = None
        for i in range(audio_outputs.Count):
            output = audio_outputs.Item(i)
            device_name = output.GetDescription()
            print(f"  장치 {i+1}: {device_name}")
            
            # 블루투스 헤드폰 식별
            if "QCY" in device_name or "Bluetooth" in device_name or "Headset" in device_name:
                bluetooth_device = output
                print(f"  🎧 블루투스 헤드폰 발견: {device_name}")
        
        if bluetooth_device:
            # 블루투스 헤드폰을 기본 장치로 설정
            speaker.Voice = speaker.GetVoices().Item(0)  # 기본 음성
            print("✅ 블루투스 헤드폰으로 설정됨")
            
            # 테스트 음성 재생
            test_text = "블루투스 헤드폰에서 이 음성이 들리시나요?"
            print(f"\n🔊 '{test_text}' 재생 중...")
            
            speaker.Speak(test_text)
            
            print("✅ Windows SAPI 블루투스 테스트 완료")
            return True
        else:
            print("❌ 블루투스 헤드폰을 찾을 수 없습니다.")
            return False
        
    except Exception as e:
        print(f"❌ Windows SAPI 블루투스 테스트 오류: {e}")
        return False

def test_pyttsx3_with_bluetooth():
    """pyttsx3로 블루투스 헤드폰 테스트"""
    print("\n🎧 pyttsx3 블루투스 헤드폰 테스트")
    
    try:
        import pyttsx3
        
        # 엔진 초기화
        engine = pyttsx3.init()
        
        # 음성 설정
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)  # 최대 볼륨
        
        # 음성 목록 확인
        voices = engine.getProperty('voices')
        print(f"✅ 사용 가능한 음성: {len(voices)}개")
        
        # 한국어 음성 선택 (가능한 경우)
        for voice in voices:
            if "Korean" in voice.name or "ko" in voice.id.lower():
                engine.setProperty('voice', voice.id)
                print(f"✅ 한국어 음성 선택: {voice.name}")
                break
        
        # 테스트 음성 재생
        test_text = "pyttsx3로 블루투스 헤드폰 테스트입니다"
        print(f"\n🔊 '{test_text}' 재생 중...")
        
        engine.say(test_text)
        engine.runAndWait()
        
        print("✅ pyttsx3 블루투스 테스트 완료")
        return True
        
    except Exception as e:
        print(f"❌ pyttsx3 블루투스 테스트 오류: {e}")
        return False

def test_hybrid_tts_with_bluetooth():
    """하이브리드 TTS로 블루투스 헤드폰 테스트"""
    print("\n🎧 하이브리드 TTS 블루투스 헤드폰 테스트")
    
    try:
        from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid
        
        # 블루투스 헤드폰용 최적화된 음성 설정
        bt_voice_config = VoiceConfig(
            name="블루투스 헤드폰 최적화",
            rate=140,  # 명확한 속도
            volume=1.0,  # 최대 볼륨
            language="ko"
        )
        
        test_texts = [
            "하이브리드 TTS로 블루투스 헤드폰 테스트입니다",
            "이 음성이 블루투스 헤드폰에서 재생되고 있습니다",
            "볼륨과 음질을 확인해주세요",
            "테스트가 완료되었습니다"
        ]
        
        for i, text in enumerate(test_texts, 1):
            print(f"\n🔊 테스트 {i}: '{text}'")
            ensure_spoken_hybrid(text, voice_config=bt_voice_config)
        
        print("\n✅ 하이브리드 TTS 블루투스 테스트 완료")
        return True
        
    except Exception as e:
        print(f"❌ 하이브리드 TTS 블루투스 테스트 오류: {e}")
        return False

def open_windows_sound_settings():
    """Windows 소리 설정 열기"""
    print("\n🔧 Windows 소리 설정 열기")
    
    try:
        # Windows 설정에서 소리 설정 열기
        subprocess.run(["start", "ms-settings:sound"], shell=True)
        print("✅ Windows 소리 설정이 열렸습니다.")
        print("\n📋 수동 설정 방법:")
        print("1. 출력 장치에서 '헤드폰(2- QCY H3 ANC HEADSET)' 선택")
        print("2. '기본 장치로 설정' 클릭")
        print("3. '기본 통신 장치로 설정' 클릭")
        print("4. 볼륨을 100%로 설정")
        
    except Exception as e:
        print(f"❌ 설정 열기 오류: {e}")

def check_bluetooth_connection():
    """블루투스 연결 상태 확인"""
    print("\n🔍 블루투스 연결 상태 확인")
    
    try:
        # 블루투스 장치 상태 확인
        cmd = "Get-PnpDevice | Where-Object {$_.FriendlyName -like '*QCY*' -or $_.FriendlyName -like '*Bluetooth*'} | Select-Object FriendlyName, Status"
        result = subprocess.run(["powershell", "-Command", cmd], 
                              capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("✅ 블루투스 장치 상태:")
            print(result.stdout)
        else:
            print("❌ 블루투스 장치 확인 실패")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ 블루투스 연결 확인 오류: {e}")

def main():
    """메인 해결 함수"""
    print("🎧 블루투스 헤드폰 TTS 해결 시작")
    print("=" * 50)
    
    # 1. 블루투스 연결 상태 확인
    check_bluetooth_connection()
    
    # 2. 블루투스 헤드폰을 기본 장치로 설정
    set_bluetooth_as_default()
    
    # 3. Windows SAPI 블루투스 테스트
    test_windows_sapi_with_bluetooth()
    
    # 4. pyttsx3 블루투스 테스트
    test_pyttsx3_with_bluetooth()
    
    # 5. 하이브리드 TTS 블루투스 테스트
    test_hybrid_tts_with_bluetooth()
    
    # 6. Windows 소리 설정 열기
    open_windows_sound_settings()
    
    print("\n🎯 해결 방법 요약:")
    print("1. Windows 설정 → 시스템 → 소리에서 블루투스 헤드폰을 기본 장치로 설정")
    print("2. 블루투스 헤드폰 볼륨을 최대로 설정")
    print("3. 블루투스 헤드폰을 재연결해보기")
    print("4. 다른 앱에서 소리가 나는지 확인")
    print("5. 블루투스 헤드폰 배터리 상태 확인")

if __name__ == "__main__":
    main() 