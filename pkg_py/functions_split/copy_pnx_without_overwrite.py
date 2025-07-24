import yt_dlp


import win32con
import uuid
import tomllib
import toml
import toml
import timeit
import time
import threading
import sys
import subprocess, time
import sqlite3
import shlex
import requests
import random
import pyglet
import pygetwindow
import pyaudio
import pickle
import paramiko
import mysql.connector
import math
import keyboard
import json
import cv2
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote
from telethon import TelegramClient, events
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.is_os_windows import is_os_windows
from PIL import Image
from os import path
from moviepy import VideoFileClip
from fastapi import HTTPException
from dirsync import sync
from datetime import date
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def copy_pnx_without_overwrite(pnx, dst):
    import os
    import random
    import re
    import shutil
    import traceback

    if not os.path.exists(pnx):
        print(f"소스 경로 '{pnx}'가 존재하지 않습니다.")
        return

    if not os.path.exists(dst):
        ensure_pnx_made(pnx=pnx, mode='d')
    if is_f(pnx):
        shutil.copy2(pnx, dst)
        print(f"f '{pnx}'을(를) '{dst}'로 복사했습니다.")
    elif is_d(pnx):
        try:
            pnx_p = os.path.dirname(pnx)
            time_pattern_with_underbar = rf"_{get_time_as_('now')}"
            pnx_n = get_n(pnx)
            pnx_x = get_x(pnx)
            pnx_new = rf"{dst}\{pnx_n}{pnx_x}"
            pattern = r'\d{4}_\d{2}_\d{2}_(월|화|수|목|금|토|일)_\d{2}_\d{2}_\d{2}_\d{3}'
            pnx_n = re.sub(pattern=pattern, repl='', string=pnx_n)
            pk_print(str_working=rf'''pnx="{pnx}"  {'%%%FOO%%%' if LTA else ''}''')
            pk_print(str_working=rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''')
            dst_nx = None
            if not does_pnx_exist(pnx=pnx_new):
                dst_nx = rf"{dst}\{pnx_n}{pnx_x}"
            else:
                dst_nx = rf"{dst}\{pnx_n}{time_pattern_with_underbar}{random.randint(10, 99)}{pnx_x}"
            shutil.copytree(src=pnx, dst=dst_nx)
        except:
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    else:
        print(f"소스 경로 '{pnx}'는 f도 d도 아닙니다.")
