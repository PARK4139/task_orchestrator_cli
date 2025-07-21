

# import win32process
import win32con
import uuid
import tqdm
import tomllib
import time
import tarfile
import string
import shlex
import random
# import pywin32
# import pywin32
import pyautogui
import psutil
import pickle
import os.path
import nest_asyncio
import keyboard
import inspect
import easyocr
import cv2
import colorama
import clipboard
import chardet
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB

from passlib.context import CryptContext
from os import path
from moviepy import VideoFileClip
from functools import lru_cache
from dirsync import sync
from datetime import datetime, timedelta
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from collections import Counter
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from pkg_py.pk_system_layer_etc import PkFilter, PK_UNDERLINE
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_014_pk_print import pk_print


def get_list_duplicated(working_list):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    items_duplicated = []
    seen = set()  # 이미 본 요소를 추적할 집합
    for item in working_list:
        if item in seen and item not in items_duplicated:
            items_duplicated.append(item)
        else:
            seen.add(item)
    return items_duplicated
