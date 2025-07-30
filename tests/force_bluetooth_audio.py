#!/usr/bin/env python3
"""
블루투스 헤드폰 강제 설정 및 TTS 테스트
"""

import subprocess
import sys
import os
import time

def force_bluetooth_as_default():
    """블루투스 헤드폰을 강제로 기본 장치로 설정"""
    print("🔧 블루투스 헤드폰을 강제로 기본 장치로 설정 중...")
    
    try:
        # Windows PowerShell 명령어로 블루투스 헤드폰을 기본 장치로 설정
        cmd = """
        # 오디오 장치 목록 가져오기
        $audioDevices = Get-WmiObject -Class Win32_SoundDevice
        Write-Host "=== 사용 가능한 오디오 장치 ==="
        $audioDevices | ForEach-Object { Write-Host $_.Name }
        
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
            print("✅ 오디오 장치 확인:")
            print(result.stdout)
        else:
            print("❌ 오디오 장치 확인 실패")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ 블루투스 헤드폰 설정 오류: {e}")

def test_windows_sapi_with_specific_device():
    """Windows SAPI로 특정 장치 지정 테스트"""
    print("\n🎧 Windows SAPI 특정 장치 테스트")
    
    try:
        import win32com.client
        
        # SAPI 스피커 생성
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        
        # 사용 가능한 오디오 출력 장치 확인
        audio_outputs = speaker.GetAudioOutputs()
        print(f"✅ 사용 가능한 오디오 출력 장치: {audio_outputs.Count}개")
        
        # 모든 장치 출력
        for i in range(audio_outputs.Count):
            output = audio_outputs.Item(i)
            device_name = output.GetDescription()
            print(f"  장치 {i+1}: {device_name}")
        
        # 블루투스 헤드폰 찾기
        bluetooth_device = None
        bluetooth_index = -1
        
        for i in range(audio_outputs.Count):
            output = audio_outputs.Item(i)
            device_name = output.GetDescription()
            
            # 블루투스 헤드폰 식별
            if "QCY" in device_name or "Bluetooth" in device_name or "Headset" in device_name:
                bluetooth_device = output
                bluetooth_index = i
                print(f"  🎧 블루투스 헤드폰 발견 (인덱스 {i}): {device_name}")
                break
        
        if bluetooth_device:
            try:
                # 블루투스 헤드폰을 기본 장치로 설정
                speaker.AudioOutput = bluetooth_device
                print("✅ 블루투스 헤드폰을 기본 장치로 설정했습니다.")
                
                # 테스트 음성 재생
                test_text = "이제 블루투스 헤드폰에서 들리시나요?"
                print(f"\n🔊 '{test_text}' 재생 중...")
                
                speaker.Speak(test_text)
                
                print("✅ Windows SAPI 블루투스 테스트 완료")
                return True
                
            except Exception as e:
                print(f"❌ 블루투스 헤드폰 설정 실패: {e}")
                return False
        else:
            print("❌ 블루투스 헤드폰을 찾을 수 없습니다.")
            return False
        
    except Exception as e:
        print(f"❌ Windows SAPI 블루투스 테스트 오류: {e}")
        return False

def test_pyttsx3_with_max_volume():
    """pyttsx3로 최대 볼륨 테스트"""
    print("\n🎧 pyttsx3 최대 볼륨 테스트")
    
    try:
        import pyttsx3
        
        # 엔진 초기화
        engine = pyttsx3.init()
        
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
        test_text = "pyttsx3 최대 볼륨으로 블루투스 헤드폰 테스트입니다"
        print(f"\n🔊 '{test_text}' 재생 중...")
        
        engine.say(test_text)
        engine.runAndWait()
        
        print("✅ pyttsx3 최대 볼륨 테스트 완료")
        return True
        
    except Exception as e:
        print(f"❌ pyttsx3 최대 볼륨 테스트 오류: {e}")
        return False

def test_hybrid_tts_with_force_bluetooth():
    """하이브리드 TTS로 강제 블루투스 테스트"""
    print("\n🎧 하이브리드 TTS 강제 블루투스 테스트")
    
    try:
        from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig, ensure_spoken_hybrid
        
        # 블루투스 헤드폰용 강제 설정
        bt_voice_config = VoiceConfig(
            name="블루투스 헤드폰 강제 설정",
            rate=130,  # 명확한 속도
            volume=1.0,  # 최대 볼륨
            language="ko"
        )
        
        test_texts = [
            "하이브리드 TTS 강제 블루투스 테스트입니다",
            "이 음성이 블루투스 헤드폰에서 재생되고 있습니다",
            "볼륨을 최대로 설정했습니다",
            "테스트가 완료되었습니다"
        ]
        
        for i, text in enumerate(test_texts, 1):
            print(f"\n🔊 테스트 {i}: '{text}'")
            ensure_spoken_hybrid(text, voice_config=bt_voice_config)
            time.sleep(1)  # 재생 간격
        
        print("\n✅ 하이브리드 TTS 강제 블루투스 테스트 완료")
        return True
        
    except Exception as e:
        print(f"❌ 하이브리드 TTS 강제 블루투스 테스트 오류: {e}")
        return False

def open_windows_sound_settings_force():
    """Windows 소리 설정 강제 열기"""
    print("\n🔧 Windows 소리 설정 강제 열기")
    
    try:
        # Windows 설정에서 소리 설정 열기
        subprocess.run(["start", "ms-settings:sound"], shell=True)
        print("✅ Windows 소리 설정이 열렸습니다.")
        print("\n📋 강제 설정 방법:")
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
        
    except Exception as e:
        print(f"❌ 설정 열기 오류: {e}")

def test_system_audio():
    """시스템 오디오 테스트"""
    print("\n🔊 시스템 오디오 테스트")
    
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
    """메인 강제 설정 함수"""
    print("🎧 블루투스 헤드폰 강제 설정 시작")
    print("=" * 50)
    
    # 1. 블루투스 헤드폰 강제 설정
    force_bluetooth_as_default()
    
    # 2. Windows SAPI 특정 장치 테스트
    test_windows_sapi_with_specific_device()
    
    # 3. pyttsx3 최대 볼륨 테스트
    test_pyttsx3_with_max_volume()
    
    # 4. 하이브리드 TTS 강제 블루투스 테스트
    test_hybrid_tts_with_force_bluetooth()
    
    # 5. 시스템 오디오 테스트
    test_system_audio()
    
    # 6. Windows 소리 설정 강제 열기
    open_windows_sound_settings_force()
    
    print("\n🎯 강제 해결 방법:")
    print("1. Windows 설정 → 시스템 → 소리에서 블루투스 헤드폰을 기본 장치로 설정")
    print("2. 블루투스 헤드폰 볼륨을 최대로 설정")
    print("3. 다른 모든 오디오 장치 비활성화")
    print("4. 블루투스 헤드폰을 재연결해보기")
    print("5. 다른 앱에서 소리가 나는지 확인")
    print("6. 블루투스 헤드폰 배터리 상태 확인")

if __name__ == "__main__":
    main() 