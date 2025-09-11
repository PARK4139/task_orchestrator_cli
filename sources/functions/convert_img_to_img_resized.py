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
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened import is_window_opened
import logging

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.objects.pk_map_texts import PkTexts

from moviepy import VideoFileClip
from functools import partial
from functools import lru_cache
from enum import Enum
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from sources.functions.get_nx import get_nx

from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_f import is_f
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from sources.functions.get_pnxs import get_pnxs


def convert_img_to_img_resized(img_pnx, width_px, height_px):
    import inspect
    from PIL import Image
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    img_converted = Image.open(img_pnx).resize((width_px, height_px))
    img_converted.show()
