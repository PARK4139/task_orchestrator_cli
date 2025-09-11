

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


from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.encodings import Encoding

from sources.objects.pk_local_test_activate import LTA

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
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path

from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
import logging

import logging
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


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
    logging.debug("Table nyaa_magnets ready")
