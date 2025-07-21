import zlib
import win32con
import undetected_chromedriver as uc
import tomllib
import threading
import sys
import sqlite3
import pyautogui
import functools
import calendar
import browser_cookie3
from selenium.webdriver.chrome.options import Options
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated
from PIL import Image
from os import path
from dirsync import sync
from cryptography.hazmat.primitives import padding
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from base64 import b64encode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def parse_youtube_video_id(url):
    import inspect
    import urllib
    from urllib.parse import quote

    func_n = inspect.currentframe().f_code.co_name
    keyword_shorts = '/shorts/'
    keyword_slash = '/'
    if keyword_shorts in url:
        youtube_video_id = url.split(keyword_shorts)[1]
        youtube_video_id = youtube_video_id.split(keyword_slash)[0]
        pk_print(working_str=rf'''youtube_video_id="{youtube_video_id}"  {'%%%FOO%%%' if LTA else ''}''')
        return youtube_video_id
    query = urllib.parse.urlparse(url=url)
    # pk_print(query.scheme)
    # pk_print(query.netloc)
    # pk_print(query.hostname)
    # pk_print(query.port)
    # pk_print(query._replace(fragment="").geturl())
    # pk_print(query)
    # pk_print(query["v"][0])
    if query.hostname == 'youtu.be':
        pk_print(working_str=rf'''query.path[1:]="{query.path[1:]}"  {'%%%FOO%%%' if LTA else ''}''')
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = urllib.parse.parse_qs(query.query)
            pk_print(working_str=rf'''p['v'][0]="{p['v'][0]}"  {'%%%FOO%%%' if LTA else ''}''')
            return p['v'][0]
        if query.path[:7] == '/embed/':
            pk_print(
                working_str=rf'''query.path.split('/')[2]="{query.path.split('/')[2]}"  {'%%%FOO%%%' if LTA else ''}''')
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            pk_print(
                working_str=rf'''query.path.split('/')[2]="{query.path.split('/')[2]}"  {'%%%FOO%%%' if LTA else ''}''')
            return query.path.split('/')[2]
