import yt_dlp

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
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_printed_once import ensure_printed_once
import logging

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f

from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_database import PkSqlite3DB

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
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided

from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_f import is_f
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def classify_pnxs_to_pkg_document(pnx, without_walking=True):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    # target_pnx가 유효한 _d_인지 확인
    if is_f(pnx=pnx):
        logging.debug(f"{pnx} 는 정리할 수 있는 _d_가 아닙니다")
        return

    # f과 _d_ get
    txt_to_exclude_list = [
        F_DB_YAML,
        F_SUCCESS_LOG,
        F_LOCAL_PKG_CACHE_PRIVATE,
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
            ensure_pnx_moved(pnx=file_pnx, d_dst=dst)
            logging.debug(rf'''file_pnx="{file_pnx}"  {'%%%FOO%%%' if LTA else ''}''')
    logging.debug(rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''')
