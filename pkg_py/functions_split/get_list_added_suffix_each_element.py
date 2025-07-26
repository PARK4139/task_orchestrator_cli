import yt_dlp
import win32con
import webbrowser
import tomllib
import threading
import pygetwindow
import pickle
import keyboard
import inspect
import cv2
import asyncio
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from prompt_toolkit.styles import Style
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from passlib.context import CryptContext
from gtts import gTTS
from dirsync import sync
from bs4 import ResultSet
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def get_list_added_suffix_each_element(working_list, suffix):
    return [f"{line}{suffix}" for line in working_list]
