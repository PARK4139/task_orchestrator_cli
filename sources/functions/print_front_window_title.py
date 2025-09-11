import zlib
import yt_dlp


import win32con
import win32con
import urllib.parse
import undetected_chromedriver as uc
import traceback
import tqdm
import time
import tarfile
import subprocess
import string
import sqlite3
import socket
import shutil
import shlex
import requests

import pythoncom
import pygetwindow
import pyautogui
import pyaudio
import os, inspect
import nest_asyncio
import mutagen
import keyboard
import inspect
import functools
import colorama
import colorama
import clipboard
import chardet
import calendar
import asyncio
from yt_dlp import YoutubeDL
from urllib.parse import unquote, urlparse, parse_qs
from typing import TypeVar, List
from telegram import Bot, Update
from seleniumbase import Driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from pynput import mouse
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_printed_once import ensure_printed_once

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_list_sorted import get_list_sorted



from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_context import SpeedControlContext
from sources.objects.pk_local_test_activate import LTA

from PIL import Image
from passlib.context import CryptContext
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import partial
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from sources.functions.get_nx import get_nx
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


def print_front_window_title():
    front_window_title = get_front_window_title()
    logging.debug(f'''front_window_title={front_window_title}  {'%%%FOO%%%' if LTA else ''}''')
    raise
