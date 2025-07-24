from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.map_massages import PkMessages2025

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.system_object.directories import D_WORKING
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


def download_youtube_videos(urls=None):
    # from pkg_py.system_object.state_via_database import PkSqlite3DB
    # from pkg_py.system_object.map_massages import PkMessages2025
    # , D_WORKING
    # from pkg_py.system_object.files import F_FFMPEG_EXE
    #
    # from pkg_py.system_object.files_and_directories_logic import get_pnx_os_style, get_nx
    # from pkg_py.system_object.is_os_windows import is_os_windows
    #
    import inspect
    import yt_dlp
    import os
    import traceback

    func_n = inspect.currentframe().f_code.co_name
    f_func_txt = os.path.join(D_PKG_TXT, f"{func_n}.txt")
    db = PkSqlite3DB()
    ensure_pnx_made(f_func_txt, mode="f")

    extensions_allowed = {
        ".mp4", ".mkv", ".webm", ".mov", ".avi", ".flv", ".wmv", ".mpeg"
    }

    if is_os_windows():
        D_FFMPEG_LOCATION = get_pnx_os_style(get_p(F_FFMPEG_EXE))
    else:
        ensure_ubuntu_pkg_installed('ffmpeg')
        D_FFMPEG_LOCATION = get_pnx_ubuntu_pkg_installed('ffmpeg')

    if urls is None:
        open_pnx_by_ext(f_func_txt)
        ensure_window_to_front(window_title_seg=get_nx(f_func_txt))

        db_id = 'are_you_ready_to_download_urls?'
        db.reset_values(db_id=db_id)
        db.save_answer(
            question=f"{db_id}",
            options=[PkMessages2025.YES, PkMessages2025.NO],
            db_id=db_id
        )

        value = db.get_values(db_id=db_id)
        if value != PkMessages2025.YES:
            pk_print("🚫 사용자 요청으로 종료합니다.", print_color="yellow")
            return

        urls_raw = get_list_from_f(f_func_txt)
        urls = get_list_deduplicated([
            line.strip() for line in urls_raw if line.strip()
        ])

        if not urls:
            pk_print("❗ URL이 입력되지 않았습니다.", print_color="red")
            return

    for url in urls:
        url = url.strip()

        if url.startswith("#"):
            pk_print(f"주석 처리된 URL, 건너뜀: {url}", print_color="yellow")
            continue

        try:
            pk_print(f"메타데이터 수집 중... {url}")
            info, title, clip_id, ext = get_youtube_video_metadata(yt_dlp=yt_dlp, url=url)

            output_filename = f"{title} [{clip_id}].{ext}"
            f_output = os.path.join(D_WORKING, output_filename)

            f_pnx_downloaded = get_f_contained_feature_str(feature_str=output_filename, d_pnx=D_WORKING)
            if f_pnx_downloaded and f_pnx_downloaded.lower().endswith(tuple(extensions_allowed)):
                pk_print(f"download skip for {clip_id}({f_pnx_downloaded})", print_color="yellow")
                mark_url_as_done(f_func_txt, original_url=url)

                value = db.get_values(db_id='download_option')
                if value == PkMessages2025.play:
                    open_pnx_by_ext(pnx=f_pnx_downloaded)
                continue

            download_youtube_video_via_yt_dlp_v2(D_FFMPEG_LOCATION, D_WORKING, ext, url)

            # 병합된 최종 파일 존재 여부 확인
            f_pnx_downloaded = get_f_contained_feature_str(feature_str=output_filename, d_pnx=D_WORKING)
            if f_pnx_downloaded and f_pnx_downloaded.lower().endswith(tuple(extensions_allowed)):
                pk_print(f"download complete {clip_id}({f_pnx_downloaded})", print_color="green")
                mark_url_as_done(f_func_txt, original_url=url)

                value = db.get_values(db_id='download_option')
                if value == PkMessages2025.play:
                    pk_print(f'''f_pnx_downloaded={f_pnx_downloaded} {'%%%FOO%%%' if LTA else ''}''')
                    open_pnx_by_ext(pnx=f_pnx_downloaded)
            else:
                pk_print(f"❗ 병합된 최종 파일이 존재하지 않음: {f_output}", print_color="red")

        except Exception:
            pk_print(f"❌ 예외 발생: {url}\n{traceback.format_exc()}", print_color="red")

    pk_print("🎬 전체 다운로드 작업 완료!", print_color="green")
