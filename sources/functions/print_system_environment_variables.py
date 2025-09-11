import yt_dlp

import win32con
import uuid
import urllib.parse
import urllib
import tomllib
import toml
import timeit
import subprocess
import sqlite3
import shutil
import secrets
import requests
import random
import pywintypes
import pyautogui
import platform
import paramiko
import os, inspect
import numpy as np
import nest_asyncio
import mutagen
import math
import ipdb
import inspect
import importlib
import functools
import clipboard
import chardet

from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import unquote, urlparse, parse_qs
from tkinter import UNDERLINE
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.set_pk_context_state import set_pk_context_state


from sources.objects.encodings import Encoding
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext

from sources.objects.pk_local_test_activate import LTA

from pathlib import Path
from passlib.context import CryptContext
from os import path
from mutagen.mp3 import MP3
from functools import partial
from enum import Enum
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from sources.functions.get_nx import get_nx
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.functions.is_f import is_f

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

from sources.functions.get_d_working import get_d_working


def print_system_environment_variables():
    import sys
    """print 시스템 환경변수 path"""
    from os.path import dirname
    sys.path.insert(0, dirname)
    sys.path.append(r'C:\Python312\Lib\site-packages')
    for i in sys.path:
        print(i)
