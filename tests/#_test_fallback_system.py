"""
기본 옵션 + Fallback 시스템 테스트
"""

import sys
import os

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pkg_py.functions_split.download_youtube_video_via_yt_dlp_v2 import download_youtube_video_via_yt_dlp_v2
from pkg_py.functions_split.get_youtube_video_metadata import get_youtube_video_metadata
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.map_massages import PkMessages2025
import yt_dlp


def test_fallback_system():
    """Fallback 시스템 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.FALLBACK_SYSTEM_TEST_START}", print_color="cyan")
    
    # 테스트 URL들 (일반 비디오 + 나이 제한 비디오)
    test_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # 일반 비디오 (기본 옵션 성공 예상)
        "https://www.youtube.com/watch?v=6jQOQQA7-eA",  # 나이 제한 비디오 (fallback 필요 예상)
    ]
    
    # 테스트 설정
    D_FFMPEG_LOCATION = r"C:\Users\wjdgn\Downloads\pk_archived\LosslessCut-win-x64\resources"
    D_PK_WORKING = r"C:\Users\wjdgn\Downloads\pk_working"
    ext = "mp4"
    
    for i, url in enumerate(test_urls, 1):
        ensure_printed(f"🔍 {PkMessages2025.TEST} {i}: {url}", print_color="yellow")
        ensure_printed("=" * 50, print_color="white")
        
        # 1. 메타데이터 추출 테스트
        ensure_printed(f"📊 1단계: {PkMessages2025.METADATA_EXTRACTION_TEST}", print_color="cyan")
        try:
            info, title, clip_id, ext_result = get_youtube_video_metadata(yt_dlp, url)
            if info and title and clip_id:
                ensure_printed(f"✅ {PkMessages2025.METADATA_SUCCESS}: {title} ({clip_id})", print_color="green")
            else:
                ensure_printed(f"❌ {PkMessages2025.METADATA_FAILED}", print_color="red")
                continue
        except Exception as e:
            ensure_printed(f"❌ {PkMessages2025.METADATA_EXCEPTION}: {str(e)[:100]}", print_color="red")
            continue
        
        # 2. 다운로드 테스트
        ensure_printed(f"📥 2단계: {PkMessages2025.DOWNLOAD_TEST}", print_color="cyan")
        try:
            result = download_youtube_video_via_yt_dlp_v2(D_FFMPEG_LOCATION, D_PK_WORKING, ext, url)
            if result:
                ensure_printed(f"✅ {PkMessages2025.DOWNLOAD_SUCCESS}", print_color="green")
            else:
                ensure_printed(f"❌ {PkMessages2025.DOWNLOAD_FAILED_ALT}", print_color="red")
        except Exception as e:
            ensure_printed(f"❌ {PkMessages2025.DOWNLOAD_EXCEPTION}: {str(e)[:100]}", print_color="red")
        
        ensure_printed("", print_color="white")


def test_basic_vs_fallback():
    """기본 옵션 vs Fallback 옵션 비교 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.BASIC_VS_FALLBACK_COMPARISON}", print_color="cyan")
    
    test_url = "https://www.youtube.com/watch?v=6jQOQQA7-eA"  # 나이 제한 비디오
    
    # 기본 옵션만 테스트
    basic_opts = {
        'quiet': True,
        'skip_download': True,
        'cookiefile': r"pkg_txt/youtube_cookies.txt" if os.path.exists(r"pkg_txt/youtube_cookies.txt") else None,
        'no_warnings': False,
        'ignoreerrors': True,
    }
    
    # Fallback 옵션 테스트
    fallback_opts = {
        'quiet': True,
        'skip_download': True,
        'retries': 10,
        'fragment_retries': 10,
        'extractor_retries': 10,
        'geo_bypass': True,
        'age_limit': 0,
        'ignoreerrors': True,
        'no_warnings': False,
        'no_check_age': True,
        'extract_flat': False,
        'no_check_certificate': True,
        'prefer_insecure': True,
        'force_generic_extractor': False,
        'cookiefile': r"pkg_txt/youtube_cookies.txt" if os.path.exists(r"pkg_txt/youtube_cookies.txt") else None,
    }
    
    # 1. 기본 옵션 테스트
    ensure_printed(f"🔍 {PkMessages2025.BASIC_OPTION_TEST}", print_color="yellow")
    try:
        with yt_dlp.YoutubeDL(basic_opts) as ydl:
            info = ydl.extract_info(test_url, download=False)
            if info:
                ensure_printed(f"✅ {PkMessages2025.BASIC_OPTION_SUCCESS}", print_color="green")
            else:
                ensure_printed(f"❌ {PkMessages2025.BASIC_OPTION_FAILED}", print_color="red")
    except Exception as e:
        ensure_printed(f"❌ {PkMessages2025.BASIC_OPTION_EXCEPTION}: {str(e)[:100]}", print_color="red")
    
    # 2. Fallback 옵션 테스트
    ensure_printed(f"🔄 {PkMessages2025.FALLBACK_OPTION_TEST}", print_color="yellow")
    try:
        with yt_dlp.YoutubeDL(fallback_opts) as ydl:
            info = ydl.extract_info(test_url, download=False)
            if info:
                ensure_printed(f"✅ {PkMessages2025.FALLBACK_OPTION_SUCCESS}", print_color="green")
            else:
                ensure_printed(f"❌ {PkMessages2025.FALLBACK_OPTION_FAILED}", print_color="red")
    except Exception as e:
        ensure_printed(f"❌ {PkMessages2025.FALLBACK_OPTION_EXCEPTION}: {str(e)[:100]}", print_color="red")


def test_error_pattern_detection():
    """오류 패턴 감지 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.ERROR_PATTERN_DETECTION_TEST}", print_color="cyan")
    
    # 테스트 오류 메시지들
    test_errors = [
        "age restricted content",
        "sign in to confirm your age",
        "requested format is not available",
        "nsig extraction failed",
        "signature extraction failed",
        "video unavailable",
        "unknown error"
    ]
    
    for error in test_errors:
        # 오류 패턴 확인 로직
        is_age_restricted = any(keyword in error.lower() for keyword in [
            'age restricted', 'sign in to confirm your age', 'age verification'
        ])
        is_format_unavailable = any(keyword in error.lower() for keyword in [
            'requested format is not available', 'no formats found'
        ])
        is_signature_failed = any(keyword in error.lower() for keyword in [
            'signature extraction failed', 'nsig extraction failed'
        ])
        
        should_fallback = is_age_restricted or is_format_unavailable or is_signature_failed
        
        ensure_printed(f"🔍 오류: {error}", print_color="cyan")
        ensure_printed(f"  - 나이 제한: {is_age_restricted}", print_color="cyan")
        ensure_printed(f"  - 형식 불가: {is_format_unavailable}", print_color="cyan")
        ensure_printed(f"  - 서명 실패: {is_signature_failed}", print_color="cyan")
        ensure_printed(f"  - Fallback 필요: {should_fallback}", print_color="green" if should_fallback else "yellow")


def main():
    """메인 테스트 함수"""
    ensure_printed(f"🚀 {PkMessages2025.FALLBACK_SYSTEM_TEST_START}", print_color="cyan")
    ensure_printed("=" * 60, print_color="white")
    
    # 1. 오류 패턴 감지 테스트
    test_error_pattern_detection()
    ensure_printed("", print_color="white")
    
    # 2. 기본 vs Fallback 옵션 비교
    test_basic_vs_fallback()
    ensure_printed("", print_color="white")
    
    # 3. 전체 Fallback 시스템 테스트
    test_fallback_system()
    
    ensure_printed("=" * 60, print_color="white")
    ensure_printed(f"🏁 {PkMessages2025.ALL_TESTS_COMPLETE}", print_color="cyan")


if __name__ == "__main__":
    main() 