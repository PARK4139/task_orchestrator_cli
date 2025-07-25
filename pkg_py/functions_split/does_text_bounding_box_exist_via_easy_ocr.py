import zipfile
import winreg

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
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_state import pk_print_state

from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
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
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def does_text_bounding_box_exist_via_easy_ocr(string):  # GPU 없으면 동작안함

    text_coordinates = get_text_coordinates_via_easy_ocr(string=string)
    if not text_coordinates:
        print(rf"[not found] {string}")
        return 0
    x_abs, y_abs = text_coordinates
    pk_print(str_working=rf'''x_abs="{x_abs}"  {'%%%FOO%%%' if LTA else ''}''')
    pk_print(str_working=rf'''y_abs="{y_abs}"  {'%%%FOO%%%' if LTA else ''}''')
    move_mouse(x_abs=x_abs, y_abs=y_abs)
    return 1
