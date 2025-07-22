

import zipfile
import yt_dlp
import winreg
# import win32process
# import win32gui
import win32con
import win32con
import win32com.client
import webbrowser
import uuid
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tomllib
import tomllib
import timeit
import time
import tarfile
import sys
import subprocess, time
import subprocess
import speech_recognition as sr
import socket
import shlex
import pywintypes
# import pywin32
import platform
import pickle
import numpy as np
import mutagen
import math
import keyboard
import json
import ipdb
import inspect
import importlib
import hashlib
import colorama
import clipboard
import calendar
from zipfile import BadZipFile
from urllib.parse import urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from queue import Queue, Empty
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.pk_system_object.etc import PkFilter
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.directories import D_PKG_TXT, D_WORKING
from pkg_py.pk_system_object.print_red import print_red
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.Local_test_activate import LTA

from PIL import Image, ImageFilter
from os.path import dirname
from os import path
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from enum import Enum
from dirsync import sync
from datetime import datetime, time
from datetime import date
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from base64 import b64decode
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.pk_system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_object.directories import D_WORKING, D_DOWNLOADS, D_PKG_PKL, D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.pk_system_object.Local_test_activate import LTA

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def print_window_opened_list():
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    window_opened_list = get_windows_opened()
    for window_opened in window_opened_list:
        pk_print(working_str=rf'[window_opened] {window_opened}')
