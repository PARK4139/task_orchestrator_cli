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
from sources.functions.get_historical_list import get_historical_list


from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_state_printed import ensure_state_printed
import logging
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.pk_etc import PkFilter

from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING
from sources.objects.pk_state_via_context import SpeedControlContext
from sources.objects.performance_logic import ensure_seconds_measured, pk_measure_memory

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
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_f import is_f
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.objects.pk_local_test_activate import LTA
from sources.functions.does_pnx_exist import is_pnx_existing

import logging
from sources.functions.get_d_working import get_d_working


def run_venv_in_cmd_exe():
    f_p = rf'{D_TASK_ORCHESTRATOR_CLI_RESOURCES}'
    f_n = 'pk_ensure_chrome_youtube_cookies_saved_to_file'
    f_pn_py = Path(rf"{f_p}/{f_n}.py")
    f_cmd = rf"{D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES}\{f_n}.cmd"
    activate_bat = rf'{D_TASK_ORCHESTRATOR_CLI}\.venv_windows\Scripts\activate.cmd'
python_exe = rf'{D_TASK_ORCHESTRATOR_CLI}\.venv_windows\Scripts\python.exe'
    CRLF = '%%%CRLF%%%'
    script_str = rf'''
       :: @echo off{CRLF}
       chcp 65001 >NUL{CRLF}
       title %~nx0{CRLF}   
       cls{CRLF}

       :: 관리자 권한 요청{CRLF}
       :: net session >NUL 2>&1{CRLF}
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
    logging.debug(rf"set PYTHONPATH={D_TASK_ORCHESTRATOR_CLI}")
    # ensure_command_executed(cmd=rf'notepad "{activate_bat}"')
    # ensure_command_executed(cmd=rf'notepad "{f_pn_bat}"')
    ensure_command_executed(cmd=rf'start call "{f_cmd}" ', encoding=Encoding.UTF8, mode='a')
