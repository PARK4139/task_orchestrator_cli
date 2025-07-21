import zipfile
import yt_dlp
# import win32process
# import win32gui
import urllib
import traceback
import tomllib
import toml
import toml
import tarfile
import shlex
import pythoncom
import pygetwindow
import pyaudio
import platform
import pickle
import paramiko
import pandas as pd
import numpy as np
import json
import clipboard
from yt_dlp import YoutubeDL
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_os import is_os_windows

from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from datetime import datetime, timedelta
from datetime import datetime, time
from datetime import date
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def download_youtube_list(via_f_txt=None, video_url_list=None):
    import inspect
    from urllib.parse import quote

    func_n = inspect.currentframe().f_code.co_name
    f_func_n_txt = rf'{D_PROJECT}\pkg_txt\{func_n}.txt'
    ensure_pnx_made(pnx=f_func_n_txt, mode="f")

    if via_f_txt is None and video_url_list is None:
        pk_print(rf"{func_n}() 동작 조건 불충족")
        return

    if via_f_txt is True and video_url_list is None:
        if not is_window_opened(window_title_seg=func_n):
            cmd_to_os(cmd=rf"explorer {f_func_n_txt}")
        video_url_list = get_list_from_f(f=f_func_n_txt)
        video_url_list = get_list_removed_element_contain_prompt(working_list=video_url_list, prompt="#")

    elif via_f_txt is None and video_url_list is None:
        video_url_list = get_list_via_user_input(ment=rf"다운로드할 유튜브 리스트를 \n 단위로 입력하세요", func_n=func_n)

    elif video_url_list is not None:
        video_url_list = video_url_list
    else:
        pk_print(f'''  {'%%%FOO%%%' if LTA else ''} ''', print_color='red')
        return

    video_url_list = get_list_removed_by_removing_runtine(working_list=video_url_list)
    print_iterable_as_vertical(item_iterable=video_url_list, item_iterable_n="urls")
    pk_print(rf'''len(urls)="{len(video_url_list)}"''')
    if len(video_url_list) == 0:
        return
    string_playlist_positive = 'list='
    for url in video_url_list:
        if string_playlist_positive in url:
            encoded_url = quote(url, safe=':/?&=')
            from pytube import Playlist
            playlist = Playlist(encoded_url)
            pk_print(working_str=rf'''playlist="{playlist}"  {'%%%FOO%%%' if LTA else ''}''')
            pk_print(working_str=rf'''playlist.title="{playlist.title}"  {'%%%FOO%%%' if LTA else ''}''')
            pk_print(
                working_str=rf'''len(playlist.video_urls)="{len(playlist.video_urls)}"  {'%%%FOO%%%' if LTA else ''}''')
            for index, video in enumerate(playlist.videos, start=1):
                pk_print(working_str=rf'''video.watch_url="{video.watch_url}"  {'%%%FOO%%%' if LTA else ''}''')
                download_youtube_videos(urls=[video.watch_url])
        else:
            download_youtube_videos(urls=[url])
