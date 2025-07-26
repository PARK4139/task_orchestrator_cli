import win32con
import toml
import time
import tarfile
import string
import sqlite3
import pickle
import os.path
import mysql.connector
import ipdb
import inspect
import importlib
from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.press import press
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.cmd_to_os import cmd_to_os

from passlib.context import CryptContext
from mutagen.mp3 import MP3
from gtts import gTTS
from datetime import timedelta
from Cryptodome.Random import get_random_bytes
from bs4 import ResultSet
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def ask_to_google(question: str):
    # str preprocess
    question = question.replace(" ", "+")
    question = question.strip()

    # search in google
    cmd = f'explorer "https://www.google.com/search?q={question}"  >nul'
    cmd_to_os(cmd=cmd)
    ensure_printed(f'''{cmd}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")

    # move window to front
    window_title_seg = rf"{question} - Google"
    while 1:
        ensure_window_to_front(window_title_seg=window_title_seg)
        if is_front_window_title(window_title_seg=window_title_seg):
            break
