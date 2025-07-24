import zlib
import zipfile
import yt_dlp
import winreg
# import win32gui
import win32com.client
import uuid
import tqdm
import toml
import toml
import timeit
import time
import threading
import tarfile
import speech_recognition as sr
# import pywin32
import pythoncom
import pygetwindow
import platform
import pickle
import os.path
import nest_asyncio
import mysql.connector
import mutagen
import keyboard
import easyocr
import asyncio
from zipfile import BadZipFile
from urllib.parse import unquote, urlparse, parse_qs
from telegram import Bot, Update
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image
from passlib.context import CryptContext
from os import path
from moviepy import VideoFileClip
from functools import partial as functools_partial
from fastapi import HTTPException
from enum import Enum
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from bs4 import ResultSet
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def pk_input_v1(str_working, limit_seconds, return_default, get_input_validated=None):
    import sys
    import threading
    import time
    from queue import Queue, Empty

    pk_print(f'''str_working={str_working} {'%%%FOO%%%' if LTA else ''}''')
    pk_print(f'''limit_seconds={limit_seconds} {'%%%FOO%%%' if LTA else ''}''')
    pk_print(f'''return_default={return_default} {'%%%FOO%%%' if LTA else ''}''')
    pk_print(f'''get_input_validated={get_input_validated} {'%%%FOO%%%' if LTA else ''}''')
    input_queue = Queue()

    def read_input():
        try:
            user_input = sys.stdin.readline()
            input_queue.put(user_input.strip())
        except Exception as e:
            input_queue.put(None)

    input_thread = threading.Thread(target=read_input, daemon=True)
    input_thread.start()

    start_time = time.time()
    remaining = limit_seconds

    try:
        while remaining > 0:
            user_input = ""
            try:
                user_input = input_queue.get(timeout=1)
                print()  # 줄 바꿈
                if get_input_validated and not get_input_validated(user_input):
                    pk_print("[RETRY] 유효하지 않은 입력입니다. 다시 시도해주세요.", print_color='red')
                    return pk_input(str_working, limit_seconds, return_default, get_input_validated)
                return user_input
            except Empty:
                remaining = limit_seconds - int(time.time() - start_time)
                print(f"\r⏳ remaining seconds : {remaining:2d} {str_working}{user_input}", end="", flush=True)
        print()  # 줄 바꿈 (시간 초과 시)
        pk_print(f"[TIMEOUT] 입력 시간 초과 → 기본값 반환: {return_default}", print_color='red')
        return return_default

    except KeyboardInterrupt:
        print()  # 줄 바꿈
        pk_print("[INTERRUPT] 사용자 입력 취소됨 → 기본값 반환", print_color='red')
        return return_default
