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
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding

from os import path
from Cryptodome.Random import get_random_bytes
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def ensure_wsl_distro_installed(wsl_distro_n):
    if is_os_windows():
        if not is_os_wsl_linux():
            if not is_wsl_distro_installed(wsl_distro_n=wsl_distro_n):
                install_wsl_distro(wsl_distro_n=wsl_distro_n)
                if not is_wsl_distro_installed(wsl_distro_n=wsl_distro_n):
                    pk_print(rf"{wsl_distro_n} install  {'%%%FOO%%%' if LTA else ''}", print_color='red')
                    raise
