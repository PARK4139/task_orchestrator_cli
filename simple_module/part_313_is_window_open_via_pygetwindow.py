# import win32process
# import win32gui
import win32com.client
import webbrowser
import urllib.parse
import traceback
import tqdm
import tomllib
import subprocess
import string
import sqlite3
import shutil
import secrets
import random
import pywintypes
import paramiko
import mysql.connector
import ipdb
import clipboard
from zipfile import BadZipFile
from typing import TypeVar, List
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated
from PIL import Image
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from os import path
from functools import partial as functools_partial
from functools import partial
from cryptography.hazmat.primitives import padding
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def is_window_open_via_pygetwindow(window_title):
    import pygetwindow
    windows = pygetwindow.getAllTitles()  # 모든 열린 창들의 제목을 가져옴
    return window_title in windows  # 특정 창이 열려 있는지 확인
