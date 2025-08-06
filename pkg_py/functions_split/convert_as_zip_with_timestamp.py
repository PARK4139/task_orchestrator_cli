import zlib
import zipfile
import yt_dlp
import winreg
import win32com.client
import webbrowser
import traceback
import tomllib
import toml
import toml
import threading
import tarfile
import string
import socket, time
import shutil
import requests
import re
import pyglet
import pyautogui
import pyaudio
import platform
import os.path
import os, inspect
import numpy as np
import nest_asyncio
import math
import keyboard
import json
import importlib
import hashlib
import functools
import datetime

import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from telegram import Bot, Update
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from queue import Queue, Empty
from pytube import Playlist
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories  import D_PROJECT
# from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.local_test_activate import LTA
from PIL import Image, ImageFont, ImageDraw
from PIL import Image
from os.path import dirname
from gtts import gTTS
from functools import partial as functools_partial
from functools import lru_cache
from datetime import timedelta
from datetime import datetime, timedelta
from cryptography.hazmat.primitives import padding
from collections import Counter
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def convert_as_zip_with_timestamp(f):
    import os
    import traceback

    starting_d = get_d_working()
    try:
        target_dirname = os.path.dirname(f)
        target_dirname_dirname = os.path.dirname(target_dirname)
        target_basename = os.path.basename(f).split(".")[0]
        target_zip = rf'$zip_{target_basename}.zip'
        target_yyyy_mm_dd_HH_MM_SS_zip = rf'{target_basename} - {get_time_as_("%Y %m %d %H %M %S")}.zip'
        # ensure_printed(rf'# target_dirname_dirname 로 이동')
        os.chdir(target_dirname_dirname)
        # ensure_printed(rf'부모d로 백업')
        cmd = f'bandizip.exe c "{target_zip}" "{f}"'
        ensure_command_excuted_to_os_like_person_as_admin(cmd)
        # ensure_printed(rf'이름변경')
        cmd = f'ren "{target_zip}" "$deleted_{target_yyyy_mm_dd_HH_MM_SS_zip}"'
        ensure_command_excuted_to_os_like_person_as_admin(cmd)
        # ensure_printed(rf'부모d에서 백업될 d로 이동')
        cmd = f'move "$deleted_{target_yyyy_mm_dd_HH_MM_SS_zip}" "{target_dirname}"'
        ensure_command_excuted_to_os_like_person_as_admin(cmd)
        # ensure_printed(rf'백업될 d로 이동')
        os.chdir(target_dirname)
        # ensure_printed(str_working="os.getcwd()")
        # ensure_printed(os.getcwd())
        # ensure_printed(str_working="원본f삭제")
        os.remove(f)
    except:
        ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    finally:
        ensure_printed(rf'프로젝트 d로 이동')
        os.chdir(starting_d)
