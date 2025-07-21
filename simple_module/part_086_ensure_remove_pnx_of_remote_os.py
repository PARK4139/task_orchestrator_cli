import winreg
# import win32process
# import win32gui
import win32con
import uuid
import urllib.parse
import urllib
import tqdm
import toml
import toml
import timeit
import threading
import tarfile
import socket
import requests
import re
import random
import pywintypes
# import pywin32
import platform
import paramiko
import os.path
import numpy as np
import mysql.connector
import json
import ipdb
import inspect
import hashlib
import functools
import easyocr
import colorama
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from PIL import Image, ImageFilter
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from enum import Enum
from dirsync import sync
from datetime import datetime
from datetime import date
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def ensure_remove_pnx_of_remote_os(pnx, **config_remote_os):
    std_out_list, std_err_list = cmd_to_remote_os(cmd=f"rm -rf {pnx}", **config_remote_os)
    std_out_list, std_err_list = cmd_to_remote_os(cmd=f"ls {pnx}", **config_remote_os)
    signiture = 'todo'
    for std_out in std_out_list:
        if signiture in std_out:
            pk_print(f'''remove {pnx} at {config_remote_os['ip']}  {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        else:
            pk_print(f'''remove {pnx} at {config_remote_os['ip']}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            raise
