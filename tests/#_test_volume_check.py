#!/usr/bin/env python3
"""
볼륨 및 오디오 상태 확인 테스트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PKG_SOUND

def test_volume_check():
    """볼륨과 오디오 상태를 확인"""
    ensure_printed("🔊 볼륨 및 오디오 상태 확인", print_color="blue")
    ensure_printed("=" * 50, print_color="blue")
    
    # 1. 시스템 사운드 테스트
    ensure_printed("1. Windows 시스템 사운드 테스트...", print_color="yellow")
    try:
        import winsound
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        ensure_printed("✅ 시스템 사운드 재생됨", print_color="green")
    except Exception as e:
        ensure_printed(f"❌ 시스템 사운드 실패: {e}", print_color="red")
    
    # 2. 간단한 비프음 테스트
    ensure_printed("2. 간단한 비프음 테스트...", print_color="yellow")
    try:
        import winsound
        winsound.Beep(1000, 500)  # 1000Hz, 500ms
        ensure_printed("✅ 비프음 재생됨", print_color="green")
    except Exception as e:
        ensure_printed(f"❌ 비프음 실패: {e}", print_color="red")
    
    # 3. 기존 WAV 파일 재생 (볼륨 부스트 없이)
    ensure_printed("3. 기존 WAV 파일 재생 (볼륨 부스트 없이)...", print_color="yellow")
    wav_files = [f for f in os.listdir(D_PKG_SOUND) if f.endswith('.wav')]
    if wav_files:
        latest_wav = max(wav_files, key=lambda x: os.path.getctime(os.path.join(D_PKG_SOUND, x)))
        wav_path = os.path.join(D_PKG_SOUND, latest_wav)
        
        try:
            import winsound
            winsound.PlaySound(wav_path, winsound.SND_FILENAME)
            ensure_printed(f"✅ WAV 파일 재생됨: {latest_wav}", print_color="green")
        except Exception as e:
            ensure_printed(f"❌ WAV 파일 재생 실패: {e}", print_color="red")
    else:
        ensure_printed("❌ 재생할 WAV 파일이 없음", print_color="red")
    
    # 4. 볼륨 부스트 테스트
    ensure_printed("4. 볼륨 부스트 테스트...", print_color="yellow")
    if wav_files:
        try:
            from pydub import AudioSegment
            
            # 원본 오디오 로드
            audio = AudioSegment.from_file(wav_path, format="wav")
            ensure_printed(f"📊 원본 오디오 길이: {len(audio)}ms", print_color="blue")
            
            # 볼륨 부스트 (더 강하게)
            boosted_audio = audio + 30  # 30dB 증가
            ensure_printed("📈 볼륨 부스트 적용됨 (+30dB)", print_color="blue")
            
            # 임시 파일로 저장
            temp_boosted = wav_path.replace('.wav', '_temp_boosted_30db.wav')
            boosted_audio.export(temp_boosted, format="wav", parameters=["-ar", "44100", "-ac", "2"])
            ensure_printed(f"💾 임시 파일 저장: {os.path.basename(temp_boosted)}", print_color="blue")
            
            # 부스트된 파일 재생
            import winsound
            winsound.PlaySound(temp_boosted, winsound.SND_FILENAME)
            ensure_printed("✅ 볼륨 부스트 재생 완료 (+30dB)", print_color="green")
            
            # 임시 파일 삭제
            os.remove(temp_boosted)
            ensure_printed("🗑️ 임시 파일 삭제됨", print_color="blue")
            
        except Exception as e:
            ensure_printed(f"❌ 볼륨 부스트 테스트 실패: {e}", print_color="red")
    
    # 5. 사용자 확인
    ensure_printed("=" * 50, print_color="blue")
    ensure_printed("🔍 위의 테스트에서 소리가 들렸나요?", print_color="blue")
    ensure_printed("1. 시스템 사운드: 들림/안들림", print_color="yellow")
    ensure_printed("2. 비프음: 들림/안들림", print_color="yellow")
    ensure_printed("3. WAV 파일: 들림/안들림", print_color="yellow")
    ensure_printed("4. 볼륨 부스트: 들림/안들림", print_color="yellow")
    ensure_printed("=" * 50, print_color="blue")

if __name__ == "__main__":
    test_volume_check() 