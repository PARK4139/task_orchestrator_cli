
import win32com.client
import traceback
import sqlite3
import socket
import shutil
import pyglet
import pyautogui
import paramiko
import pandas as pd
import keyboard
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pytube import Playlist
from sources.functions.get_d_working import get_d_working
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.encodings import Encoding

from passlib.context import CryptContext
from colorama import init as pk_colorama_init
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.functions.is_d import is_d
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows

from sources.objects.pk_local_test_activate import LTA


def is_midnight():
    from datetime import datetime
    now = datetime.now()
    if now.hour == 0 and now.minute == 0 and now.second == 0:
        return 1
    else:
        return 0
