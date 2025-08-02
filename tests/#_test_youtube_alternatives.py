"""
YouTube 다운로드 대안 테스트
"""

import sys
import os
import subprocess
import requests

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.files import F_YOUTUBE_COOKIES_TXT
from pkg_py.system_object.map_massages import PkMessages2025
import yt_dlp


def test_yt_dlp_alternative_options():
    """yt-dlp의 다른 옵션 조합 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.ALTERNATIVE_OPTIONS_TEST}", print_color="cyan")
    
    test_url = "https://www.youtube.com/watch?v=6jQOQQA7-eA"
    
    # 대안 1: 더 간단한 format 옵션
    ydl_opts_1 = {
        'format': 'best',
        'cookiefile': F_YOUTUBE_COOKIES_TXT,
        'age_limit': 0,
        'no_check_age': True,
        'ignoreerrors': True,
        'quiet': False,
    }
    
    # 대안 2: format을 완전히 제거
    ydl_opts_2 = {
        'cookiefile': F_YOUTUBE_COOKIES_TXT,
        'age_limit': 0,
        'no_check_age': True,
        'ignoreerrors': True,
        'quiet': False,
    }
    
    # 대안 3: extractor_args 사용
    ydl_opts_3 = {
        'format': 'best',
        'cookiefile': F_YOUTUBE_COOKIES_TXT,
        'age_limit': 0,
        'no_check_age': True,
        'ignoreerrors': True,
        'quiet': False,
        'extractor_args': {
            'youtube': {
                'player_client': ['web'],
            }
        },
    }
    
    alternatives = [
        ("대안 1: 간단한 format", ydl_opts_1),
        ("대안 2: format 제거", ydl_opts_2),
        ("대안 3: extractor_args", ydl_opts_3),
    ]
    
    for name, opts in alternatives:
        ensure_printed(f"🔍 {name} {PkMessages2025.TESTING}...", print_color="yellow")
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(test_url, download=False)
                if info:
                    ensure_printed(f"✅ {name}: {PkMessages2025.TEST_SUCCESS}", print_color="green")
                else:
                    ensure_printed(f"❌ {name}: {PkMessages2025.TEST_FAILED}", print_color="red")
        except Exception as e:
            ensure_printed(f"❌ {name}: {str(e)[:100]}", print_color="red")
        
        ensure_printed("-" * 50, print_color="white")


def test_yt_dlp_list_formats():
    """사용 가능한 형식 목록 확인"""
    ensure_printed(f"🧪 {PkMessages2025.AVAILABLE_FORMATS_CHECK}", print_color="cyan")
    
    test_url = "https://www.youtube.com/watch?v=6jQOQQA7-eA"
    
    ydl_opts = {
        'cookiefile': F_YOUTUBE_COOKIES_TXT,
        'age_limit': 0,
        'no_check_age': True,
        'quiet': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(test_url, download=False)
            if info and 'formats' in info:
                formats = info['formats']
                ensure_printed(f"📊 {PkMessages2025.AVAILABLE_FORMATS_COUNT}: {len(formats)}", print_color="cyan")
                
                # 첫 5개 형식만 표시
                for i, fmt in enumerate(formats[:5]):
                    format_id = fmt.get('format_id', 'N/A')
                    ext = fmt.get('ext', 'N/A')
                    height = fmt.get('height', 'N/A')
                    filesize = fmt.get('filesize', 'N/A')
                    ensure_printed(f"  {i+1}. ID: {format_id}, {PkMessages2025.EXTENSION}: {ext}, 높이: {height}, 크기: {filesize}", print_color="cyan")
            else:
                ensure_printed(f"❌ {PkMessages2025.FORMAT_INFO_UNAVAILABLE}", print_color="red")
    except Exception as e:
        ensure_printed(f"❌ {PkMessages2025.FORMAT_LIST_CHECK_FAILED}: {str(e)[:100]}", print_color="red")


def test_yt_dlp_direct_download():
    """직접 다운로드 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.DIRECT_DOWNLOAD_TEST}", print_color="cyan")
    
    test_url = "https://www.youtube.com/watch?v=6jQOQQA7-eA"
    output_dir = r"C:\Users\wjdgn\Downloads\pk_working"
    
    # 가장 기본적인 옵션으로 테스트
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s [%(id)s].%(ext)s'),
        'cookiefile': F_YOUTUBE_COOKIES_TXT,
        'age_limit': 0,
        'no_check_age': True,
        'ignoreerrors': True,
        'quiet': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ensure_printed(f"📥 {PkMessages2025.DOWNLOAD_START}: {test_url}", print_color="yellow")
            ydl.download([test_url])
            ensure_printed(f"✅ {PkMessages2025.DOWNLOAD_COMPLETE}", print_color="green")
    except Exception as e:
        ensure_printed(f"❌ {PkMessages2025.DOWNLOAD_FAILED}: {str(e)[:100]}", print_color="red")


def test_yt_dlp_with_user_agent():
    """User-Agent를 사용한 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.USER_AGENT_TEST}", print_color="cyan")
    
    test_url = "https://www.youtube.com/watch?v=6jQOQQA7-eA"
    
    ydl_opts = {
        'cookiefile': F_YOUTUBE_COOKIES_TXT,
        'age_limit': 0,
        'no_check_age': True,
        'ignoreerrors': True,
        'quiet': False,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate',
        }
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(test_url, download=False)
            if info:
                ensure_printed(f"✅ {PkMessages2025.USER_AGENT_SUCCESS}", print_color="green")
            else:
                ensure_printed(f"❌ {PkMessages2025.USER_AGENT_FAILED}", print_color="red")
    except Exception as e:
        ensure_printed(f"❌ {PkMessages2025.USER_AGENT_TEST}: {str(e)[:100]}", print_color="red")


def test_yt_dlp_with_referer():
    """Referer를 사용한 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.REFERER_TEST}", print_color="cyan")
    
    test_url = "https://www.youtube.com/watch?v=6jQOQQA7-eA"
    
    ydl_opts = {
        'cookiefile': F_YOUTUBE_COOKIES_TXT,
        'age_limit': 0,
        'no_check_age': True,
        'ignoreerrors': True,
        'quiet': False,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.youtube.com/',
        }
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(test_url, download=False)
            if info:
                ensure_printed(f"✅ {PkMessages2025.REFERER_SUCCESS}", print_color="green")
            else:
                ensure_printed(f"❌ {PkMessages2025.REFERER_FAILED}", print_color="red")
    except Exception as e:
        ensure_printed(f"❌ {PkMessages2025.REFERER_TEST}: {str(e)[:100]}", print_color="red")


def main():
    """메인 테스트 함수"""
    ensure_printed(f"🚀 {PkMessages2025.ALTERNATIVE_TEST_START}", print_color="cyan")
    ensure_printed("=" * 60, print_color="white")
    
    # 1. yt-dlp 대안 옵션 테스트
    test_yt_dlp_alternative_options()
    ensure_printed("", print_color="white")
    
    # 2. 사용 가능한 형식 목록 확인
    test_yt_dlp_list_formats()
    ensure_printed("", print_color="white")
    
    # 3. User-Agent 테스트
    test_yt_dlp_with_user_agent()
    ensure_printed("", print_color="white")
    
    # 4. Referer 테스트
    test_yt_dlp_with_referer()
    ensure_printed("", print_color="white")
    
    # 5. 직접 다운로드 테스트
    test_yt_dlp_direct_download()
    
    ensure_printed("=" * 60, print_color="white")
    ensure_printed(f"🏁 {PkMessages2025.ALL_ALTERNATIVE_TESTS_COMPLETE}", print_color="cyan")


if __name__ == "__main__":
    main() 