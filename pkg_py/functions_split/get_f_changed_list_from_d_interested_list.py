import zlib
import winreg
import win32con
import webbrowser
import uuid
import urllib.parse
import urllib
import timeit
import string
import secrets
import requests
import pywintypes
import pythoncom
import pygetwindow
import pyautogui
import pyaudio
import psutil
import paramiko
import os, inspect
import mysql.connector
import mutagen
import math
import importlib
import hashlib
import functools
import datetime
import colorama
import chardet
import calendar

import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from urllib.parse import quote, urlparse
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pytube import Playlist
from pynput import mouse
from prompt_toolkit.styles import Style
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed

from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.get_list_calculated import get_list_calculated

from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from base64 import b64encode
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL, D_PKG_PY
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.get_d_working import get_d_working


def get_f_changed_list_from_d_interested_list(d_interested_list, monitoring_interval=0.2, time_limit=None,
                                              change_cnt_limit=None):
    import time

    import importlib

    # 모듈 자체를 먼저 import
    watchdog_observers = importlib.import_module("watchdog.observers")
    watchdog_events = importlib.import_module("watchdog.events")
    pkg_cli = importlib.import_module("pkg_py.interface_cmd_line")
    pkg_constants = importlib.import_module("pkg_py.constants")

    # 필요한 속성만 참조
    Observer = watchdog_observers.Observer
    FileSystemEventHandler = watchdog_events.FileSystemEventHandler
    ensure_printed = pkg_cli.ensure_printed
    DOWNLOADS = D_DOWNLOADS

    d_interested_list = [get_pnx_os_style(d) for d in d_interested_list]

    class FileChangeHandler(FileSystemEventHandler):
        def __init__(self, observer, change_cnt_limit=None):
            super().__init__()
            self.observer = observer  # Observer 인스턴스를 받아 저장
            self.f_changed_list = []
            self.f_change_level = 0
            self.change_cnt_limit = change_cnt_limit

        def on_created(self, event):
            ensure_printed(f"f_created={event.src_path}")
            self.f_changed_list.append(event.src_path)
            self.f_change_level += 1
            self.check_limit()

        def on_deleted(self, event):
            ensure_printed(f"f_deleted={event.src_path}")
            self.f_changed_list.append(event.src_path)
            self.f_change_level += 1
            self.check_limit()

        def on_modified(self, event):
            ensure_printed(f"f_modified={event.src_path}")
            self.f_changed_list.append(event.src_path)
            self.f_change_level += 1
            self.check_limit()

        def check_limit(self):
            if self.change_cnt_limit is not None and self.f_change_level >= self.change_cnt_limit:
                ensure_printed("Change limit reached. Stopping observer.")
                self.observer.stop()  # Stop the observer instead of raising an exception

    event_handler = FileChangeHandler(change_cnt_limit)
    observer = Observer()

    for d in d_interested_list:
        observer.schedule(event_handler, d, recursive=True)

    ensure_printed(
        rf"[DETECT F_CHANGED LOOP STARTED] monitoring_interval={monitoring_interval}, len(d_interested_list)={len(d_interested_list)}",
        print_color='blue')

    observer.start()
    start_time = time.time()

    try:
        while 1:
            if time_limit is not None and (time.time() - start_time > time_limit):
                break
            ensure_slept(seconds=monitoring_interval)
    except StopIteration:
        pass
    except KeyboardInterrupt:
        ensure_printed("Monitoring stopped by user.")

    observer.stop()
    observer.join()

    return event_handler.f_changed_list
