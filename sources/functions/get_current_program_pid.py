
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

from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from pathlib import Path
from passlib.context import CryptContext
from moviepy import VideoFileClip
from fastapi import HTTPException
from enum import Enum
from cryptography.hazmat.backends import default_backend
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from pathlib import Path

import logging
from sources.functions.get_pnxs import get_pnxs


def get_current_program_pid():
    import inspect
    import subprocess

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    pro = subprocess.check_output(
        rf'powershell (Get-WmiObject Win32_Process -Filter ProcessId=$PID).ParentProcessId', shell=True).decode(
        'utf-8')  # 실험해보니 subprocess.check_output(cmd,shell=True).decode('utf-8') 코드는 프로세스가 알아서 죽는 것 같다. 모르겠는데 " " 가 있어야 동작함
    lines = pro.split('\n')
    pids = []
    for line in lines:
        if "" != line.strip():
            pid = line
            pids.append(pid)
            logging.debug(f'pid: {pid}')
    return pids
