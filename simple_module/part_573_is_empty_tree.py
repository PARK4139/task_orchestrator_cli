# import win32process
# import win32gui
import tomllib
import threading
import secrets
import pywintypes
import pyglet
import os
import hashlib
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from selenium.webdriver.common.keys import Keys
from prompt_toolkit.styles import Style
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_directories import D_DOWNLOADS, D_PKG_PKL
from passlib.context import CryptContext
from os import path
from functools import partial as functools_partial
from dirsync import sync
from datetime import datetime
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_layer_directories import D_PKG_PY

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def is_empty_tree(d):
    import os

    pk_print(f"d={d}  {'%%%FOO%%%' if LTA else ''}")

    try:
        with os.scandir(d) as entries:
            for entry in entries:
                if entry.is_file():
                    pk_print(rf"is not empty d {d}")
                    return 0
        pk_print(rf"is not empty d 있습니다.{d}")
        return 1
    except:
        # pk_print(f"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}", print_color='red')
        return 0
