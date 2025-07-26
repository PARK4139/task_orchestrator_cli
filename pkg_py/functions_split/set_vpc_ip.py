
import win32com.client
import webbrowser
import uuid
import urllib
import undetected_chromedriver as uc
import traceback
import tomllib
import sys
import string
import pythoncom
import pygetwindow
import pyautogui
import pyaudio
import paramiko
import pandas as pd
import numpy as np
import nest_asyncio
import math
import clipboard
import chardet
import asyncio
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import UNDERLINE
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from pynput import mouse
from prompt_toolkit.styles import Style
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical

from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.print_red import print_red

from os.path import dirname
from moviepy import VideoFileClip
from gtts import gTTS
from functools import lru_cache
from fastapi import HTTPException
from dirsync import sync
from datetime import date
from concurrent.futures import ThreadPoolExecutor
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows

from pkg_py.system_object.local_test_activate import LTA


def set_vpc_ip(vpc_data, **config_remote_os):
    set_wired_connection(vpc_data.vpc_wired_connection_1_new, **config_remote_os)
    set_wired_connection(vpc_data.vpc_wired_connection_3_new, **config_remote_os)
