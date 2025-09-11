import zlib
import zipfile
import yt_dlp
import winreg
import win32com.client
import webbrowser
import traceback
import tomllib
import toml
import toml
import threading
import tarfile
import string
import socket, time
import shutil
import requests
import re
import pyglet
import pyautogui
import pyaudio
import platform
import os.path
import os, inspect
import numpy as np
import nest_asyncio
import math
import keyboard
import json
import importlib
import hashlib
import functools
import datetime

import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from telegram import Bot, Update
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from queue import Queue, Empty
from pytube import Playlist

from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_printed_once import ensure_printed_once

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI

from sources.objects.pk_local_test_activate import LTA
from PIL import Image, ImageFont, ImageDraw
from PIL import Image
from os.path import dirname
from gtts import gTTS
from functools import partial as functools_partial
from functools import lru_cache
from datetime import timedelta
from datetime import datetime, timedelta
from cryptography.hazmat.primitives import padding
from collections import Counter

from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def convert_as_zip_with_timestamp(f):
    import os
    import traceback

    starting_d = get_d_working()
    try:
        target_dirname = os.path.dirname(f)
        target_dirname_dirname = os.path.dirname(target_dirname)
        target_basename = os.path.basename(f).split(".")[0]
        target_zip = rf'$zip_{target_basename}.zip'
        target_yyyy_mm_dd_HH_MM_SS_zip = rf'{target_basename} - {get_time_as_("%Y %m %d %H %M %S")}.zip'
        # logging.debug(rf'# target_dirname_dirname 로 이동')
        os.chdir(target_dirname_dirname)
        # logging.debug(rf'부모d로 백업')
        cmd = f'bandizip.exe c "{target_zip}" "{f}"'
        ensure_command_executed_like_human_as_admin(cmd)
        # logging.debug(rf'이름변경')
        cmd = f'ren "{target_zip}" "$deleted_{target_yyyy_mm_dd_HH_MM_SS_zip}"'
        ensure_command_executed_like_human_as_admin(cmd)
        # logging.debug(rf'부모d에서 백업될 d로 이동')
        cmd = f'move "$deleted_{target_yyyy_mm_dd_HH_MM_SS_zip}" "{target_dirname}"'
        ensure_command_executed_like_human_as_admin(cmd)
        # logging.debug(rf'백업될 d로 이동')
        os.chdir(target_dirname)
        # logging.debug("os.getcwd()")
        # logging.debug(os.getcwd())
        # logging.debug("원본f삭제")
        os.remove(f)
    except:
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
    finally:
        logging.debug(rf'프로젝트 d로 이동')
        os.chdir(starting_d)
