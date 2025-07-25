
def pk_here(item_str=None):
from enum import Enum
from gtts import gTTS
from mutagen.mp3 import MP3
from os.path import dirname
from pathlib import Path
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.print import pk_print
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.performance_logic import pk_measure_seconds, pk_measure_memory
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from prompt_toolkit.styles import Style
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse
func_n = inspect.currentframe().f_code.co_name
if item_str is None:
import inspect
import numpy as np
import pyautogui
import toml
import traceback
import undetected_chromedriver as uc
import webbrowser
import win32com.client
import zlib
item_str = ''
pk_print(rf"{str(str(item_str) + ' ') * 242:.100} here!")
