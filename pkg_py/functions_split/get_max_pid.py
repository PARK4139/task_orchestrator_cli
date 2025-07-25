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
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.performance_logic import pk_measure_seconds, pk_measure_memory
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.get_list_calculated import get_list_calculated
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
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.is_f import is_f
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def get_max_pid(process_img_n: str):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    pids = get_pids(process_img_n=process_img_n)

    pk_print(f'''pids="{pids}"  {'%%%FOO%%%' if LTA else ''}''')

    return max(pids)
