import zipfile
import winreg

import undetected_chromedriver as uc
import traceback
import tomllib
import tomllib
import socket
import pyaudio
import mysql.connector
import asyncio
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.directories  import D_PROJECT
from pkg_py.system_object.get_list_calculated import get_list_calculated
from os.path import dirname
from moviepy import VideoFileClip
from functools import partial
from functools import lru_cache
from enum import Enum
from colorama import init as pk_colorama_init
from collections import Counter
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs


def get_f_video_of_d_working(d_working, ext_list_allowed):
    import os
    ensure_printed(f'''d_working={d_working} extension_list_allowed={ext_list_allowed} {'%%%FOO%%%' if LTA else ''}''')
    if not os.path.exists(d_working):
        ensure_printed(f"d_working does not exists {d_working}")
    if os.path.exists(d_working):
        for f_nx in os.listdir(d_working):
            f = os.path.join(d_working, f_nx)
            ext = os.path.splitext(f)[1].lower()
            if not ext in ext_list_allowed:
                # ensure_printed(f"f={f}, ext={ext}, 조건 만족 여부: {ext in extensions}")
                pass
    f_list_of_d_working = [os.path.join(d_working, f) for f in os.listdir(d_working)]
    ensure_printed(f'''len(f_list_of_d_working)={len(f_list_of_d_working)}  {'%%%FOO%%%' if LTA else ''}''')
    f_videos_allowed = [
        f for f in f_list_of_d_working
        if os.path.splitext(f)[1].lower() in ext_list_allowed
           and not any(keyword in os.path.basename(f).lower() for keyword in ["seg", "temp"])
    ]
    ensure_printed(f'''len(f_videos_allowed)={len(f_videos_allowed)}  {'%%%FOO%%%' if LTA else ''}''')
    if f_videos_allowed:
        f_videos_allowed.sort()
        return f_videos_allowed[0]
    else:
        ensure_printed("조건에 맞는 f 없습니다.", print_color='red')
        return None
