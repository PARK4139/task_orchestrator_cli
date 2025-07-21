import winreg
# import win32gui
import win32con
import tomllib
import tomllib
import toml
import speech_recognition as sr
import shutil
import pywintypes
import pyglet
import pygetwindow
import os, inspect
import functools
import colorama
from yt_dlp import YoutubeDL
from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from queue import Queue, Empty
from pytube import Playlist
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from mutagen.mp3 import MP3
from enum import Enum
from datetime import timedelta
from Cryptodome.Random import get_random_bytes
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA


def make_project_tree_for_pk_system():
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    leaf_d_list = [
        D_PKG_DPL
    ]
    for item in leaf_d_list:
        ensure_pnx_made(pnx=item, mode="d")
    leaf_files = [
        # ...
    ]
    for item in leaf_files:
        ensure_pnx_made(pnx=item, mode="f")
