import zipfile

import win32con
import urllib.parse
import urllib
import tomllib
import toml
import timeit
import threading
import tarfile
import sqlite3
import speech_recognition as sr
import shlex
import requests
import random


import pyaudio
import platform
import pickle
import paramiko
import pandas as pd
import os
import nest_asyncio
import mysql.connector
import math
import keyboard
import inspect
import functools
import datetime

from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from telegram import Bot
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from pytube import Playlist
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
# from pkg_py.system_object.is_os_windows import is_os_windows
from pathlib import Path
from os.path import dirname
from os import path
from functools import lru_cache
from enum import Enum
from dirsync import sync
from datetime import datetime
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_window_to_front_of_pycharm():
    # pycharm64.exe 에 열린 탭으로 이동해야하는데
    try:
        pids = get_pids(process_img_n="pycharm64.exe")
        for pid in pids:
            ensure_window_to_front(pid=pid)
    except:
        ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
    # move_and_ensure_window_to_front(window_title_seg='pk_system_ – test.py')
