import zipfile
import yt_dlp


import win32con
import win32con
import webbrowser
import uuid
import timeit
import sys
import string
import shutil


import psutil
import os
import math
import importlib
import hashlib
import colorama
from yt_dlp import YoutubeDL
from urllib.parse import quote
from tkinter import UNDERLINE
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from queue import Queue, Empty
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession

from sources.functions.does_pnx_exist import is_pnx_existing
import logging
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_local_test_activate import LTA
from mutagen.mp3 import MP3
from functools import lru_cache
from datetime import date
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from bs4 import ResultSet
from base64 import b64encode
from base64 import b64decode
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

from sources.objects.pk_local_test_activate import LTA
import logging


def print_function_info(thing_curious):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    logging.debug(f"{inspect.currentframe().f_code.co_name} {str(thing_curious.__code__.co_varnames)}")
    print(help(thing_curious))
    logging.debug(f'# of the Arguments : {thing_curious.__code__.co_argcount}')
    # logging.debug(f'Name of the Arguments : {thing_curious.__code__.co_varnames}')
    logging.debug("┌>print via getsource s")
    print(inspect.getsource(thing_curious))
    logging.debug("└>print via getsource e")
