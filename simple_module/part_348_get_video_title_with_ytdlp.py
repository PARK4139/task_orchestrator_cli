import winreg
# import win32process
# import win32gui
import win32con
import win32com.client
import webbrowser
import uuid
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tomllib
import toml
import timeit
import time
import tarfile
import subprocess
import sqlite3
import speech_recognition as sr
import socket, time
import shlex
import requests
import pywintypes
import pyglet
import pyautogui
import pyaudio
import psutil
import pickle
import paramiko
import os.path
import nest_asyncio
import math
import keyboard
import inspect
import hashlib
import functools
import datetime
import cv2
import colorama
from zipfile import BadZipFile
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram import Bot, Update
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

from pathlib import Path
from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial as functools_partial
from functools import lru_cache
from datetime import datetime
from cryptography.hazmat.backends import default_backend
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def get_video_title_with_ytdlp(clip_id):
    from yt_dlp import YoutubeDL
    # URL 정리
    url = normalize_youtube_url(f"https://www.youtube.com/watch?v={clip_id}")

    ydl_opts = {
        'quiet': True,
        'skip_download': True,  # 다운로드는 건너뜀
        'force_generic_extractor': False,  # 유튜브 전용 처리
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            # YouTube 영상 ID 추출
            clip_id = info.get('id', None)
            title = info.get('title', None)
            if title is None:
                pk_print(f"Could not retrieve title for {clip_id}. Using default title.", print_color='red')
                if clip_id:
                    pk_print(f"Could not retrieve clip_id for URL: {url}.", print_color='red')
                    return rf"Unknown_Title({clip_id})"
                return "Unknown_Title(unknown_clip_id)"
            return title

    except:
        DESCRIPTION = f"yt_dlp를 사용하여 제목을 가져오는 데 실패했습니다"  # 제목에 이모지나 특수문자를 포함한 경우 실패할 수 있음
        pk_print(f"{DESCRIPTION}  {'%%%FOO%%%' if LTA else ''}", print_color='red')
        return "Unknown_Title"
