

import zipfile
import winreg
# import win32process
import win32con
import urllib.parse
import traceback
import subprocess
import socket
import shlex
import re
import random
# import pywin32
import pyautogui
import psutil
import os.path
import nest_asyncio
import importlib
import colorama
import chardet
from yt_dlp import YoutubeDL
from telegram import Bot, Update
from selenium.webdriver.common.by import By
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_100_os import is_os_windows
from pathlib import Path
from moviepy import VideoFileClip
from datetime import timedelta
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.simple_module.part_014_pk_print import pk_print


def get_available_pk_python_program_pnx(pk_idx):
    # from pkg_py.pk_system_layer_100_etc import get_pk_system_process_pnx_and_idx_dict
    pk_pnx_working_with_idx_dict = get_pk_system_process_pnx_and_idx_dict()
    pk_python_program_pnx_working = pk_pnx_working_with_idx_dict[pk_idx]
    return pk_python_program_pnx_working
