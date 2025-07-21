import zlib
import yt_dlp
# import win32process
import win32con
import webbrowser
import uuid
import urllib.parse
import toml
import threading
import sys
import string
import socket, time
import socket
# import pywin32
import pygetwindow
import pyautogui
import platform
import pickle
import pandas as pd
import mutagen
import inspect
import importlib
import datetime
import cv2
import clipboard
import calendar
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from telethon import TelegramClient, events
from telegram import Bot, Update
from selenium.webdriver.chrome.service import Service
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

from passlib.context import CryptContext
from functools import lru_cache
from dirsync import sync
from datetime import timedelta
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import BeautifulSoup
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.pk_system_layer_100_os import is_os_windows

from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def ensure_ubuntu_pkg_installed(ubuntu_pkg_n):
    import shutil

    while 1:
        ubuntu_pkg_bin = shutil.which(ubuntu_pkg_n)
        if not ubuntu_pkg_bin:
            pk_print(f"{ubuntu_pkg_n} is not installed")
            pk_print(f"try to install {ubuntu_pkg_n} now")
            cmd_to_os(f"sudo apt install -y {ubuntu_pkg_n}")
            ubuntu_pkg_bin = get_pnx_ubuntu_pkg_installed(ubuntu_pkg_n)
            if ubuntu_pkg_bin is None:
                continue
        else:
            pk_print(f"{ubuntu_pkg_n} is installed")
            break
