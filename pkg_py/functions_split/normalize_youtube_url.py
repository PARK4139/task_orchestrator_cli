import zlib
import zipfile
import yt_dlp
import win32con
import win32com.client
import webbrowser
import uuid
import urllib
import traceback
import tomllib
import sys
import sqlite3
import socket
import requests
import pywintypes
import pyglet
import platform
import paramiko
import os.path
import functools
import colorama
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote
from selenium.webdriver.common.keys import Keys
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.print_red import print_red
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from functools import partial as functools_partial
from functools import partial
from enum import Enum
from datetime import datetime
from datetime import date
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.pk_system_object.local_test_activate import LTA

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def normalize_youtube_url(url):
    """ YouTube URL을 표준 형식으로 변환 """
    if "youtube.com/watch?v=" in url and "youtu.be" in url:
        url = url.replace("https://www.youtube.com/watch?v=https://youtu.be/", "https://youtu.be/")

    # youtu.be 형식의 단축 URL을 표준 watch?v= 형식으로 변환
    if "youtu.be/" in url:
        video_id = url.split("youtu.be/")[-1].split("?")[0]  # YouTube 영상 ID 추출
        url = f"https://www.youtube.com/watch?v={video_id}"

    return url
