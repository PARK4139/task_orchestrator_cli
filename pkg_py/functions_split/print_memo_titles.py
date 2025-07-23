import zlib
import yt_dlp
import winreg
# import win32process
import win32con
import uuid
import urllib.parse
import undetected_chromedriver as uc
import traceback
import tomllib
import tomllib
import toml
import time
import threading
import tarfile
import string
import socket, time
import secrets
import requests
import random
import pyaudio
import psutil
import platform
import pickle
import numpy as np
import nest_asyncio
import ipdb
import inspect
import importlib
import datetime
import cv2
import clipboard
import asyncio
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_print_once import pk_print_once

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.directories import D_WORKING
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated
from passlib.context import CryptContext
from os.path import dirname
from os import path
from functools import partial as functools_partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from datetime import timedelta
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def print_memo_titles(f):
    # todo
    lines_list = get_line_list_to_include_search_keyword(f=f, search_keywords=["[todo]"])
    lines_list = get_list_removed_element_startswith_str(working_list=lines_list, string="#")
    liens_str = get_str_from_list(working_list=lines_list, item_connector='')

    highlight_config_dict = {
        "bright_red": [
            f'{' %%%FOO%%% ' if LTA else ''}'
        ],
        "white": [
            '[todo]'
        ],
    }
    print_highlighted(txt_whole=liens_str, highlight_config_dict=highlight_config_dict)
