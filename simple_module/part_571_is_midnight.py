# import win32gui
import win32com.client
import traceback
import sqlite3
import socket
import shutil
import pyglet
import pyautogui
import paramiko
import pandas as pd
import keyboard
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pytube import Playlist
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_800_print_util import print_red
from passlib.context import CryptContext
from colorama import init as pk_colorama_init
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows

from pkg_py.pk_system_layer_100_Local_test_activate import LTA


def is_midnight():
    from datetime import datetime
    now = datetime.now()
    if now.hour == 0 and now.minute == 0 and now.second == 0:
        return 1
    else:
        return 0
