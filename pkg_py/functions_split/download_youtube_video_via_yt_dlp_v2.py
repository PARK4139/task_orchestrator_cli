"""
YouTube 비디오 다운로드 함수 (yt-dlp v2)
"""

import os
import sys
import yt_dlp
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.files import F_YOUTUBE_COOKIES_TXT
from pathlib import Path


def download_youtube_video_via_yt_dlp_v2(url, output_dir=None, output_filename=None, extract_only=False):
    """YouTube 비디오 다운로드 (v2) - 기본 옵션과 fallback 옵션 사용"""
    try:
        # Lazy import to avoid circular dependency
        try:
            from pkg_py.functions_split.ensure_printed import ensure_printed
            from pkg_py.system_object.map_massages import PkMessages2025
        except ImportError:
            print = lambda msg, **kwargs: print(msg)
            PkMessages2025 = type('PkMessages2025', (), {
                'YOUTUBE_COOKIES_SETUP_FAILED_CONTINUE': 'YouTube 쿠키 파일이 없습니다',
                'OPERATION_IN_PROGRESS': '작업 진행 중',
                'OPERATION_SUCCESS': '작업 성공',
                'OPERATION_FAILED': '작업 실패',
                'FALLBACK_NEEDED': 'Fallback 옵션으로 재시도'
            })()

        # YouTube 쿠키 확인
        from pkg_py.system_object.files import F_YOUTUBE_COOKIES_TXT
        if not Path(F_YOUTUBE_COOKIES_TXT).exists():
            ensure_printed(f"[{PkMessages2025.YOUTUBE_COOKIES_SETUP_FAILED_CONTINUE}] {F_YOUTUBE_COOKIES_TXT}", print_color="yellow")

        # 기본 옵션으로 시도
        ensure_printed(f"[{PkMessages2025.OPERATION_IN_PROGRESS}] 1단계: 기본 옵션으로 다운로드 시도", print_color="yellow")
        
        try:
            ensure_printed(f"[{PkMessages2025.OPERATION_IN_PROGRESS}] 기본 옵션으로 다운로드 시작: {url}", print_color="yellow")
            result = download_with_basic_options(url, output_dir, output_filename, extract_only)
            if result:
                ensure_printed(f"[{PkMessages2025.OPERATION_SUCCESS}] 기본 옵션으로 다운로드 성공", print_color="green")
                return result
            else:
                error_msg = "Unknown error in basic options"
                ensure_printed(f"[{PkMessages2025.OPERATION_FAILED}] 기본 옵션 실패: {error_msg[:100]}", print_color="red")
        except Exception as e:
            error_msg = str(e)
            ensure_printed(f"[{PkMessages2025.OPERATION_FAILED}] 기본 옵션 실패: {error_msg[:100]}", print_color="red")

        # Fallback 옵션으로 재시도
        ensure_printed(f"[{PkMessages2025.FALLBACK_NEEDED}]", print_color="yellow")
        
        try:
            ensure_printed(f"[{PkMessages2025.OPERATION_IN_PROGRESS}] Fallback 옵션으로 다운로드 시작: {url}", print_color="yellow")
            result = download_with_fallback_options(url, output_dir, output_filename, extract_only)
            if result:
                ensure_printed(f"[{PkMessages2025.OPERATION_SUCCESS}] Fallback 옵션으로 다운로드 성공", print_color="green")
                return result
            else:
                ensure_printed(f"[{PkMessages2025.OPERATION_FAILED}] Fallback 옵션도 실패: 알 수 없는 오류", print_color="red")
                return None
        except Exception as e2:
            ensure_printed(f"[{PkMessages2025.OPERATION_FAILED}] Fallback 옵션도 실패: {str(e2)[:100]}", print_color="red")
            return None

    except Exception as e:
        ensure_printed(f"[{PkMessages2025.OPERATION_FAILED}] Fallback 옵션으로 재시도하지 않음 (알 수 없는 오류)", print_color="red")
        return None
