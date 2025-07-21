# import win32gui
import win32con
import win32con
import webbrowser
import urllib.parse
import traceback
import tqdm
import time
import sqlite3
import socket
import re
import os, inspect
import nest_asyncio
import mutagen
import ipdb
import inspect
import datetime
import clipboard
import chardet
import calendar
import browser_cookie3
from yt_dlp import YoutubeDL
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from pytube import Playlist
from prompt_toolkit.styles import Style
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025

from passlib.context import CryptContext
from mysql.connector import connect, Error
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from functools import partial
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.simple_module.part_014_pk_print import pk_print


def get_random_urlsafe():
    import secrets

    return secrets.token_urlsafe(16)  # 16바이트의 난수를 URL-safe 문자열로 생성
