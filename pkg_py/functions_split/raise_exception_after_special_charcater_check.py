import zlib
import zipfile

import win32con
import webbrowser
import uuid
import urllib
import undetected_chromedriver as uc
import traceback
import tomllib
import tomllib
import toml
import toml
import timeit
import threading
import subprocess, time
import socket, time
import socket
import shutil
import re
import random, math
import pywintypes
            

import pythoncom
import pyglet
import pyautogui
import pyaudio
import psutil
import platform
import pickle
import os.path
import numpy as np
import nest_asyncio
import mysql.connector
import mutagen
import math
import keyboard
import json
import ipdb
import inspect
import hashlib
import easyocr
import cv2
import colorama
import colorama
import chardet
import calendar

from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import quote, urlparse
from urllib.parse import quote
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.press import press
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from datetime import timedelta
from datetime import datetime, time
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import ResultSet
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def raise_exception_after_special_charcater_check(value, inspect_currentframe_f_code_co_name,
                                                  ignore_list: [str] = None):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    if is_containing_special_characters(value, ignore_list):
        word_english = inspect_currentframe_f_code_co_name
        word_english = word_english.replace('validate_', "")
        word_english = word_english.replace("_", " ")
        word_english = word_english.strip()
        word_korean = get_kor_from_eng(english_word=word_english)
        ment = f"유효한 {word_korean}이(가) 아닙니다. 특수문자가 없어야 합니다 {value}"
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=ment)
