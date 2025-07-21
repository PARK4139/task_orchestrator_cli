import zipfile
import yt_dlp
# import win32process
# import win32gui
import win32con
import win32com.client
import webbrowser
import urllib
import undetected_chromedriver as uc
import tqdm
import toml
import shlex
import secrets
import pyaudio
import platform
import paramiko
import pandas as pd
import nest_asyncio
import easyocr
import datetime
import browser_cookie3
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from os.path import dirname
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from datetime import datetime
from cryptography.hazmat.primitives import padding
from base64 import b64decode
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def get_str_url_decoded(str_working):
    import urllib
    from urllib.parse import quote
    return urllib.parse.unquote(str_working)
