# import win32gui
import undetected_chromedriver as uc
import tqdm
import timeit
import time
import shutil
import requests
import pywintypes
import pyglet
import pyaudio
import psutil
import os
import numpy as np
import ipdb
import inspect
import functools
import colorama
import calendar
import asyncio
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit import PromptSession
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.pk_print_once import pk_print_once

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_FFMPEG_EXE

from PIL import Image
from mutagen.mp3 import MP3
from enum import Enum
from datetime import datetime, time
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.get_d_working import get_d_working


def is_aifw_running():
    # cmd_to_remote_os(jetpack version)
    todo('%%%FOO%%%')
