import zipfile
import yt_dlp
import winreg
# import win32gui
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
# import pywin32
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
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories import D_WORKING, D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

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
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def get_cpu_usage(interval, process_n):
    """LosslessCut 프로세스의 CPU 사용량을 측정"""
    import psutil
    print("🔍 현재 exec  중인 프로세스 목록:")
    process_n_list = []
    process_pid_list = []
    for process in psutil.process_iter(attrs=["pid", "name"]):
        # process_pid_list.append(process.info['pid'])
        process_n_list.append(process.info['name'])
    # print_iterable_as_vertical(item_iterable=process_n_list, item_iterable_n='process_n_list')
    for process in psutil.process_iter(attrs=["name", "cpu_percent"]):
        if process_n in process.info["name"]:
            return process.cpu_percent(interval=interval)  # CPU 사용량 리턴
    return None  # 프로세스가 없으면 None 반환
