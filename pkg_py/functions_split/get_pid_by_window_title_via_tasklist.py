import zlib
# import win32process
import win32con
import undetected_chromedriver as uc
import timeit
import socket
import re
import random
import pywintypes
import pyautogui
import pyaudio
import platform
import numpy as np
import nest_asyncio
import hashlib
import easyocr
import cv2
import colorama
import colorama
import clipboard
import browser_cookie3
from urllib.parse import urlparse
from telegram import Bot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.write_list_to_f import write_list_to_f

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.directories import D_WORKING
from pkg_py.pk_system_object.map_massages import PkMessages2025
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated

from os.path import dirname
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from gtts import gTTS
from enum import Enum
from datetime import timedelta
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.pk_system_object.local_test_activate import LTA

from pkg_py.functions_split.get_pnx_list import get_pnx_list


def get_pid_by_window_title_via_tasklist(window_title_seg):
    try:
        cmd = rf'tasklist'
        lines = cmd_to_os(cmd=cmd)
        matching_lines = None
        for line in lines:
            if window_title_seg in line:
                matching_lines = line

        pids = []
        parts = matching_lines.split()
        if len(parts) > 1 and window_title_seg in parts[0]:
            pids.append(parts[1])

        if len(pids) == 1:
            return pids[0]
        else:
            return pids
    except Exception as e:
        return str(e)
