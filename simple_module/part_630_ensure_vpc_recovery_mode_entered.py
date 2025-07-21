import zlib
import zipfile
import yt_dlp
import winreg
# import win32process
# import win32gui
import win32con
import win32con
import win32com.client
import uuid
import urllib.parse
import urllib
import tqdm
import tomllib
import toml
import tarfile
import subprocess, time
import string
import speech_recognition as sr
import socket
import shutil
import secrets
import requests
import re
import random
import pywintypes
# import pywin32
import pythoncom
import pyglet
import pygetwindow
import pyautogui
import pyaudio
import platform
import pickle
import paramiko
import mysql.connector
import mutagen
import math
import ipdb
import inspect
import importlib
import hashlib
import functools
import easyocr
import datetime
import cv2
import colorama
import colorama
import clipboard
import chardet
import browser_cookie3
import asyncio
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram import Bot, Update
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from prompt_toolkit.styles import Style
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories import D_PKG_TXT, D_WORKING
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated

from pathlib import Path
from paramiko import SSHClient, AutoAddPolicy
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from datetime import timedelta
from datetime import datetime, time
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def ensure_vpc_recovery_mode_entered(vpc_data, wsl_data, config_remote_os):
    if 'no' in vpc_data.vpc_identifier:
        #  vpc 전원연결
        #  REC + PWR 버튼으로 recovery mode 부팅
        #  플래시 하려는 Side와 PC USB 연결
        pass
    elif 'nx' in vpc_data.vpc_identifier:
        pass
    elif 'xc' in vpc_data.vpc_identifier:
        pass
    elif 'evm' in vpc_data.vpc_identifier:
        # connect power
        # remove auto power mode selector pin
        # 전원 진입버튼 # EVM 의 왼쪽 버튼
        # Recovery mode 진입버튼 # EVM 의 가운데 버튼
        # recovery mode 버튼을 3초간 누르고 홀드
        # 전원버튼 3초간 누르고 홀드
        # 두 버튼을 모두 release
        # reinstall auto power mode selector pin
        pass
    else:
        pk_print(f'''unknown vpc_identifier ({vpc_data.vpc_identifier}) {'%%%FOO%%%' if LTA else ''}''',
                 print_color='red')
        raise
    if not is_vpc_recovery_mode(vpc_data):
        # [ATEMPED] 네트워크 케이블 remove 후 재시도
        # [DIAGNOSED] [HUMAN ERROR] 플래시 케이블 연결안함
        pass
