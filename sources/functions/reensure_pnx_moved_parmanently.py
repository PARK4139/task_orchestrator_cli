import zlib
import zipfile
import winreg


import webbrowser
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tomllib
import tomllib
import toml
import timeit
import subprocess
import string
import sqlite3
import speech_recognition as sr
import socket
import shutil
import secrets
import pywintypes


import pythoncom
import paramiko
import os.path
import os
import numpy as np
import nest_asyncio
import mysql.connector
import mutagen
import inspect
import importlib
import functools
import cv2
import colorama
import clipboard
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote, urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit.styles import Style
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front


from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_state_printed import ensure_state_printed
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext


from PIL import Image, ImageFilter
from PIL import Image
from pathlib import Path
from os.path import dirname
from os import path
from gtts import gTTS
from functools import lru_cache
from enum import Enum
from dirsync import sync
from datetime import timedelta
from datetime import datetime, time
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from sources.functions.get_nx import get_nx

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided

from sources.objects.pk_etc import PK_UNDERLINE
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.is_os_windows import is_os_windows
from sources.objects.pk_local_test_activate import LTA
import logging

from sources.objects.pk_local_test_activate import LTA
import logging


def reensure_pnx_moved_parmanently(pnx):
    import inspect
    import os
    import platform
    import shutil
    import traceback

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if platform.system() == 'Windows':
        try:
            if validate_and_return(value=pnx) is not False:
                os.chdir(os.path.dirname(pnx))
                if os.path.exists(pnx):
                    if is_d(pnx):
                        # shutil.rmtree(pnx_todo)
                        # if is_d(pnx_todo):
                        #     run_via_cmd_exe(rf'echo y | rmdir /s "{pnx_todo}"')
                        ensure_pnxs_move_to_recycle_bin(pnx)
                    elif is_f(pnx):
                        # os.remove(pnx_todo)
                        # if is_f(pnx_todo):
                        #     run_via_cmd_exe(rf'echo y | del /f "{pnx_todo}"')
                        ensure_pnxs_move_to_recycle_bin(pnx)

                    # logging.debug(f"{'%%%FOO%%%' if LTA else ''} green {texts}")
                    # logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
        except:
            logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")

        finally:
            os.chdir(D_TASK_ORCHESTRATOR_CLI)
    else:
        from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()
        try:
            if validate_and_return(value=pnx) is not False:
                os.chdir(os.path.dirname(pnx))
                if os.path.exists(pnx):
                    if is_d(pnx):
                        shutil.rmtree(pnx)
                    elif is_f(pnx):
                        os.remove(pnx)
        except:
            logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")

        finally:
            os.chdir(D_TASK_ORCHESTRATOR_CLI)
