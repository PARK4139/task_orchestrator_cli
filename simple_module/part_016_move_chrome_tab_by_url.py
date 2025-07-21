

import yt_dlp
import winreg
# import win32gui
import win32con
import win32con
import urllib.parse
import urllib
import traceback
import toml
import toml
import timeit
import threading
import tarfile
import sys
import subprocess, time
import subprocess
import speech_recognition as sr
import shutil
import secrets
import requests
import pywintypes
# import pywin32
import pyglet
import pygetwindow
import platform
import pickle
import paramiko
import pandas as pd
import os.path
import numpy as np
import nest_asyncio
import mutagen
import keyboard
import json
import ipdb
import functools
import easyocr
import datetime
import clipboard
import chardet
import calendar
import asyncio
from zipfile import BadZipFile
from urllib.parse import urlparse
from urllib.parse import quote
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from PySide6.QtWidgets import QApplication
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_100_os import is_os_windows
from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from moviepy import VideoFileClip
from gtts import gTTS
from functools import lru_cache
from enum import Enum
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows

from pkg_py.simple_module.part_014_pk_print import pk_print


def move_chrome_tab_by_url(url):
    # todo : test 버퍼 지워지는 것 같음.

    minimize_all_windows()
    window_title_seg = get_window_title(window_title_seg="Chrome")
    window_titles = get_window_title_list()
    for window_title in window_titles:
        if "Chrome".lower() in window_title.lower():
            ensure_window_to_front(window_title_seg=window_title)
            loop_limit = 30
            loop_cnt = 0
            while 1:
                if loop_cnt == loop_limit:
                    return
                loop_cnt = loop_cnt + 1
                pk_sleep(milliseconds=15)
                pk_press("ctrl", "l")
                pk_sleep(milliseconds=15)
                url_dragged = get_text_dragged()
                if url_dragged == url:
                    pk_print(f'''url_to_move = "{url}"''')
                    pk_print(f'''url_dragged = "{url_dragged}"''')
                    break
                pass
