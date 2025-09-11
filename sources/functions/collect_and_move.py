import zlib
import zipfile
import yt_dlp


import win32con
import urllib.parse
import tqdm
import tomllib
import toml
import timeit
import tarfile
import string
import sqlite3
import secrets
import requests
import random
import platform
import pandas as pd
import os, inspect
import numpy as np
import mysql.connector
import math
import hashlib
import easyocr
import datetime
import calendar
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import quote
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_command_executed import ensure_command_executed

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_state_via_context import SpeedControlContext
from sources.objects.pk_local_test_activate import LTA
from PIL import Image
from moviepy import VideoFileClip
from functools import partial
from functools import lru_cache
from enum import Enum
from dirsync import sync
from datetime import timedelta
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from bs4 import BeautifulSoup
from base64 import b64encode
from sources.functions.get_nx import get_nx

from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

import logging
from sources.functions.get_d_working import get_d_working


def collect_and_move(file_list, src_root):
    """file_list를 src_root+'_merged' 폴더로 이동, 중복 파일명에 (n) 붙임"""
    import os
    import shutil

    dst_root = f"{src_root.rstrip(os.sep)}_merged"
    os.makedirs(dst_root, exist_ok=True)

    for src_path in file_list:
        name = os.path.basename(src_path)
        unique_name = ensure_unique(dst_root, name)
        dst_path = os.path.join(dst_root, unique_name)
        shutil.move(src_path, dst_path)
        print(f"Moved: {src_path} -> {dst_path}")
