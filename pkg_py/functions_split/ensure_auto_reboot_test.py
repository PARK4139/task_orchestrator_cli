import zlib
import zipfile
import winreg

import win32con
import uuid
import urllib.parse
import traceback
import tqdm
import toml
import string
import sqlite3
import socket, time
import shlex
import secrets
import requests
import pythoncom
import paramiko
import pandas as pd
import math
import ipdb
import datetime

import asyncio
from zipfile import BadZipFile
from tkinter import UNDERLINE
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from queue import Queue, Empty
from pynput import mouse
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
# pk_#
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.get_list_calculated import get_list_calculated
from functools import lru_cache
from datetime import datetime, time
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from bs4 import ResultSet
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA


def ensure_auto_reboot_test():
    # EVM
    # poweroff
    # disconnect power
    # connect 2pin jumper #EVM의 경우, J#xx 점퍼로 전원인가를 자동화
    # connect power
    pass
