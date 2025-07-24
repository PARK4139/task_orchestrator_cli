import zlib
import zipfile
import yt_dlp
import winreg
import win32com.client
import webbrowser
import tqdm
import tomllib
import timeit
import threading
import sys
import speech_recognition as sr
import socket
import secrets
import requests
import random
import pyglet
import pyaudio
import pandas as pd
import os, inspect
import os
import mysql.connector
import mutagen
import math
import ipdb
import hashlib
import functools
import cv2
from webdriver_manager.chrome import ChromeDriverManager
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from queue import Queue, Empty
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_print_state import pk_print_state

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.is_os_windows import is_os_windows
from pathlib import Path
from passlib.context import CryptContext
from functools import lru_cache
from enum import Enum
from dirsync import sync
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.pk_print import pk_print


def save_chrome_youtube_cookies_to_f():
    import browser_ cookie3

    f_cookie = rf"{D_PKG_TXT}/chrome_youtube_cookies.txt"
    f_cookie = get_pnx_os_style(pnx=f_cookie)

    try:
        cj = browser_cookie3.chrome(domain_name=".youtube.com")  # Chrome에서 youtube.com 쿠키 가져오기
        with open(file=f_cookie, mode="w") as f:
            for cookie in cj:
                f.write(
                    f"{cookie.domain}\tTRUE\t{cookie.path}\tFALSE\t{cookie.expires}\t{cookie.name}\t{cookie.value}\n")
        pk_print(f"save cookies {f_cookie}", print_color="green")
    except:
        pk_print(f"save cookies {f_cookie}", print_color='red')
