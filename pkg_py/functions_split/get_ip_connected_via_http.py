

import zlib
# import win32process
import win32con
import webbrowser
import tomllib
import timeit
import tarfile
import requests
import pywintypes
import pygetwindow
import pyautogui
import paramiko
import mysql.connector
import math
import json
import hashlib
import chardet
import calendar
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_opened import is_window_opened

from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.print_red import print_red
from pkg_py.pk_system_object.Local_test_activate import LTA
from passlib.context import CryptContext
from os import path
from functools import lru_cache
from cryptography.hazmat.primitives import padding
from collections import Counter
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def get_ip_connected_via_http(url):
    import requests
    """Check if an IP is reachable via HTTP."""
    try:
        if not url.startswith(("http://", "https://")):
            url = f"http://{url}"  # Default to HTTP
        response = requests.get(url, timeout=2)
        return response.status_code == 200
    except requests.RequestException as e:
        pk_print(f"HTTP connection to {url} failed: {e}", print_color='red')
        return 0
