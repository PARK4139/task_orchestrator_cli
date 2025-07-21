import zlib
import zipfile
import yt_dlp
# import win32process
# import win32gui
import win32con
import urllib.parse
import tqdm
import tomllib
import toml
import timeit
import tarfile
import string
import sqlite3
import secrets
import requests
import random
import platform
import pandas as pd
import os, inspect
import numpy as np
import mysql.connector
import math
import hashlib
import easyocr
import datetime
import calendar
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import quote
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from PIL import Image
from moviepy import VideoFileClip
from functools import partial
from functools import lru_cache
from enum import Enum
from dirsync import sync
from datetime import timedelta
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from bs4 import BeautifulSoup
from base64 import b64encode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def collect_and_move(file_list, src_root):
    """file_list를 src_root+'_merged' 폴더로 이동, 중복 파일명에 (n) 붙임"""
    import os
    import shutil

    dst_root = f"{src_root.rstrip(os.sep)}_merged"
    os.makedirs(dst_root, exist_ok=True)

    for src_path in file_list:
        name = os.path.basename(src_path)
        unique_name = ensure_unique(dst_root, name)
        dst_path = os.path.join(dst_root, unique_name)
        shutil.move(src_path, dst_path)
        print(f"Moved: {src_path} -> {dst_path}")
