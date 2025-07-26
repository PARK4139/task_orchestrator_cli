import win32con
import uuid
import undetected_chromedriver as uc
import toml
import threading
import tarfile
import sqlite3
import socket
import pywintypes
import pythoncom
import os
import hashlib
import calendar
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from urllib.parse import quote
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PK_WORKING, D_PK_RECYCLE_BIN

from passlib.context import CryptContext
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from enum import Enum
from datetime import datetime
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from collections import Counter
from bs4 import ResultSet
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def get_pk_token(f_token, initial_str):
    import os

    f_master_key = rf"{D_PKG_TOML}/pk_token_key.toml"

    if not does_pnx_exist(pnx=f_master_key):
        ensure_pnx_removed(D_PK_RECYCLE_BIN)
        ensure_repo_cloned_via_git(repo_url='http://github.com/PARK4139/pkg_toml.git', d_dst=D_PK_RECYCLE_BIN)
        f_master_key_cloned = os.path.join(D_PK_RECYCLE_BIN, "pk_token_key.toml")
        if not os.path.exists(f_master_key_cloned):
            raise FileNotFoundError(f"Cloned key file not found at: {f_master_key_cloned}")
        move_pnx(pnx=f_master_key_cloned, d_dst=D_PKG_TOML)

    set_pk_plain_str(f_token=f_token, plain_str=initial_str, f_key=f_master_key)
    pk_plain_str = get_pk_plain_str(f_token=f_token, f_key=f_master_key)

    if LTA:
        ensure_printed(f'''pk_plain_str={pk_plain_str} {'%%%FOO%%%' if LTA else ''}''', print_color='blue')

    return pk_plain_str
