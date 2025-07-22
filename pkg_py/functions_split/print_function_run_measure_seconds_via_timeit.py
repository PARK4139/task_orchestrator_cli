import zlib
import zipfile
import winreg
# import win32gui
# import win32gui
import win32con
import win32con
import win32com.client
import webbrowser
import uuid
import urllib
import undetected_chromedriver as uc
import traceback
import timeit
import sys
import shutil
import shlex
import secrets
import requests
import re
import pywintypes
# import pywin32
# import pywin32
import pythoncom
import pyglet
import pyautogui
import pyaudio
import pickle
import pandas as pd
import os.path
import os, inspect
import nest_asyncio
import mysql.connector
import mutagen
import keyboard
import json
import ipdb
import importlib
import hashlib
import functools
import easyocr
import datetime
import cv2
import colorama
import colorama
import clipboard
import calendar
import browser_cookie3
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import unquote, urlparse, parse_qs
from urllib.parse import quote, urlparse
from typing import TypeVar, List
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_object.etc import PkFilter
from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.directories import D_WORKING
from pkg_py.pk_system_object.directories import D_PKG_TXT, D_WORKING
from pkg_py.pk_system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_object.print_red import print_red
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated
from PIL import Image, ImageFilter
from PIL import Image
from pathlib import Path
from os import path
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial as functools_partial
from enum import Enum
from dirsync import sync
from datetime import timedelta
from datetime import datetime, timedelta
from datetime import date
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from bs4 import ResultSet
from bs4 import BeautifulSoup
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def print_function_run_measure_seconds_via_timeit(function, repeat):
    """
    특정 함수의 평균 exec  시간을 측정하여 로그로 출력합니다.
    """
    # todo : f에 결과즐 저장해서 통계를 내릴 수 있도록한다.
    from pkg_py.functions_split.pk_print import pk_print
    import timeit
    from functools import partial as functools_partial

    if isinstance(function, functools_partial):
        func_n = function.func.__name__
    else:
        func_n = function.__name__

    execution_time = timeit.timeit(function, number=repeat)
    pk_print(f"{func_n}() : {repeat}번 반복 평균 exec  시간: {execution_time:.6f} seconds", print_color='yellow')
