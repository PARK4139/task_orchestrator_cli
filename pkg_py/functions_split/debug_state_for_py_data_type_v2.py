
# from project_database.test_project_database import MySqlUtil
# pk_print(f'''element={element} {'%%%FOO%%%' if LTA else ''}''')
break
def pk_debug_state_for_py_data_type_v2(pk_stamp, data_working, highlight_config_dict, with_LTA=1):
elapsed = time.time() - pk_time_s
elif isinstance(data_working, dict):
elif isinstance(data_working, str):
elif with_LTA == 0:  # LTA=0 이더라도 출력은 그대로 쓸때
for element in data_working:
for key, value in data_working.items():
from PIL import Image
from colorama import init as pk_colorama_init
from cryptography.hazmat.primitives import padding
from datetime import timedelta
from enum import Enum
from functools import lru_cache
from functools import partial as functools_partial
from gtts import gTTS
from os import path
from os.path import dirname
from pathlib import Path
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.press import pk_press
from pkg_py.functions_split.print import pk_print
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.get_list_calculated import get_list_calculated
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.state_via_database import PkSqlite3DB
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from pynput import mouse
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from seleniumbase import Driver
from telegram import Bot
from telethon import TelegramClient, events
from tkinter import UNDERLINE
from yt_dlp import YoutubeDL
if LTA == 1:
if data_working:
if elapsed >= pk_time_limit:
if isinstance(data_working, list):
if not user_input:
if user_input == "":
if with_LTA == 1:
import calendar
import clipboard
import colorama
import datetime
import easyocr
import hashlib
import importlib
import ipdb
import nest_asyncio
import os.path
import pandas as pd
import pyaudio
import pygetwindow
import pyglet
import pywintypes
import random
import re
import secrets
import shutil
import socket
import sqlite3
import string
import subprocess, time
import sys
import tarfile
import threading
import time
import timeit
import tomllib
import urllib
import winreg
import yt_dlp
import zipfile
pk_print(element, highlight_config_dict)
pk_print(f'''time out (pk_time_limit={pk_time_limit}) {'%%%FOO%%%' if LTA else ''}''')
pk_print(f'{data_working}', highlight_config_dict)
pk_print(f'{key}: {value}', highlight_config_dict)
pk_time_limit = 30
pk_time_s = time.time()
str_working=rf'{STAMP_PK_DEBUGER_ENVIRONMENT} {pk_stamp} Press Enter to continue.',
timeout_secs=int(pk_time_limit - elapsed))
user_input = ""
user_input = pk_input_with_timeout(
while 1:
