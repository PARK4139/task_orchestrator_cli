import zlib

import win32con
import webbrowser
import uuid
import urllib
import tomllib
import toml
import subprocess
import shutil
import secrets
import pywintypes


import pythoncom
import pyglet
import pyautogui
import psutil
import platform
import pandas as pd
import numpy as np
import inspect
import colorama
import asyncio
from webdriver_manager.chrome import ChromeDriverManager
from telegram import Bot, Update
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories_reuseable import D_PROJECT

from PIL import Image, ImageFilter
from PIL import Image
from os.path import dirname
from os import path
from gtts import gTTS
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from dataclasses import dataclass
from collections import defaultdict, Counter
from collections import Counter
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_d_working import get_d_working


def get_set_differenced(set_a, set_b):
    return get_difference_set(set_a, set_b)
