from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.download_youtube_video_via_yt_dlp import download_youtube_video_via_yt_dlp
from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.ensure_ubuntu_pkg_enabled import ensure_ubuntu_pkg_enabled
from pkg_py.functions_split.get_f_contained_feature_str import get_f_contained_feature_str
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_list_deduplicated import get_list_deduplicated
from pkg_py.functions_split.get_list_from_f import get_list_from_f
from pkg_py.functions_split.get_list_removed_element_contain_prompt import get_list_removed_element_contain_prompt
from pkg_py.functions_split.get_list_removed_element_empty import get_list_removed_empty
from pkg_py.functions_split.get_list_striped_element import get_list_striped_element
from pkg_py.functions_split.get_p import get_p
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_ubuntu_pkg_enabled import get_pnx_ubuntu_pkg_enabled
from pkg_py.functions_split.get_str_from_clipboard import get_str_from_clipboard
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_youtube_clip_id import get_youtube_clip_id
from pkg_py.functions_split.is_f_contained_feature_str import is_f_contained_feature_str
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.is_url import is_url
from pkg_py.functions_split.normalize_youtube_url import normalize_youtube_url
from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.remove_lines_within_keyword_from_f import remove_lines_within_keyword_from_f
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.etc import PK_BLANK
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.state_via_database import PkSqlite3DB


def download_youtube_video():
    try:
        import inspect

        import yt_dlp
        import os
        import sys

        d_pnx = D_PK_WORKING
        func_n = inspect.currentframe().f_code.co_name
        f_func_n_txt = rf'{D_PKG_TXT}/{func_n}.txt'  # success log 기록 # 불필요함.  success 이면 f_historical 에서 삭제되도록 함.

        cookie_f = rf"{D_PKG_TXT}/chrome_youtube_cookies.txt"
        if is_os_windows():
            ffmpeg_location = rf'{get_pnx_os_style(get_p(F_FFMPEG_EXE))}'
        else:
            ensure_ubuntu_pkg_enabled('ffmpeg')
            ffmpeg_location = get_pnx_ubuntu_pkg_enabled('ffmpeg')
        ydl_opts = {
            'ffmpeg_location': ffmpeg_location,
            'format': 'bestvideo+bestaudio/best',  # 최상의 비디오 & 오디오 선택
            'outtmpl': os.path.join(d_pnx, '%(title)s [%(id)s].%(ext)s'),
            'quiet': False,
            'noplaylist': True,
            'merge_output_format': 'mp4',  # 병합 시 MP4로 저장
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'  # 변환 후 MP4로 저장
            }],
            'geo_bypass': True,  # 지역 제한 우회
            'cookiefile': cookie_f  # 유튜브영상 성인인증
        }

        # search_keyword = input(f"{pk_get_colorful_str_working_with_stamp_enviromnet(func_n=func_n, ment='WRITE URL TO DOWNLOAD')} >")

        f_historical = rf'{D_PKG_TXT}/historical_{func_n}.txt'
        ensure_pnx_made(pnx=f_historical, mode='f')

        pk_db = PkSqlite3DB()

        value = pk_db.get_values(db_id='open historical f')
        if value == PkMessages2025.YES:
            ensure_pnx_opened_by_ext(pnx=f_historical)
            pk_db.set_values(db_id="open historical f", values="YES, one time done")  # 프로그램 실생 중 1회만 실행제한

        youtube_video_url_from_clipboard = get_str_from_clipboard()
        marker_for_clipboard = f'{PK_BLANK}(url from clipboard)'
        youtube_video_url_from_clipboard = rf"{youtube_video_url_from_clipboard}{marker_for_clipboard}"

        historical_lines = get_historical_list(f=f_historical)
        if youtube_video_url_from_clipboard and is_url(youtube_video_url_from_clipboard):
            youtube_clip_id = youtube_video_url_from_clipboard.split("v=")[-1]
            if is_f_contained_feature_str(feature_str=youtube_clip_id, d_pnx=d_pnx):
                youtube_clip_id_stamp = f"[{youtube_clip_id}]"
                ensure_printed(f"{youtube_clip_id_stamp} is already downloaded, {youtube_video_url_from_clipboard}",
                         print_color="green")

                value = pk_db.get_values(db_id='download_option')
                # play or skip video
                if value == PkMessages2025.play:
                    # play video
                    f_pnx_downloaded = get_f_contained_feature_str(feature_str=youtube_clip_id, d_pnx=d_pnx)
                    if f_pnx_downloaded:
                        ensure_pnx_opened_by_ext(pnx=f_pnx_downloaded)
                if value == PkMessages2025.SKIP:
                    pass

                # 다운로드 여부 확인 후 제거
                remove_lines_within_keyword_from_f(f=f_historical, keyword=youtube_clip_id)

                # get historical list
                historical_lines = get_historical_list(f=f_historical)
            else:
                option_values = [youtube_video_url_from_clipboard] + historical_lines

        option_values = historical_lines

        for historical_url in historical_lines:
            historical_url = historical_url.strip()

            youtube_clip_id = historical_url.split("v=")[-1]
            youtube_clip_id_stamp = f"[{youtube_clip_id}]"
            if not is_url(historical_url):
                # URL 아닌 건 제거
                remove_lines_within_keyword_from_f(f=f_historical, keyword=youtube_clip_id)
                continue

            if is_f_contained_feature_str(feature_str=youtube_clip_id_stamp, d_pnx=d_pnx):
                ensure_printed(f"{youtube_clip_id_stamp} is already downloaded, {historical_url}", print_color="green")
                pk_db = PkSqlite3DB()
                db_id = 'download_option'
                value = pk_db.get_values(db_id=db_id)
                ensure_printed(f'''db_id=value : {db_id}={value} {'%%%FOO%%%' if LTA else ''}''', print_color="green")

                # play or skip video
                if value == PkMessages2025.play:
                    # play video
                    f_pnx_downloaded = get_f_contained_feature_str(feature_str=youtube_clip_id, d_pnx=d_pnx)
                    if f_pnx_downloaded:
                        ensure_pnx_opened_by_ext(pnx=f_pnx_downloaded)
                if value == PkMessages2025.SKIP:
                    pass

                # 다운로드 여부 확인 후 제거
                remove_lines_within_keyword_from_f(f=f_historical, keyword=youtube_clip_id)

        # get historical list
        historical_lines = get_historical_list(f=f_historical)

        answer = get_value_completed(key_hint='YOUTUBE URL TO DOWNLOAD=', values=option_values)
        answer = answer.strip()
        if answer.lower() == "x" or answer.lower() == "exit" or answer.lower() == "q" or answer.lower() == "quit":
            sys.exit(0)
        url = answer
        ensure_list_written_to_f(f=f_historical, working_list=[url] + historical_lines, mode="w")
        url = url.replace(marker_for_clipboard, "")

        if not does_pnx_exist(pnx=f_historical):
            ensure_pnx_made(pnx=f_historical, mode="f")
        working_list = get_list_from_f(f=f_historical)
        working_list = get_list_removed_element_contain_prompt(working_list=working_list, prompt="#")
        working_list = get_list_deduplicated(working_list=working_list)
        working_list = get_list_removed_empty(working_list=working_list)
        working_list = get_list_striped_element(working_list=working_list)
        urls = [url] + working_list
        ensure_printed(str_working=str(len(urls)))
        urls = get_list_removed_empty(working_list=urls)
        ensure_printed(str_working=str(len(urls)))
        if len(urls) == 0:
            ensure_printed(f'''len(urls)={len(urls)}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            return

        if is_os_windows():
            youtube_clip_id = get_youtube_clip_id(url=url)
            download_youtube_video_via_yt_dlp(url_list=[youtube_clip_id], d_pnx=d_pnx, f_func_n_txt=f_func_n_txt)

            youtube_clip_id_stamp = f"[{youtube_clip_id}]"
            if is_f_contained_feature_str(feature_str=youtube_clip_id_stamp, d_pnx=d_pnx):
                ensure_printed(f"{youtube_clip_id_stamp} is already downloaded, {url}", print_color="green")
                pk_db = PkSqlite3DB()
                db_id = 'download_option'
                value = pk_db.get_values(db_id=db_id)
                if value == PkMessages2025.play:
                    # play video
                    f_pnx_downloaded = get_f_contained_feature_str(feature_str=youtube_clip_id, d_pnx=d_pnx)
                    if f_pnx_downloaded:
                        ensure_pnx_opened_by_ext(pnx=f_pnx_downloaded)
                if value == PkMessages2025.SKIP:
                    pass

            # 다운로드 여부 확인 후 제거
            remove_lines_within_keyword_from_f(f=f_historical, keyword=youtube_clip_id)

            # get historical list
            historical_lines = get_historical_list(f=f_historical)
        else:
            url_list = [normalize_youtube_url(url) for url in urls]  # Shorts URL 변환
            # 자동으로 쿠키를 가져옴

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    for url in url_list:
                        url = normalize_youtube_url(url)
                        info = ydl.extract_info(url, download=False)
                        youtube_clip_id = info.get('id', None)
                        youtube_clip_id_stamp = f"[{youtube_clip_id}]"
                        clip_title = info.get('title')
                        url_list = [str(url)]
                        ensure_printed(f'''clip_id={youtube_clip_id} {'%%%FOO%%%' if LTA else ''}''')
                        ensure_printed(f'''clip_title={clip_title} {'%%%FOO%%%' if LTA else ''}''')

                        # skip download
                        if is_f_contained_feature_str(feature_str=youtube_clip_id_stamp, d_pnx=d_pnx):
                            ensure_printed(f"{youtube_clip_id_stamp} is already downloaded, {clip_title}({url})",
                                     print_color="green")

                            # play/skip decision
                            pk_db = PkSqlite3DB()
                            db_id = 'download_option'
                            value = pk_db.get_values(db_id=db_id)
                            ensure_printed(f'''db_id=value : {db_id}={value} {'%%%FOO%%%' if LTA else ''}''',
                                     print_color="green")
                            if value == PkMessages2025.play:
                                # play video
                                f_pnx_downloaded = get_f_contained_feature_str(feature_str=youtube_clip_id, d_pnx=d_pnx)
                                if f_pnx_downloaded:
                                    ensure_pnx_opened_by_ext(pnx=f_pnx_downloaded)
                            if value == PkMessages2025.SKIP:
                                pass

                            # remove f in f_historical after download
                            remove_lines_within_keyword_from_f(f=f_historical, keyword=youtube_clip_id)

                            # get historical list
                            historical_lines = get_historical_list(f=f_historical)
                            continue

                        # download
                        ydl.download(url_list)

                        # check f after download
                        if is_f_contained_feature_str(feature_str=youtube_clip_id_stamp, d_pnx=d_pnx):
                            ensure_printed(f"f saved in '{d_pnx}'. {url}", print_color="green")

                            # remove f in f_historical after download
                            remove_lines_within_keyword_from_f(f=f_historical, keyword=youtube_clip_id)

                            # get historical list
                            historical_lines = get_historical_list(f=f_historical)
                            continue

            except:
                import traceback
                traceback.print_exc()
                ensure_printed(f'''Download {url} \n {traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}" ''',
                         print_color='red')
    except SystemExit as e:
        if e.code == 0:
            ensure_printed('[정상 종료됨: SystemExit(0)]', print_color='green')
            sys.exit(0)
        else:
            raise  # 비정상 종료는 그대로 propagate
    except:
        import traceback
        import sys
        traceback.print_exc()
