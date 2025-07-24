
import urllib
import tomllib
import toml
import timeit
import sqlite3
import pyaudio
import pickle
import mutagen
import inspect
import importlib
import functools
import easyocr
import calendar
import asyncio
from typing import TypeVar, List
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from queue import Queue, Empty
from prompt_toolkit.styles import Style
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pathlib import Path
from passlib.context import CryptContext
from moviepy import VideoFileClip
from fastapi import HTTPException
from enum import Enum
from cryptography.hazmat.backends import default_backend
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def get_current_program_pid():
    import inspect
    import subprocess

    func_n = inspect.currentframe().f_code.co_name
    pro = subprocess.check_output(
        rf'powershell (Get-WmiObject Win32_Process -Filter ProcessId=$PID).ParentProcessId', shell=True).decode(
        'utf-8')  # 실험해보니 subprocess.check_output(cmd,shell=True).decode('utf-8') 코드는 프로세스가 알아서 죽는 것 같다. 모르겠는데 " " 가 있어야 동작함
    lines = pro.split('\n')
    pids = []
    for line in lines:
        if "" != line.strip():
            pid = line
            pids.append(pid)
            pk_print(f'pid: {pid}', print_color='blue')
    return pids
