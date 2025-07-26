import traceback
import sqlite3

import pickle
import keyboard
import inspect
from yt_dlp import YoutubeDL
from tkinter import UNDERLINE
from seleniumbase import Driver
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_context import SpeedControlContext
from passlib.context import CryptContext
from colorama import init as pk_colorama_init
from pkg_py.functions_split.is_d import is_d
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.ensure_printed import ensure_printed


def get_random_special_character(length_limit: int):
    import random
    import string

    result = ''
    for _ in range(length_limit):
        result += random.choice(string.printable)
    return
