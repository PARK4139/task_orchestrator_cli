import zlib
import zipfile
import yt_dlp
import win32con
import webbrowser
import urllib
import tomllib
import toml
import socket
import secrets
import random
import pywintypes
import pygetwindow
import paramiko
import pandas as pd
import os
import numpy as np
import nest_asyncio
import mutagen
import ipdb
import easyocr
import colorama
import colorama
import calendar
import browser_cookie3
import asyncio
from yt_dlp import YoutubeDL
from urllib.parse import unquote, urlparse, parse_qs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_object.etc import PkFilter
from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated

from pathlib import Path
from passlib.context import CryptContext
from moviepy import VideoFileClip
from enum import Enum
from bs4 import BeautifulSoup
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def save_power_as_s3():
    # 절전모드
    # cmd_to_os(cmd=rf"powercfg /setacvalueindex scheme_current sub_buttons button=1-3 action=0")
    cmd = rf"rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
    if is_os_windows():
        cmd_to_os(cmd=cmd)
    else:
        cmd = get_pnx_wsl_unix_style(pnx=cmd)
        cmd_to_os(cmd=cmd)
