import yt_dlp

import win32con
import win32con
import uuid
import tomllib
import timeit
import threading
import subprocess
import shlex
import secrets


import pyaudio
import platform
import pickle
import os.path
import os, inspect
import keyboard
import hashlib
import functools
import easyocr
import colorama
import clipboard
import calendar
from urllib.parse import quote, urlparse
from urllib.parse import quote
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from selenium.webdriver.support import expected_conditions as EC
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.performance_logic import measure_seconds, pk_measure_memory
from pkg_py.system_object.is_os_windows import is_os_windows

from paramiko import SSHClient, AutoAddPolicy
from os import path
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from enum import Enum
from datetime import datetime
from datetime import date
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from collections import Counter
from bs4 import BeautifulSoup
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.ensure_printed import ensure_printed


def get_age_korean(birth_day):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    # 2023-1994=29(생일후)
    # 2024-1994=30(생일후)
    # 만나이 == 생물학적나이
    # 생일 전 만나이
    # 생일 후 만나이
    pass
