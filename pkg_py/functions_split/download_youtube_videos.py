def download_youtube_videos(urls=None):
    import inspect
    import yt_dlp
    import os
    from pkg_py.functions_split.download_youtube_video_via_yt_dlp_v2 import download_youtube_video_via_yt_dlp_v2
    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    from pkg_py.functions_split.ensure_ubuntu_pkg_enabled import ensure_ubuntu_pkg_enabled
    from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
    from pkg_py.functions_split.get_f_contained_feature_str import get_f_contained_feature_str
    from pkg_py.functions_split.get_list_deduplicated import get_list_deduplicated
    from pkg_py.functions_split.get_list_from_f import get_list_from_f
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_p import get_p
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_pnx_ubuntu_pkg_enabled import get_pnx_ubuntu_pkg_enabled
    from pkg_py.functions_split.get_youtube_video_metadata import get_youtube_video_metadata
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.functions_split.mark_url_as_done import mark_url_as_done
    from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
    from pkg_py.functions_split.add_to_potplayer_playlist import add_to_potplayer_playlist
    from pkg_py.functions_split.ensure_potplayer_started import ensure_potplayer_started
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.directories import D_PKG_TXT
    from pkg_py.system_object.directories import D_PK_WORKING
    from pkg_py.system_object.files import F_FFMPEG_EXE
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.system_object.state_via_database import PkSqlite3DB

    import traceback

    func_n = inspect.currentframe().f_code.co_name
    f_func_txt = os.path.join(D_PKG_TXT, f"{func_n}.txt")
    db = PkSqlite3DB()
    ensure_pnx_made(f_func_txt, mode="f")

    if urls is None:
        ensure_pnx_opened_by_ext(f_func_txt)
        ensure_window_to_front(window_title_seg=get_nx(f_func_txt))

    extensions_allowed = {
        ".mp4", ".mkv", ".webm", ".mov", ".avi", ".flv", ".wmv", ".mpeg"
    }

    if is_os_windows():
        D_FFMPEG_LOCATION = get_pnx_os_style(get_p(F_FFMPEG_EXE))
    else:
        ensure_ubuntu_pkg_enabled('ffmpeg')
        D_FFMPEG_LOCATION = get_pnx_ubuntu_pkg_enabled('ffmpeg')

    if urls is None:
        db_id = 'are_you_ready_to_download_urls?'
        db.reset_values(db_id=db_id)
        db.save_answer(
            question=f"{db_id}",
            options=[PkMessages2025.YES, PkMessages2025.NO],
            db_id=db_id
        )

        value = db.get_values(db_id=db_id)
        if value != PkMessages2025.YES:
            ensure_printed("🚫 사용자 요청으로 종료합니다.", print_color="yellow")
            return

        # YouTube 쿠키 확인 및 설정
        try:
            from pkg_py.functions_split.ensure_youtube_cookies_available import ensure_youtube_cookies_available
            ensure_youtube_cookies_available()
        except Exception as e:
            ensure_printed(f"⚠️ YouTube 쿠키 설정 실패, 계속 진행: {e}", print_color="yellow")

        # PotPlayer 시작 (단일 인스턴스)
        try:
            ensure_potplayer_started()
        except Exception as e:
            ensure_printed(f"⚠️ PotPlayer 시작 실패, 계속 진행: {e}", print_color="yellow")

        urls_raw = get_list_from_f(f_func_txt)
        urls = get_list_deduplicated([
            line.strip() for line in urls_raw if line.strip()
        ])

        if not urls:
            ensure_printed("❗ URL이 입력되지 않았습니다.", print_color="red")
            return

    for url in urls:
        url = url.strip()

        if url.startswith("#"):
            ensure_printed(f"주석 처리된 URL, 건너뜀: {url}", print_color="yellow")
            continue

        try:
            ensure_printed(f"메타데이터 수집 중... {url}")
            info, title, clip_id, ext = get_youtube_video_metadata(yt_dlp=yt_dlp, url=url)

            # 메타데이터 추출 실패 시 건너뛰기
            if info is None or title is None or clip_id is None or ext is None:
                ensure_printed(f"⚠️ 메타데이터 추출 실패로 건너뜀: {url}", print_color="yellow")
                continue

            # ext 변수 로깅 추가
            ensure_printed(f"🔍 DEBUG: 메타데이터에서 받은 ext = '{ext}' (타입: {type(ext)})", print_color="yellow")
            ensure_printed(f"🔍 DEBUG: title = '{title}'", print_color="yellow")
            ensure_printed(f"🔍 DEBUG: clip_id = '{clip_id}'", print_color="yellow")

            # ext 변수를 사용하여 파일명 생성
            output_filename = f"{title} [{clip_id}].{ext}"
            f_output = os.path.join(D_PK_WORKING, output_filename)
            
            ensure_printed(f"🔍 DEBUG: 생성된 output_filename = '{output_filename}'", print_color="yellow")

            f_pnx_downloaded = get_f_contained_feature_str(feature_str=output_filename, d_pnx=D_PK_WORKING)
            if f_pnx_downloaded and f_pnx_downloaded.lower().endswith(tuple(extensions_allowed)):
                ensure_printed(f"download skip for {clip_id}({f_pnx_downloaded})", print_color="yellow")
                mark_url_as_done(f_func_txt, original_url=url)

                value = db.get_values(db_id='download_option')
                if value == PkMessages2025.play:
                    ensure_pnx_opened_by_ext(pnx=f_pnx_downloaded)
                continue

            ensure_printed(f"🔍 DEBUG: download_youtube_video_via_yt_dlp_v2 호출 - ext='{ext}'", print_color="yellow")
            download_youtube_video_via_yt_dlp_v2(D_FFMPEG_LOCATION, D_PK_WORKING, ext, url)

            # 병합된 최종 파일 존재 여부 확인 (파일명 정규화 포함)
            f_pnx_downloaded = get_f_contained_feature_str(feature_str=output_filename, d_pnx=D_PK_WORKING)
            
            # 파일명 정규화: 전각 파이프를 일반 파이프로 변경
            normalized_filename = output_filename.replace('｜', '|')
            if not f_pnx_downloaded:
                f_pnx_downloaded = get_f_contained_feature_str(feature_str=normalized_filename, d_pnx=D_PK_WORKING)
            
            # clip_id로도 검색 시도
            if not f_pnx_downloaded:
                f_pnx_downloaded = get_f_contained_feature_str(feature_str=f"[{clip_id}]", d_pnx=D_PK_WORKING)
            
            if f_pnx_downloaded and f_pnx_downloaded.lower().endswith(tuple(extensions_allowed)):
                ensure_printed(f"download complete {clip_id}({f_pnx_downloaded})", print_color="green")
                mark_url_as_done(f_func_txt, original_url=url)

                # PotPlayer 재생목록에 추가
                try:
                    add_to_potplayer_playlist(f_pnx_downloaded)
                    ensure_printed(f"🎬 PotPlayer 재생목록에 추가됨: {f_pnx_downloaded}", print_color="cyan")
                except Exception as e:
                    ensure_printed(f"⚠️ PotPlayer 재생목록 추가 실패: {e}", print_color="yellow")

                value = db.get_values(db_id='download_option')
                if value == PkMessages2025.play:
                    ensure_printed(f'''f_pnx_downloaded={f_pnx_downloaded} {'%%%FOO%%%' if LTA else ''}''')
                    # PotPlayer가 이미 실행 중이므로 새 인스턴스 생성하지 않음
                    # ensure_pnx_opened_by_ext(pnx=f_pnx_downloaded)  # 주석 처리
            else:
                ensure_printed(f"❗ 병합된 최종 파일이 존재하지 않음: {f_output}", print_color="red")
                ensure_printed(f"🔍 DEBUG: 정규화된 파일명 = '{normalized_filename}'", print_color="yellow")
                ensure_printed(f"🔍 DEBUG: clip_id 검색 = '[{clip_id}]'", print_color="yellow")

        except Exception:
            ensure_printed(f"❌ 예외 발생: {url}\n{traceback.format_exc()}", print_color="red")

    ensure_printed("🎬 전체 다운로드 작업 완료!", print_color="green")
