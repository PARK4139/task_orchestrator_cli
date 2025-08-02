import zlib
import win32com.client
import uuid
import traceback
import tomllib
import tomllib
import toml
import time
import sys
import socket, time
import shlex
import re
import random, math

import pyaudio
import pickle
import pandas as pd
import numpy as np
import nest_asyncio
import keyboard
import ipdb
import importlib
import functools
import calendar
from urllib.parse import quote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.get_list_calculated import get_list_calculated
from pathlib import Path
from os import path
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from datetime import datetime
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS, D_PKG_PKL, D_PKG_PY
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def get_list_included(working_list, include_element):
    pnx_filtered_list = []
    for item in working_list:
        if include_element in item:
            pnx_filtered_list.append(item)
    return pnx_filtered_list
