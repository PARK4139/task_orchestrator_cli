#!/usr/bin/env python3
"""
음질 개선 테스트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PKG_IMAGE_AND_VIDEO_AND_SOUND

def test_audio_quality():
    """음질 개선 테스트"""
    ensure_printed("🎵 음질 개선 테스트", print_color="blue")
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
    
    # 1. 현재 오디오 정보 확인
    ensure_printed("1. 현재 오디오 정보 확인...", print_color="yellow")
    try:
        from pydub import AudioSegment
        
        # 오디오 로드
        audio = AudioSegment.from_wav(wav_path)
        ensure_printed(f"📊 오디오 길이: {len(audio)}ms", print_color="blue")
        ensure_printed(f"📊 샘플레이트: {audio.frame_rate}Hz", print_color="blue")
        ensure_printed(f"📊 채널: {audio.channels}개", print_color="blue")
        ensure_printed(f"📊 샘플 너비: {audio.sample_width} bytes", print_color="blue")
        
    except Exception as e:
        ensure_printed(f"❌ 오디오 정보 확인 실패: {e}", print_color="red")
    
    # 2. 고품질 오디오 생성 테스트
    ensure_printed("2. 고품질 오디오 생성 테스트...", print_color="yellow")
    try:
        from pydub import AudioSegment
        from pydub.playback import play
        
        # 원본 오디오 로드
        audio = AudioSegment.from_wav(wav_path)
        
        # 고품질 설정으로 변환 (48kHz, 24bit, 스테레오)
        high_quality = audio.set_frame_rate(48000).set_sample_width(3).set_channels(2)
        ensure_printed("📈 고품질 변환: 48kHz, 24bit, 스테레오", print_color="blue")
        
        # 임시 파일로 저장
        temp_high_quality = wav_path.replace('.wav', '_high_quality.wav')
        high_quality.export(temp_high_quality, format="wav", parameters=[
            "-ar", "48000",  # 48kHz 샘플레이트
            "-ac", "2",      # 스테레오
            "-sample_fmt", "s24"  # 24bit
        ])
        ensure_printed(f"💾 고품질 파일 저장: {os.path.basename(temp_high_quality)}", print_color="blue")
        
        # 고품질 오디오 재생
        play(high_quality)
        ensure_printed("✅ 고품질 오디오 재생 완료", print_color="green")
        
        # 임시 파일 삭제
        os.remove(temp_high_quality)
        ensure_printed("🗑️ 임시 파일 삭제됨", print_color="blue")
        
    except Exception as e:
        ensure_printed(f"❌ 고품질 오디오 생성 실패: {e}", print_color="red")
    
    # 3. TTS 고품질 설정 테스트
    ensure_printed("3. TTS 고품질 설정 테스트...", print_color="yellow")
    try:
        from pkg_py.functions_split.ensure_spoken import ensure_spoken
        
        # 고품질 TTS 생성
        test_text = "고품질 음성 테스트입니다"
        ensure_printed(f"📝 테스트 텍스트: '{test_text}'", print_color="blue")
        
        ensure_spoken(test_text)
        ensure_printed("✅ 고품질 TTS 생성 완료", print_color="green")
        
    except Exception as e:
        ensure_printed(f"❌ 고품질 TTS 생성 실패: {e}", print_color="red")
    
    ensure_printed("=" * 50, print_color="blue")
    ensure_printed("🔍 음질 개선 테스트 완료", print_color="blue")

if __name__ == "__main__":
    test_audio_quality() 