import winreg
# import win32gui
import uuid
import tomllib
import threading
import tarfile
import sqlite3
import speech_recognition as sr
import socket
import secrets
import re
import random
import pyglet
import pyautogui
import os.path
import keyboard
import json
import importlib
import chardet
import calendar
import asyncio
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pytube import Playlist
from prompt_toolkit.styles import Style
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_100_os import is_os_windows

from pathlib import Path
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial as functools_partial
from functools import lru_cache
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from collections import Counter
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux

from pkg_py.simple_module.part_014_pk_print import pk_print


def is_sql_injection_safe_simply(data: str):
    import re

    sql_pattern = r"(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|TRUNCATE|GRANT|REVOKE)"
    match = re.search(sql_pattern, data, re.IGNORECASE)
    if match:
        return 0
    return 1
