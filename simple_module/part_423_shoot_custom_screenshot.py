import yt_dlp
# import win32process
# import win32gui
import urllib
import tomllib
import time
import socket
import shlex
# import pywin32
import paramiko
import os
import numpy as np
import importlib
import easyocr
import cv2
import colorama
import browser_cookie3
from zipfile import BadZipFile
from telethon import TelegramClient, events
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pathlib import Path
from mutagen.mp3 import MP3
from dirsync import sync
from dataclasses import dataclass
from base64 import b64encode
from base64 import b64decode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux

from pkg_py.simple_module.part_330_get_d_working import get_d_working


def shoot_custom_screenshot():
    import asyncio
    asyncio.run(shoot_custom_screenshot_via_asyncio())
