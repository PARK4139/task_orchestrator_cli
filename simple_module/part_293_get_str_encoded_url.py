import winreg
# import win32gui
import win32con
import uuid
import urllib
import undetected_chromedriver as uc
import toml
import sys
import shlex
import pythoncom
import pyaudio
import numpy as np
import nest_asyncio
import ipdb
import inspect
import easyocr
import cv2
import chardet
import calendar
from yt_dlp import YoutubeDL
from urllib.parse import quote
from tkinter import UNDERLINE
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
from pynput import mouse
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_800_print_util import print_red

from PIL import Image
from pathlib import Path
from os import path
from functools import partial as functools_partial
from enum import Enum
from datetime import timedelta
from datetime import datetime
from datetime import date
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def get_str_encoded_url(str_working):
    import urllib
    from urllib.parse import quote
    return urllib.parse.quote(f"{str_working}")
