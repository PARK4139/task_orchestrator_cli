import zlib
# import win32process
import webbrowser
import traceback
import toml
import toml
import timeit
import time
import random
import pywintypes
# import pywin32
import pyaudio
import platform
import cv2
import colorama
import browser_cookie3
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from tkinter import UNDERLINE
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_100_os import is_os_windows, is_os_wsl_linux
from passlib.context import CryptContext
from moviepy import VideoFileClip
from functools import partial as functools_partial
from datetime import datetime
from Cryptodome.Cipher import AES
from collections import Counter
from base64 import b64encode
from base64 import b64decode
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def click_string(string, doubleclick_mode=False):
    import time
    time_limit = 20
    time_s = time.time()
    while 1:
        # pk_print(str_working=time.time() - time_s)
        if time.time() - time_s > time_limit:
            break
        if does_text_bounding_box_exist_via_easy_ocr(string=string):
            break
        pk_sleep(seconds=0.5)
    click_mouse_left_btn(doubleclick_mode=doubleclick_mode)
