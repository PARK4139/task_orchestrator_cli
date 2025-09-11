import winreg
import urllib
import undetected_chromedriver as uc
import threading
import shlex
import requests

import pyaudio
import pickle
import numpy as np
import hashlib
import clipboard
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from tkinter import UNDERLINE
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession

from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_printed_once import ensure_printed_once

from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.pk_map_texts import PkTexts
from pathlib import Path
from gtts import gTTS
from datetime import timedelta
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def convert_wav_to_flac(pnx_wav):
    import inspect
    import os
    import subprocess

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    '''테스트 필요'''

    os.system("chcp 65001 >NUL")

    logging.debug(f'from : {pnx_wav}')
    file_edited = f'{os.path.splitext(os.path.basename(pnx_wav))[0]}.flac'
    logging.debug(f'to   : {file_edited}')

    ffmpeg_exe = F_FFMPEG_EXE
    destination = 'storage'
    try:
        os.makedirs(destination)
    except Exception as e:
        pass
    os.chdir(destination)
    logging.debug(f'"{ffmpeg_exe}" -i "{pnx_wav}" -c:a flac "{file_edited}"        를 수행합니다.')
    subprocess.check_output(f'"{ffmpeg_exe}" -i "{pnx_wav}" -c:a flac "{file_edited}"', shell=True)
