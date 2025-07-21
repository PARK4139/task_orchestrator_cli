import zipfile
import yt_dlp
import winreg
# import win32process
# import win32gui            
# import win32gui
import win32con
import win32con
import win32com.client
import webbrowser
import uuid
import urllib.parse
import undetected_chromedriver as uc
import traceback
import tqdm
import toml
import timeit
import time
import threading
import tarfile
import sys
import subprocess, time
import subprocess
import string
import sqlite3
import socket, time
import socket
import shutil
import shlex
import secrets
import requests
import re
import random, math
import random
# import pywin32
import pyglet
import pygetwindow
import pyautogui
import pyaudio
import psutil
import paramiko
import pandas as pd
import os.path
import nest_asyncio
import mysql.connector
import mutagen
import keyboard
import ipdb
import inspect
import importlib
import hashlib
import functools
import easyocr
import datetime
import colorama
import calendar
import browser_cookie3
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from urllib.parse import unquote, urlparse, parse_qs
from urllib.parse import quote, urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram import Bot, Update
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_directories import D_PKG_TXT, D_WORKING
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_100_performance_logic import pk_measure_seconds, pk_measure_memory
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated

from PIL import Image, ImageFont, ImageDraw, ImageFilter
from PIL import Image
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from functools import partial
from functools import lru_cache
from enum import Enum
from datetime import timedelta
from datetime import datetime, time
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, Counter
from base64 import b64decode
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_etc import PkFilter, PK_UNDERLINE
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def pk_speak_v2(working_str, comma_delay=1.00, thread_join_mode=False):
    import inspect
    import threading
    from functools import partial
    import pyglet

    def stop_all_sounds():
        playing_sounds = PLAYING_SOUNDS
        for player in playing_sounds:
            player.pause()  # 또는 player.stop()

    stop_all_sounds()
    if PYGLET_PLAYER is not None:
        pass
    else:
        PYGLET_PLAYER = pyglet.media.Player()
        if PYGLET_PLAYER.playing:
            PYGLET_PLAYER.pause()

    async def process_thread_speak(working_str):
        # while not exit_event.is_set(): # 쓰레드 이벤트 제어
        func_n = inspect.currentframe().f_code.co_name
        working_str = str(working_str)
        working_str = working_str.strip()
        if working_str == "":
            return None
        if is_containing_special_characters_with_thread(text=working_str):
            working_str = remove_special_characters(text=working_str)
        while 1:
            working_list = [x.strip() for x in working_str.replace(".", ",").split(
                ",")]  # from "abc,abc.abc,abc." to ["abc","abc","abc","abc"] # , or . 를 넣으면 나누어 읽도록 업데이트
            working_list = [x for x in working_list if x.strip()]  # 리스트 요소 "" remove,  from ["", A] to [A]
            for working_str in working_list:
                pk_speak(working_str, after_delay=comma_delay)
                pass
            return None

    # 비동기 이벤트 루프 설정 (simple for void async processing)
    def process_thread_loop(ment):
        import asyncio
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(process_thread_speak(ment))

    # 비동기 이벤트 루프 exec 할 쓰레드 설정 (simple for void async processing)
    thread = threading.Thread(target=partial(process_thread_loop, working_str),
                              name="thread_for_speak")  # Q: 왜 thread.name 의 case 는 다른거야 ?  wrtn: 네, 스레드의 이름은 일반적으로 대소문자를 구분하지 않습니다.
    thread.start()
    if thread_join_mode == 1:
        thread.join()
