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
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern



from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext

from sources.objects.pk_local_test_activate import LTA
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
from sources.functions.get_nx import get_nx
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

from sources.objects.pk_local_test_activate import LTA
import logging


def raise_exception_after_special_charcater_check(value, inspect_currentframe_f_code_co_name,
                                                  ignore_list: [str] = None):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if is_containing_special_characters(value, ignore_list):
        word_english = inspect_currentframe_f_code_co_name
        word_english = word_english.replace('validate_', "")
        word_english = word_english.replace("_", " ")
        word_english = word_english.strip()
        word_korean = get_kor_from_eng(english_word=word_english)
        ment = f"유효한 {word_korean}이(가) 아닙니다. 특수문자가 없어야 합니다 {value}"
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=ment)
