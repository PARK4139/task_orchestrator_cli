import zlib
import zipfile
import yt_dlp
import winreg

import win32com.client
import uuid
import tqdm
import toml
import toml
import timeit
import time
import threading
import tarfile
import speech_recognition as sr

import pythoncom
import pygetwindow
import platform
import pickle
import os.path
import nest_asyncio
import mysql.connector
import mutagen
import keyboard
import easyocr
import asyncio
from zipfile import BadZipFile
from urllib.parse import unquote, urlparse, parse_qs
from telegram import Bot, Update
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style

from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_printed_once import ensure_printed_once
import logging

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding


from sources.objects.pk_local_test_activate import LTA

from PIL import Image
from passlib.context import CryptContext
from os import path
from moviepy import VideoFileClip
from functools import partial as functools_partial
from fastapi import HTTPException
from enum import Enum
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from bs4 import ResultSet
from sources.functions.get_nx import get_nx

from sources.objects.pk_etc import PK_UNDERLINE
from pathlib import Path
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.objects.pk_local_test_activate import LTA
import logging

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def input_v1(str_working, limit_seconds, return_default, get_input_validated=None):
    import sys
    import threading
    import time
    from queue import Queue, Empty

    logging.debug(f'''str_working={str_working} {'%%%FOO%%%' if LTA else ''}''')
    logging.debug(f'''limit_seconds={limit_seconds} {'%%%FOO%%%' if LTA else ''}''')
    logging.debug(f'''return_default={return_default} {'%%%FOO%%%' if LTA else ''}''')
    logging.debug(f'''get_input_validated={get_input_validated} {'%%%FOO%%%' if LTA else ''}''')
    input_queue = Queue()

    def read_input():
        try:
            user_input = sys.stdin.readline()
            input_queue.put(user_input.strip())
        except Exception as e:
            input_queue.put(None)

    input_thread = threading.Thread(target=read_input, daemon=True)
    input_thread.start()

    start_time = time.time()
    remaining = limit_seconds

    try:
        while remaining > 0:
            user_input = ""
            try:
                user_input = input_queue.get(timeout=1)
                print()  # 줄 바꿈
                if get_input_validated and not get_input_validated(user_input):
                    logging.debug("[RETRY] 유효하지 않은 입력입니다. 다시 시도해주세요.")
                    return pk_input(str_working, limit_seconds, return_default, get_input_validated)
                return user_input
            except Empty:
                remaining = limit_seconds - int(time.time() - start_time)
                print(f"\r remaining seconds : {remaining:2d} {str_working}{user_input}", end="", flush=True)
        print()  # 줄 바꿈 (시간 초과 시)
        logging.debug(f"[TIMEOUT] 입력 시간 초과 → 기본값 반환: {return_default}")
        return return_default

    except KeyboardInterrupt:
        print()  # 줄 바꿈
        logging.debug("[INTERRUPT] 사용자 입력 취소됨 → 기본값 반환")
        return return_default
