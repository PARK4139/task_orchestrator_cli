"""
YouTube 다운로드 기능 테스트
"""

import sys
import os

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pkg_py.functions_split.download_youtube_video_via_yt_dlp_v2 import download_youtube_video_via_yt_dlp_v2
from pkg_py.functions_split.get_youtube_video_metadata import get_youtube_video_metadata
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.files import F_YOUTUBE_COOKIES_TXT
from pkg_py.system_object.map_massages import PkMessages2025
import yt_dlp


def test_youtube_metadata_extraction():
    """YouTube 메타데이터 추출 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.METADATA_EXTRACTION_TEST}", print_color="cyan")
    
    # 테스트 URL들
    test_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # 일반 비디오
        "https://www.youtube.com/watch?v=6jQOQQA7-eA",  # 나이 제한 비디오
    ]
    
    for url in test_urls:
        ensure_printed(f"🔍 {PkMessages2025.TEST_URL}: {url}", print_color="yellow")
        
        try:
            info, title, clip_id, ext = get_youtube_video_metadata(yt_dlp, url)
            
            if info and title and clip_id:
                ensure_printed(f"✅ {PkMessages2025.SUCCESS}: {title} ({clip_id})", print_color="green")
                ensure_printed(f"📊 {PkMessages2025.EXTENSION}: {ext}", print_color="cyan")
            else:
                ensure_printed(f"❌ {PkMessages2025.FAILURE}: {PkMessages2025.METADATA_FAILED}", print_color="red")
                
        except Exception as e:
            ensure_printed(f"❌ {PkMessages2025.EXCEPTION_OCCURRED}: {e}", print_color="red")
        
        ensure_printed("-" * 50, print_color="white")


def test_youtube_download():
    """YouTube 다운로드 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.DOWNLOAD_TEST}", print_color="cyan")
    
    # 테스트 설정
    D_FFMPEG_LOCATION = r"C:\Users\wjdgn\Downloads\pk_archived\LosslessCut-win-x64\resources"
    D_PK_WORKING = r"C:\Users\wjdgn\Downloads\pk_working"
    ext = "mp4"
    
    # 테스트 URL들
    test_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # 일반 비디오
        "https://www.youtube.com/watch?v=6jQOQQA7-eA",  # 나이 제한 비디오
    ]
    
    for url in test_urls:
        ensure_printed(f"🔍 {PkMessages2025.TEST_URL}: {url}", print_color="yellow")
        
        try:
            download_youtube_video_via_yt_dlp_v2(D_FFMPEG_LOCATION, D_PK_WORKING, ext, url)
            ensure_printed(f"✅ {PkMessages2025.DOWNLOAD_COMPLETE}: {url}", print_color="green")
            
        except Exception as e:
            ensure_printed(f"❌ {PkMessages2025.DOWNLOAD_FAILED}: {e}", print_color="red")
        
        ensure_printed("-" * 50, print_color="white")


def test_cookie_file():
    """쿠키 파일 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.COOKIE_FILE_TEST_START}", print_color="cyan")
    
    if os.path.exists(F_YOUTUBE_COOKIES_TXT):
        file_size = os.path.getsize(F_YOUTUBE_COOKIES_TXT)
        ensure_printed(f"✅ {PkMessages2025.COOKIE_FILE_EXISTS}: {F_YOUTUBE_COOKIES_TXT}", print_color="green")
        ensure_printed(f"📊 {PkMessages2025.FILE_SIZE}: {file_size} bytes", print_color="cyan")
        
        # 쿠키 파일 내용 확인
        with open(F_YOUTUBE_COOKIES_TXT, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            youtube_cookies = [line for line in lines if '.youtube.com' in line and not line.startswith('#')]
            ensure_printed(f"🍪 {PkMessages2025.YOUTUBE_COOKIES_COUNT}: {len(youtube_cookies)}", print_color="cyan")
            
            # 중요한 쿠키들 확인
            important_cookies = ['SID', 'HSID', 'SSID', 'APISID', 'SAPISID', '__Secure-1PSID', '__Secure-3PSID']
            found_cookies = []
            for line in youtube_cookies:
                for cookie_name in important_cookies:
                    if cookie_name in line:
                        found_cookies.append(cookie_name)
                        break
            
            ensure_printed(f"🔑 {PkMessages2025.IMPORTANT_COOKIES_FOUND}: {list(set(found_cookies))}", print_color="cyan")
    else:
        ensure_printed(f"❌ {PkMessages2025.COOKIE_FILE_NOT_FOUND}: {F_YOUTUBE_COOKIES_TXT}", print_color="red")


def test_yt_dlp_version():
    """yt-dlp 버전 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.VERSION_TEST}", print_color="cyan")
    
    try:
        version = yt_dlp.version.__version__
        ensure_printed(f"📦 yt-dlp {PkMessages2025.VERSION}: {version}", print_color="cyan")
        
        # 최신 버전인지 확인 (2024년 이후)
        if "2024" in version or "2025" in version:
            ensure_printed(f"✅ {PkMessages2025.VERSION_LATEST}", print_color="green")
        else:
            ensure_printed(f"⚠️ {PkMessages2025.VERSION_OLD}", print_color="yellow")
            
    except Exception as e:
        ensure_printed(f"❌ {PkMessages2025.VERSION_CHECK_FAILED}: {e}", print_color="red")


def main():
    """메인 테스트 함수"""
    ensure_printed(f"🚀 {PkMessages2025.FUNCTION_TEST_START}", print_color="cyan")
    ensure_printed("=" * 60, print_color="white")
    
    # 1. yt-dlp 버전 테스트
    test_yt_dlp_version()
    ensure_printed("", print_color="white")
    
    # 2. 쿠키 파일 테스트
    test_cookie_file()
    ensure_printed("", print_color="white")
    
    # 3. 메타데이터 추출 테스트
    test_youtube_metadata_extraction()
    ensure_printed("", print_color="white")
    
    # 4. 다운로드 테스트
    test_youtube_download()
    
    ensure_printed("=" * 60, print_color="white")
    ensure_printed(f"🏁 {PkMessages2025.ALL_TESTS_COMPLETE}", print_color="cyan")


if __name__ == "__main__":
    main() 