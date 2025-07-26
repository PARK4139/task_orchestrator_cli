import zlib
import yt_dlp
import winreg


import win32con
import uuid
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tqdm
import sys
import pythoncom
import pygetwindow
import pyautogui
import pickle
import inspect
import cv2
import chardet

import asyncio
from urllib.parse import urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.get_list_calculated import get_list_calculated
from moviepy import VideoFileClip
from functools import partial
from functools import lru_cache
from enum import Enum
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.functions_split.get_pnx_list import get_pnx_list


def convert_img_to_img_resized(img_pnx, width_px, height_px):
    import inspect
    from PIL import Image
    func_n = inspect.currentframe().f_code.co_name
    img_converted = Image.open(img_pnx).resize((width_px, height_px))
    img_converted.show()
