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
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PKG_TXT, D_WORKING
from pkg_py.system_object.state_via_context import SpeedControlContext
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
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def send_f_to_remote_os(f_local_src, f_remote_dst, **config_remote_os):
    import paramiko
    import os

    ip = config_remote_os['ip']
    pw = config_remote_os['pw']
    port = config_remote_os['port']
    user_n = config_remote_os['user_n']

    f_local_src = get_pnx_os_style(f_local_src)
    if not os.path.exists(f_local_src):
        pk_print(f"{f_local_src} can not send, for not found", print_color='red')
        raise

    ssh = None
    sftp = None
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=user_n, password=pw)
        sftp = ssh.open_sftp()

        # send f_local
        pk_print(f"started to send f{(f_local_src)} to remote os({config_remote_os['ip']})")
        sftp.put(f_local_src, f_remote_dst)

        # f 전송 상태 확인
        f_local_size = os.path.getsize(f_local_src)
        f_remote_size = sftp.stat(f_remote_dst).st_size
        if f_local_size == f_remote_size:
            pk_print(f"send pnx ({f_remote_dst})", print_color="green")
            return 1  # 성공 시 True 반환
        else:
            pk_print(f"send pnx ({f_remote_dst})", print_color='red')
            raise
    except Exception as e:
        pk_print(f"send pnx : {e}", print_color='red')
        raise
    finally:
        # 리소스 정리
        if sftp:
            sftp.close()
        if ssh:
            ssh.close()
        if LTA:
            pk_print(str_working="SSH connection closed.")
