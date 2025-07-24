# import win32process
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
import pyaudio
import pandas as pd
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
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.get_list_calculated import get_list_calculated
from gtts import gTTS
from dirsync import sync
from datetime import datetime, time
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from base64 import b64decode
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.pk_print import pk_print


def is_target_type_str(target):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    if isinstance(target, str):
        return 1
    else:
        return 0
