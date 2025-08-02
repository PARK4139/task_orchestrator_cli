#!/usr/bin/env python3
"""
TTS 속도 개선 테스트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PKG_SOUND

def test_tts_speed():
    """TTS 속도 개선 테스트"""
    ensure_printed("⚡ TTS 속도 개선 테스트", print_color="blue")
    ensure_printed("=" * 50, print_color="blue")
    
    # 1. 기본 TTS 속도 테스트
    ensure_printed("1. 기본 TTS 속도 테스트...", print_color="yellow")
    try:
        from pkg_py.functions_split.ensure_spoken import ensure_spoken
        
        test_text = "이것은 기본 속도로 읽는 테스트 문장입니다"
        ensure_printed(f"📝 테스트 텍스트: '{test_text}'", print_color="blue")
        
        ensure_spoken(test_text)
        ensure_printed("✅ 기본 TTS 속도 테스트 완료", print_color="green")
        
    except Exception as e:
        ensure_printed(f"❌ 기본 TTS 속도 테스트 실패: {e}", print_color="red")
    
    # 2. 고속 TTS 테스트
    ensure_printed("2. 고속 TTS 테스트...", print_color="yellow")
    try:
        from pkg_py.functions_split.ensure_spoken import ensure_spoken
        
        test_text = "이것은 고속으로 읽는 테스트 문장입니다"
        ensure_printed(f"📝 테스트 텍스트: '{test_text}'", print_color="blue")
        
        # 고속 TTS 함수 호출 (속도 개선된 버전)
        ensure_spoken_fast(test_text)
        ensure_printed("✅ 고속 TTS 테스트 완료", print_color="green")
        
    except Exception as e:
        ensure_printed(f"❌ 고속 TTS 테스트 실패: {e}", print_color="red")
    
    ensure_printed("=" * 50, print_color="blue")
    ensure_printed("🔍 TTS 속도 테스트 완료", print_color="blue")

def ensure_spoken_fast(text, speed_factor=1.5):
    """고속 TTS 함수"""
    from pkg_py.functions_split.ensure_spoken import ensure_spoken
    from pkg_py.system_object.directories import D_PKG_SOUND
    import os
    import time
    import json
    
    # 기존 ensure_spoken 함수를 수정해서 고속 재생
    def play_audio_fast(wav_path, speed_factor=1.5):
        from pydub import AudioSegment
        from pydub.playback import play
        import os
        
        try:
            ensure_printed(f"⚡ 고속 오디오 재생 시작: {os.path.basename(wav_path)}", print_color="blue")
            
            # 오디오 로드
            audio = AudioSegment.from_wav(wav_path)
            
            # 속도 조절 (1.5배 빠르게)
            fast_audio = audio.speedup(playback_speed=speed_factor)
            ensure_printed(f"⚡ 속도 조절: {speed_factor}배 빠르게", print_color="blue")
            
            # 노이즈 제거 및 정규화
            from pydub.effects import normalize
            fast_audio = normalize(fast_audio)
            ensure_printed("📊 오디오 정규화 완료", print_color="blue")
            
            # 고속 재생
            play(fast_audio)
            ensure_printed(f"✅ 고속 재생 완료 ({speed_factor}배)", print_color="green")
            
        except Exception as e:
            ensure_printed(f"❌ 고속 재생 실패: {e}", print_color="red")
    
    # 기존 파일이 있으면 고속 재생
    index_file = os.path.join(D_PKG_SOUND, "index.json")
    if os.path.exists(index_file):
        try:
            with open(index_file, 'r', encoding='utf-8') as f:
                index_data = json.load(f)
            
            if text in index_data and os.path.exists(index_data[text]):
                play_audio_fast(index_data[text], speed_factor)
                return
        except:
            pass
    
    # 새로 생성하고 고속 재생
    ensure_spoken(text)
    
    # 생성된 파일을 고속 재생
    if os.path.exists(index_file):
        try:
            with open(index_file, 'r', encoding='utf-8') as f:
                index_data = json.load(f)
            
            if text in index_data and os.path.exists(index_data[text]):
                play_audio_fast(index_data[text], speed_factor)
        except:
            pass

if __name__ == "__main__":
    test_tts_speed() 