import zipfile
import winreg
import urllib
import tqdm
import toml
import tarfile
import sys
import string
import socket
import secrets
import pyglet
import pandas as pd
import os.path
import keyboard
import json
import ipdb
import inspect
import importlib
import datetime
import cv2
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from prompt_toolkit.styles import Style
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pathlib import Path
from passlib.context import CryptContext
from fastapi import HTTPException
from dirsync import sync
from datetime import timedelta
from datetime import datetime, time
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from collections import Counter
from bs4 import ResultSet
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.get_d_working import get_d_working


def merge_pnx_list_via_text_file():
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    f_func_n_txt = rf'{D_PROJECT}\pkg_txt\{func_n}.txt'
    ensure_pnx_made(pnx=f_func_n_txt, mode="f")
    # if not is_window_opened(window_title=f_func_n_txt):
    #     open_pnx(f_func_n_txt, debug_mode=True)
    pnxs = get_list_from_f(f=f_func_n_txt)
    merge_d_list(d_list=pnxs)
