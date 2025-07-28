import zipfile
import yt_dlp

import win32com.client
import urllib.parse
import traceback
import tqdm
import tomllib
import toml
import toml
import time
import threading
import tarfile
import subprocess, time
import speech_recognition as sr
import pywintypes
import pygetwindow
import pyautogui
import paramiko
import pandas as pd
import os.path
import os
import numpy as np
import nest_asyncio
import mysql.connector
import importlib
import easyocr
import colorama
import chardet

from zipfile import BadZipFile
from urllib.parse import urlparse
from telegram import Bot, Update
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.performance_logic import ensure_seconds_measured, pk_measure_memory
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.get_list_calculated import get_list_calculated

from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial
from functools import lru_cache
from datetime import timedelta
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.get_d_working import get_d_working


def add_data_to_f_toml(f_toml, data_new):
    from enum import Enum
    encoding: Enum

    import toml
    # TOML f 읽기
    with open(file=f_toml, mode="r", encoding=Encoding.UTF8.value) as f:
        toml_data = toml.load(f)

    # 새로운 데이터 추가
    for key, value in data_new.items():
        if key in toml_data:
            # 기존 데이터와 병합
            toml_data[key].update(value)
        else:
            # 새로운 키 추가
            toml_data[key] = value

    # TOML f 다시 저장
    with open(file=f_toml, mode="w", encoding=Encoding.UTF8.value) as f:
        toml.dump(toml_data, f)
