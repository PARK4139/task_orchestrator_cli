import yt_dlp

import win32con
import win32com.client
import webbrowser
import uuid
import undetected_chromedriver as uc
import traceback
import threading
import tarfile
import sqlite3
import socket
import shutil
import re
import random


import pygetwindow
import pyaudio
import platform
import pandas as pd
import os.path
import mysql.connector
import keyboard
import inspect
import datetime
import cv2
import clipboard
import chardet

import asyncio
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from typing import TypeVar, List
from tkinter import UNDERLINE
from telegram import Bot, Update
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from pynput import mouse
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_state_printed import ensure_state_printed
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.pk_etc import PkFilter


from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING
from sources.objects.pk_state_via_context import SpeedControlContext
from PIL import Image, ImageFilter
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from datetime import timedelta
from datetime import date
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from base64 import b64decode
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from pathlib import Path
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.objects.pk_local_test_activate import LTA
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def send_f_to_remote_os(f_local_src, f_remote_dst, **remote_device_target_config):
    import paramiko
    import os

    ip = remote_device_target_config['ip']
    pw = remote_device_target_config['pw']
    port = remote_device_target_config['port']
    user_n = remote_device_target_config['user_n']

    f_local_src = Path(f_local_src)
    if not os.path.exists(f_local_src):
        logging.debug(f"{f_local_src} can not send, for not found")
        raise

    ssh = None
    sftp = None
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=user_n, password=pw)
        sftp = ssh.open_sftp()

        # send f_local
        logging.debug(f"started to send f{(f_local_src)} to remote os({remote_device_target_config['ip']})")
        sftp.put(f_local_src, f_remote_dst)

        # f 전송 상태 확인
        f_local_size = os.path.getsize(f_local_src)
        f_remote_size = sftp.stat(f_remote_dst).st_size
        if f_local_size == f_remote_size:
            logging.debug(f"send pnx ({f_remote_dst})")
            return 1  # 성공 시 True 반환
        else:
            logging.debug(f"send pnx ({f_remote_dst})")
            raise
    except Exception as e:
        logging.debug(f"send pnx : {e}")
        raise
    finally:
        # 리소스 정리
        if sftp:
            sftp.close()
        if ssh:
            ssh.close()
        if LTA:
            logging.debug("SSH connection closed.")
