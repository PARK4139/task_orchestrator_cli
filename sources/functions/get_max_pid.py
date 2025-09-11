import zlib
import yt_dlp
import winreg
import win32com.client
import webbrowser
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tomllib
import toml
import threading
import sys
import subprocess
import string
import sqlite3
import socket
import re
import random, math

import pythoncom
import pygetwindow
import pyautogui
import pyaudio
import platform
import pickle
import pandas as pd
import os, inspect
import os
import numpy as np
import nest_asyncio
import math
import keyboard
import ipdb
import inspect
import importlib
import hashlib
import functools
import easyocr
import datetime
import cv2
import colorama
import chardet
import calendar

import asyncio
from zipfile import BadZipFile
from urllib.parse import urlparse
from telethon import TelegramClient, events
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit import PromptSession

from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_printed_once import ensure_printed_once
import logging

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.performance_logic import ensure_seconds_measured, pk_measure_memory
from sources.objects.pk_local_test_activate import LTA

from PIL import Image, ImageFilter
from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from os import path
from gtts import gTTS
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from datetime import datetime, timedelta
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from bs4 import ResultSet
from base64 import b64decode
from sources.functions.get_nx import get_nx
from sources.functions.is_f import is_f

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging


def get_max_pid(process_img_n: str):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    pids = get_pids(process_img_n=process_img_n)

    logging.debug(f'''pids="{pids}"  {'%%%FOO%%%' if LTA else ''}''')

    return max(pids)
