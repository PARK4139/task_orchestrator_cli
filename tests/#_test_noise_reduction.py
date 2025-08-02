#!/usr/bin/env python3
"""
노이즈 제거 테스트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PKG_SOUND

def test_noise_reduction():
    """노이즈 제거 테스트"""
    ensure_printed("🔇 노이즈 제거 테스트", print_color="blue")
    ensure_printed("=" * 50, print_color="blue")
    
    # 기존 WAV 파일 찾기
    wav_files = [f for f in os.listdir(D_PKG_SOUND) if f.endswith('.wav')]
    if not wav_files:
        ensure_printed("❌ 테스트할 WAV 파일이 없음", print_color="red")
        return
    
    # 가장 최근 파일 선택
    latest_wav = max(wav_files, key=lambda x: os.path.getctime(os.path.join(D_PKG_SOUND, x)))
    wav_path = os.path.join(D_PKG_SOUND, latest_wav)
    
    ensure_printed(f"📁 테스트 파일: {latest_wav}", print_color="blue")
    
    # 1. 노이즈 제거 테스트
    ensure_printed("1. 노이즈 제거 테스트...", print_color="yellow")
    try:
        from pydub import AudioSegment
        from pydub.playback import play
        from pydub.effects import normalize
        
        # 오디오 로드
        audio = AudioSegment.from_wav(wav_path)
        ensure_printed(f"📊 원본 오디오 길이: {len(audio)}ms", print_color="blue")
        
        # 1-1. 볼륨 부스트 줄이기 (20dB → 10dB)
        reduced_boost = audio + 10  # 10dB로 줄임
        ensure_printed("📈 볼륨 부스트 줄임 (+10dB)", print_color="blue")
        
        # 1-2. 노이즈 게이트 적용 (낮은 볼륨 제거)
        # -40dB 이하의 소리는 제거
        noise_gate_threshold = -40  # dB
        noise_gated = reduced_boost.apply_gain_stereo(
            noise_gate_threshold, noise_gate_threshold
        )
        ensure_printed("🔇 노이즈 게이트 적용 (-40dB)", print_color="blue")
        
        # 1-3. 저주파 필터링 (60Hz 이하 제거)
        from pydub.filters import high_pass_filter
        filtered_audio = high_pass_filter(noise_gated, 60)
        ensure_printed("🔊 저주파 필터링 (60Hz 이하 제거)", print_color="blue")
        
        # 1-4. 정규화 (클리핑 방지)
        normalized_audio = normalize(filtered_audio)
        ensure_printed("📊 오디오 정규화", print_color="blue")
        
        # 노이즈 제거된 오디오 재생
        play(normalized_audio)
        ensure_printed("✅ 노이즈 제거 오디오 재생 완료", print_color="green")
        
    except Exception as e:
        ensure_printed(f"❌ 노이즈 제거 테스트 실패: {e}", print_color="red")
    
    # 2. TTS 노이즈 제거 설정 테스트
    ensure_printed("2. TTS 노이즈 제거 설정 테스트...", print_color="yellow")
    try:
        from pkg_py.functions_split.ensure_spoken import ensure_spoken
        
        # 노이즈 제거된 TTS 생성
        test_text = "노이즈가 제거된 깨끗한 음성입니다"
        ensure_printed(f"📝 테스트 텍스트: '{test_text}'", print_color="blue")
        
        ensure_spoken(test_text)
        ensure_printed("✅ 노이즈 제거 TTS 생성 완료", print_color="green")
        
    except Exception as e:
        ensure_printed(f"❌ 노이즈 제거 TTS 생성 실패: {e}", print_color="red")
    
    ensure_printed("=" * 50, print_color="blue")
    ensure_printed("🔍 노이즈 제거 테스트 완료", print_color="blue")

if __name__ == "__main__":
    test_noise_reduction() 