import winreg
import win32con
import traceback
import toml
import tarfile
import socket
import re
import pygetwindow
import platform
import paramiko
import mutagen
import hashlib
import functools
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding

from os import path
from Cryptodome.Random import get_random_bytes
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_wsl_distro_enabled(wsl_distro_n):
    if is_os_windows():
        if not is_os_wsl_linux():
            if not is_wsl_distro_enabled(wsl_distro_n=wsl_distro_n):
                install_wsl_distro(wsl_distro_n=wsl_distro_n)
                if not is_wsl_distro_enabled(wsl_distro_n=wsl_distro_n):
                    ensure_printed(rf"{wsl_distro_n} install  {'%%%FOO%%%' if LTA else ''}", print_color='red')
                    raise
