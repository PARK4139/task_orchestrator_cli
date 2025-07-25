

import zipfile
import winreg
import win32con
import win32com.client
import undetected_chromedriver as uc
import tqdm
import tomllib
import tomllib
import toml
import toml
import time
import string
import socket
import shutil
import requests
import pyautogui
import platform
import pandas as pd
import hashlib
import easyocr
import datetime
import chardet
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from typing import TypeVar, List
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.is_os_windows import is_os_windows
from PIL import Image
from passlib.context import CryptContext
from os import path
from moviepy import VideoFileClip
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from dirsync import sync
from datetime import date
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def decompress_f_tar_gz(src, dst):  # not tested
    import tarfile
    import os
    # Ensure the archive exists
    if not os.path.exists(src):
        raise FileNotFoundError(f"Archive file '{src}' does not exist.")
    # Extract the archive
    with tarfile.open(src, "r:gz") as tar:
        # Preserve permissions, ownership, and timestamps during extraction
        def is_within_directory(directory, target):
            """
            Ensure the target path is within the directory to prevent path traversal attacks.
            """
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
            return os.path.commonpath([abs_directory, abs_target]) == abs_directory

        for member in tar.getmembers():
            # Ensure path traversal is prevented
            member_path = os.path.join(dst, member.name)
            if not is_within_directory(dst, member_path):
                raise Exception(f"Path traversal attempt detected: {member.name}")
        tar.extractall(path=dst)
