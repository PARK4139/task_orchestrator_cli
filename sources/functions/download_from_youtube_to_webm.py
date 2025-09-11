

import win32con
import win32com.client
import webbrowser
import tomllib
import toml
import toml
import timeit
import threading
import socket, time
import re
import pywintypes
import pickle
import numpy as np
import importlib
import chardet
import asyncio
from tkinter import UNDERLINE
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from pynput import mouse
from prompt_toolkit.styles import Style
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern

from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f

from sources.functions.ensure_console_cleared import ensure_console_cleared


from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_state_via_context import SpeedControlContext

from pathlib import Path
from os.path import dirname
from moviepy import VideoFileClip
from dirsync import sync
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from sources.functions.get_nx import get_nx

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.functions.get_pnxs import get_pnxs
from sources.functions.is_d import is_d

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging


def download_from_youtube_to_webm(urls):
    import inspect
    import sys
    import traceback

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    while 1:
        urls = str(urls).strip()
        if urls is None:
            ensure_spoken_v2(str_working="다운로드할 대상 목록에 아무것도 입력되지 않았습니다", comma_delay=0.98)
            break
        if urls == "None":
            ensure_spoken_v2(str_working="다운로드할 대상 목록에 이상한 것이 입력되었습니다", comma_delay=0.98)
            break

        if "\n" in urls:
            urls = urls.split("\n")
        else:
            urls = [urls]

        urls = [x for x in urls if x.strip("\n")]  # 리스트 요소 "" remove,  from ["", A] to [A]       [""] to []
        GuiUtil.pop_up_as_complete(title="작업중간보고", ment=f"{len(urls)} 개의 url이 입력되었습니다",
                                   auto_click_positive_btn_after_seconds=1)

        try:
            urls.append(sys.argv[1])
        except IndexError:
            pass
        except Exception:
            logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
            pass

        # urls 중복remove(ordered way)
        urls_removed_duplicated_element: [str] = []
        for url in urls:
            if url not in urls_removed_duplicated_element:
                if url is not None:
                    # if url is not "None":
                    urls_removed_duplicated_element.append(url)
        urls = urls_removed_duplicated_element
        print_magenta(f'''urls : \n{urls}''')
        print_magenta(rf'''type(urls) : {type(urls)}''')
        print_magenta(rf'''len(urls) : {len(urls)}''')

        only_clip_id = ''
        for i in urls:
            logging.debug(i)
            only_clip_id = i

        if len(urls) == 0:
            GuiUtil.pop_up_as_complete(title="작업성공보고", ment=f"다운로드할 대상이 없습니다", auto_click_positive_btn_after_seconds=5)
            # TtsUtil.speak_ments(ment="다운로드할 대상이 없습니다", sleep_after_play=0.65)
            break

        if len(urls) != 1:
            ensure_spoken_v2(f"{str(len(urls))}개의 다운로드 대상이 확인되었습니다", comma_delay=0.98)
        for url in urls:
            url = url.strip()  # url에 공백이 있어도 다운로드 가능하도록 설정
            if '&list=' in url:
                logging.debug(f'clips mode')
                from pytube import Playlist
                playlist = Playlist(url)  # 이걸로도 parsing 기능 수행 생각 중
                logging.debug(f"predicted clips cnt : {len(playlist.video_urls)}")
                ensure_spoken_v2(str_working=f"{len(playlist.video_urls)}개의 다운로드 목록이 확인되었습니다", comma_delay=0.98)
                # os.system(f'echo "여기서부터 비디오 리스트 시작 {url}" >> success_yt_dlp.log')
                for video_id in playlist.video_urls:
                    try:
                        download_video_f(video_id)
                    except Exception:
                        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
                        continue
                # os.system(f'echo "여기서부터 비디오 리스트 종료 {url}" >> success_yt_dlp.log')
            else:
                if parse_youtube_video_id(url) is not None:
                    logging.debug(f'{UNDERLINE}youtube video id parsing mode')
                    try:
                        download_video_f(f'https://www.youtube.com/watch?v={parse_youtube_video_id(url)}')
                    except Exception:
                        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
                        continue
                else:
                    logging.debug(f'{UNDERLINE}experimental mode with clip id only')
                    download_video_mp4(f'https://www.youtube.com/watch?v={only_clip_id}')
                    try:
                        logging.debug(rf'''try:2024-04-12 18:04''')
                        url_parts_useless = [
                            "https://youtu.be/",
                            "https://www.youtube.com/shorts/",
                        ]
                        try:
                            for index, useless_str in enumerate(url_parts_useless):
                                if useless_str in url:
                                    print(rf'url.split(useless_str)[1] : {url.split(useless_str)[1]}')
                                    download_video_f(url=url.split(useless_str)[1])
                        except Exception:
                            download_video_f(url)
                            logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
                    except Exception:
                        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
                    continue
        break
