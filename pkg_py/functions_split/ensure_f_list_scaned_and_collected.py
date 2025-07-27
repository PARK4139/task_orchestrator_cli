import zipfile
import yt_dlp
import winreg

import webbrowser
import uuid
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tqdm
import tomllib
import toml
import time
import threading
import tarfile
import subprocess
import sqlite3
import socket
import shutil
import shlex
import requests
import re
import random

import pythoncom
import pyglet
import pygetwindow
import pyautogui
import psutil
import platform
import pickle
import paramiko
import os.path
import os
import nest_asyncio
import mutagen
import json
import ipdb
import inspect
import importlib
import easyocr
import datetime
import colorama
import colorama
import clipboard
import chardet
import calendar
import asyncio
from urllib.parse import urlparse
from typing import TypeVar, List
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red

from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from paramiko import SSHClient, AutoAddPolicy
from os.path import dirname
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import partial
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from datetime import datetime, timedelta
from datetime import datetime, time
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS, D_PKG_PY
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def ensure_f_list_scaned_and_collected():
    """메인 흐름: 스캔 후 이동"""
    import os
    import sys

    tab_completer = [D_PK_WORKING, D_PROJECT, D_DOWNLOADS, rf"{D_DOWNLOADS}\[]\pk_ani"]

    # 명령 인자 우선
    if len(sys.argv) == 2:
        working_dir = sys.argv[1]
    else:
        working_dir = None

    while True:
        if not working_dir:
            working_dir = get_value_completed(key_hint='d_working=', values=tab_completer)
            tab_completer.append(working_dir)

        if not os.path.isdir(working_dir):
            print_red(f"Error: '{working_dir}' 는 유효한 디렉토리가 아닙니다.")
            sys.exit(1)

        f_list = collect_f_list_recursive(working_dir)
        total_before = len(f_list)
        if total_before == 0:
            ensure_printed("수집 대상이 없습니다.", print_color='green')
            ensure_printed(f'''"수집 대상이 없습니다." {'%%%FOO%%%' if LTA else ''}''', print_color='green')

            break

        print_f_list_preview(f_list)

        choice = get_value_completed(key_hint='choice (o/x)=', values=['o', 'x'])
        if choice.strip().lower() != 'o':
            print("수집 취소됨.")
            return

        # 이동 전 파일 수 확인
        print(f"이동 전 파일 개수: {total_before}개")
        collect_and_move(f_list, working_dir)
        # 이동 후 파일 수 확인
        dst_dir = f"{working_dir.rstrip(os.sep)}_merged"
        moved_count = len([name for name in os.listdir(dst_dir) if os.path.isfile(os.path.join(dst_dir, name))])
        print(f"이동 후 파일 개수: {moved_count}개")

        print(f"모든 항목을 '{working_dir}_merged'로 이동했습니다. (이동됨: {moved_count}/{total_before})")
        continue

        choice = get_value_completed(key_hint='choice (o/x)=', values=['o', 'x'])
        if choice.strip().lower() != 'o':
            print("수집 취소됨.")
            continue

        collect_and_move(f_list, working_dir)
        print(f"모든 항목을 '{working_dir}_merged'로 이동했습니다.")
        continue
