
import win32con
import uuid
import traceback
import tqdm
import subprocess, time
import string
import speech_recognition as sr
import shlex
import secrets
import random

import pythoncom
import pyaudio
import nest_asyncio
import math
import ipdb
import hashlib
import datetime
import calendar
from seleniumbase import Driver
from selenium.webdriver.chrome.options import Options
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
# pk_#
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.directories  import D_PROJECT
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.local_test_activate import LTA

from passlib.context import CryptContext
from os.path import dirname
from mutagen.mp3 import MP3
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs


def get_dict_merged(dict_1, dict_2):
    # todo  dict + dict
    pass
