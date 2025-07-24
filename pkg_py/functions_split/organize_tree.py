import zlib
import yt_dlp
import win32con
import traceback
import tomllib
import threading
import sys
import shutil
import random, math
import pyaudio
import psutil
import pandas as pd
import os.path
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from typing import TypeVar, List
from selenium.webdriver.support import expected_conditions as EC
from pynput import mouse
from prompt_toolkit.styles import Style
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.cmd_to_os import cmd_to_os

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories import D_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from functools import partial
from enum import Enum
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style


def organize_tree(d_working, with_walking):
    # src=rf"{USERPROFILE}\Downloads" # __init__.py   init_.py 가 되어 문제가 되었다.
    mode = 'f'
    gather_f_useless_at_tree(d_working=d_working)
    rename_pnx_list_at_d(d_working=d_working, mode=mode, with_walking=with_walking)
    classify_pnx_list_at_tree(d_working=d_working, mode=mode, with_walking=with_walking)
    rename_pnx_list_at_d(d_working=d_working, mode=mode, with_walking=with_walking)
    gather_empty_d(d_working=d_working)
    # empty_recycle_bin() # 비우기

    mode = 'd'
    gather_f_useless_at_tree(d_working=d_working)
    rename_pnx_list_at_d(d_working=d_working, mode=mode, with_walking=with_walking)
    classify_pnx_list_at_tree(d_working=d_working, mode=mode, with_walking=with_walking)
    rename_pnx_list_at_d(d_working=d_working, mode=mode, with_walking=with_walking)
    gather_empty_d(d_working=d_working)
    # empty_recycle_bin()  # 비우기
