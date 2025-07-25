import yt_dlp

import win32com.client
import webbrowser
import undetected_chromedriver as uc
import tqdm
import tomllib
import time
import subprocess
import string
import speech_recognition as sr
import shlex
import requests
import random
import pyautogui
import platform
import paramiko
import os.path
import importlib
import easyocr
import datetime
import colorama
import calendar

from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from paramiko import SSHClient, AutoAddPolicy
from mysql.connector import connect, Error
from dirsync import sync
from datetime import timedelta
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from collections import defaultdict, Counter
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def is_current_hostname(hostname):
    current_hostname = get_hostname()
    pk_print(str_working=rf'''hostname="{hostname}"  {'%%%FOO%%%' if LTA else ''}''')
    pk_print(str_working=rf'''current_hostname="{current_hostname}"  {'%%%FOO%%%' if LTA else ''}''')
    if current_hostname == hostname:
        return 1
    else:
        return 0
