import winreg

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



from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.does_pnx_exist import is_pnx_existing
import logging
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.pk_map_texts import PkTexts


from pathlib import Path
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial as functools_partial
from functools import lru_cache
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from collections import Counter

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from pathlib import Path
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux

import logging


def is_sql_injection_safe_simply(data: str):
    import re

    sql_pattern = r"(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|TRUNCATE|GRANT|REVOKE)"
    match = re.search(sql_pattern, data, re.IGNORECASE)
    if match:
        return 0
    return 1
