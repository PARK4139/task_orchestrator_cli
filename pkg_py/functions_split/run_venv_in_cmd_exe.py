import yt_dlp
import winreg


import win32con
import undetected_chromedriver as uc
import time
import sys
import subprocess
import sqlite3
import socket
import shutil
import secrets
import requests
import re
import random

import pyglet
import pygetwindow
import pyautogui
import os.path
import os
import math
import ipdb
import inspect
import datetime
import chardet
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote
from typing import TypeVar, List
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_state_printed import ensure_state_printed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
# pk_#
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories  import D_PROJECT
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.directories import D_PKG_CACHE_PRIVATE, D_PK_WORKING
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.performance_logic import ensure_seconds_measured, pk_measure_memory

from pathlib import Path
from paramiko import SSHClient, AutoAddPolicy
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial
from functools import lru_cache
from datetime import datetime, time
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def run_venv_in_cmd_exe():
    f_p = rf'{D_PKG_PY}'
    f_n = 'pk_ensure_chrome_youtube_cookies_saved_to_file'
    f_pn_py = get_pnx_os_style(pnx=rf"{f_p}/{f_n}.py")
    f_cmd = rf"{D_PKG_WINDOWS}\{f_n}.cmd"
    activate_bat = rf'{D_PROJECT}\.venv\Scripts\activate.cmd'
    python_exe = rf'{D_PROJECT}\.venv\Scripts\python.exe'
    CRLF = '%%%CRLF%%%'
    script_str = rf'''
       :: @echo off{CRLF}
       chcp 65001 >nul{CRLF}
       title %~nx0{CRLF}   
       cls{CRLF}

       :: 관리자 권한 요청{CRLF}
       :: net session >nul 2>&1{CRLF}
       :: if %errorLevel% neq 0 ({CRLF}
       ::     powershell -Command "Start-Process python -ArgumentList '\"%~dp0myscript.py\"' -Verb RunAs"{CRLF}
       ::     exit /b{CRLF}
       :: ){CRLF}               
       :: cls{CRLF}

       call "{activate_bat}"{CRLF}
     '''
    script_list = script_str.split(CRLF)
    script_list = get_list_replaced_element_from_str_to_str(working_list=script_list, from_str='    ', to_str='')
    ensure_pnx_made(pnx=f_cmd, mode='f', script_list=script_list)
    ensure_printed(rf"set PYTHONPATH={D_PROJECT}", print_color='blue')
    # ensure_command_excuted_to_os(cmd=rf'notepad "{activate_bat}"')
    # ensure_command_excuted_to_os(cmd=rf'notepad "{f_pn_bat}"')
    ensure_command_excuted_to_os(cmd=rf'start call "{f_cmd}" ', encoding=Encoding.UTF8, mode='a')
