
import uuid
import urllib.parse
import tomllib
import toml
import time
import tarfile
import sys
import sqlite3
import secrets
import requests

import pythoncom
import pyglet
import pyautogui
import pyaudio
import psutil
import pickle
import pandas as pd
import nest_asyncio
import mysql.connector
import mutagen
import math
import keyboard
import inspect
import importlib
import hashlib
import functools
from urllib.parse import urlparse, parse_qs, unquote
from telegram import Bot, Update
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.press import press
from pkg_py.functions_split.print_state import print_state
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import lru_cache
from datetime import date
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def ensure_wsl_distro_session(wsl_distro_n):
    import subprocess

    if is_os_windows():
        if not is_os_wsl_linux():
            if not is_wsl_distro_started(wsl_distro_n):
                subprocess.Popen(f"wsl -d {wsl_distro_n}", creationflags=subprocess.CREATE_NO_WINDOW)
            if is_wsl_distro_started(wsl_distro_n):
                ensure_printed(
                    f'''{wsl_distro_n} is started already in wsl with keeping session {'%%%FOO%%%' if LTA else ''}''')
            else:
                ensure_printed(f'''{wsl_distro_n} is not started in wsl with keeping session {'%%%FOO%%%' if LTA else ''}''',
                         print_color='red')
                raise
