import winreg
# import win32process
import tomllib
import sys
import socket
import re
import pywintypes
# import pywin32
import pyglet
import os.path
import importlib
from tkinter import UNDERLINE
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.print_red import print_red

from pkg_py.pk_system_object.local_test_activate import LTA
from moviepy import VideoFileClip
from gtts import gTTS
from datetime import timedelta
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.functions_split.get_d_working import get_d_working


def get_modified_f_list(previous_state, current_state):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    return DataStructureUtil.get_different_elements(list1=current_state, list2=previous_state)
