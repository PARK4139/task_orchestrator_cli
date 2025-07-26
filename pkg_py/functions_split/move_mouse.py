import zlib
import zipfile
import yt_dlp
import winreg

import win32con
import win32con
import uuid
import urllib.parse
import undetected_chromedriver as uc
import tqdm
import tomllib
import tomllib
import toml
import toml
import timeit
import time
import tarfile
import shutil
import pywintypes
import psutil
import platform
import nest_asyncio
import mysql.connector
import mutagen
import keyboard
import colorama
import asyncio
from zipfile import BadZipFile
from urllib.parse import quote
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.state_via_database import PkSqlite3DB
from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from mysql.connector import connect, Error
from gtts import gTTS
from functools import lru_cache
from fastapi import HTTPException
from datetime import datetime
from cryptography.hazmat.primitives import padding
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def move_mouse(x_abs: float, y_abs: float, duration=1):
    import pyautogui
    # func_n = inspect.currentframe().f_code.co_name
    pyautogui.moveTo(x_abs, y_abs, duration)
