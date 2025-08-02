#!/usr/bin/env python3
"""
시스템 볼륨과 기본 오디오 테스트
"""

import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed

def test_system_volume():
    """시스템 볼륨과 기본 오디오 테스트"""
    print("🔊 시스템 볼륨 테스트")
    print("=" * 30)
    
    # 1. Windows 시스템 사운드 테스트
    print("1. Windows 시스템 사운드 테스트")
    try:
        import winsound
        winsound.MessageBeep(winsound.MB_OK)
        print("✅ Windows 시스템 사운드 재생됨")
    except Exception as e:
        print(f"❌ Windows 시스템 사운드 실패: {e}")
    
    print()
    
    # 2. 간단한 비프음 테스트
    print("2. 간단한 비프음 테스트")
    try:
        import winsound
        winsound.Beep(440, 1000)  # 440Hz, 1초
        print("✅ 비프음 재생됨")
    except Exception as e:
        print(f"❌ 비프음 실패: {e}")
    
    print()
    
    # 3. WAV 파일 직접 재생 테스트
    print("3. WAV 파일 직접 재생 테스트")
    try:
        import winsound
        wav_file = os.path.join("pkg_sound", "pop_sound.wav")
        if os.path.exists(wav_file):
            winsound.PlaySound(wav_file, winsound.SND_FILENAME)
            print("✅ WAV 파일 직접 재생됨")
        else:
            print("❌ WAV 파일이 존재하지 않습니다")
    except Exception as e:
        print(f"❌ WAV 파일 직접 재생 실패: {e}")
    
    print()
    print("🎉 시스템 볼륨 테스트 완료!")
    print("💡 만약 위의 테스트에서도 소리가 안 들린다면:")
    print("   - 시스템 볼륨을 확인해주세요")
    print("   - 스피커/헤드폰이 제대로 연결되어 있는지 확인해주세요")
    print("   - 오디오 드라이버를 업데이트해보세요")

if __name__ == "__main__":
    test_system_volume() 