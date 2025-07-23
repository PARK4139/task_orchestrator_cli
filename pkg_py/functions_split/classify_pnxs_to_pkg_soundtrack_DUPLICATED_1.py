import winreg
import win32com.client
import undetected_chromedriver as uc
import traceback
import tomllib
import toml
import toml
import timeit
import sys
import subprocess
import shlex
import re
# import pywin32
# import pywin32
import pyaudio
import os, inspect
import os
import math
import functools
import cv2
import asyncio
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.directories import D_WORKING
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pkg_py.pk_system_object.is_os_windows import is_os_windows

from PIL import Image, ImageFont, ImageDraw, ImageFilter
from PIL import Image
from os import path
from dirsync import sync
from datetime import datetime, time
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import ResultSet
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def classify_pnxs_to_pkg_soundtrack(pnx, without_walking=True):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    # 유효d 확인
    if is_f(pnx=pnx):
        pk_print(f"{pnx} 는 정리할 수 있는 d가 아닙니다")
        return

    # f과 d get
    txt_to_exclude_list = [
        F_DB_YAML,
        F_SUCCESS_LOG,
        F_LOCAL_PKG_CACHE,
    ]
    if without_walking == False:
        d_list, f_list = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list)
    else:
        d_list, f_list = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list, without_walking=0)

    # f 처리
    x_allowed = [".mp3", '.flac', '.wav']
    x_allowed = x_allowed + get_list_replaced_element_from_str_to_upper_case(working_list=x_allowed)
    pnx = get_pn(pnx)
    dst = rf"{pnx}\pkg_soundtrack"
    for f in f_list:
        f = f[0]
        file_p = get_p(f)
        file_x = get_x(f).replace(".", "")  # 확장자에서 점(.) remove
        if file_x in [ext.replace(".", "") for ext in x_allowed]:  # x_allowed의 확장자와 비교
            ensure_pnx_made(dst, mode="d")
            move_pnx(pnx=f, d_dst=dst)
            pk_print(working_str=rf'''f="{f}"  {'%%%FOO%%%' if LTA else ''}''')
    pk_print(working_str=rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''')
