import winreg
# import win32gui
import urllib
import traceback
import tqdm
import toml
import subprocess
import shlex
import requests
import random, math
import random
import pywintypes
import pythoncom
import pygetwindow
import pyautogui
import pyaudio
import pandas as pd
import os
import numpy as np
import nest_asyncio
import mysql.connector
import inspect
import importlib
import hashlib
import easyocr
import cv2
from urllib.parse import urlparse
from urllib.parse import quote
from telegram import Bot, Update
from selenium.webdriver.support import expected_conditions as EC
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pathlib import Path
from paramiko import SSHClient, AutoAddPolicy
from moviepy import VideoFileClip
from dirsync import sync
from datetime import timedelta
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import ResultSet
from base64 import b64decode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def ensure_remove_and_make_remote_d(d, config_remote_os):
    # remove d
    ensure_remove_pnx_of_remote_os(d=d, **config_remote_os)

    # make d
    std_out_list, std_err_list = cmd_to_remote_os(d=f"mkdir -p {d}", **config_remote_os)
    for std_out in std_out_list:
        pk_print(working_str=rf'''std_out={std_out}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        raise
