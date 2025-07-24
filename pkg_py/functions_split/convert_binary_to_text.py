

import yt_dlp
# import win32process
# import win32gui
import win32con
import win32con
import win32com.client
import uuid
import urllib
import tqdm
import tomllib
import toml
import time
import tarfile
import sys
import subprocess
import string
import sqlite3
import socket
import shutil
import shlex
import re
import pywintypes
# import pywin32
import pyaudio
import pickle
import pandas as pd
import os.path
import os, inspect
import os
import numpy as np
import nest_asyncio
import mutagen
import math
import json
import ipdb
import inspect
import importlib
import hashlib
import functools
import easyocr
import cv2
import colorama
import clipboard
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from urllib.parse import unquote, urlparse, parse_qs
from urllib.parse import quote, urlparse
from tkinter import UNDERLINE
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_state import pk_print_state

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.write_list_to_f import write_list_to_f

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_WORKING
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.get_list_calculated import get_list_calculated

from PIL import Image, ImageFont, ImageDraw, ImageFilter
from PIL import Image, ImageFilter
from PIL import Image
from pathlib import Path
from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
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
from datetime import datetime, time
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import BeautifulSoup
from base64 import b64encode
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_WORKING, D_DOWNLOADS, D_PKG_PKL, D_PKG_PY
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def convert_binary_to_text(binary_f, txt_f):
    # todo : chore : 내가 기대한 대로 fix 안됨. 재시도 필요
    # 바이너리 f을 'rb' 모드로 열고 데이터를 읽습니다.
    with open(binary_f, 'rb') as bin_file:
        binary_data = bin_file.read()

    # 읽은 바이너리 데이터를 'utf-8'로 디코딩하여 텍스트로 변환
    try:
        text_data = binary_data.decode('utf-8')
    except UnicodeDecodeError:
        # utf-8로 디코딩이 실패할 경우 다른 인코딩을 시도
        print(f"Failed to decode with utf-8, trying cp949...")
        text_data = binary_data.decode('cp949', errors='ignore')  # 잘못된 인코딩은 무시

    # 변환된 텍스트 데이터를 텍스트 f로 저장
    with open(txt_f, 'w', encoding='utf-8') as text_file:
        text_file.write(text_data)
