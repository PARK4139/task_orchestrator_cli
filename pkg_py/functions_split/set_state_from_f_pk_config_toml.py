import zlib
import yt_dlp

import win32con
import uuid
import urllib.parse
import urllib
import undetected_chromedriver as uc
import toml
import threading
import tarfile
import sys
import subprocess, time
import string


import pythoncom
import pygetwindow
import pyautogui
import pyaudio
import pandas as pd
import os
import nest_asyncio
import mysql.connector
import mutagen
import math
import keyboard
import easyocr
import clipboard
from zipfile import BadZipFile
from urllib.parse import urlparse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.ensure_state_printed import ensure_state_printed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.get_list_calculated import get_list_calculated

from passlib.context import CryptContext
from functools import partial
from enum import Enum
from cryptography.hazmat.primitives import padding
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs


def set_state_from_f_pk_config_toml(pk_state_address, pk_state_value):
    pk_toml_address_list = pk_state_address.split('/')
    if LTA:
        ensure_printed(f'''pk_state_address={pk_state_address} {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''pk_state_value={pk_state_value} {'%%%FOO%%%' if LTA else ''}''')
    level_1_dict_n = ""
    level_2_dict_n = ""
    level_3_dict_n = ""
    try:
        level_1_dict_n = pk_toml_address_list[0]
        level_2_dict_n = pk_toml_address_list[1]
        level_3_dict_n = pk_toml_address_list[2]
    except:
        if LTA:
            ensure_printed(f'''{len(pk_toml_address_list)} is idx limit. in setter {'%%%FOO%%%' if LTA else ''}''')

    level_1_dict = {}
    level_2_dict = {}
    level_3_dict = {}
    try:
        level_1_dict = toml.load(F_PK_CONFIG_TOML)[level_1_dict_n]
    except KeyError:
        ensure_printed(f'''level_1_dict={level_1_dict}에 해당하는 key 가 없어 생성합니다. {'%%%FOO%%%' if LTA else ''}''')
        level_1_dict = toml.load(F_PK_CONFIG_TOML)[level_1_dict]
        with open(F_PK_CONFIG_TOML, "w") as f:
            toml.dump(level_1_dict, f)
    try:
        level_2_dict = level_1_dict[level_2_dict_n]
    except KeyError:
        ensure_printed(f'''level_2_dict_n={level_2_dict_n}에 해당하는 key 가 없어 생성합니다. {'%%%FOO%%%' if LTA else ''}''')
        level_1_dict[level_2_dict_n] = pk_state_value
        with open(F_PK_CONFIG_TOML, "w") as f:
            toml.dump(level_1_dict, f)
    if len(pk_toml_address_list) == 2:
        level_1_dict[level_2_dict_n] = pk_state_value
        with open(F_PK_CONFIG_TOML, "w") as f:
            toml.dump(level_1_dict, f)
    try:
        level_3_dict = level_2_dict[level_3_dict_n]
    except KeyError:
        ensure_printed(f'''level_3_dict_n={level_3_dict_n}에 해당하는 key 가 없어 생성합니다. {'%%%FOO%%%' if LTA else ''}''')
        level_2_dict[level_3_dict_n] = pk_state_value
        with open(F_PK_CONFIG_TOML, "w") as f:
            toml.dump(level_2_dict, f)
    if len(pk_toml_address_list) == 3:
        level_2_dict[level_3_dict_n] = pk_state_value
        with open(F_PK_CONFIG_TOML, "w") as f:
            toml.dump(level_2_dict, f)
