#!/usr/bin/env python3
"""
ensure_spoken 함수 단순화 테스트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PKG_IMAGE_AND_VIDEO_AND_SOUND

def test_simple_ensure_spoken():
    """ensure_spoken 함수를 단순화해서 테스트"""
    ensure_printed("🔊 ensure_spoken 단순화 테스트", print_color="blue")
    ensure_printed("=" * 50, print_color="blue")
    
    # 기존 WAV 파일 찾기
    wav_files = [f for f in os.listdir(D_PKG_IMAGE_AND_VIDEO_AND_SOUND) if f.endswith('.wav')]
    if not wav_files:
        ensure_printed("❌ 테스트할 WAV 파일이 없음", print_color="red")
        return
    
    # 가장 최근 파일 선택
    latest_wav = max(wav_files, key=lambda x: os.path.getctime(os.path.join(D_PKG_IMAGE_AND_VIDEO_AND_SOUND, x)))
    wav_path = os.path.join(D_PKG_IMAGE_AND_VIDEO_AND_SOUND, latest_wav)
    
    ensure_printed(f"📁 테스트 파일: {latest_wav}", print_color="blue")
    
    # 1. 단순 winsound 재생 (볼륨 부스트 없이)
    ensure_printed("1. 단순 winsound 재생 테스트...", print_color="yellow")
    try:
        import winsound
        winsound.PlaySound(wav_path, winsound.SND_FILENAME)
        ensure_printed("✅ 단순 winsound 재생 완료", print_color="green")
    except Exception as e:
        ensure_printed(f"❌ 단순 winsound 재생 실패: {e}", print_color="red")
    
    # 2. 볼륨 부스트만 테스트
    ensure_printed("2. 볼륨 부스트 테스트...", print_color="yellow")
    try:
        from pydub import AudioSegment
        
        # 원본 오디오 로드
        audio = AudioSegment.from_file(wav_path, format="wav")
        ensure_printed(f"📊 원본 오디오 길이: {len(audio)}ms", print_color="blue")
        
        # 볼륨 부스트
        boosted_audio = audio + 20  # 20dB 증가
        ensure_printed("📈 볼륨 부스트 적용됨", print_color="blue")
        
        # 임시 파일로 저장
        temp_boosted = wav_path.replace('.wav', '_temp_boosted.wav')
        boosted_audio.export(temp_boosted, format="wav")
        ensure_printed(f"💾 임시 파일 저장: {os.path.basename(temp_boosted)}", print_color="blue")
        
        # 부스트된 파일 재생
        import winsound
        winsound.PlaySound(temp_boosted, winsound.SND_FILENAME)
        ensure_printed("✅ 볼륨 부스트 재생 완료", print_color="green")
        
        # 임시 파일 삭제
        os.remove(temp_boosted)
        ensure_printed("🗑️ 임시 파일 삭제됨", print_color="blue")
        
    except Exception as e:
        ensure_printed(f"❌ 볼륨 부스트 테스트 실패: {e}", print_color="red")
    
    # 3. silent.wav 연결 테스트
    ensure_printed("3. silent.wav 연결 테스트...", print_color="yellow")
    try:
        silent_wav = os.path.join(D_PKG_IMAGE_AND_VIDEO_AND_SOUND, "silent.wav")
        if os.path.exists(silent_wav):
            from pkg_py.functions_split.ensure_ffmpeg_installed_to_pkg_windows import ensure_ffmpeg_installed_to_pkg_windows
            import subprocess
            
            ffmpeg_path, ffprobe_path = ensure_ffmpeg_installed_to_pkg_windows()
            if ffmpeg_path:
                # 임시 파일명 생성
                temp_connected = wav_path.replace('.wav', '_with_silent.wav')
                
                # ffmpeg로 silent.wav와 원본 wav를 연결
                cmd = f'"{ffmpeg_path}" -i "concat:{os.path.abspath(silent_wav)}|{os.path.abspath(wav_path)}" -acodec pcm_s16le "{os.path.abspath(temp_connected)}" -y'
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                
                if os.path.exists(temp_connected):
                    ensure_printed("✅ silent.wav 연결 성공", print_color="green")
                    
                    # 연결된 파일 재생
                    import winsound
                    winsound.PlaySound(temp_connected, winsound.SND_FILENAME)
                    ensure_printed("✅ 연결된 파일 재생 완료", print_color="green")
                    
                    # 임시 파일 삭제
                    os.remove(temp_connected)
                    ensure_printed("🗑️ 연결 임시 파일 삭제됨", print_color="blue")
                else:
                    ensure_printed(f"❌ silent.wav 연결 실패: {result.stderr}", print_color="red")
            else:
                ensure_printed("❌ FFmpeg를 찾을 수 없음", print_color="red")
        else:
            ensure_printed("❌ silent.wav 파일이 없음", print_color="red")
            
    except Exception as e:
        ensure_printed(f"❌ silent.wav 연결 테스트 실패: {e}", print_color="red")
    
    ensure_printed("=" * 50, print_color="blue")
    ensure_printed("🔍 단순화 테스트 완료", print_color="blue")

if __name__ == "__main__":
    test_simple_ensure_spoken() 