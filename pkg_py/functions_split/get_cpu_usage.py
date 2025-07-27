import zipfile
import yt_dlp
import winreg

import win32con
import win32con
import win32com.client
import urllib.parse
import urllib
import traceback
import tqdm
import threading
import subprocess
import string
import shlex
import secrets
import requests
import pywintypes

import pyautogui
import pyaudio
import psutil
import pickle
import paramiko
import os.path
import os
import numpy as np
import keyboard
import ipdb
import inspect
import functools
import easyocr
import colorama
import clipboard
import chardet
import calendar
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import UNDERLINE
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f

from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA

from PIL import Image
from pathlib import Path
from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from dirsync import sync
from datetime import datetime
from dataclasses import dataclass
from collections import Counter
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_d_working import get_d_working


def get_cpu_usage(interval, process_n):
    """LosslessCut 프로세스의 CPU 사용량을 측정"""
    import psutil
    print("🔍 현재 exec  중인 프로세스 목록:")
    process_n_list = []
    process_pid_list = []
    for process in psutil.process_iter(attrs=["pid", "name"]):
        # process_pid_list.append(process.info['pid'])
        process_n_list.append(process.info['name'])
    # ensure_iterable_printed_as_vertical(item_iterable=process_n_list, item_iterable_n='process_n_list')
    for process in psutil.process_iter(attrs=["name", "cpu_percent"]):
        if process_n in process.info["name"]:
            return process.cpu_percent(interval=interval)  # CPU 사용량 리턴
    return None  # 프로세스가 없으면 None 반환
