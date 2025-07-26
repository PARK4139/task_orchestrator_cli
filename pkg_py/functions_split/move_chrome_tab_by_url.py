

import yt_dlp
import winreg

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
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.press import press
from pkg_py.functions_split.print_state import print_state
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.is_os_windows import is_os_windows
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
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows

from pkg_py.functions_split.ensure_printed import ensure_printed


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
                ensure_slept(milliseconds=15)
                pk_press("ctrl", "l")
                ensure_slept(milliseconds=15)
                url_dragged = get_text_dragged()
                if url_dragged == url:
                    ensure_printed(f'''url_to_move = "{url}"''')
                    ensure_printed(f'''url_dragged = "{url_dragged}"''')
                    break
                pass
