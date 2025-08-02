#!/usr/bin/env python3
"""
Debug script to identify which import is causing the issue
"""

def test_imports_one_by_one():
    """Test imports one by one to identify the problem"""
    
    print("🧪 Testing imports one by one...")
    
    # 테스트 1: 기본 함수들
    try:
        from pkg_py.functions_split import get_time_as_
        print("✓ get_time_as_ imported successfully")
    except Exception as e:
        print(f"❌ get_time_as_ failed: {e}")
    
    try:
        from pkg_py.functions_split import ensure_printed
        print("✓ ensure_printed imported successfully")
    except Exception as e:
        print(f"❌ ensure_printed failed: {e}")
    
    try:
        from pkg_py.functions_split import ensure_spoken
        print("✓ ensure_spoken imported successfully")
    except Exception as e:
        print(f"❌ ensure_spoken failed: {e}")
    
    # 테스트 2: TTS 관련 함수들
    try:
        from pkg_py.functions_split import VoiceConfig
        print("✓ VoiceConfig imported successfully")
    except Exception as e:
        print(f"❌ VoiceConfig failed: {e}")
    
    try:
        from pkg_py.functions_split import ensure_spoken_hybrid
        print("✓ ensure_spoken_hybrid imported successfully")
    except Exception as e:
        print(f"❌ ensure_spoken_hybrid failed: {e}")
    
    # 테스트 3: YouTube 관련 함수들
    try:
        from pkg_py.functions_split import download_youtube_video_via_yt_dlp_v2
        print("✓ download_youtube_video_via_yt_dlp_v2 imported successfully")
    except Exception as e:
        print(f"❌ download_youtube_video_via_yt_dlp_v2 failed: {e}")
    
    try:
        from pkg_py.functions_split import get_youtube_video_metadata
        print("✓ get_youtube_video_metadata imported successfully")
    except Exception as e:
        print(f"❌ get_youtube_video_metadata failed: {e}")

if __name__ == "__main__":
    test_imports_one_by_one() 