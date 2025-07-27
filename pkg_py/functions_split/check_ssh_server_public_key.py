import zipfile

import win32com.client
import urllib.parse
import urllib
import traceback
import tqdm
import tomllib
import threading
import random, math
import pyautogui
import platform
import pickle
import os.path
import nest_asyncio
import json
import hashlib
import datetime
import colorama
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from pytube import Playlist
from PySide6.QtWidgets import QApplication
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB

from PIL import Image
from pathlib import Path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from datetime import timedelta
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs


def check_ssh_server_public_key(key_public, **config_remote_os):
    import paramiko

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ip = config_remote_os['ip']
    port = config_remote_os['port']
    user_n = config_remote_os['user_n']
    pw = config_remote_os['pw']

    try:
        ssh.connect(hostname=ip, port=port, username=user_n, password=pw)

        cmd = f'grep -qxF "{key_public}" ~/.ssh/authorized_keys && echo "Key exists" || echo "Key not found"'
        stdin, stdout, stderr = ssh.exec_command(cmd)
        std_out_str = stdout.read().decode().strip()
        signiture = "Key exists"
        if signiture == std_out_str:
            ensure_printed(str_working="PUBLIC KEY IS ALREADY REGISTERED ON THE REMOTE SERVER.")
            return 1
        else:
            ensure_printed(str_working="PUBLIC KEY IS NOT REGISTERED ON THE REMOTE SERVER.", print_color='red')
            return 0

    except Exception as e:
        ensure_printed(f"{STAMP_ERROR} {e}", print_color='red')
        raise
    finally:
        ssh.close()
        if LTA:
            ensure_printed(rf"SSH connection closed.")
