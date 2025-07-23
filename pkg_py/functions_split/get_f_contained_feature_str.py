import zipfile
# import win32process
import win32con
import tomllib
import timeit
import sqlite3
import speech_recognition as sr
import shutil
import requests
import random, math
import random
import pygetwindow
import pickle
import os.path
import mysql.connector
import mutagen
import keyboard
import ipdb
import importlib
import easyocr
import datetime
import colorama
import colorama
import browser_cookie3
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import urlparse
from urllib.parse import quote, urlparse
from telethon import TelegramClient, events
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_object.etc import PkFilter
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.print_red import print_red
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pkg_py.pk_system_object.is_os_windows import is_os_windows

from os import path
from moviepy import VideoFileClip
from fastapi import HTTPException
from datetime import timedelta
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def get_f_contained_feature_str(feature_str, d_pnx):
    import os
    if not os.path.exists(d_pnx):
        pk_print(f'''Directory does not exist: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return None
    else:
        pk_print(f'''Searching for feature_str="{feature_str}" in directory: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''')
    for filename in os.listdir(d_pnx):
        if feature_str in filename:
            full_path = os.path.join(d_pnx, filename)
            pk_print(f'''Found file: {full_path}  {'%%%FOO%%%' if LTA else ''}''')
            return full_path
    else:
        pk_print(
            f'''No file containing feature_str="{feature_str}" found in directory: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''')
    return None
