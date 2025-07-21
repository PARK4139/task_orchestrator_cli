import tomllib
import toml
import shlex
import secrets
import re
import random, math
# import pywin32
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
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_100_performance_logic import pk_measure_seconds, pk_measure_memory
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from fastapi import HTTPException
from enum import Enum
from datetime import datetime, time
from Cryptodome.Random import get_random_bytes
from base64 import b64decode
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


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
