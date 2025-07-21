import zlib
import zipfile
import yt_dlp
import win32con
import win32com.client
import uuid
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tqdm
import tomllib
import tomllib
import toml
import toml
import sys
import sqlite3
import shutil
import shlex
import secrets
import requests
import re
import random
import pywintypes
# import pywin32
import pythoncom
import pyglet
import pygetwindow
import pyautogui
import pyaudio
import psutil
import platform
import pickle
import paramiko
import pandas as pd
import os.path
import os
import nest_asyncio
import keyboard
import json
import ipdb
import inspect
import hashlib
import easyocr
import datetime
import cv2
import colorama
import colorama
import clipboard
import chardet
import browser_cookie3
import asyncio
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote, urlparse
from urllib.parse import quote
from telegram import Bot, Update
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from queue import Queue, Empty
from PySide6.QtWidgets import QApplication
from pynput import mouse
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories import D_WORKING, D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_directories import D_PKG_TXT, D_WORKING
from pkg_py.pk_system_layer_directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_os import is_os_windows, is_os_wsl_linux
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated

from PIL import Image
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from datetime import timedelta
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import BeautifulSoup
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def is_wired_pnx(pnx):
    import inspect
    import os
    import string

    func_n = inspect.currentframe().f_code.co_name
    # wired 이상한 pnx 인지 확인
    # required 가 나은 것 같은데
    if pnx == "":
        pk_print(f'''입력된 pnx가 "" 입니다 pnx={pnx} {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return 1
    connected_drives = []
    for drive_letter in string.ascii_uppercase:
        drive_path = drive_letter + ":\\"
        if os.path.exists(drive_path):
            connected_drives.append(drive_path)
            if pnx == drive_path:
                pk_print(f'''입력된 pnx는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
                return 1
    if not os.path.exists(pnx):
        pk_print(f'''입력된 pnx가 존재하지 않습니다 pnx={pnx} {'%%%FOO%%%' if LTA else ''}''')
        return 1
