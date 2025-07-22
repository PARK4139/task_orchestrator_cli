import zlib
import yt_dlp
import win32con
import win32com.client
import uuid
import tomllib
import toml
import threading
import tarfile
import sys
import sqlite3
import secrets
import random
# import pywin32
import pyautogui
import platform
import paramiko
import numpy as np
import json
import inspect
import importlib
import hashlib
import easyocr
import colorama
import chardet
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.functions_split.pk_print_state import pk_print_state

from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_object.print_red import print_red
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from mutagen.mp3 import MP3
from gtts import gTTS
from dirsync import sync
from datetime import datetime, time
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def get_pid_by_window_title(window_title_seg):  # 테스트필요
    import psutil

    import inspect
    import pygetwindow
    func_n = inspect.currentframe().f_code.co_name
    # window_titles=pygetwindow.getAllTitles()
    window_titles = get_window_title_list()
    matching_window = [w for w in window_titles if window_title_seg.lower() in w.lower()]

    if not matching_window:
        return f"No window found with title containing: '{window_title_seg}'"

    # Assuming the first match
    window_title_match = matching_window[0]
    print(f"Found window: {window_title_match}")

    for process in psutil.process_iter(['pid', 'name']):
        try:
            process_name = process.info['name']
            process_id = process.info['pid']
            process_window_titles = pygetwindow.getWindowsWithTitle(window_title_match)

            pk_print(f'process_name="{process_name}"  {'%%%FOO%%%' if LTA else ''}')
            pk_print(f'process_id="{process_id}"  {'%%%FOO%%%' if LTA else ''}')
            pk_print(f'process_window_titles="{process_window_titles}"  {'%%%FOO%%%' if LTA else ''}')

            if process_window_titles:
                return process_id
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:

            pk_print(f"Error processing {process.info['pid']}: {e}")
            continue
    return f"No PID found for window title: '{window_title_match}'"
