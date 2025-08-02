#!/usr/bin/env python3
"""
ensure_spoken 함수 상세 디버깅 테스트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PKG_SOUND

def test_ensure_spoken_step_by_step():
    """ensure_spoken 함수의 각 단계를 자세히 테스트"""
    ensure_printed("🔍 ensure_spoken 함수 상세 디버깅", print_color="blue")
    ensure_printed("=" * 50, print_color="blue")
    
    # 1. 기본 import 테스트
    ensure_printed("1. 모듈 import 테스트...", print_color="yellow")
    try:
        from pkg_py.functions_split.ensure_spoken import ensure_spoken
        ensure_printed("✅ ensure_spoken import 성공", print_color="green")
    except Exception as e:
        ensure_printed(f"❌ ensure_spoken import 실패: {e}", print_color="red")
        return
    
    # 2. 디렉토리 확인
    ensure_printed("2. 오디오 디렉토리 확인...", print_color="yellow")
    if os.path.exists(D_PKG_SOUND):
        ensure_printed(f"✅ 오디오 디렉토리 존재: {D_PKG_SOUND}", print_color="green")
        files = os.listdir(D_PKG_SOUND)
        ensure_printed(f"📁 파일 개수: {len(files)}", print_color="blue")
    else:
        ensure_printed(f"❌ 오디오 디렉토리 없음: {D_PKG_SOUND}", print_color="red")
    
    # 3. index.json 확인
    ensure_printed("3. index.json 확인...", print_color="yellow")
    index_file = os.path.join(D_PKG_SOUND, "index.json")
    if os.path.exists(index_file):
        try:
            import json
            with open(index_file, 'r', encoding='utf-8') as f:
                index_data = json.load(f)
            ensure_printed(f"✅ index.json 로드 성공, 항목 수: {len(index_data)}", print_color="green")
        except Exception as e:
            ensure_printed(f"❌ index.json 로드 실패: {e}", print_color="red")
    else:
        ensure_printed("⚠️ index.json 파일 없음", print_color="yellow")
    
    # 4. silent.wav 확인
    ensure_printed("4. silent.wav 확인...", print_color="yellow")
    silent_wav = os.path.join(D_PKG_SOUND, "silent.wav")
    if os.path.exists(silent_wav):
        size = os.path.getsize(silent_wav)
        ensure_printed(f"✅ silent.wav 존재, 크기: {size} bytes", print_color="green")
    else:
        ensure_printed("❌ silent.wav 없음", print_color="red")
    
    # 5. 실제 ensure_spoken 호출 (짧은 텍스트)
    ensure_printed("5. ensure_spoken 함수 호출 테스트...", print_color="yellow")
    test_text = "테스트"
    ensure_printed(f"📝 테스트 텍스트: '{test_text}'", print_color="blue")
    
    try:
        # 함수 호출 전 파일 개수 확인
        before_files = len([f for f in os.listdir(D_PKG_SOUND) if f.endswith('.wav')])
        ensure_printed(f"📊 함수 호출 전 WAV 파일 개수: {before_files}", print_color="blue")
        
        # 함수 호출
        ensure_printed("🔄 ensure_spoken 함수 호출 중...", print_color="yellow")
        ensure_spoken(test_text)
        
        # 함수 호출 후 파일 개수 확인
        after_files = len([f for f in os.listdir(D_PKG_SOUND) if f.endswith('.wav')])
        ensure_printed(f"📊 함수 호출 후 WAV 파일 개수: {after_files}", print_color="blue")
        
        if after_files > before_files:
            ensure_printed("✅ 새 WAV 파일이 생성됨", print_color="green")
        else:
            ensure_printed("⚠️ 새 WAV 파일이 생성되지 않음", print_color="yellow")
            
    except Exception as e:
        ensure_printed(f"❌ ensure_spoken 호출 실패: {e}", print_color="red")
        import traceback
        ensure_printed(f"📋 상세 오류: {traceback.format_exc()}", print_color="red")
    
    # 6. 최신 WAV 파일 확인
    ensure_printed("6. 최신 WAV 파일 확인...", print_color="yellow")
    wav_files = [f for f in os.listdir(D_PKG_SOUND) if f.endswith('.wav')]
    if wav_files:
        latest_wav = max(wav_files, key=lambda x: os.path.getctime(os.path.join(D_PKG_SOUND, x)))
        latest_path = os.path.join(D_PKG_SOUND, latest_wav)
        size = os.path.getsize(latest_path)
        ensure_printed(f"📁 최신 WAV 파일: {latest_wav} (크기: {size} bytes)", print_color="blue")
        
        # 파일 직접 재생 테스트
        ensure_printed("7. 최신 WAV 파일 직접 재생 테스트...", print_color="yellow")
        try:
            import winsound
            winsound.PlaySound(latest_path, winsound.SND_FILENAME)
            ensure_printed("✅ 직접 재생 성공", print_color="green")
        except Exception as e:
            ensure_printed(f"❌ 직접 재생 실패: {e}", print_color="red")
    else:
        ensure_printed("❌ WAV 파일이 없음", print_color="red")
    
    ensure_printed("=" * 50, print_color="blue")
    ensure_printed("🔍 디버깅 완료", print_color="blue")

if __name__ == "__main__":
    test_ensure_spoken_step_by_step() 