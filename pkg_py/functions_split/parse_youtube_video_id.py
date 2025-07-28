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

from selenium.webdriver.chrome.options import Options
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image
from os import path
from dirsync import sync
from cryptography.hazmat.primitives import padding
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.is_d import is_d
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


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
        ensure_printed(str_working=rf'''youtube_video_id="{youtube_video_id}"  {'%%%FOO%%%' if LTA else ''}''')
        return youtube_video_id
    query = urllib.parse.urlparse(url=url)
    # ensure_printed(query.scheme)
    # ensure_printed(query.netloc)
    # ensure_printed(query.hostname)
    # ensure_printed(query.port)
    # ensure_printed(query._replace(fragment="").geturl())
    # ensure_printed(query)
    # ensure_printed(query["v"][0])
    if query.hostname == 'youtu.be':
        ensure_printed(str_working=rf'''query.path[1:]="{query.path[1:]}"  {'%%%FOO%%%' if LTA else ''}''')
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = urllib.parse.parse_qs(query.query)
            ensure_printed(str_working=rf'''p['v'][0]="{p['v'][0]}"  {'%%%FOO%%%' if LTA else ''}''')
            return p['v'][0]
        if query.path[:7] == '/embed/':
            ensure_printed(
                str_working=rf'''query.path.split('/')[2]="{query.path.split('/')[2]}"  {'%%%FOO%%%' if LTA else ''}''')
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            ensure_printed(
                str_working=rf'''query.path.split('/')[2]="{query.path.split('/')[2]}"  {'%%%FOO%%%' if LTA else ''}''')
            return query.path.split('/')[2]
