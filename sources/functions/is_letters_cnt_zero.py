import yt_dlp
import winreg
import win32con
import webbrowser
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tqdm
import tomllib
import toml
import timeit
import time
import tarfile
import sys
import subprocess
import shutil
import requests
import random
import pywintypes

import pythoncom
import pygetwindow
import pyautogui
import pyaudio
import psutil
import platform
import pickle
import paramiko
import os
import numpy as np
import mysql.connector
import mutagen
import math
import keyboard
import json
import ipdb
import functools
import easyocr
import datetime
import cv2
import colorama
import clipboard

import asyncio
from yt_dlp import YoutubeDL
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import urlparse
from urllib.parse import quote
from typing import TypeVar, List
from tkinter import UNDERLINE
from telegram import Bot, Update
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession

from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext

from sources.objects.pk_local_test_activate import LTA

from PIL import Image, ImageFont, ImageDraw
from PIL import Image, ImageFilter
from PIL import Image
from pathlib import Path
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from fastapi import HTTPException
from datetime import datetime, time
from datetime import datetime
from datetime import date
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from collections import Counter
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.functions.is_f import is_f

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.objects.pk_local_test_activate import LTA
import logging

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


def is_letters_cnt_zero(f):
    import traceback

    try:
        with open(file=f, mode='r') as file:
            contents = file.read().strip()
            # print(rf'len(contents) : {len(contents)}')
            if len(contents) == 0:
                return 1
    except FileNotFoundError:
        logging.debug("f을 찾을 수 없습니다.")
        return 0
    except UnicodeDecodeError:

        with open(file=f, mode='r', encoding=Encoding.UTF8.value) as file:
            contents = file.read().strip()
            # print(rf'len(contents) : {len(contents)}')
            if len(contents) == 0:
                return 1
        return 0
    except:
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
        logging.debug("오류가 발생했습니다.")
        return 0
