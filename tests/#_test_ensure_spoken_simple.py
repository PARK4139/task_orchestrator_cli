#!/usr/bin/env python3
"""
ensure_spoken 함수 단순화 테스트 (볼륨 부스트 없이)
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PKG_IMAGE_AND_VIDEO_AND_SOUND

def test_ensure_spoken_simple():
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
    
    # 2. ensure_spoken 함수의 play_audio 부분을 단순화해서 테스트
    ensure_printed("2. 단순화된 play_audio 테스트...", print_color="yellow")
    try:
        # ensure_spoken 함수의 play_audio 부분을 단순화
        def simple_play_audio(wav_path):
            import winsound
            ensure_printed(f"🔊 단순 재생 시작: {os.path.basename(wav_path)}", print_color="blue")
            winsound.PlaySound(wav_path, winsound.SND_FILENAME)
            ensure_printed("✅ 단순 재생 완료", print_color="green")
        
        simple_play_audio(wav_path)
        
    except Exception as e:
        ensure_printed(f"❌ 단순화된 play_audio 실패: {e}", print_color="red")
    
    # 3. 실제 ensure_spoken 함수 호출 (기존 파일 재생)
    ensure_printed("3. 실제 ensure_spoken 함수 호출...", print_color="yellow")
    try:
        from pkg_py.functions_split.ensure_spoken import ensure_spoken
        
        # index.json에서 기존 텍스트 찾기
        index_file = os.path.join(D_PKG_IMAGE_AND_VIDEO_AND_SOUND, "index.json")
        if os.path.exists(index_file):
            import json
            with open(index_file, 'r', encoding='utf-8') as f:
                index_data = json.load(f)
            
            # 해당 파일과 매칭되는 텍스트 찾기
            matching_text = None
            for text, file_path in index_data.items():
                if os.path.basename(file_path) == latest_wav:
                    matching_text = text
                    break
            
            if matching_text:
                ensure_printed(f"📝 매칭된 텍스트: '{matching_text}'", print_color="blue")
                ensure_spoken(matching_text)
                ensure_printed("✅ ensure_spoken 함수 실행 완료", print_color="green")
            else:
                ensure_printed("⚠️ 매칭된 텍스트를 찾을 수 없음", print_color="yellow")
        else:
            ensure_printed("❌ index.json 파일이 없음", print_color="red")
            
    except Exception as e:
        ensure_printed(f"❌ ensure_spoken 함수 호출 실패: {e}", print_color="red")
        import traceback
        ensure_printed(f"📋 상세 오류: {traceback.format_exc()}", print_color="red")
    
    ensure_printed("=" * 50, print_color="blue")
    ensure_printed("🔍 단순화 테스트 완료", print_color="blue")

if __name__ == "__main__":
    test_ensure_spoken_simple() 