#!/usr/bin/env python3
"""
pydub를 사용한 오디오 재생 테스트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PKG_IMAGE_AND_VIDEO_AND_SOUND

def test_pydub_playback():
    """pydub를 사용한 오디오 재생 테스트"""
    ensure_printed("🔊 pydub 오디오 재생 테스트", print_color="blue")
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
    
    # 1. pydub.playback.play 테스트
    ensure_printed("1. pydub.playback.play 테스트...", print_color="yellow")
    try:
        from pydub import AudioSegment
        from pydub.playback import play
        
        # 오디오 로드
        audio = AudioSegment.from_wav(wav_path)
        ensure_printed(f"📊 오디오 로드됨: {len(audio)}ms", print_color="blue")
        
        # 재생
        play(audio)
        ensure_printed("✅ pydub.playback.play 재생 완료", print_color="green")
        
    except Exception as e:
        ensure_printed(f"❌ pydub.playback.play 실패: {e}", print_color="red")
    
    # 2. pydub + 볼륨 부스트 테스트
    ensure_printed("2. pydub + 볼륨 부스트 테스트...", print_color="yellow")
    try:
        from pydub import AudioSegment
        from pydub.playback import play
        
        # 오디오 로드
        audio = AudioSegment.from_wav(wav_path)
        
        # 볼륨 부스트
        boosted_audio = audio + 20  # 20dB 증가
        ensure_printed("📈 볼륨 부스트 적용됨 (+20dB)", print_color="blue")
        
        # 재생
        play(boosted_audio)
        ensure_printed("✅ pydub + 볼륨 부스트 재생 완료", print_color="green")
        
    except Exception as e:
        ensure_printed(f"❌ pydub + 볼륨 부스트 실패: {e}", print_color="red")
    
    # 3. pydub + silent.wav 연결 테스트
    ensure_printed("3. pydub + silent.wav 연결 테스트...", print_color="yellow")
    try:
        from pydub import AudioSegment
        from pydub.playback import play
        
        # silent.wav 로드
        silent_wav = os.path.join(D_PKG_IMAGE_AND_VIDEO_AND_SOUND, "silent.wav")
        if os.path.exists(silent_wav):
            silent_audio = AudioSegment.from_wav(silent_wav)
            main_audio = AudioSegment.from_wav(wav_path)
            
            # 연결
            combined_audio = silent_audio + main_audio
            ensure_printed("🔗 silent.wav와 메인 오디오 연결됨", print_color="blue")
            
            # 재생
            play(combined_audio)
            ensure_printed("✅ pydub + silent.wav 연결 재생 완료", print_color="green")
        else:
            ensure_printed("❌ silent.wav 파일이 없음", print_color="red")
            
    except Exception as e:
        ensure_printed(f"❌ pydub + silent.wav 연결 실패: {e}", print_color="red")
    
    ensure_printed("=" * 50, print_color="blue")
    ensure_printed("🔍 pydub 테스트 완료", print_color="blue")

if __name__ == "__main__":
    test_pydub_playback() 