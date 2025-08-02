

import win32com.client
import uuid
import urllib.parse
import urllib
import toml
import sys
import string
import shutil

import easyocr
import datetime
import calendar
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.ensure_state_printed import ensure_state_printed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pathlib import Path
from passlib.context import CryptContext
from os import path
from enum import Enum
from dirsync import sync
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def save_cash_to_f_pkl(F_CACHE, status):
    import time
    import pickle
    with open(F_CACHE, "wb") as f:
        pickle.dump({
            "timestamp": time.time(),
            "status": status
        }, f)
