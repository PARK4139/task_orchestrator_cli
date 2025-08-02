#!/usr/bin/env python3
"""
MP3 파일들을 WAV로 변환하는 스크립트
"""

import os
import glob
from pydub import AudioSegment
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PKG_SOUND
from pkg_py.functions_split.ensure_ffmpeg_installed_to_pkg_windows import ensure_ffmpeg_installed_to_pkg_windows

def convert_mp3_to_wav():
    """pkg_sound 디렉토리의 모든 MP3 파일을 WAV로 변환합니다."""
    
    # FFmpeg 설정
    ffmpeg_path, ffprobe_path = ensure_ffmpeg_installed_to_pkg_windows()
    if ffmpeg_path and ffprobe_path:
        AudioSegment.converter = ffmpeg_path
        AudioSegment.ffprobe = ffprobe_path
    
    # pkg_sound 디렉토리의 모든 MP3 파일 찾기
    mp3_pattern = os.path.join(D_PKG_SOUND, "*.mp3")
    mp3_files = glob.glob(mp3_pattern)
    
    if not mp3_files:
        ensure_printed("변환할 MP3 파일이 없습니다.", print_color="yellow")
        return
    
    ensure_printed(f"총 {len(mp3_files)}개의 MP3 파일을 WAV로 변환합니다...", print_color="blue")
    
    converted_count = 0
    failed_count = 0
    
    for mp3_file in mp3_files:
        try:
            # WAV 파일명 생성
            wav_file = mp3_file.replace('.mp3', '.wav')
            
            # 이미 WAV 파일이 존재하면 건너뛰기
            if os.path.exists(wav_file):
                ensure_printed(f"이미 존재함: {os.path.basename(wav_file)}", print_color="yellow")
                continue
            
            # MP3를 WAV로 변환
            ensure_printed(f"변환 중: {os.path.basename(mp3_file)} → {os.path.basename(wav_file)}", print_color="green")
            
            audio = AudioSegment.from_mp3(mp3_file)
            # 고품질 WAV로 변환 (44.1kHz, 스테레오, 16비트)
            audio.export(wav_file, format="wav", parameters=["-ar", "44100", "-ac", "2"])
            
            converted_count += 1
            ensure_printed(f"✅ 변환 완료: {os.path.basename(wav_file)}", print_color="green")
            
        except Exception as e:
            failed_count += 1
            ensure_printed(f"❌ 변환 실패: {os.path.basename(mp3_file)} - {e}", print_color="red")
    
    # 결과 요약
    ensure_printed(f"변환 완료: {converted_count}개 성공, {failed_count}개 실패", print_color="blue")
    
    # index.json 파일 업데이트
    update_index_file()

def update_index_file():
    """index.json 파일의 파일 경로를 MP3에서 WAV로 업데이트합니다."""
    import json
    
    index_file = os.path.join(D_PKG_SOUND, "index.json")
    
    if not os.path.exists(index_file):
        ensure_printed("index.json 파일이 없습니다.", print_color="yellow")
        return
    
    try:
        # index.json 읽기
        with open(index_file, "r", encoding="utf-8") as f:
            index_data = json.load(f)
        
        updated_count = 0
        
        # 모든 경로를 MP3에서 WAV로 변경
        for key, file_path in index_data.items():
            if file_path.endswith('.mp3'):
                wav_path = file_path.replace('.mp3', '.wav')
                # WAV 파일이 실제로 존재하는지 확인
                if os.path.exists(wav_path):
                    index_data[key] = wav_path
                    updated_count += 1
                    ensure_printed(f"경로 업데이트: {os.path.basename(file_path)} → {os.path.basename(wav_path)}", print_color="green")
        
        # 업데이트된 index.json 저장
        with open(index_file, "w", encoding="utf-8") as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)
        
        ensure_printed(f"index.json 업데이트 완료: {updated_count}개 경로 변경", print_color="blue")
        
    except Exception as e:
        ensure_printed(f"index.json 업데이트 실패: {e}", print_color="red")

def cleanup_mp3_files():
    """변환 완료 후 MP3 파일들을 삭제합니다."""
    mp3_pattern = os.path.join(D_PKG_SOUND, "*.mp3")
    mp3_files = glob.glob(mp3_pattern)
    
    if not mp3_files:
        ensure_printed("삭제할 MP3 파일이 없습니다.", print_color="yellow")
        return
    
    ensure_printed(f"총 {len(mp3_files)}개의 MP3 파일을 삭제합니다...", print_color="blue")
    
    deleted_count = 0
    
    for mp3_file in mp3_files:
        try:
            # 해당하는 WAV 파일이 존재하는지 확인
            wav_file = mp3_file.replace('.mp3', '.wav')
            if os.path.exists(wav_file):
                os.remove(mp3_file)
                deleted_count += 1
                ensure_printed(f"삭제 완료: {os.path.basename(mp3_file)}", print_color="green")
            else:
                ensure_printed(f"WAV 파일이 없어서 보존: {os.path.basename(mp3_file)}", print_color="yellow")
        except Exception as e:
            ensure_printed(f"삭제 실패: {os.path.basename(mp3_file)} - {e}", print_color="red")
    
    ensure_printed(f"삭제 완료: {deleted_count}개 파일 삭제", print_color="blue")

def main():
    """메인 함수"""
    ensure_printed("🎵 MP3 → WAV 변환 작업 시작", print_color="blue")
    print("=" * 50)
    
    # 1. MP3를 WAV로 변환
    convert_mp3_to_wav()
    print()
    
    # 2. index.json 업데이트
    update_index_file()
    print()
    
    # 3. 사용자에게 MP3 파일 삭제 여부 확인
    response = input("변환 완료 후 MP3 파일들을 삭제하시겠습니까? (y/N): ").strip().lower()
    if response in ['y', 'yes']:
        cleanup_mp3_files()
    else:
        ensure_printed("MP3 파일들이 보존되었습니다.", print_color="yellow")
    
    ensure_printed("🎉 변환 작업 완료!", print_color="blue")

if __name__ == "__main__":
    main() 