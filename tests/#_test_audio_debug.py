#!/usr/bin/env python3
"""
오디오 재생 문제 진단 스크립트
"""

import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PKG_SOUND

def test_audio_system():
    """오디오 시스템 진단"""
    print("🔊 오디오 시스템 진단")
    print("=" * 40)
    
    # 1. 기본 오디오 테스트
    print("1. 기본 오디오 테스트")
    try:
        from pydub import AudioSegment
        from pydub.playback import play
        
        # 간단한 비프음 생성
        beep = AudioSegment.sine(440, duration=1000)  # 440Hz, 1초
        print("비프음 재생 중...")
        play(beep)
        print("✅ 기본 오디오 재생 성공")
    except Exception as e:
        print(f"❌ 기본 오디오 재생 실패: {e}")
    
    print()
    
    # 2. WAV 파일 직접 재생 테스트
    print("2. WAV 파일 직접 재생 테스트")
    try:
        from pydub import AudioSegment
        from pydub.playback import play
        
        # 기존 WAV 파일 재생
        wav_file = os.path.join(D_PKG_SOUND, "20250801_211619_안녕하세요.wav")
        if os.path.exists(wav_file):
            print(f"WAV 파일 재생 중: {os.path.basename(wav_file)}")
            audio = AudioSegment.from_file(wav_file, format="wav")
            play(audio)
            print("✅ WAV 파일 재생 성공")
        else:
            print("❌ WAV 파일이 존재하지 않습니다")
    except Exception as e:
        print(f"❌ WAV 파일 재생 실패: {e}")
    
    print()
    
    # 3. 시스템 사운드 테스트
    print("3. 시스템 사운드 테스트")
    try:
        from pydub import AudioSegment
        from pydub.playback import play
        
        pop_sound = os.path.join(D_PKG_SOUND, "pop_sound.wav")
        if os.path.exists(pop_sound):
            print("시스템 사운드 재생 중...")
            audio = AudioSegment.from_file(pop_sound, format="wav")
            play(audio)
            print("✅ 시스템 사운드 재생 성공")
        else:
            print("❌ 시스템 사운드 파일이 존재하지 않습니다")
    except Exception as e:
        print(f"❌ 시스템 사운드 재생 실패: {e}")
    
    print()
    
    # 4. ensure_spoken 함수 테스트
    print("4. ensure_spoken 함수 테스트")
    try:
        from pkg_py.functions_split.ensure_spoken import ensure_spoken
        
        print("ensure_spoken 함수 호출 중...")
        ensure_spoken("테스트 음성입니다")
        print("✅ ensure_spoken 함수 실행 완료")
    except Exception as e:
        print(f"❌ ensure_spoken 함수 실패: {e}")
    
    print()
    print("🎉 진단 완료!")

if __name__ == "__main__":
    test_audio_system() 