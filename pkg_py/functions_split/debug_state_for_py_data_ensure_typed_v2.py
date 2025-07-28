import zipfile
import yt_dlp
import winreg


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
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.map_massages import PkMessages2025
# from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.get_list_calculated import get_list_calculated

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
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def debug_state_for_py_data_ensure_typed_v2(pk_stamp, data_working, highlight_config_dict, with_LTA=1):
    import time
    if with_LTA == 1:
        if LTA == 1:
            if data_working:
                if isinstance(data_working, list):
                    for element in data_working:
                        # ensure_printed(f'''element={element} {'%%%FOO%%%' if LTA else ''}''')
                        ensure_printed(element, highlight_config_dict)
                elif isinstance(data_working, dict):
                    for key, value in data_working.items():
                        ensure_printed(f'{key}: {value}', highlight_config_dict)
                elif isinstance(data_working, str):
                    ensure_printed(f'{data_working}', highlight_config_dict)

            pk_time_limit = 30
            pk_time_s = time.time()
            while 1:
                elapsed = time.time() - pk_time_s
                if elapsed >= pk_time_limit:
                    ensure_printed(f'''time out (pk_time_limit={pk_time_limit}) {'%%%FOO%%%' if LTA else ''}''')
                    break
                user_input = input_with_timeout(
                    str_working=rf'{STAMP_PK_DEBUGER_ENVIRONMENT} {pk_stamp} Press Enter to continue.',
                    timeout_secs=int(pk_time_limit - elapsed))
                if not user_input:
                    user_input = ""
                if user_input == "":
                    break
    elif with_LTA == 0:  # LTA=0 이더라도 출력은 그대로 쓸때
        if data_working:
            if isinstance(data_working, list):
                for element in data_working:
                    ensure_printed(element, highlight_config_dict)
            elif isinstance(data_working, dict):
                for key, value in data_working.items():
                    ensure_printed(f'{key}: {value}', highlight_config_dict)
            elif isinstance(data_working, str):
                ensure_printed(f'{data_working}', highlight_config_dict)
