import zlib
import winreg
import urllib
import traceback
import tomllib
import tomllib
import timeit
import time
import threading
import tarfile
import sys
import subprocess, time
import string
import sqlite3
import speech_recognition as sr
import shutil
# import pywin32
import pythoncom
import pyglet
import pyaudio
import psutil
import platform
import pandas as pd
import os.path
import os, inspect
import numpy as np
import nest_asyncio
import mysql.connector
import json
import ipdb
import hashlib
import easyocr
import datetime
import cv2
import colorama
import chardet
import calendar
from urllib.parse import urlparse
from urllib.parse import quote, urlparse
from urllib.parse import quote
from selenium.webdriver.chrome.options import Options
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from functools import partial
from functools import lru_cache
from dirsync import sync
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from colorama import init as pk_colorama_init
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def move_f_list_by_category(categorized, base_p="."):
    import os
    import shutil
    for category, f_nx_list in categorized.items():
        if category == "기타":
            continue
        d_n = category.replace(" ", "_")
        category_d = os.path.join(base_p, d_n)
        os.makedirs(category_d, exist_ok=True)
        for f_nx in f_nx_list:
            src = os.path.join(base_p, f_nx)
            dst = os.path.join(category_d, f_nx)
            if os.path.exists(src):
                shutil.move(src, dst)
