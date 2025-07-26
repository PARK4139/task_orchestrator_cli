import zlib
import zipfile
import winreg



import win32con
import win32com.client
import webbrowser
import urllib.parse
import undetected_chromedriver as uc
import traceback
import tqdm
import toml
import time
import tarfile
import sys
import sqlite3
import socket
import pywintypes
import pyglet
import pygetwindow
import pyaudio
import psutil
import platform
import pickle
import paramiko
import pandas as pd
import os, inspect
import numpy as np
import nest_asyncio
import mutagen
import keyboard
import importlib
import functools
import cv2
import colorama
import chardet
import calendar
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from typing import TypeVar, List
from tkinter import UNDERLINE
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.get_list_calculated import get_list_calculated

from PIL import Image, ImageFilter
from os.path import dirname
from os import path
from gtts import gTTS
from functools import partial as functools_partial
from enum import Enum
from dirsync import sync
from datetime import timedelta
from datetime import datetime, timedelta
from datetime import datetime, time
from datetime import datetime
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from collections import Counter
from base64 import b64encode
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS, D_PKG_PKL, D_PKG_PY
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def test_api():
    # def save_data_via_api_server():
    import requests
    import json

    import toml

    # SWAGGER ACCESS # FASTAPI # INCLUDE ROUTING TEST
    config = toml.load(F_CONFIG_TOML)
    pk_protocol_type = config["pk_uvicorn"]["protocol_type"]
    pk_host = config["pk_uvicorn"]["host"]
    pk_port = config["pk_uvicorn"]["port"]
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {pk_protocol_type}://{pk_host}:{pk_port}/docs")
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {pk_protocol_type}://{pk_host}:{pk_port}/redoc")
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {pk_protocol_type}://{pk_host}:{pk_port}")

    # TODO : ROUTING TEST

    # POST REQUEST TEST
    url = "https://pk_system.store/api/db-maria/items"
    data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "pw": "pw",
    }
    json_data = json.dumps(data)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json_data)
    if response.status_code == 201:
        print("데이터가 성공적으로 저장되었습니다.")
    else:
        print("데이터 저장에 실패했습니다.")
