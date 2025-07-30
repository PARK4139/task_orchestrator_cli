#!/usr/bin/env python3
"""
현재 오디오 장치 상태 확인 및 블루투스 헤드폰 재설정
"""

import subprocess
import sys
import os
import time

def check_current_audio_devices():
    """현재 오디오 장치 상태 확인"""
    print("🔍 현재 오디오 장치 상태 확인 중...")
    
    try:
        # Windows PowerShell 명령어로 현재 오디오 장치 확인
        cmd = """
        # 현재 기본 오디오 장치 확인
        $audioDevices = Get-WmiObject -Class Win32_SoundDevice
        Write-Host "=== 현재 오디오 장치 목록 ==="
        $audioDevices | ForEach-Object { 
            Write-Host "장치: $($_.Name), 상태: $($_.Status)" 
        }
        
        # 블루투스 헤드폰 찾기
        $bluetoothDevice = $audioDevices | Where-Object {$_.Name -like "*QCY*" -or $_.Name -like "*Bluetooth*" -or $_.Name -like "*Headset*"}
        if ($bluetoothDevice) {
            Write-Host "=== 블루투스 헤드폰 발견 ==="
            Write-Host $bluetoothDevice.Name
        } else {
            Write-Host "블루투스 헤드폰을 찾을 수 없습니다."
        }
        """
        
        result = subprocess.run(["powershell", "-Command", cmd], 
                              capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("✅ 현재 오디오 장치 상태:")
            print(result.stdout)
        else:
            print("❌ 오디오 장치 확인 실패")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ 오디오 장치 확인 오류: {e}")

def test_windows_sapi_current_device():
    """Windows SAPI로 현재 장치 테스트"""
    print("\n🎧 Windows SAPI 현재 장치 테스트")
    
    try:
        import win32com.client
        
        # SAPI 스피커 생성
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        
        # 사용 가능한 오디오 출력 장치 확인
        audio_outputs = speaker.GetAudioOutputs()
        print(f"✅ 사용 가능한 오디오 출력 장치: {audio_outputs.Count}개")
        
        # 현재 설정된 장치 확인
        current_output = speaker.AudioOutput
        print(f"현재 설정된 장치: {current_output.GetDescription()}")
        
        # 모든 장치 출력
        for i in range(audio_outputs.Count):
            output = audio_outputs.Item(i)
            device_name = output.GetDescription()
            print(f"  장치 {i+1}: {device_name}")
        
        # 블루투스 헤드폰 찾기
        bluetooth_device = None
        for i in range(audio_outputs.Count):
            output = audio_outputs.Item(i)
            device_name = output.GetDescription()
            
            # 블루투스 헤드폰 식별
            if "QCY" in device_name or "Bluetooth" in device_name or "Headset" in device_name:
                bluetooth_device = output
                print(f"  🎧 블루투스 헤드폰 발견: {device_name}")
                break
        
        if bluetooth_device:
            # 블루투스 헤드폰을 기본 장치로 설정
            speaker.AudioOutput = bluetooth_device
            print("✅ 블루투스 헤드폰을 기본 장치로 다시 설정했습니다.")
            
            # 테스트 음성 재생
            test_text = "블루투스 헤드폰이 다시 설정되었습니다. 들리시나요?"
            print(f"\n🔊 '{test_text}' 재생 중...")
            
            speaker.Speak(test_text)
            
            print("✅ Windows SAPI 현재 장치 테스트 완료")
            return True
        else:
            print("❌ 블루투스 헤드폰을 찾을 수 없습니다.")
            return False
        
    except Exception as e:
        print(f"❌ Windows SAPI 현재 장치 테스트 오류: {e}")
        return False

def test_pyttsx3_current_device():
    """pyttsx3로 현재 장치 테스트"""
    print("\n🎧 pyttsx3 현재 장치 테스트")
    
    try:
        import pyttsx3
        
        # 엔진 초기화
        engine = pyttsx3.init()
        
        # 현재 설정 확인
        rate = engine.getProperty('rate')
        volume = engine.getProperty('volume')
        voice = engine.getProperty('voice')
        
        print(f"현재 설정:")
        print(f"  속도: {rate}")
        print(f"  볼륨: {volume}")
        print(f"  음성: {voice}")
        
        # 최대 볼륨으로 설정
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)  # 최대 볼륨
        
        # 음성 목록 확인
        voices = engine.getProperty('voices')
        print(f"✅ 사용 가능한 음성: {len(voices)}개")
        
        # 한국어 음성 선택
        for voice in voices:
            if "Korean" in voice.name or "ko" in voice.id.lower():
                engine.setProperty('voice', voice.id)
                print(f"✅ 한국어 음성 선택: {voice.name}")
                break
        
        # 테스트 음성 재생
        test_text = "pyttsx3 현재 장치 테스트입니다. 블루투스 헤드폰에서 들리시나요?"
        print(f"\n🔊 '{test_text}' 재생 중...")
        
        engine.say(test_text)
        engine.runAndWait()
        
        print("✅ pyttsx3 현재 장치 테스트 완료")
        return True
        
    except Exception as e:
        print(f"❌ pyttsx3 현재 장치 테스트 오류: {e}")
        return False

def test_hybrid_tts_current_device():
    """하이브리드 TTS로 현재 장치 테스트"""
    print("\n🎧 하이브리드 TTS 현재 장치 테스트")
    
    try:
        from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid
        
        # 현재 장치용 음성 설정
        current_voice_config = VoiceConfig(
            name="현재 장치 테스트",
            rate=140,  # 명확한 속도
            volume=1.0,  # 최대 볼륨
            language="ko"
        )
        
        test_texts = [
            "하이브리드 TTS 현재 장치 테스트입니다",
            "블루투스 헤드폰에서 이 음성이 들리시나요?",
            "볼륨을 최대로 설정했습니다",
            "테스트가 완료되었습니다"
        ]
        
        for i, text in enumerate(test_texts, 1):
            print(f"\n🔊 테스트 {i}: '{text}'")
            ensure_spoken_hybrid(text, voice_config=current_voice_config)
            time.sleep(1)  # 재생 간격
        
        print("\n✅ 하이브리드 TTS 현재 장치 테스트 완료")
        return True
        
    except Exception as e:
        print(f"❌ 하이브리드 TTS 현재 장치 테스트 오류: {e}")
        return False

def force_bluetooth_again():
    """블루투스 헤드폰을 다시 강제 설정"""
    print("\n🔧 블루투스 헤드폰을 다시 강제 설정 중...")
    
    try:
        # Windows PowerShell 명령어로 블루투스 헤드폰을 다시 기본 장치로 설정
        cmd = """
        # 블루투스 헤드폰을 다시 기본 장치로 설정하는 방법 안내
        Write-Host "=== 블루투스 헤드폰 재설정 방법 ==="
        Write-Host "1. Windows 설정 → 시스템 → 소리 열기"
        Write-Host "2. 출력 장치에서 '헤드폰(2- QCY H3 ANC HEADSET)' 선택"
        Write-Host "3. '기본 장치로 설정' 클릭"
        Write-Host "4. '기본 통신 장치로 설정' 클릭"
        Write-Host "5. 볼륨을 100%로 설정"
        Write-Host "6. 다른 모든 장치 비활성화"
        """
        
        result = subprocess.run(["powershell", "-Command", cmd], 
                              capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("✅ 블루투스 헤드폰 재설정 안내:")
            print(result.stdout)
        else:
            print("❌ 블루투스 헤드폰 재설정 안내 실패")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ 블루투스 헤드폰 재설정 오류: {e}")

def open_windows_sound_settings_again():
    """Windows 소리 설정 다시 열기"""
    print("\n🔧 Windows 소리 설정 다시 열기")
    
    try:
        # Windows 설정에서 소리 설정 열기
        subprocess.run(["start", "ms-settings:sound"], shell=True)
        print("✅ Windows 소리 설정이 다시 열렸습니다.")
        print("\n📋 재설정 방법:")
        print("1. 출력 장치에서 '헤드폰(2- QCY H3 ANC HEADSET)' 선택")
        print("2. '기본 장치로 설정' 클릭")
        print("3. '기본 통신 장치로 설정' 클릭")
        print("4. 볼륨을 100%로 설정")
        print("5. 다른 모든 장치 비활성화")
        
        # 추가 안내
        print("\n⚠️ 추가 확인사항:")
        print("- 블루투스 헤드폰 볼륨이 최대인지 확인")
        print("- 다른 앱에서 소리가 나는지 확인")
        print("- 블루투스 헤드폰을 재연결해보기")
        print("- 블루투스 헤드폰 배터리 상태 확인")
        
    except Exception as e:
        print(f"❌ 설정 열기 오류: {e}")

def test_system_audio_again():
    """시스템 오디오 다시 테스트"""
    print("\n🔊 시스템 오디오 다시 테스트")
    
    try:
        # Windows 시스템 사운드 재생
        import winsound
        
        # 시스템 비프음 재생
        print("🔊 시스템 비프음 재생 중...")
        winsound.Beep(1000, 1000)  # 1000Hz, 1초
        
        print("✅ 시스템 오디오 테스트 완료")
        return True
        
    except Exception as e:
        print(f"❌ 시스템 오디오 테스트 오류: {e}")
        return False

def main():
    """메인 현재 장치 확인 함수"""
    print("🎧 현재 오디오 장치 상태 확인 및 블루투스 헤드폰 재설정")
    print("=" * 60)
    
    # 1. 현재 오디오 장치 상태 확인
    check_current_audio_devices()
    
    # 2. Windows SAPI 현재 장치 테스트
    test_windows_sapi_current_device()
    
    # 3. pyttsx3 현재 장치 테스트
    test_pyttsx3_current_device()
    
    # 4. 하이브리드 TTS 현재 장치 테스트
    test_hybrid_tts_current_device()
    
    # 5. 블루투스 헤드폰 다시 강제 설정
    force_bluetooth_again()
    
    # 6. 시스템 오디오 다시 테스트
    test_system_audio_again()
    
    # 7. Windows 소리 설정 다시 열기
    open_windows_sound_settings_again()
    
    print("\n🎯 재설정 방법 요약:")
    print("1. Windows 설정 → 시스템 → 소리에서 블루투스 헤드폰을 기본 장치로 설정")
    print("2. 블루투스 헤드폰 볼륨을 최대로 설정")
    print("3. 다른 모든 오디오 장치 비활성화")
    print("4. 블루투스 헤드폰을 재연결해보기")
    print("5. 다른 앱에서 소리가 나는지 확인")
    print("6. 블루투스 헤드폰 배터리 상태 확인")

if __name__ == "__main__":
    main() 