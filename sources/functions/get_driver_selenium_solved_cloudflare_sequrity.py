
import traceback
import toml
import timeit
import tarfile
import re
import random

import pyautogui
import psutil
import os, inspect
import numpy as np
import mutagen
import math
import keyboard
import clipboard
import chardet
import calendar
import asyncio
from yt_dlp import YoutubeDL
from tkinter import UNDERLINE
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from pynput import mouse
from prompt_toolkit import PromptSession
from sources.functions.get_historical_list import get_historical_list
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened import is_window_opened
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_context import SpeedControlContext

from PIL import Image, ImageFont, ImageDraw, ImageFilter
from mutagen.mp3 import MP3
from functools import partial
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from base64 import b64encode
from sources.functions.get_nx import get_nx

from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.is_d import is_d
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging

import logging
from sources.functions.get_pnxs import get_pnxs


def get_driver_selenium_solved_cloudflare_sequrity(headless_mode=True):
    """
    [ATTEMPTED] cloudflare sequrity challange
    driver.uc_open_with_reconnect(magnet_page_url, reconnect_time=6)
    page_src = driver.page_source
    [SUCCESS] cloudflare sequrity challange
    """
    from seleniumbase import Driver
    driver = Driver(uc=True, headless=headless_mode)
    return driver
