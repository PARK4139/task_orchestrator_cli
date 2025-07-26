import winreg

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
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_context import SpeedControlContext
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
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def ensure_remove_and_make_remote_d(d, config_remote_os):
    # remove d
    ensure_remove_pnx_of_remote_os(d=d, **config_remote_os)

    # make d
    std_out_list, std_err_list = cmd_to_remote_os(d=f"mkdir -p {d}", **config_remote_os)
    for std_out in std_out_list:
        ensure_printed(str_working=rf'''std_out={std_out}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        raise
