import zlib
import zipfile
import yt_dlp

import win32con
import win32con
import traceback
import tqdm
import tomllib
import toml
import time
import threading
import sys
import subprocess
import sqlite3
import shlex
import requests
import pywintypes


import pyautogui
import pyaudio
import platform
import pandas as pd
import os.path
import numpy as np
import nest_asyncio
import mutagen
import keyboard
import inspect
import importlib
import colorama
import clipboard
import chardet
import calendar
from urllib.parse import unquote, urlparse, parse_qs
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.chrome.service import Service
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.performance_logic import ensure_seconds_measured, pk_measure_memory
from pkg_py.system_object.local_test_activate import LTA
from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import lru_cache
from datetime import timedelta
from datetime import datetime, timedelta
from datetime import datetime, time
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from collections import Counter
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs


def get_line_list_to_include_search_keyword(f, search_keywords):
    lines_list = get_list_from_f(f=f)
    target_lines = []

    for line in lines_list:
        if any(keyword in line for keyword in search_keywords):
            target_lines.append(line)

    return target_lines
