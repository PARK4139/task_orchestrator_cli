import zlib
import yt_dlp

import win32con
import tomllib
import toml
import threading
import subprocess
import shutil

import pyautogui
import importlib
import hashlib
import functools
import datetime
import colorama
import colorama
import clipboard
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from tkinter import UNDERLINE
from telegram import Bot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once

from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.encodings import Encoding
# from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.performance_logic import ensure_seconds_measured, pk_measure_memory

from PIL import Image, ImageFilter
from functools import partial as functools_partial
from functools import lru_cache
from enum import Enum
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def fix_f_n_weired(working_d, f_nx_from='init_.py', f_nx_to='__init__.py'):
    import os
    """
    주어진 디렉터리 내의 모든 'init_.py' f을 '__init__.py'로 이름 변경합니다.
    """
    for root, d_nx_list, f_nx_list in os.walk(working_d):
        for f_nx in f_nx_list:
            if f_nx == f_nx_from:
                old_f = os.path.join(root, f_nx)
                new_f = os.path.join(root, f_nx_to)
                try:
                    os.rename(old_f, new_f)
                    print(f"Renamed: {old_f} ->> {new_f}")
                except Exception as e:
                    print(f"Error renaming {old_f}: {e}")
