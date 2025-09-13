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
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.get_list_sorted import get_list_sorted

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts



from sources.objects.pk_local_test_activate import LTA
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
from sources.functions.get_nx import get_nx

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING, D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_f import is_f
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def ensure_files_scaned_and_collected():
    """메인 흐름: 스캔 후 이동"""
    import os
    import sys

    tab_completer = [D_PK_WORKING, D_TASK_ORCHESTRATOR_CLI, D_DOWNLOADS, rf"{D_DOWNLOADS}\[]\pk_ani"]

    # 명령 인자 우선
    if len(sys.argv) == 2:
        working_dir = sys.argv[1]
    else:
        working_dir = None

    while True:
        if not working_dir:
            working_dir = ensure_value_completed(key_hint='d_working', options=tab_completer)
            tab_completer.append(working_dir)

        if not os.path.isdir(working_dir):
            print_red(f"Error: '{working_dir}' 는 유효한 디렉토리가 아닙니다.")
            sys.exit(1)

        f_list = collect_f_list_recursive(working_dir)
        total_before = len(f_list)
        if total_before == 0:
            logging.debug("수집 대상이 없습니다.")
            logging.debug(f'''"수집 대상이 없습니다." {'%%%FOO%%%' if LTA else ''}''')

            break

        print_f_list_preview(f_list)

        choice = ensure_value_completed(key_hint='choice (o/x)', options=['o', 'x'])
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

        choice = ensure_value_completed(key_hint='choice (o/x)', options=['o', 'x'])
        if choice.strip().lower() != 'o':
            print("수집 취소됨.")
            continue

        collect_and_move(f_list, working_dir)
        print(f"모든 항목을 '{working_dir}_merged'로 이동했습니다.")
        continue
