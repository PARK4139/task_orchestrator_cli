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

from sources.functions.get_historical_list import get_historical_list
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
import logging
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.objects.pk_etc import PkFilter

from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING

from sources.objects.pk_state_via_database import PkSqlite3DB
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

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def is_current_hostname(hostname):
    current_hostname = get_hostname()
    logging.debug(rf'''hostname="{hostname}"  {'%%%FOO%%%' if LTA else ''}''')
    logging.debug(rf'''current_hostname="{current_hostname}"  {'%%%FOO%%%' if LTA else ''}''')
    if current_hostname == hostname:
        return 1
    else:
        return 0
