import zipfile

import win32con
import win32com.client
import urllib
import tqdm
import tomllib
import shlex
import secrets
import random, math
import random
import pyglet
import pyautogui
import platform
import os.path
import os
import mutagen
import json
import ipdb
import functools
import datetime
import cv2
import colorama
import asyncio
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from queue import Queue, Empty
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA

from pathlib import Path
from passlib.context import CryptContext
from gtts import gTTS
from functools import partial
from enum import Enum
from dirsync import sync
from datetime import datetime
from datetime import date
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def ensure_file_contents_filled_with_auto_no_option2(template_str: str, word_monitored: str, auto_cnt_starting_no=0):
    """
    input
    --------
    -----1--
    ---1----
    ---1----
    -------1
    ouput
    --------
    -----1--
    ---2----
    ---3----
    -------4
    """
    line_splited_by_word_monitored_list = template_str.split(word_monitored)

    line_list_filtered = []
    for index, line_splited_by_word_monitored in enumerate(line_splited_by_word_monitored_list):
        if index != len(line_splited_by_word_monitored_list) - 1:
            line_list_filtered.append(line_splited_by_word_monitored + str(auto_cnt_starting_no))
            auto_cnt_starting_no = auto_cnt_starting_no + 1
        else:
            line_list_filtered.append(line_splited_by_word_monitored)
    lines_new_as_str = "".join(line_list_filtered)
    return lines_new_as_str
