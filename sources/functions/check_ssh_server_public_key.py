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

from sources.functions.get_historical_list import get_historical_list
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE

from sources.objects.pk_state_via_database import PkSqlite3DB

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
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f

from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


def check_ssh_server_public_key(key_public, **remote_device_target_config):
    import paramiko

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ip = remote_device_target_config['ip']
    port = remote_device_target_config['port']
    user_n = remote_device_target_config['user_n']
    pw = remote_device_target_config['pw']

    try:
        ssh.connect(hostname=ip, port=port, username=user_n, password=pw)

        cmd = f'grep -qxF "{key_public}" ~/.ssh/authorized_keys && echo "Key exists" || echo "Key not found"'
        stdin, stdout, stderr = ssh.exec_command(cmd)
        std_out_str = stdout.read().decode().strip()
        signiture = "Key exists"
        if signiture == std_out_str:
            logging.debug("PUBLIC KEY IS ALREADY REGISTERED ON THE REMOTE SERVER.")
            return 1
        else:
            logging.debug("PUBLIC KEY IS NOT REGISTERED ON THE REMOTE SERVER.")
            return 0

    except Exception as e:
        logging.debug(f"{"[ ERROR ]"} {e}")
        raise
    finally:
        ssh.close()
        if LTA:
            logging.debug(rf"SSH connection closed.")
