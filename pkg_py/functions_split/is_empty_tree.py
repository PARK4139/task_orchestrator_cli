

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
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.system_object.directories  import D_PROJECT
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_CACHE_PRIVATE
from passlib.context import CryptContext
from os import path
from functools import partial as functools_partial
from dirsync import sync
from datetime import datetime
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.system_object.directories import D_PKG_PY

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def is_empty_tree(d):
    import os

    ensure_printed(f"d={d}  {'%%%FOO%%%' if LTA else ''}")

    try:
        with os.scandir(d) as entries:
            for entry in entries:
                if entry.is_file():
                    ensure_printed(rf"is not empty d {d}")
                    return 0
        ensure_printed(rf"is not empty d 있습니다.{d}")
        return 1
    except:
        # ensure_printed(f"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}", print_color='red')
        return 0
