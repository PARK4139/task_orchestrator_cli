


import win32con
import uuid
import tqdm
import tomllib
import time
import tarfile
import string
import shlex
import random


import pyautogui
import psutil
import pickle
import os.path
import nest_asyncio
import keyboard
import inspect
import easyocr
import cv2
import colorama
import clipboard
import chardet
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.set_pk_context_state import set_pk_context_state

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.encodings import Encoding
from sources.objects.pk_state_via_database import PkSqlite3DB

from passlib.context import CryptContext
from os import path
from moviepy import VideoFileClip
from functools import lru_cache
from dirsync import sync
from datetime import datetime, timedelta
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from collections import Counter
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.objects.pk_local_test_activate import LTA
from sources.functions.does_pnx_exist import is_pnx_existing

import logging


def get_list_duplicated(working_list):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    items_duplicated = []
    seen = set()  # 이미 본 요소를 추적할 집합
    for item in working_list:
        if item in seen and item not in items_duplicated:
            items_duplicated.append(item)
        else:
            seen.add(item)
    return items_duplicated
