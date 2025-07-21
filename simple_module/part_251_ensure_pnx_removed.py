import zipfile
# import win32gui
import undetected_chromedriver as uc
import tqdm
import tomllib
import timeit
import time
import subprocess
import string
import speech_recognition as sr
import socket, time
import socket
import re
import random, math
# import pywin32
# import pywin32
import pyglet
import pyaudio
import os.path
import math
import json
import inspect
import importlib
import hashlib
import easyocr
import colorama
import clipboard
import chardet
import calendar
import browser_cookie3
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote, urlparse
from urllib.parse import quote
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated

from mysql.connector import connect, Error
from mutagen.mp3 import MP3
from gtts import gTTS
from fastapi import HTTPException
from dirsync import sync
from datetime import datetime, timedelta
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from collections import Counter
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def ensure_pnx_removed(pnx):
    import os
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    if not does_pnx_exist(pnx):
        pk_print(f'''삭제할 {get_nx(pnx)} 가 없습니다. {'%%%FOO%%%' if LTA else ''}''')
        return
    if does_pnx_exist(pnx):
        # 1
        # if is_f(pnx):
        #     cmd = rf'echo y | del /f "{pnx}"'
        # else:
        #     cmd = rf'echo y | rmdir /s "{pnx}"'
        # cmd_to_os(cmd=cmd)

        # 2
        # if does_pnx_exist(pnx):
        #     os.remove(pnx)

        # 3
        move_pnx_to_pk_recycle_bin(pnx)
    if not os.path.exists(pnx):
        pk_print(rf"[{func_n}] pnx={pnx} {'%%%FOO%%%' if LTA else ''}", print_color='green')
    else:
        pk_print(rf"[{func_n}] pnx={pnx} {'%%%FOO%%%' if LTA else ''}", print_color='red')
