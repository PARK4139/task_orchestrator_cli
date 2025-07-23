

import yt_dlp
# import win32process
# import win32gui
import win32con
import webbrowser
import uuid
import undetected_chromedriver as uc
import tqdm
import tomllib
import tomllib
import toml
import toml
import time
import tarfile
import subprocess
import string
import sqlite3
import speech_recognition as sr
import shutil
import requests
import re
import pywintypes
# import pywin32
import pythoncom
import pyglet
import pygetwindow
import pyautogui
import pyaudio
import psutil
import pickle
import pandas as pd
import os.path
import numpy as np
import nest_asyncio
import mysql.connector
import mutagen
import json
import ipdb
import functools
import easyocr
import datetime
import cv2
import colorama
import colorama
import browser_cookie3
import asyncio
from urllib.parse import urlparse, parse_qs, unquote
from typing import TypeVar, List
from telethon import TelegramClient, events
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.write_list_to_f import write_list_to_f

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.directories import D_PKG_TXT, D_WORKING
from pkg_py.pk_system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_object.map_massages import PkMessages2025
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from PIL import Image, ImageFilter
from pathlib import Path
from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from moviepy import VideoFileClip
from functools import lru_cache
from enum import Enum
from dirsync import sync
from datetime import timedelta
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from base64 import b64decode
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def classify_pnxs_to_pkg_document(pnx, without_walking=True):
    import inspect
    func_n = inspect.currentframe().f_code.co_name

    # target_pnx가 유효한 _d_인지 확인
    if is_f(pnx=pnx):
        pk_print(f"{pnx} 는 정리할 수 있는 _d_가 아닙니다")
        return

    # f과 _d_ get
    txt_to_exclude_list = [
        F_DB_YAML,
        F_SUCCESS_LOG,
        F_LOCAL_PKG_CACHE,
    ]
    if without_walking == False:
        dir_pnxs, file_pnxs = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list)
    else:
        dir_pnxs, file_pnxs = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list, without_walking=0)

    # f 처리
    x_allowed = [".txt", '.ximind', '.pdf', '.xls']
    x_allowed = x_allowed + get_list_replaced_element_from_str_to_upper_case(working_list=x_allowed)
    pnx = get_pn(pnx)
    dst = rf"{pnx}\pkg_document"
    for file_pnx in file_pnxs:
        file_pnx = file_pnx[0]
        file_p = get_p(file_pnx)
        file_x = get_x(file_pnx).replace(".", "")  # 확장자에서 점(.) remove
        if file_x in [ext.replace(".", "") for ext in x_allowed]:  # x_allowed의 확장자와 비교
            ensure_pnx_made(dst, mode="d")
            move_pnx(pnx=file_pnx, d_dst=dst)
            pk_print(working_str=rf'''file_pnx="{file_pnx}"  {'%%%FOO%%%' if LTA else ''}''')
    pk_print(working_str=rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''')
