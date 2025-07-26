import win32con
import uuid
import toml
import threading
import sys
import speech_recognition as sr
import socket
import requests
import re

import pyglet
import pygetwindow
import pyautogui
import pickle
import os.path
import os
import nest_asyncio
import math
import keyboard
import ipdb
import inspect
import cv2
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import UNDERLINE
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from queue import Queue, Empty
from pynput import mouse
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image
from paramiko import SSHClient, AutoAddPolicy
from os.path import dirname
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def is_pattern_in_prompt(prompt: str, pattern: any, with_case_ignored=True):
    import inspect
    import re

    # ensure_printed(string = rf'''string="{string}"  {'%%%FOO%%%' if LTA else ''}''')
    # ensure_printed(string = rf'''regex="{regex}"  {'%%%FOO%%%' if LTA else ''}''')
    func_n = inspect.currentframe().f_code.co_name
    ensure_printed(str_working=rf'''{PK_UNDERLINE}{func_n}()  {'%%%FOO%%%' if LTA else ''}''')
    if with_case_ignored == True:
        pattern = re.compile(pattern, re.IGNORECASE)
    else:
        pattern = re.compile(pattern)
    m = pattern.search(prompt)
    if m:
        # ensure_printed("function name   here here here")
        # ensure_printed(rf"contents: {contents}")
        # ensure_printed(rf"regex: {regex}")
        # ensure_printed(rf"True")
        return 1
    else:
        # ensure_printed(rf"contents: {contents}")
        # ensure_printed(rf"regex: {regex}")
        # ensure_printed(rf"False")
        return 0
