
import win32con
import win32con
import tqdm
import tomllib
import threading
import string
import sqlite3
import speech_recognition as sr
import shlex
import random
import pythoncom
import pygetwindow
# import pyaudio
# import pandas as pd
import numpy as np
import nest_asyncio
import inspect
import hashlib
import datetime
import colorama
import clipboard
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from typing import TypeVar, List
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from prompt_toolkit import PromptSession
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical

from sources.functions.is_window_title_front import is_window_title_front
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.pk_local_test_activate import LTA

from gtts import gTTS
from dirsync import sync
from datetime import datetime, time
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from base64 import b64decode
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
import logging


def is_target_type_str(target):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if isinstance(target, str):
        return 1
    else:
        return 0
