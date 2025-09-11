import yt_dlp
import win32con
import webbrowser
import tomllib
import threading
import pygetwindow
import pickle
import keyboard
import inspect
import cv2
import asyncio
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from prompt_toolkit.styles import Style
from sources.functions.ensure_window_to_front import ensure_window_to_front



from sources.functions.ensure_command_executed import ensure_command_executed

from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX

from sources.objects.pk_state_via_database import PkSqlite3DB
from passlib.context import CryptContext
from gtts import gTTS
from dirsync import sync
from bs4 import ResultSet

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.is_d import is_d
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def get_list_added_suffix_each_element(working_list, suffix):
    return [f"{line}{suffix}" for line in working_list]
