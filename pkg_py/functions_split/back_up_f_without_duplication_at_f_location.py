import zipfile
# import win32gui
# import win32gui
import win32con
import win32com.client
import uuid
import undetected_chromedriver as uc
import traceback
import tqdm
import tomllib
import time
import threading
import subprocess
import speech_recognition as sr
import re
import pywintypes
import pyglet
import pyautogui
import pyaudio
import psutil
import os
import mutagen
import keyboard
import ipdb
import colorama
import colorama
import clipboard
import calendar
import browser_cookie3
from zipfile import BadZipFile
from urllib.parse import urlparse
from telegram import Bot
from seleniumbase import Driver
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.state_via_database import PkSqlite3DB

from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial
from functools import lru_cache
from datetime import datetime, timedelta
from datetime import datetime
from bs4 import ResultSet
from base64 import b64decode
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def back_up_f_without_duplication_at_f_location(f: str) -> str:
    import os
    import shutil
    import re

    if not os.path.isfile(f):
        pk_print(f"[ERROR][BACKUP] File not found: {f}", print_color='red')
        raise FileNotFoundError(f"File not found: {f}")
    base_p, f_nx = os.path.split(f)
    f_n, f_x = os.path.splitext(f_nx)
    pattern = re.compile(rf"^{re.escape(f_n)} \((\d+)\)\.bak$")
    existing_nums = []
    try:
        for name in os.listdir(base_p):
            m = pattern.fullmatch(name)
            if m:
                existing_nums.append(int(m.group(1)))
    except Exception as e:
        pk_print(f"[WARN] Failed to scan directory: {e}", print_color='red')
    try:
        next_num = max(existing_nums, default=0) + 1
        candidate = os.path.join(base_p, f"{f_n} ({next_num}).bak")
        shutil.copy2(f, candidate)
        pk_print(f"[BACKUP] {candidate}", print_color='green')
        return candidate
    except Exception as e:
        pk_print(f"[ERROR][BACKUP] Failed to create backup: {e}", print_color='red')
        raise
