# import win32process
# import win32gui
import tomllib
import toml
import toml
import timeit
import time
import string
import sqlite3
import speech_recognition as sr
import socket, time
import shutil
import requests
import random
import pywintypes
# import pywin32            
# import pywin32
import pyaudio
import pickle
import pandas as pd
import os.path
import os, inspect
import nest_asyncio
import math
import keyboard
import datetime
import colorama
import colorama
from typing import TypeVar, List
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.pk_system_object.local_test_activate import LTA

from pathlib import Path
from os import path
from enum import Enum
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def ensure_create_table():
    #
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS nyaa_magnets (
      id INT AUTO_INCREMENT PRIMARY KEY,
      magnet TEXT UNIQUE,
      title VARCHAR(255),
      loaded TINYINT(1) DEFAULT 0,
      collected_at DATETIME DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB CHARSET=utf8mb4;
    """
    )
    conn.commit()
    cur.close()
    conn.close()
    pk_print("Table nyaa_magnets ready")
