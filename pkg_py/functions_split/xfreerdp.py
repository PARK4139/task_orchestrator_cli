import zipfile
import winreg


import win32con
import win32com.client
import webbrowser
import urllib
import tomllib
import timeit
import threading
import shutil
import secrets
import requests

import pyglet
import pyautogui
import psutil
import os, inspect
import nest_asyncio
import mysql.connector
import mutagen
import json
import easyocr
import datetime
import cv2
import colorama
import chardet

from yt_dlp import YoutubeDL
from urllib.parse import quote, urlparse
from typing import TypeVar, List
from tkinter import UNDERLINE
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from pytube import Playlist
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.ensure_state_printed import ensure_state_printed

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.performance_logic import ensure_seconds_measured, pk_measure_memory
from pkg_py.system_object.is_os_windows import is_os_windows

from passlib.context import CryptContext
from os.path import dirname
from functools import partial
from datetime import timedelta
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from collections import Counter
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.ensure_printed import ensure_printed


def xfreerdp(users, ip, remote_os_distro_n, wsl_window_title_seg, pw, exit_mode):
    # todo
    cmd = 'wsl sudo apt update'
    ensure_command_excuted_to_os(cmd=cmd)

    cmd = 'sudo apt install freerdp2-x11'
    ensure_command_excuted_to_os(cmd=cmd)

    #         ensure_writen_like_person(rf'xfreerdp /v:{ip}:3390 /u:{users} /p:{pw} /sec:nla /clipboard',remote_os_distro_n=remote_os_distro_n, wsl_window_title_seg=wsl_window_title_seg)
    #         ensure_writen_like_person(rf'xfreerdp /v:{ip}:3390 /u:{users} /p:{pw} /sec:tls /clipboard',remote_os_distro_n=remote_os_distro_n, wsl_window_title_seg=wsl_window_title_seg)
    cmd_to_wsl_os_like_person(cmd=rf'xfreerdp /v:{ip}:3390 /u:{users} /p:{pw} /clipboard',
                              remote_os_distro_n=remote_os_distro_n, wsl_window_title_seg=wsl_window_title_seg)
