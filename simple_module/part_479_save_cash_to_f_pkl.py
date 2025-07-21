# import win32process
# import win32gui
import win32com.client
import uuid
import urllib.parse
import urllib
import toml
import sys
import string
import shutil
# import pywin32
import easyocr
import datetime
import calendar
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pathlib import Path
from passlib.context import CryptContext
from os import path
from enum import Enum
from dirsync import sync
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style

from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def save_cash_to_f_pkl(F_CACHE, status):
    import time
    import pickle
    with open(F_CACHE, "wb") as f:
        pickle.dump({
            "timestamp": time.time(),
            "status": status
        }, f)
