import zipfile
import yt_dlp
import winreg
# import win32gui
# import win32gui
import urllib
import tomllib
import timeit
import time
import threading
import tarfile
import sys
import subprocess, time
import string
import sqlite3
import socket
import shutil
import secrets
import re
import random
import pywintypes
# import pywin32
import pyglet
import pygetwindow
import pyaudio
import pandas as pd
import os.path
import nest_asyncio
import ipdb
import importlib
import hashlib
import easyocr
import datetime
import colorama
import colorama
import clipboard
import calendar
import browser_cookie3
from yt_dlp import YoutubeDL
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated

from PIL import Image
from pathlib import Path
from os.path import dirname
from os import path
from gtts import gTTS
from functools import partial as functools_partial
from functools import lru_cache
from enum import Enum
from datetime import timedelta
from cryptography.hazmat.primitives import padding
from colorama import init as pk_colorama_init
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_etc import PkFilter, PK_UNDERLINE
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def pk_debug_state_for_py_data_type_v2(pk_stamp, data_working, highlight_config_dict, with_LTA=1):
    import time
    if with_LTA == 1:
        if LTA == 1:
            if data_working:
                if isinstance(data_working, list):
                    for element in data_working:
                        # pk_print(f'''element={element} {'%%%FOO%%%' if LTA else ''}''')
                        pk_print(element, highlight_config_dict)
                elif isinstance(data_working, dict):
                    for key, value in data_working.items():
                        pk_print(f'{key}: {value}', highlight_config_dict)
                elif isinstance(data_working, str):
                    pk_print(f'{data_working}', highlight_config_dict)

            pk_time_limit = 30
            pk_time_s = time.time()
            while 1:
                elapsed = time.time() - pk_time_s
                if elapsed >= pk_time_limit:
                    pk_print(f'''time out (pk_time_limit={pk_time_limit}) {'%%%FOO%%%' if LTA else ''}''')
                    break
                user_input = pk_input_with_timeout(
                    working_str=rf'{STAMP_PK_DEBUGER_ENVIRONMENT} {pk_stamp} Press Enter to continue.',
                    timeout_secs=int(pk_time_limit - elapsed))
                if not user_input:
                    user_input = ""
                if user_input == "":
                    break
    elif with_LTA == 0:  # LTA=0 이더라도 출력은 그대로 쓸때
        if data_working:
            if isinstance(data_working, list):
                for element in data_working:
                    pk_print(element, highlight_config_dict)
            elif isinstance(data_working, dict):
                for key, value in data_working.items():
                    pk_print(f'{key}: {value}', highlight_config_dict)
            elif isinstance(data_working, str):
                pk_print(f'{data_working}', highlight_config_dict)
