

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



from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
import logging
import logging
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.pk_etc import PkFilter

from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING

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
from sources.functions.get_nx import get_nx


from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_pnxs import get_pnxs
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.objects.pk_local_test_activate import LTA
import logging

import logging
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


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
