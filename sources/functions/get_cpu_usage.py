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
from sources.functions.ensure_window_to_front import ensure_window_to_front


from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
import logging

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING, D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.pk_state_via_context import SpeedControlContext

from sources.objects.pk_local_test_activate import LTA

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
from sources.functions.get_nx import get_nx
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_f import is_f
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

import logging
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def get_cpu_usage(interval, process_n):
    """LosslessCut 프로세스의 CPU 사용량을 측정"""
    import psutil
    print("현재 exec  중인 프로세스 목록:")
    process_n_list = []
    process_pid_list = []
    for process in psutil.process_iter(attrs=["pid", "name"]):
        # process_pid_list.append(process.info['pid'])
        process_n_list.append(process.info['name'])
    # ensure_iterable_log_as_vertical(item_iterable=process_n_list, item_iterable_n='process_n_list')
    for process in psutil.process_iter(attrs=["name", "cpu_percent"]):
        if process_n in process.info["name"]:
            return process.cpu_percent(interval=interval)  # CPU 사용량 리턴
    return None  # 프로세스가 없으면 None 반환
