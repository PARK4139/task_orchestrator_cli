

import winreg
# import win32gui
import win32con
import webbrowser
import uuid
import urllib.parse
import urllib
import undetected_chromedriver as uc
import traceback
import tomllib
import timeit
import time
import tarfile
import subprocess, time
import subprocess
import string
import sqlite3
import speech_recognition as sr
import socket
import shlex
import secrets
import requests
import re
import random
import pywintypes
# import pywin32
import pythoncom
import pyaudio
import pandas as pd
import os.path
import numpy as np
import nest_asyncio
import mysql.connector
import mutagen
import json
import ipdb
import hashlib
import functools
import easyocr
import datetime
import cv2
import chardet
import calendar
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_performance_logic import pk_measure_seconds, pk_measure_memory
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated

from PIL import Image, ImageFont, ImageDraw
from PIL import Image
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import lru_cache
from fastapi import HTTPException
from dirsync import sync
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def compress_pnx_to_f_tar_gz(pnx, dst):
    import tarfile
    import os

    pnx = get_pnx_windows_style(pnx)
    dst = get_pnx_windows_style(dst)

    # Ensure the source exists
    if not os.path.exists(pnx):
        raise FileNotFoundError(f"Source path '{pnx}' does not exist.")

    # Create a tar.gz archive
    with tarfile.open(dst, "w:gz") as tar:
        def preserve_metadata(tarinfo):
            """
            Preserve file metadata (permissions, ownership, timestamps).
            """
            tarinfo.preserve = True  # Ensure extended metadata is kept
            return tarinfo

        # Add the source directory, preserving metadata
        tar.add(pnx, arcname=os.path.basename(pnx), recursive=True, filter=preserve_metadata)
