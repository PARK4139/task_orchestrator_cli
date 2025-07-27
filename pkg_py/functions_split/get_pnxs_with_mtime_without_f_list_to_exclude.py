import zipfile
import yt_dlp
import win32com.client
import tarfile
import subprocess
import string
import secrets
import random, math
import random

import pyautogui
import pyaudio
import psutil
import numpy as np
import mutagen
import hashlib
import functools
import easyocr
import cv2
import calendar

from urllib.parse import quote
from typing import TypeVar, List
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.state_via_database import PkSqlite3DB

from os.path import dirname
from moviepy import VideoFileClip
from datetime import datetime
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from base64 import b64encode
from base64 import b64decode
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def get_pnxs_with_mtime_without_f_list_to_exclude(d_src):
    import os

    f_list_to_exclude = [
        F_DB_YAML,
        F_SUCCESS_LOG,
        F_LOCAL_PKG_CACHE,
    ]
    f_list_of_d = []
    for root, _, f_nx_list in os.walk(d_src):
        for f_nx in f_nx_list:
            if not f_nx.endswith(".mp3"):  # 모든 mp3 f을 배제
                f = os.path.join(root, f_nx)
                if f not in f_list_to_exclude:
                    # files_of_d[rf"{file_path}"]=os.path.getmtime(file_path)
                    f_list_of_d.append([f, os.path.getmtime(f)])
    return f_list_of_d
