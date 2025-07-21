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
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_100_performance_logic import pk_measure_seconds, pk_measure_memory
from pkg_py.pk_system_layer_100_os import is_os_windows

from pathlib import Path
from os.path import dirname
from mutagen.mp3 import MP3
from gtts import gTTS
from enum import Enum
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style

from pkg_py.simple_module.part_014_pk_print import pk_print


def pk_here(item_str=None):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    if item_str is None:
        item_str = ''
    pk_print(rf"{str(str(item_str) + ' ') * 242:.100} here!")
