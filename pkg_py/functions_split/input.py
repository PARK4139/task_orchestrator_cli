import sys
import subprocess
import speech_recognition as sr
import secrets
import requests
import pygetwindow
import pyautogui
import pyaudio
import pandas as pd
import os.path
import numpy as np
import keyboard
import easyocr
import colorama
import clipboard
from urllib.parse import urlparse
from typing import TypeVar, List
from telegram import Bot, Update
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from prompt_toolkit.styles import Style
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.press import press

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_context import SpeedControlContext
from pathlib import Path
from gtts import gTTS
from datetime import timedelta
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.functions_split.ensure_printed import ensure_printed


def input(str_working, limit_seconds, return_default, get_input_validated=None):
    return pk_input_v44_uv_theme(str_working, limit_seconds, return_default, get_input_validated)
