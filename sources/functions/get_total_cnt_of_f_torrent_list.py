import zipfile
import winreg

import win32con
import uuid
import urllib
import traceback
import tqdm
import toml
import toml
import timeit
import time
import threading
import tarfile
import sys
import subprocess, time
import subprocess
import sqlite3
import socket
import re
import random, math

import pythoncom
import pyglet
import pygetwindow
import pyautogui
import pyaudio
import os
import numpy as np
import mysql.connector
import math
import keyboard
import importlib
import clipboard
import chardet
import calendar

import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import quote
from typing import TypeVar, List
from tkinter import UNDERLINE
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from pytube import Playlist
from prompt_toolkit.styles import Style
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern


from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_printed_once import ensure_printed_once
import logging

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared


from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_database import PkSqlite3DB

from pathlib import Path
from passlib.context import CryptContext
from gtts import gTTS
from functools import lru_cache
from enum import Enum
from datetime import date
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from base64 import b64encode
from base64 import b64decode

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING, D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


def get_total_cnt_of_f_torrent_list(h3_text):
    import re
    total_cnt_of_f_torrent_list = None
    logging.debug(f'''h3_text={h3_text}  {'%%%FOO%%%' if LTA else ''}''')
    match = re.search(r"\((\d+)\)", h3_text)
    if match:
        matched_group = match.group(1)  # 첫 번째 캡처 그룹 (숫자) 반환
        logging.debug(f'''matched_group={matched_group}  {'%%%FOO%%%' if LTA else ''}''')
        total_cnt_of_f_torrent_list = int(matched_group)
        logging.debug(f'''total_cnt_of_f_torrent_list={total_cnt_of_f_torrent_list}  {'%%%FOO%%%' if LTA else ''}''')
    return total_cnt_of_f_torrent_list
