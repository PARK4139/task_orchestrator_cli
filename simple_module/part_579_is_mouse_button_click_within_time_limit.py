import zipfile
import yt_dlp
# import win32gui
# import win32gui
import win32con
import uuid
import urllib.parse
import time
import subprocess
import sqlite3
import socket
import shutil
import requests
import pyglet
import nest_asyncio
import json
import chardet
import asyncio
from zipfile import BadZipFile
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_100_performance_logic import pk_measure_seconds, pk_measure_memory

from PIL import Image
from os.path import dirname
from functools import partial as functools_partial
from functools import lru_cache
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def is_mouse_button_click_within_time_limit(key="left", time_limit=10):
    from pynput import mouse
    if key == "left":
        listener = mouse.Listener(on_click=on_left_click)
    elif key == "right":
        listener = mouse.Listener(on_click=on_right_click)
        # listener=mouse.Listener(on_click=on_right_click())
    listener.start()  # Listener 시작
    listener.join(time_limit)  # 주어진 시간 동안 대기
    listener.stop()  # Listener 종료

    return click_detected  # 클릭 감지 여부 반환
