

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
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.ensure_state_printed import ensure_state_printed
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.encodings import Encoding
from sources.objects.pk_state_via_database import PkSqlite3DB
from pathlib import Path
from passlib.context import CryptContext
from os import path
from enum import Enum
from dirsync import sync
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes


from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_unix_style import get_pnx_unix_style

import logging
from sources.functions.get_d_working import get_d_working


def save_cash_to_f_pkl(F_CACHE, status):
    import time
    import pickle
    with open(F_CACHE, "wb") as f:
        pickle.dump({
            "timestamp": time.time(),
            "status": status
        }, f)
