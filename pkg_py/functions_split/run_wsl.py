import winreg

import win32con
import win32com.client
import urllib.parse
import undetected_chromedriver as uc
import tqdm
import socket
import random

import pythoncom
import pyaudio
import paramiko
import os.path
import os
import numpy as np
import math
import importlib
import clipboard
import chardet
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from PIL import Image
from os import path
from mysql.connector import connect, Error
from fastapi import HTTPException
from enum import Enum
from cryptography.hazmat.backends import default_backend
from bs4 import ResultSet
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.system_object.local_test_activate import LTA


def run_wsl(remote_os_distro_n, wsl_window_title_seg):
    # install wsl
    # install_wsl(remote_os_distro_n)

    if not is_window_opened(window_title_seg=wsl_window_title_seg):
        open_and_move_wsl_console_to_front(remote_os_distro_n=remote_os_distro_n, window_title_seg=wsl_window_title_seg)
    while 1:
        if is_front_window_title(window_title_seg=wsl_window_title_seg):
            break
        ensure_window_to_front(window_title_seg=wsl_window_title_seg)
