import zlib
import zipfile
# import win32process
import webbrowser
import urllib.parse
import toml
import threading
import tarfile
import subprocess
import string
import socket
import shutil
import shlex
import secrets
import pyglet
import pyaudio
import psutil
import platform
import pickle
import os.path
import math
import json
import ipdb
import easyocr
import datetime
import colorama
import browser_cookie3
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from prompt_toolkit.styles import Style
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_directories import D_PKG_TXT
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_os import is_os_windows
from PIL import Image, ImageFilter
from passlib.context import CryptContext
from os.path import dirname
from os import path
from functools import lru_cache
from datetime import timedelta
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import BeautifulSoup
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def make_pnx_interested_list_to_f_txt_x(d_working_list, exclusion_list):
    import inspect

    # todo : chore : f 내용 초기화
    func_n = inspect.currentframe().f_code.co_name
    pnx_processed_list = []
    file_cnt = 0
    write_cnt = 0
    write_cnt_limit = 1000000
    for pnx_interested in d_working_list:
        pnxs_with_walking = get_pnx_list(d_working=pnx_interested, mode="f", with_walking=1)

        # 'pnxs_exclude'를 set으로 변경하여 'in' 연산을 최적화
        func_n_file_cnt_txt = None
        for pnx_with_walking in pnxs_with_walking:
            # 빠른 'in' 연산을 위해 set으로 변환된 pnxs_exclude 활용
            if any(pnx_exclude in pnx_with_walking for pnx_exclude in exclusion_list):
                continue  # 'pnx_exclude'에 포함되면 건너뛰기
            # 'exclude' 목록에 포함되지 않으면 'pnx_processed_list'에 추가
            pnx_processed_list.append(pnx_with_walking)
            # pk_print(str_working=rf'''len(pnx_processed_list)="{len(pnx_processed_list)}"  {'%%%FOO%%%' if LTA else ''}''')
            if write_cnt == write_cnt_limit % 2 == 0:
                file_cnt = file_cnt + 1
                # print_iterable_as_vertical(item_iterable=pnx_processed_list, item_iterable_n="pnx_processed_list")
                # func_n_file_cnt_txt=rf"{D_PKG_TXT}\{func_n}_{file_cnt}.txt"
                # write_list_to_file(texts=pnx_processed_list, pnx=func_n_file_cnt_txt, mode="w")
            func_n_file_cnt_txt = rf"{D_PKG_TXT}\{func_n}_{file_cnt}.txt"
            # pk_print(str_working=rf'''write_cnt="{write_cnt}"  {'%%%FOO%%%' if LTA else ''}''')
            write_str_to_f(msg=f"{pnx_with_walking}\n", f=func_n_file_cnt_txt, mode="a")
            write_cnt = write_cnt + 1
            if write_cnt == write_cnt_limit % 2 == 0:
                window_title = rf"{func_n}_{file_cnt}"
                # if not is_window_open(window_title_seg=window_title):
                #     open_pnx(pnx=func_n_file_cnt_txt)
