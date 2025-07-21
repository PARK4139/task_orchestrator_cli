import zlib
# import win32process
# import win32gui
import win32con
import win32com.client
import webbrowser
import urllib
import undetected_chromedriver as uc
import traceback
import tomllib
import toml
import timeit
import threading
import socket
import shutil
import shlex
import secrets
import requests
import re
import pywintypes
import pythoncom
import pyglet
import pygetwindow
import psutil
import platform
import pickle
import pandas as pd
import mysql.connector
import mutagen
import json
import inspect
import hashlib
import easyocr
import datetime
import cv2
import colorama
import calendar
import asyncio
from zipfile import BadZipFile
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_100_performance_logic import pk_measure_seconds, pk_measure_memory
from pkg_py.pk_system_layer_100_os import is_os_windows
from pathlib import Path
from passlib.context import CryptContext
from gtts import gTTS
from functools import partial as functools_partial
from functools import lru_cache
from enum import Enum
from datetime import timedelta
from datetime import datetime, time
from datetime import datetime
from datetime import date
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def ensure_jetson_setup():
    download_jetson_setup()
    exec_jetson_up()
