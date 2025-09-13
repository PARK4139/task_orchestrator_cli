from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.get_f_contained_feature_str import get_f_contained_feature_str
from sources.functions.get_p import get_p
from pathlib import Path
from sources.functions.get_str_url_decoded import get_str_url_decoded
from sources.functions.get_url_list_encoded_element import get_url_list_encoded_element
from sources.functions.get_video_title_with_ytdlp import get_video_title_with_ytdlp
from sources.functions.is_f_contained_feature_str import is_f_contained_feature_str
from sources.functions.log_success_to_f import log_success_to_f
from sources.functions.normalize_youtube_url import normalize_youtube_url
from sources.functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext
import logging
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE, F_DOWNLOAD_YOUTUBE_VIDEOS_HISTORY
from sources.objects.pk_local_test_activate import LTA


def ensure_youtube_videos_downloaded_v2_via_yt_dlp(url_list, d_pnx, f_func_n_txt):
    import yt_dlp
    import os

    url_list = [normalize_youtube_url(url) for url in url_list]  # Shorts URL 변환

    if not is_pnx_existing(pnx=d_pnx):
        logging.debug(f'''d_pnx="{d_pnx}" does not exist. Creating it.''')

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

    cookie_f = rf"{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/youtube_cookies.txt"
    ydl_opts = {
        'ffmpeg_location': rf'{Path(get_p(F_FFMPEG_EXE))}',
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
        'cookiefile': cookie_f,  # 유튜브영상 성인인증
        'extractor_args': ['youtube:player_client=web'],
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140 Safari/537.36'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in url_list:
            url = normalize_youtube_url(url)
            # clip_id = url.split("v=")[-1]
            info = ydl.extract_info(url, download=False)
            logging.debug(f"Type of info: {type(info)}")
            logging.debug(f"Content of info: {info}")
            clip_id = info.get('id', None)
            feature_str = f"[{clip_id}]"
            if is_f_contained_feature_str(feature_str=feature_str, d_pnx=d_pnx):
                if LTA:
                    logging.debug(f"{feature_str} found in file system. Skipping download.")
                f_downloaded = get_f_contained_feature_str(feature_str=feature_str, d_pnx=d_pnx)
                logging.debug(f'''f_downloaded="{f_downloaded}"  {'%%%FOO%%%' if LTA else ''}''')
                if f_downloaded:
                    ensure_pnx_opened_by_ext(pnx=f_downloaded)
                FEATURE_NICK_NAME = get_video_title_with_ytdlp(clip_id=clip_id)
                FEATURE_NICK_NAME = get_url_list_encoded_element(working_list=[FEATURE_NICK_NAME])[0]
                FEATURE_NICK_NAME = get_str_url_decoded(FEATURE_NICK_NAME)
                log_success_to_f(FEATURE_ID=rf"{url} {clip_id}", FEATURE_REMOVAL_ID=clip_id,
                                 FEATURE_NICK_NAME=FEATURE_NICK_NAME, f=F_DOWNLOAD_YOUTUBE_VIDEOS_HISTORY)

                continue

            DESCRIPTION = rf'{url}'
            if LTA:
                logging.debug(f'''{DESCRIPTION}  {'%%%FOO%%%' if LTA else ''}''')
            url_list = [str(url)]

            try:
                ydl.download(url_list)
                logging.debug(f"f saved in '{d_pnx}'. {url}")
                FEATURE_NICK_NAME = get_video_title_with_ytdlp(clip_id=clip_id)
                FEATURE_NICK_NAME = get_url_list_encoded_element(working_list=[FEATURE_NICK_NAME])[0]
                FEATURE_NICK_NAME = get_str_url_decoded(FEATURE_NICK_NAME)
                log_success_to_f(FEATURE_ID=rf"{url} {clip_id}", FEATURE_REMOVAL_ID=clip_id,
                                 FEATURE_NICK_NAME=FEATURE_NICK_NAME, f=f_func_n_txt)
            except:
                import traceback
                logging.debug(f'''Download {url} \n {traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}" ''',
                         print_color='yellow')

                continue
