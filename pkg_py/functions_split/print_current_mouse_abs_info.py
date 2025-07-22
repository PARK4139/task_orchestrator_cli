import win32com.client
import undetected_chromedriver as uc
import traceback
import tomllib
import tomllib
import toml
import timeit
import sqlite3
import socket, time
import socket
import shutil
import requests
import pythoncom
import psutil
import paramiko
import os, inspect
import mysql.connector
import mutagen
import math
import json
import ipdb
import hashlib
import functools
import datetime
import cv2
import chardet
import calendar
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated
from PIL import Image, ImageFilter
from os.path import dirname
from moviepy import VideoFileClip
from functools import partial
from functools import lru_cache
from enum import Enum
from dirsync import sync
from datetime import datetime, time
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.is_os_windows import is_os_windows

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def print_current_mouse_abs_info():
    import inspect

    import ipdb
    func_n = inspect.currentframe().f_code.co_name
    x, y = get_current_mouse_abs_info()
    pk_print(f'''x="{x}"''')
    pk_print(f'''y="{y}"''')

    ipdb.set_trace()
