import zlib
import zipfile
import winreg
# import win32gui
# import win32gui
import webbrowser
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tomllib
import tomllib
import toml
import timeit
import subprocess
import string
import sqlite3
import speech_recognition as sr
import socket
import shutil
import secrets
import pywintypes
# import pywin32
# import pywin32
import pythoncom
import paramiko
import os.path
import os
import numpy as np
import nest_asyncio
import mysql.connector
import mutagen
import inspect
import importlib
import functools
import cv2
import colorama
import clipboard
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote, urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit.styles import Style
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_WORKING
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image, ImageFilter
from PIL import Image
from pathlib import Path
from os.path import dirname
from os import path
from gtts import gTTS
from functools import lru_cache
from enum import Enum
from dirsync import sync
from datetime import timedelta
from datetime import datetime, time
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def remove_pnx_parmanently(pnx):
    import inspect
    import os
    import platform
    import shutil
    import traceback

    func_n = inspect.currentframe().f_code.co_name
    if platform.system() == 'Windows':
        try:
            if validate_and_return(value=pnx) is not False:
                pk_chdir(os.path.dirname(pnx))
                if os.path.exists(pnx):
                    if is_d(pnx):
                        # shutil.rmtree(pnx_todo)
                        # if is_d(pnx_todo):
                        #     run_via_cmd_exe(rf'echo y | rmdir /s "{pnx_todo}"')
                        move_pnx_to_pk_recycle_bin(pnx)
                    elif is_f(pnx):
                        # os.remove(pnx_todo)
                        # if is_f(pnx_todo):
                        #     run_via_cmd_exe(rf'echo y | del /f "{pnx_todo}"')
                        move_pnx_to_pk_recycle_bin(pnx)

                    # pk_print(f" {'%%%FOO%%%' if LTA else ''} green {texts}" , print_color='blue)
                    # pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        except:
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        finally:
            pk_chdir(D_PROJECT)
    else:
        func_n = inspect.currentframe().f_code.co_name
        try:
            if validate_and_return(value=pnx) is not False:
                pk_chdir(os.path.dirname(pnx))
                if os.path.exists(pnx):
                    if is_d(pnx):
                        shutil.rmtree(pnx)
                    elif is_f(pnx):
                        os.remove(pnx)
        except:
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        finally:
            pk_chdir(D_PROJECT)
