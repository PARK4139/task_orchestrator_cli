# import win32gui
import win32con
import webbrowser
import uuid
import urllib
import undetected_chromedriver as uc
import traceback
import tomllib
import timeit
import time
import shutil
import re
# import pywin32
import pyglet
import pyautogui
import pickle
import os
import numpy as np
import mysql.connector
import mutagen
import math
import json
import hashlib
import cv2
import chardet
import browser_cookie3
from zipfile import BadZipFile
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_100_os import is_os_windows

from PIL import Image
from gtts import gTTS
from functools import lru_cache
from enum import Enum
from datetime import date
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from collections import Counter
from base64 import b64decode
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.pk_system_layer_100_Local_test_activate import LTA


def check_root_right():
    # root 권한 검사
    import os
    if os.geteuid() != 0:
        return False
    return True
