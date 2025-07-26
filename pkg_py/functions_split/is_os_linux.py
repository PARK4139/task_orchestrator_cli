

import webbrowser
import traceback
import tomllib
import toml
import subprocess

import pyautogui
import pandas as pd
import numpy as np
import importlib
import functools

from urllib.parse import urlparse
from urllib.parse import quote, urlparse
from selenium.webdriver.common.keys import Keys
from queue import Queue, Empty
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.state_via_database import PkSqlite3DB
from moviepy import VideoFileClip
from functools import partial as functools_partial
from dirsync import sync
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows


def is_os_linux():
    #
    # todo 명시적으로 업데이트 필요
    if is_os_wsl_linux():
        return True
    if not is_os_windows():
        return True
