import winreg
import urllib
import undetected_chromedriver as uc
import threading
import shlex
import requests
# import pywin32
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
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pathlib import Path
from gtts import gTTS
from datetime import timedelta
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def convert_wav_to_flac(pnx_wav):
    import inspect
    import os
    import subprocess

    func_n = inspect.currentframe().f_code.co_name

    '''테스트 필요'''

    os.system("chcp 65001 >nul")

    pk_print(f'from : {pnx_wav}', print_color='blue')
    file_edited = f'{os.path.splitext(os.path.basename(pnx_wav))[0]}.flac'
    pk_print(f'to   : {file_edited}', print_color='blue')

    ffmpeg_exe = F_FFMPEG_EXE
    destination = 'storage'
    try:
        os.makedirs(destination)
    except Exception as e:
        pass
    pk_chdir(destination)
    pk_print(f'"{ffmpeg_exe}" -i "{pnx_wav}" -c:a flac "{file_edited}"        를 수행합니다.', print_color='blue')
    subprocess.check_output(f'"{ffmpeg_exe}" -i "{pnx_wav}" -c:a flac "{file_edited}"', shell=True)
