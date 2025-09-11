import zipfile
import yt_dlp


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

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.performance_logic import ensure_seconds_measured, pk_measure_memory

from PIL import Image
from os.path import dirname
from functools import partial as functools_partial
from functools import lru_cache
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from base64 import b64decode

from sources.functions.is_f import is_f
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.functions.get_pnxs import get_pnxs


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
