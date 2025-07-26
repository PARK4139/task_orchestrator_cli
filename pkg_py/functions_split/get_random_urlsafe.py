
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
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.press import press
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.map_massages import PkMessages2025

from passlib.context import CryptContext
from mysql.connector import connect, Error
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from functools import partial
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_printed import ensure_printed


def get_random_urlsafe():
    import secrets

    return secrets.token_urlsafe(16)  # 16바이트의 난수를 URL-safe 문자열로 생성
