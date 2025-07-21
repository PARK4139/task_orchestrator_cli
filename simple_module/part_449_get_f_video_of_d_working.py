import zipfile
import winreg
# import win32gui
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
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated
from os.path import dirname
from moviepy import VideoFileClip
from functools import partial
from functools import lru_cache
from enum import Enum
from colorama import init as pk_colorama_init
from collections import Counter
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def get_f_video_of_d_working(d_working, ext_list_allowed):
    import os
    pk_print(f'''d_working={d_working} extension_list_allowed={ext_list_allowed} {'%%%FOO%%%' if LTA else ''}''')
    if not os.path.exists(d_working):
        pk_print(f"d_working does not exists {d_working}")
    if os.path.exists(d_working):
        for f_nx in os.listdir(d_working):
            f = os.path.join(d_working, f_nx)
            ext = os.path.splitext(f)[1].lower()
            if not ext in ext_list_allowed:
                # pk_print(f"f={f}, ext={ext}, 조건 만족 여부: {ext in extensions}")
                pass
    f_list_of_d_working = [os.path.join(d_working, f) for f in os.listdir(d_working)]
    pk_print(f'''len(f_list_of_d_working)={len(f_list_of_d_working)}  {'%%%FOO%%%' if LTA else ''}''')
    f_video_list_allowed = [
        f for f in f_list_of_d_working
        if os.path.splitext(f)[1].lower() in ext_list_allowed
           and not any(keyword in os.path.basename(f).lower() for keyword in ["seg", "temp"])
    ]
    pk_print(f'''len(f_video_list_allowed)={len(f_video_list_allowed)}  {'%%%FOO%%%' if LTA else ''}''')
    if f_video_list_allowed:
        f_video_list_allowed.sort()
        return f_video_list_allowed[0]
    else:
        pk_print("조건에 맞는 f 없습니다.", print_color='red')
        return None
