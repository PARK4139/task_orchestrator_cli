import tomllib
import toml
import sys
import sqlite3
import shlex
import pywintypes
# import pywin32            
# import pywin32
import pyautogui
import pyaudio
import ipdb
import hashlib
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote, urlparse
from selenium.webdriver.support import expected_conditions as EC
from PySide6.QtWidgets import QApplication
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025
from dirsync import sync
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.functions_split.get_d_working import get_d_working


def get_pk_key_from_f(f):
    f = get_pnx_os_style(f)
    with open(f, "r", encoding="utf-8") as f:
        key_byte = f.read().strip().encode()  # 문자열을 bytes로
        return key_byte
