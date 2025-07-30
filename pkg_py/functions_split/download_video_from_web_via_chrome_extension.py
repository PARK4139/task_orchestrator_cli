

import win32com.client
import uuid
import urllib.parse
import undetected_chromedriver as uc
import tqdm
import tomllib
import toml
import timeit
import time
import sqlite3
import socket
import shlex
import secrets

import pythoncom
import pygetwindow
import pyautogui
import psutil
import platform
import paramiko
import pandas as pd
import mutagen
import keyboard
import ipdb
import importlib
import easyocr
import colorama
import calendar
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import quote
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
# from pkg_py.system_object.print_red import print_red
# from pkg_py.system_object.is_os_windows import is_os_windows
from mysql.connector import connect, Error
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from functools import partial
from dirsync import sync
from datetime import datetime, timedelta
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.get_d_working import get_d_working


def download_video_from_web_via_chrome_extension():
    while 1:
        # press("ctrl", "0")
        f_png = rf"{D_PROJECT}\pkg_image\download_video_via_chrome_extensions.png"
        click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, loop_limit_cnt=10)

        ensure_slept(1000)

        ensure_pressed("tab")
        ensure_slept(30)

        ensure_pressed("enter")
        ensure_slept(30)

        ensure_pressed("ctrl", "shift", "tab")

        ensure_pressed("ctrl", "0")
        ensure_pressed("ctrl", "-")
        ensure_pressed("ctrl", "-")
        break
