import zipfile
import winreg
# import win32gui
import win32con
import win32com.client
import undetected_chromedriver as uc
import toml
import string
import secrets
import requests
import re
import pythoncom
import pyautogui
import psutil
import os.path
import mutagen
import hashlib
import datetime
import colorama
import clipboard
import chardet
import asyncio
from zipfile import BadZipFile
from tkinter import UNDERLINE
from pynput import mouse
from prompt_toolkit.styles import Style
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_800_print_util import print_red
from passlib.context import CryptContext
from os import path
from functools import partial as functools_partial
from functools import lru_cache
from fastapi import HTTPException
from datetime import datetime, timedelta
from datetime import datetime
from colorama import init as pk_colorama_init
from collections import Counter
from base64 import b64decode
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def does_text_bounding_box_exist_via_easy_ocr(string):  # GPU 없으면 동작안함

    text_coordinates = get_text_coordinates_via_easy_ocr(string=string)
    if not text_coordinates:
        print(rf"[not found] {string}")
        return 0
    x_abs, y_abs = text_coordinates
    pk_print(working_str=rf'''x_abs="{x_abs}"  {'%%%FOO%%%' if LTA else ''}''')
    pk_print(working_str=rf'''y_abs="{y_abs}"  {'%%%FOO%%%' if LTA else ''}''')
    move_mouse(x_abs=x_abs, y_abs=y_abs)
    return 1
