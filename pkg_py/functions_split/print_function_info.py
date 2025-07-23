import zipfile
import yt_dlp
# import win32gui
# import win32gui
import win32con
import win32con
import webbrowser
import uuid
import timeit
import sys
import string
import shutil
# import pywin32
# import pywin32
import psutil
import os
import math
import importlib
import hashlib
import colorama
from yt_dlp import YoutubeDL
from urllib.parse import quote
from tkinter import UNDERLINE
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from queue import Queue, Empty
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_object.etc import PkFilter
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.directories import D_WORKING
from pkg_py.pk_system_object.map_massages import PkMessages2025
from pkg_py.pk_system_object.print_red import print_red
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.local_test_activate import LTA
from mutagen.mp3 import MP3
from functools import lru_cache
from datetime import date
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from bs4 import ResultSet
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_object.etc import PK_UNDERLINE
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def print_function_info(thing_curious):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{inspect.currentframe().f_code.co_name} {str(thing_curious.__code__.co_varnames)}")
    print(help(thing_curious))
    pk_print(f'# of the Arguments : {thing_curious.__code__.co_argcount}')
    # pk_print(f'Name of the Arguments : {thing_curious.__code__.co_varnames}')
    pk_print(working_str="┌>print via getsource s")
    print(inspect.getsource(thing_curious))
    pk_print(working_str="└>print via getsource e")
