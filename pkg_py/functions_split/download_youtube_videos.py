def download_youtube_videos(urls=None):
    import inspect
    import yt_dlp
    import os
    import logging
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

    logging.info(f"=== YouTube 다운로드 시작 ===")
    logging.info(f"함수: {func_n}")
    logging.info(f"URL 파일: {f_func_txt}")

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

    logging.info(f"FFmpeg 위치: {D_FFMPEG_LOCATION}")

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
            logging.info("사용자 요청으로 종료")
            ensure_printed(f"🚫 {PkMessages2025.USER_REQUESTED_EXIT}.", print_color="yellow")
            return

        # YouTube 쿠키 확인 및 설정
        try:
            from pkg_py.functions_split.ensure_youtube_cookies_available import ensure_youtube_cookies_available
            ensure_youtube_cookies_available()
        except Exception as e:
            logging.warning(f"YouTube 쿠키 설정 실패: {e}")
            ensure_printed(f"⚠️ {PkMessages2025.YOUTUBE_COOKIES_SETUP_FAILED_CONTINUE}: {e}", print_color="yellow")

        # PotPlayer 시작 (단일 인스턴스)
        try:
            ensure_potplayer_started()
        except Exception as e:
            logging.warning(f"PotPlayer 시작 실패: {e}")
            ensure_printed(f"⚠️ {PkMessages2025.POTPLAYER_START_FAILED_CONTINUE}: {e}", print_color="yellow")

        urls_raw = get_list_from_f(f_func_txt)
        logging.info(f"원본 URL 개수: {len(urls_raw)}")
        
        urls = get_list_deduplicated([
            line.strip() for line in urls_raw if line.strip()
        ])
        
        logging.info(f"중복 제거 후 URL 개수: {len(urls)}")

        if not urls:
            logging.error("URL이 입력되지 않았습니다")
            ensure_printed(f"❗ {PkMessages2025.URL_NOT_ENTERED}.", print_color="red")
            return

    success_count = 0
    failed_count = 0
    
    for i, url in enumerate(urls, 1):
        url = url.strip()
        logging.info(f"=== URL {i}/{len(urls)} 처리 중 ===")
        logging.info(f"URL: {url}")

        if url.startswith("#"):
            logging.info(f"주석 처리된 URL, 건너뜀: {url}")
            ensure_printed(f"{PkMessages2025.COMMENTED_URL_SKIP}: {url}", print_color="yellow")
            continue

        try:
            logging.info(f"메타데이터 수집 시작: {url}")
            ensure_printed(f"메타데이터 수집 중... {url}")
            info, title, clip_id, ext = get_youtube_video_metadata(yt_dlp=yt_dlp, url=url)

            # 메타데이터 추출 실패 시 건너뛰기
            if info is None or title is None or clip_id is None or ext is None:
                logging.error(f"메타데이터 추출 실패: {url}")
                ensure_printed(f"⚠️ {PkMessages2025.METADATA_EXTRACTION_FAILED_SKIP}: {url}", print_color="yellow")
                failed_count += 1
                continue

            # ext 변수 로깅 추가
            logging.info(f"메타데이터 추출 성공 - ext: {ext}, title: {title}, clip_id: {clip_id}")
            ensure_printed(f"🔍 {PkMessages2025.DEBUG_METADATA_EXT} = '{ext}' (타입: {type(ext)})", print_color="yellow")
            ensure_printed(f"🔍 DEBUG: title = '{title}'", print_color="yellow")
            ensure_printed(f"🔍 DEBUG: clip_id = '{clip_id}'", print_color="yellow")

            # ext 변수를 사용하여 파일명 생성
            output_filename = f"{title} [{clip_id}].{ext}"
            f_output = os.path.join(D_PK_WORKING, output_filename)
            
            logging.info(f"생성된 파일명: {output_filename}")
            ensure_printed(f"🔍 {PkMessages2025.DEBUG_OUTPUT_FILENAME} = '{output_filename}'", print_color="yellow")

            f_pnx_downloaded = get_f_contained_feature_str(feature_str=output_filename, d_pnx=D_PK_WORKING)
            if f_pnx_downloaded and f_pnx_downloaded.lower().endswith(tuple(extensions_allowed)):
                logging.info(f"이미 다운로드된 파일 발견: {f_pnx_downloaded}")
                ensure_printed(f"download skip for {clip_id}({f_pnx_downloaded})", print_color="yellow")
                mark_url_as_done(f_func_txt, original_url=url)

                value = db.get_values(db_id='download_option')
                if value == PkMessages2025.play:
                    ensure_pnx_opened_by_ext(pnx=f_pnx_downloaded)
                continue

            logging.info(f"다운로드 시작: {url}")
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
                logging.info(f"다운로드 성공: {f_pnx_downloaded}")
                ensure_printed(f"download complete {clip_id}({f_pnx_downloaded})", print_color="green")
                mark_url_as_done(f_func_txt, original_url=url)
                success_count += 1

                # PotPlayer 재생목록에 추가
                try:
                    add_to_potplayer_playlist(f_pnx_downloaded)
                    logging.info(f"PotPlayer 재생목록에 추가됨: {f_pnx_downloaded}")
                    ensure_printed(f"🎬 {PkMessages2025.POTPLAYER_PLAYLIST_ADDED}: {f_pnx_downloaded}", print_color="cyan")
                except Exception as e:
                    logging.warning(f"PotPlayer 재생목록 추가 실패: {e}")
                    ensure_printed(f"⚠️ {PkMessages2025.POTPLAYER_PLAYLIST_ADD_FAILED}: {e}", print_color="yellow")

                value = db.get_values(db_id='download_option')
                if value == PkMessages2025.play:
                    ensure_printed(f'''f_pnx_downloaded={f_pnx_downloaded} {'%%%FOO%%%' if LTA else ''}''')
                    # PotPlayer가 이미 실행 중이므로 새 인스턴스 생성하지 않음
                    # ensure_pnx_opened_by_ext(pnx=f_pnx_downloaded)  # 주석 처리
            else:
                logging.error(f"다운로드된 파일을 찾을 수 없음: {f_output}")
                ensure_printed(f"❗ {PkMessages2025.FINAL_FILE_NOT_FOUND}: {f_output}", print_color="red")
                ensure_printed(f"🔍 DEBUG: 정규화된 파일명 = '{normalized_filename}'", print_color="yellow")
                ensure_printed(f"🔍 DEBUG: clip_id 검색 = '[{clip_id}]'", print_color="yellow")
                failed_count += 1

        except Exception as e:
            logging.error(f"예외 발생: {url} - {traceback.format_exc()}")
            ensure_printed(f"❌ {PkMessages2025.EXCEPTION_OCCURRED}: {url}\n{traceback.format_exc()}", print_color="red")
            failed_count += 1

    logging.info(f"=== YouTube 다운로드 완료 ===")
    logging.info(f"성공: {success_count}, 실패: {failed_count}, 총 URL: {len(urls)}")
    ensure_printed(f"🎬 {PkMessages2025.TOTAL_DOWNLOAD_COMPLETED}!", print_color="green")
