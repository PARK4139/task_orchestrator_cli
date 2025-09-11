
import win32com.client
import webbrowser
import uuid
import urllib.parse
import time
import sys
import sqlite3
import shutil
import secrets
import requests
import pywintypes
import pyglet
import pyautogui
import paramiko
import numpy as np
import mutagen
import ipdb
import datetime
import cv2
import chardet

import asyncio
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from PySide6.QtWidgets import QApplication

from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical


from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_local_test_activate import LTA

from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from gtts import gTTS
from functools import lru_cache
from Cryptodome.Cipher import AES
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.objects.pk_local_test_activate import LTA

import logging


def set_data_to_f_toml(data, f):
    import toml
    with open(f, "w") as f_obj:
        toml.dump(data, f_obj)
