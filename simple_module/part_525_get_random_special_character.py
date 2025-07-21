import traceback
import sqlite3
# import pywin32
import pickle
import keyboard
import inspect
from yt_dlp import YoutubeDL
from tkinter import UNDERLINE
from seleniumbase import Driver
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from passlib.context import CryptContext
from colorama import init as pk_colorama_init
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style

from pkg_py.simple_module.part_014_pk_print import pk_print


def get_random_special_character(length_limit: int):
    import random
    import string

    result = ''
    for _ in range(length_limit):
        result += random.choice(string.printable)
    return
