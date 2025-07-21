import zipfile
import winreg
import win32con
import uuid
import tomllib
import toml
import threading
import subprocess
import socket
import random
# import pywin32
import pyautogui
import nest_asyncio
import ipdb
import inspect
import hashlib
import cv2
import colorama
import chardet
import browser_cookie3
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from tkinter import UNDERLINE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from pytube import Playlist
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated

from moviepy import VideoFileClip
from functools import partial
from fastapi import HTTPException
from datetime import datetime
from collections import Counter
from base64 import b64encode
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def get_random_korean(length_limit: int):
    import random
    import string

    result = ''
    for _ in range(length_limit):
        result += random.choice(string.printable)
    return result
