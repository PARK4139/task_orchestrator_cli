#!/usr/bin/env python3
"""
자연스러운 속도 조절 테스트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PKG_IMAGE_AND_VIDEO_AND_SOUND

def test_natural_speed():
    """자연스러운 속도 조절 테스트"""
    ensure_printed("🎯 자연스러운 속도 조절 테스트", print_color="blue")
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
    
    # 1. 기본 speedup 테스트
    ensure_printed("1. 기본 speedup 테스트 (1.3배)...", print_color="yellow")
    try:
        from pydub import AudioSegment
        from pydub.playback import play
        
        # 오디오 로드
        audio = AudioSegment.from_wav(wav_path)
        
        # 기본 speedup
        fast_audio = audio.speedup(playback_speed=1.3)
        ensure_printed("⚡ 기본 speedup: 1.3배", print_color="blue")
        
        # 재생
        play(fast_audio)
        ensure_printed("✅ 기본 speedup 재생 완료", print_color="green")
        
    except Exception as e:
        ensure_printed(f"❌ 기본 speedup 테스트 실패: {e}", print_color="red")
    
    # 2. 더 자연스러운 속도 조절 테스트
    ensure_printed("2. 자연스러운 속도 조절 테스트 (1.15배)...", print_color="yellow")
    try:
        from pydub import AudioSegment
        from pydub.playback import play
        
        # 오디오 로드
        audio = AudioSegment.from_wav(wav_path)
        
        # 더 부드러운 속도 조절
        natural_audio = audio.speedup(playback_speed=1.15)
        ensure_printed("⚡ 자연스러운 속도: 1.15배", print_color="blue")
        
        # 재생
        play(natural_audio)
        ensure_printed("✅ 자연스러운 속도 재생 완료", print_color="green")
        
    except Exception as e:
        ensure_printed(f"❌ 자연스러운 속도 테스트 실패: {e}", print_color="red")
    
    # 3. TTS 자연스러운 속도 테스트
    ensure_printed("3. TTS 자연스러운 속도 테스트...", print_color="yellow")
    try:
        from pkg_py.functions_split.ensure_spoken import ensure_spoken
        
        test_text = "이것은 자연스러운 속도로 읽는 테스트 문장입니다"
        ensure_printed(f"📝 테스트 텍스트: '{test_text}'", print_color="blue")
        
        # 1.15배 속도로 테스트
        ensure_spoken(test_text, speed_factor=1.15)
        ensure_printed("✅ TTS 자연스러운 속도 테스트 완료", print_color="green")
        
    except Exception as e:
        ensure_printed(f"❌ TTS 자연스러운 속도 테스트 실패: {e}", print_color="red")
    
    ensure_printed("=" * 50, print_color="blue")
    ensure_printed("🔍 자연스러운 속도 테스트 완료", print_color="blue")

if __name__ == "__main__":
    test_natural_speed() 