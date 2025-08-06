import winreg


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
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
# pk_#
# pk_#
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.map_massages import PkMessages2025
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
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided

from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def ensure_reensure_pnx_moved_of_remote_os(pnx, **config_remote_os):
    std_out_list, std_err_list = cmd_to_remote_os(cmd=f"rm -rf {pnx}", **config_remote_os)
    std_out_list, std_err_list = cmd_to_remote_os(cmd=f"ls {pnx}", **config_remote_os)
    signiture = 'todo'
    for std_out in std_out_list:
        if signiture in std_out:
            ensure_printed(f'''remove {pnx} at {config_remote_os['ip']}  {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        else:
            ensure_printed(f'''remove {pnx} at {config_remote_os['ip']}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            raise
