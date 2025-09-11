import win32con
import webbrowser
import uuid
import urllib
import undetected_chromedriver as uc
import traceback
import tomllib
import timeit
import time
import shutil
import re

import pyglet
import pyautogui
import pickle
import os
import numpy as np
import mysql.connector
import mutagen
import math
import json
import hashlib
import cv2
import chardet

from zipfile import BadZipFile
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical

from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING

from sources.objects.pk_state_via_database import PkSqlite3DB

from PIL import Image
from gtts import gTTS
from functools import lru_cache
from enum import Enum
from datetime import date
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from collections import Counter
from base64 import b64decode
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from pathlib import Path
from sources.functions.is_d import is_d
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.objects.pk_local_test_activate import LTA


def check_root_right():
    # root 권한 검사
    import os
    if os.geteuid() != 0:
        return False
    return True
