import zlib
import yt_dlp
import winreg

import win32con
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tqdm
import toml
import time
import tarfile
import sys
import string
import speech_recognition as sr
import shutil
import secrets
import re
import pythoncom
import numpy as np
import mutagen
import ipdb
import datetime
import colorama
import chardet
import asyncio
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import UNDERLINE
from telegram import Bot, Update
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from pytube import Playlist

from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.get_d_working import get_d_working
import logging
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_context import SpeedControlContext

from PIL import Image
from mutagen.mp3 import MP3
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from datetime import date
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from base64 import b64encode
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux

from sources.functions.get_d_working import get_d_working


def get_target_bite(start_path='.'):
    import os
    total_size = 0
    for root, d_nx_list, f_nx_list in os.walk(start_path):
        for f_nx in f_nx_list:
            f = os.path.join(root, f_nx)
            # skip if it is symbolic link
            if not os.path.islink(f):
                total_size += os.path.getsize(f)
    return total_size
