import zlib
import yt_dlp


import win32con
import win32con
import win32com.client
import uuid
import urllib.parse
import undetected_chromedriver as uc
import traceback
import tqdm
import timeit
import tarfile
import subprocess, time
import string
import shutil
import secrets
import requests
import random

import pyglet
import pyautogui
import psutil
import platform
import paramiko
import os.path
import os, inspect
import nest_asyncio
import mysql.connector
import mutagen
import math
import keyboard
import ipdb
import functools
import easyocr
import datetime
import cv2
import colorama
import colorama
import chardet
import calendar

import asyncio
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from prompt_toolkit.styles import Style

from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front


from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
import logging
import logging

from sources.functions.get_list_sorted import get_list_sorted

from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.pk_etc import PkFilter


from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext
from sources.objects.performance_logic import ensure_seconds_measured, pk_measure_memory
from sources.objects.pk_local_test_activate import LTA

from PIL import Image, ImageFilter
from PIL import Image
from os import path
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from base64 import b64encode
from base64 import b64decode
from sources.functions.get_nx import get_nx

from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

from sources.functions.get_pnxs import get_pnxs


def input_v33_nvim_theme(
        str_working: str,
        limit_seconds: int = 30,
        return_default: str | None = None,
        *,
        masked: bool = False,
        fuzzy_accept: list[tuple[str, ...]] | None = None,
        validator=None,  # Callable[[str], bool]
        vi_mode: bool = True,
        **kwargs
):
    """
    input_v33_nvim_theme 함수를 ensure_value_completed로 대체
    """
    # fuzzy_accept가 있는 경우 해당 값들을 options에 추가
    options = []
    if fuzzy_accept:
        for group in fuzzy_accept:
            options.extend(group)
    
    # return_default가 있는 경우 options에 추가
    if return_default:
        options.append(return_default)
    
    # validator가 있는 경우 기본값만 반환 (validator는 ensure_value_completed에서 지원하지 않음)
    if validator:
        return return_default
    
    # ensure_value_completed 호출
    return ensure_value_completed(key_hint=str_working, options=options)
