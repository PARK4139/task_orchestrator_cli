import zlib
import win32com.client
import webbrowser
import undetected_chromedriver as uc
import traceback
import toml
import pyautogui
import numpy as np
from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from prompt_toolkit.styles import Style
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.performance_logic import pk_measure_seconds, pk_measure_memory
from pkg_py.pk_system_object.is_os_windows import is_os_windows

from pathlib import Path
from os.path import dirname
from mutagen.mp3 import MP3
from gtts import gTTS
from enum import Enum
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.pk_print import pk_print


def pk_here(item_str=None):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    if item_str is None:
        item_str = ''
    pk_print(rf"{str(str(item_str) + ' ') * 242:.100} here!")
