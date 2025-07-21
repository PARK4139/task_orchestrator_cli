

import zipfile
import winreg
# import win32process
import win32con
import win32com.client
import undetected_chromedriver as uc
import tqdm
import tomllib
import toml
import timeit
import time
import string
import speech_recognition as sr
import random
# import pywin32
import pythoncom
import pyglet
import platform
import paramiko
import os
import mysql.connector
import json
import hashlib
import clipboard
import browser_cookie3
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from pynput import mouse
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_100_performance_logic import pk_measure_seconds, pk_measure_memory
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated
from PIL import Image, ImageFilter
from pathlib import Path
from passlib.context import CryptContext
from os import path
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import partial
from fastapi import HTTPException
from dirsync import sync
from Cryptodome.Cipher import AES
from base64 import b64encode
from base64 import b64decode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.pk_system_layer_etc import PkFilter, PK_UNDERLINE
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def get_pk_system_process_nx_list():
    # from pkg_py.pk_system_layer_100_files_and_directories_logic import get_pnx_os_style, get_nx, get_pnx_list
    # from pkg_py.pk_system_layer_100_list_logic import get_list_calculated
    # from pkg_py.pk_system_layer_directories import D_PKG_PY
    nx_filtered = []
    pnx_list = get_pnx_list(d_working=D_PKG_PY, with_walking=0)
    pnx_to_except = [rf"{D_PKG_PY}/__init__.py", f"{D_PKG_PY}/__pycache__"]
    pnx_to_except = [get_pnx_os_style(element) for element in pnx_to_except]
    pnx_excepted = get_list_calculated(origin_list=pnx_list, minus_list=pnx_to_except)
    for pnx in pnx_excepted:
        filename = get_nx(pnx)
        if filename.startswith("pk_"):
            # print(filename)
            nx_filtered.append(filename)
    return nx_filtered
