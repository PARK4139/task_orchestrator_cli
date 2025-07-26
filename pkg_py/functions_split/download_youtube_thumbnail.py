import tomllib
import toml
import shlex
import secrets
import re
import random, math

import pyautogui
import os
import numpy as np
import inspect
import datetime
import calendar
from urllib.parse import quote
from typing import TypeVar, List
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.press import press

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.performance_logic import measure_seconds, pk_measure_memory
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from fastapi import HTTPException
from enum import Enum
from datetime import datetime, time
from Cryptodome.Random import get_random_bytes
from base64 import b64decode
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.is_d import is_d
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def download_youtube_thumbnail(youtube_video_url, f_dst_jpg):
    import requests
    youtube_video_id = youtube_video_url.split('v=')[-1].split('&')[0]
    # 최대 해상도 썸네일 URL
    thumbnail_url = f'https://img.youtube.com/vi/{youtube_video_id}/maxresdefault.jpg'
    # 이미지 다운로드 및 저장
    try:
        response = requests.get(thumbnail_url, stream=True)
        response.raise_for_status()
        with open(file=f_dst_jpg, mode='wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"downloaded : {f_dst_jpg}")
    except requests.exceptions.RequestException as e:
        print(f"썸네일 다운로드 실패: {e}")
