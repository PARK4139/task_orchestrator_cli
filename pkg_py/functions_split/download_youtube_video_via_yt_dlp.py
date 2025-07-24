from pkg_py.functions_split.get_f_contained_feature_str import get_f_contained_feature_str
from pkg_py.functions_split.get_str_url_decoded import get_str_url_decoded
from pkg_py.functions_split.get_url_list_encoded_element import get_url_list_encoded_element
from pkg_py.functions_split.get_video_title_with_ytdlp import get_video_title_with_ytdlp
from pkg_py.functions_split.is_f_contained_feature_str import is_f_contained_feature_str
from pkg_py.functions_split.log_success_to_f import log_success_to_f
from pkg_py.functions_split.normalize_youtube_url import normalize_youtube_url
from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def download_youtube_video_via_yt_dlp(url_list, d_pnx, f_func_n_txt):
    import yt_dlp
    import os

    url_list = [normalize_youtube_url(url) for url in url_list]  # Shorts URL 변환

    if not does_pnx_exist(pnx=d_pnx):
        pk_print(f'''d_pnx="{d_pnx}" does not exist. Creating it.''', print_color='red')

    # 저품질 성공
    # ydl_opts = {
    #     'format': 'best',
    #     # 'format': format_selector,
    #     'outtmpl': os.path.join(d_pnx, '%(title)s [%(id)s].%(ext)s'),
    #     'quiet': False,
    #     'noplaylist': True,
    #     'force_generic_extractor': True
    # }

    # 고품질 실패
    # ydl_opts = {
    # 'format': format_selector,
    #     'outtmpl': os.path.join(d_pnx, '%(title)s [%(id)s].%(ext)s'),
    #     'quiet': False,
    #     'noplaylist': True,
    #     'force_generic_extractor': True
    # }

    # 고품질 성공
    # ydl_opts = {
    #     'format': 'bestvideo+bestaudio/best',  # 최상의 비디오 & 오디오 선택
    #     'outtmpl': os.path.join(d_pnx, '%(title)s [%(id)s].%(ext)s'),
    #     'quiet': False,
    #     'noplaylist': True,
    #     'merge_output_format': 'mp4',  # 병합 시 MP4로 저장
    #     'postprocessors': [{
    #         'key': 'FFmpegVideoConvertor',
    #         'preferedformat': 'mp4'  # 변환 후 MP4로 저장
    #     }],
    # }

    # 고품질 성공
    """ 자동으로 쿠키를 가져와서 유튜브 영상을 다운로드하는 함수 """

    cookie_f = rf"{D_PKG_TXT}/chrome_youtube_cookies.txt"
    ydl_opts = {
        'ffmpeg_location': rf'{get_pnx_os_style(get_p(F_FFMPEG_EXE))}',
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
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in url_list:
            url = normalize_youtube_url(url)
            # clip_id = url.split("v=")[-1]
            info = ydl.extract_info(url, download=False)
            clip_id = info.get('id', None)
            feature_str = f"[{clip_id}]"
            if is_f_contained_feature_str(feature_str=feature_str, d_pnx=d_pnx):
                if LTA:
                    pk_print(f"{feature_str} found in file system. Skipping download.", print_color="green")
                f_downloaded = get_f_contained_feature_str(feature_str=feature_str, d_pnx=d_pnx)
                pk_print(f'''f_downloaded="{f_downloaded}"  {'%%%FOO%%%' if LTA else ''}''')
                if f_downloaded:
                    ensure_pnx_opened_by_ext(pnx=f_downloaded)
                FEATURE_NICK_NAME = get_video_title_with_ytdlp(clip_id=clip_id)
                FEATURE_NICK_NAME = get_url_list_encoded_element(working_list=[FEATURE_NICK_NAME])[0]
                FEATURE_NICK_NAME = get_str_url_decoded(FEATURE_NICK_NAME)
                log_success_to_f(FEATURE_ID=rf"{url} {clip_id}", FEATURE_REMOVAL_ID=clip_id,
                                 FEATURE_NICK_NAME=FEATURE_NICK_NAME, f=f_func_n_txt)

                continue

            DESCRIPTION = rf'{url}'
            if LTA:
                pk_print(f'''{DESCRIPTION}  {'%%%FOO%%%' if LTA else ''}''')
            url_list = [str(url)]

            try:
                ydl.download(url_list)
                pk_print(f"f saved in '{d_pnx}'. {url}", print_color="green")
                FEATURE_NICK_NAME = get_video_title_with_ytdlp(clip_id=clip_id)
                FEATURE_NICK_NAME = get_url_list_encoded_element(working_list=[FEATURE_NICK_NAME])[0]
                FEATURE_NICK_NAME = get_str_url_decoded(FEATURE_NICK_NAME)
                log_success_to_f(FEATURE_ID=rf"{url} {clip_id}", FEATURE_REMOVAL_ID=clip_id,
                                 FEATURE_NICK_NAME=FEATURE_NICK_NAME, f=f_func_n_txt)
            except:
                import traceback
                pk_print(f'''Download {url} \n {traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}" ''',
                         print_color='red')

                continue
