import zipfile
# import win32process
import win32con
import win32com.client
import uuid
import urllib
import undetected_chromedriver as uc
import tomllib
import toml
import sys
import subprocess, time
import subprocess
import requests
import pywintypes
import pythoncom
import pyglet
import pygetwindow
import pyautogui
import psutil
import numpy as np
import ipdb
import importlib
import hashlib
import functools
import colorama
import chardet
import calendar
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import quote
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

from pathlib import Path
from passlib.context import CryptContext
from os import path
from moviepy import VideoFileClip
from functools import partial
from dirsync import sync
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

from pkg_py.simple_module.part_014_pk_print import pk_print


def get_text_coordinates_via_easy_ocr(string):  # 한글인식 잘 안되는 듯하다
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    # 화면 캡처
    screenshot = get_screenshot()

    # EsayOCR을 통해 모든텍스트 바운딩박스좌표 추출
    # coordinates_bounding_box=get_all_text_with_coordinates_via_easy_ocr(screenshot)
    # print_list_as_vertical(working_list=coordinates_bounding_box, items_name="coordinates_bounding_box")

    # EsayOCR을 통해 특정텍스트 바운딩박스좌표 추출
    coordinates_bounding_box = get_coordinates_bounding_box(image=screenshot, str_working=string)
    # print_list_as_vertical(working_list=coordinates_bounding_box, items_name="coordinates_bounding_box")

    # 중심 좌표 구하기
    if get_center_of_bounding_box(coordinates_bounding_box) is not None:
        center_x, center_y = get_center_of_bounding_box(coordinates_bounding_box)
        # pk_print(str_working=rf'''center_x="{center_x}"  {'%%%FOO%%%' if LTA else ''}''')
        # pk_print(str_working=rf'''center_y="{center_y}"  {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''"text_coordinates=({center_x}, {center_y})"''')
        return center_x, center_y
    return None
