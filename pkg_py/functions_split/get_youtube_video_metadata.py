"""
YouTube 비디오 메타데이터 추출 함수
"""

import os
import yt_dlp
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.files import F_YOUTUBE_COOKIES_TXT


def get_youtube_video_metadata(yt_dlp, url):
    """
    YouTube 비디오 메타데이터 추출 (기본 옵션 + fallback)
    
    Args:
        yt_dlp: yt-dlp 모듈
        url: YouTube URL
        
    Returns:
        tuple: (info, title, clip_id, ext) 또는 (None, None, None, None)
    """
    
    # 기본 옵션 (대부분의 비디오에 작동)
    basic_extract_opts = {
        'quiet': True,
        'skip_download': True,
        'cookiefile': F_YOUTUBE_COOKIES_TXT if os.path.exists(F_YOUTUBE_COOKIES_TXT) else None,
        'no_warnings': False,
        'ignoreerrors': True,
    }
    
    # Fallback 옵션 (나이 제한 등 문제가 있는 비디오용)
    fallback_extract_opts = {
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
        'cookiefile': F_YOUTUBE_COOKIES_TXT if os.path.exists(F_YOUTUBE_COOKIES_TXT) else None,
    }
    
    # 쿠키 파일 확인
    if os.path.exists(F_YOUTUBE_COOKIES_TXT):
        ensure_printed(f"🍪 YouTube 쿠키 파일 사용: {F_YOUTUBE_COOKIES_TXT}", print_color="cyan")
    else:
        ensure_printed(f"⚠️ YouTube 쿠키 파일이 없습니다: {F_YOUTUBE_COOKIES_TXT}", print_color="yellow")
        ensure_printed("💡 나이 제한 비디오를 다운로드하려면 쿠키 파일이 필요합니다.", print_color="yellow")
    
    # 1단계: 기본 옵션으로 시도
    ensure_printed("🔍 1단계: 기본 옵션으로 메타데이터 추출 시도", print_color="yellow")
    try:
        with yt_dlp.YoutubeDL(basic_extract_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if info:
                title = info.get('title', 'Unknown Title')
                clip_id = info.get('id', 'Unknown ID')
                ext = info.get('ext', 'mp4')
                ensure_printed("✅ 기본 옵션으로 메타데이터 추출 성공", print_color="green")
                return info, title, clip_id, ext
            else:
                ensure_printed("❌ 기본 옵션으로 메타데이터 추출 실패", print_color="red")
                raise Exception("메타데이터 추출 실패")
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
            '메타데이터 추출 실패', 'extraction failed', 'failed to extract'
        ])
        
        # 2단계: Fallback 옵션으로 시도
        if is_age_restricted or is_format_unavailable or is_signature_failed or is_generic_failure:
            ensure_printed("🔄 2단계: Fallback 옵션으로 메타데이터 추출 재시도", print_color="yellow")
            try:
                with yt_dlp.YoutubeDL(fallback_extract_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    if info:
                        title = info.get('title', 'Unknown Title')
                        clip_id = info.get('id', 'Unknown ID')
                        ext = info.get('ext', 'mp4')
                        ensure_printed("✅ Fallback 옵션으로 메타데이터 추출 성공", print_color="green")
                        return info, title, clip_id, ext
                    else:
                        ensure_printed("❌ Fallback 옵션으로 메타데이터 추출 실패", print_color="red")
                        return None, None, None, None
            except Exception as e2:
                ensure_printed(f"❌ Fallback 옵션도 실패: {str(e2)[:100]}", print_color="red")
                return None, None, None, None
        else:
            ensure_printed("❌ Fallback 옵션으로 재시도하지 않음 (알 수 없는 오류)", print_color="red")
            return None, None, None, None
