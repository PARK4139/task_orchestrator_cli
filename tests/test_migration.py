#!/usr/bin/env python3
"""
Test script to verify that the import migration worked correctly
"""

def test_migrated_imports():
    """Test that the migrated imports work correctly"""
    
    print("🧪 Testing migrated imports...")
    
    try:
        # 테스트 1: 기본 함수들
        from pkg_py.functions_split import get_time_as_, ensure_printed, ensure_spoken
        print("✓ Basic functions imported successfully")
        
        # 테스트 2: TTS 관련 함수들
        from pkg_py.functions_split import VoiceConfig, ensure_spoken_hybrid
        print("✓ TTS functions imported successfully")
        
        # 테스트 3: YouTube 관련 함수들
        from pkg_py.functions_split import download_youtube_video_via_yt_dlp_v2, get_youtube_video_metadata
        print("✓ YouTube functions imported successfully")
        
        # 테스트 4: 시스템 관련 함수들
        from pkg_py.functions_split import ensure_command_excuted_to_os, ensure_slept, does_pnx_exist
        print("✓ System functions imported successfully")
        
        # 테스트 5: 유틸리티 함수들
        from pkg_py.functions_split import get_pnx_os_style, get_value_completed, ensure_console_cleared
        print("✓ Utility functions imported successfully")
        
        # 함수 실행 테스트
        time_str = get_time_as_("now")
        print(f"✓ Function execution test: {time_str[:20]}...")
        
        # ensure_printed 테스트
        ensure_printed("✓ Migration test successful!", print_color="green")
        
        print("✅ All migration tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Migration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_migrated_imports() 