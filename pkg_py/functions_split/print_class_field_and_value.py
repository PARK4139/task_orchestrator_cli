import zlib
import zipfile
import yt_dlp
import winreg


import undetected_chromedriver as uc
import tomllib
import tomllib
import toml
import threading
import tarfile
import sys
import subprocess, time
import string
import sqlite3
import socket, time
import shutil
import shlex
import secrets
import requests
import re
import random, math

import pythoncom
import pyautogui
import psutil
import platform
import pickle
import paramiko
import pandas as pd
import os.path
import os, inspect
import os
import math
import keyboard
import inspect
import importlib
import hashlib
import easyocr
import datetime
import cv2
import colorama
import colorama
import clipboard
import chardet

import asyncio
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote, urlparse
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.pk_print import pk_print


from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.performance_logic import pk_measure_seconds, pk_measure_memory
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.get_list_calculated import get_list_calculated

from PIL import Image, ImageFilter
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from datetime import datetime, timedelta
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def print_class_field_and_value(class_n):  # print 보다는 get 으로 바꾸는게 좋겠다.

    cmd_usage_explanations = []
    cmd_usage_explanations.append(title)
    cmd_usage_explanations.append('\n')
    cmd_usage_explanations.append('<예시> : python console_blurred.py <mode_option>')
    cmd_usage_explanations.append('\n')
    longest_field = max(vars(class_n), key=len)  # mkr_get_longest_field_name
    longest_value = vars(class_n)[longest_field]  # mkr_get_longest_field_value
    for key, value in class_n.__dict__.items():  # mkr_get_field_name_and_field_value
        if not key.startswith('__'):  # 내장 속성 제외
            cmd_usage_explanations.append(f"{key}{" " * (len(longest_field) - len(key))}: {value}")
    cmd_usage_explanations.append('\n')
    for cmd_usage_explanation in cmd_usage_explanations:
        pk_print(str_working=cmd_usage_explanation)
    cmd_usage_explanations.append('\n')
