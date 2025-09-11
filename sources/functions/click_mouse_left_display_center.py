import winreg

import urllib
import undetected_chromedriver as uc
import traceback
import tqdm
import timeit
import tarfile
import string
import socket
import secrets
import random
import pywintypes
import pyglet
import psutil
import platform
import pandas as pd
import os.path
import os
import inspect
import importlib
import chardet
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from pytube import Playlist
from PySide6.QtWidgets import QApplication


from sources.functions.get_d_working import get_d_working
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_state_via_context import SpeedControlContext

from pathlib import Path
from os.path import dirname
from moviepy import VideoFileClip
from gtts import gTTS
from functools import lru_cache
from enum import Enum
from datetime import datetime, timedelta
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from collections import Counter
from base64 import b64encode
from base64 import b64decode

from pathlib import Path
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def click_mouse_left_display_center():
    import pyautogui
    screen_w, screen_h = pyautogui.size()
    center_x = screen_w // 2
    center_y = screen_h // 2
    ensure_mouse_moved(x_abs=center_x, y_abs=center_y)
    click_mouse_left_btn(x_abs=center_x, y_abs=center_y)
