"""
YouTube 비디오 다운로드 함수 (yt-dlp v2)
"""

import os
import sys
import yt_dlp
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.files import F_YOUTUBE_COOKIES_TXT


def download_youtube_video_via_yt_dlp_v2(D_FFMPEG_LOCATION, D_PK_WORKING, ext, url):
    """
    YouTube 비디오 다운로드 (기본 옵션 + fallback)
    
    Args:
        D_FFMPEG_LOCATION: FFmpeg 경로
        D_PK_WORKING: 작업 디렉토리
        ext: 출력 확장자
        url: YouTube URL
    """
    
    # 기본 옵션 (대부분의 비디오에 작동)
    basic_opts = {
        'outtmpl': os.path.join(D_PK_WORKING, '%(title)s [%(id)s].%(ext)s'),
        'merge_output_format': ext,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': ext,
        }],
        'ffmpeg_location': D_FFMPEG_LOCATION,
        'cookiefile': F_YOUTUBE_COOKIES_TXT if os.path.exists(F_YOUTUBE_COOKIES_TXT) else None,
        'quiet': True,
        'no_warnings': False,
        'ignoreerrors': True,
    }
    
    # Fallback 옵션 (나이 제한 등 문제가 있는 비디오용)
    fallback_opts = {
        'outtmpl': os.path.join(D_PK_WORKING, '%(title)s [%(id)s].%(ext)s'),
        'merge_output_format': ext,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': ext,
        }],
        'ffmpeg_location': D_FFMPEG_LOCATION,
        'cookiefile': F_YOUTUBE_COOKIES_TXT if os.path.exists(F_YOUTUBE_COOKIES_TXT) else None,
        'quiet': True,
        'no_warnings': False,
        'ignoreerrors': True,
        'age_limit': 0,
        'no_check_age': True,
        'retries': 10,
        'fragment_retries': 10,
        'extractor_retries': 10,
        'geo_bypass': True,
        'no_check_certificate': True,
        'prefer_insecure': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.youtube.com/',
        }
    }
    
    # 쿠키 파일 확인
    if os.path.exists(F_YOUTUBE_COOKIES_TXT):
        ensure_printed(f"🍪 YouTube 쿠키 파일 사용: {F_YOUTUBE_COOKIES_TXT}", print_color="cyan")
    else:
        ensure_printed(f"⚠️ YouTube 쿠키 파일이 없습니다: {F_YOUTUBE_COOKIES_TXT}", print_color="yellow")
    
    # 1단계: 기본 옵션으로 시도
    ensure_printed("🔍 1단계: 기본 옵션으로 다운로드 시도", print_color="yellow")
    try:
        with yt_dlp.YoutubeDL(basic_opts) as ydl:
            ensure_printed(f"📥 기본 옵션으로 다운로드 시작: {url}", print_color="yellow")
            ydl.download([url])
            ensure_printed("✅ 기본 옵션으로 다운로드 성공", print_color="green")
            return True
    except Exception as e:
        error_msg = str(e)
        ensure_printed(f"❌ 기본 옵션 실패: {error_msg[:100]}", print_color="red")
        
        # 특정 오류 패턴 확인
        is_age_restricted = any(keyword in error_msg.lower() for keyword in [
            'age restricted', 'sign in to confirm your age', 'age verification'
        ])
        is_format_unavailable = any(keyword in error_msg.lower() for keyword in [
            'requested format is not available', 'no formats found', 'format is not available'
        ])
        is_signature_failed = any(keyword in error_msg.lower() for keyword in [
            'signature extraction failed', 'nsig extraction failed', 'signature extraction'
        ])
        is_generic_failure = any(keyword in error_msg.lower() for keyword in [
            'download failed', 'extraction failed', 'failed to download'
        ])
        
        # 2단계: Fallback 옵션으로 시도
        if is_age_restricted or is_format_unavailable or is_signature_failed or is_generic_failure:
            ensure_printed("🔄 2단계: Fallback 옵션으로 재시도", print_color="yellow")
            try:
                with yt_dlp.YoutubeDL(fallback_opts) as ydl:
                    ensure_printed(f"📥 Fallback 옵션으로 다운로드 시작: {url}", print_color="yellow")
                    ydl.download([url])
                    ensure_printed("✅ Fallback 옵션으로 다운로드 성공", print_color="green")
                    return True
            except Exception as e2:
                ensure_printed(f"❌ Fallback 옵션도 실패: {str(e2)[:100]}", print_color="red")
                return False
        else:
            ensure_printed("❌ Fallback 옵션으로 재시도하지 않음 (알 수 없는 오류)", print_color="red")
            return False
