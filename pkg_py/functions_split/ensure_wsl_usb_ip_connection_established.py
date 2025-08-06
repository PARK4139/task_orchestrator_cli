import zlib
import winreg



import win32com.client
import webbrowser
import urllib
import tomllib
import string
import speech_recognition as sr
import socket
import shlex
import secrets
import re
import pywintypes

import pythoncom
import pyaudio
import os, inspect
import numpy as np
import mysql.connector
import math
import keyboard
import ipdb
import inspect
import importlib
import hashlib
import easyocr
import colorama
import clipboard

from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from queue import Queue, Empty
from pytube import Playlist
from prompt_toolkit.styles import Style
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
# pk_#
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PK_WORKING
# from pkg_py.system_object.print_red import print_red
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA

from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, Counter
from bs4 import ResultSet
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS, D_PKG_CACHE_PRIVATE, D_PKG_PY
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_d_working import get_d_working


def ensure_wsl_usb_ip_connection_established(wsl_distro_n, config_remote_os):
    # todo : attach_remote_os_usb_connection() 를 ensure_wsl_usb_connection_attach() 에 병합
    import re

    ensure_usbipd_enabled(config_remote_os)

    cmd = "usbipd list"  # watch -n 1 usbipd.exe list
    std_list = ensure_command_excuted_to_os(cmd=cmd, encoding=Encoding.UTF8)
    bus_id = None
    # signiture_list=["APX", "Attached" or "Shared"]
    signiture_list = ["APX"]
    pattern = re.compile(r"\d+-\d")  # "2-3 패턴" # 2-12 는 안될듯 업데이트 필요
    ensure_iterable_printed_as_vertical(item_iterable=std_list, item_iterable_n='lines')
    for std_str in std_list:
        if all(str_positive in std_str for str_positive in signiture_list):
            match = pattern.search(std_str)
            if not match:
                ensure_printed(f'''{signiture_list}가 없습니다.  {'%%%FOO%%%' if LTA else ''}" ''', print_color='red')
                raise
            ensure_printed(str_working=rf'''match="{match}"  {'%%%FOO%%%' if LTA else ''}''')
            bus_id = match.group()
    if bus_id is None:
        ensure_printed(f'''bus_id=None  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        raise
    ensure_printed(str_working=rf'''bus_id={bus_id}  {'%%%FOO%%%' if LTA else ''}''', print_color="green")

    ensure_command_excuted_to_os(cmd="wsl --shutdown", encoding='utf-16')

    std_list = ensure_command_excuted_to_os(cmd=rf"wsl -d {wsl_distro_n} -- exit", encoding='utf-16')
    if check_signiture_in_loop(time_limit=10, working_list=std_list, signiture="제공된 이름의 배포가 없습니다",
                               signiture_found_ment=rf"'{cmd}' 할수없었습니다"):
        raise

    std_list = ensure_command_excuted_to_os(cmd="wsl -l -v", encoding='utf-16')
    ensure_command_excuted_to_os(cmd=rf"usbipd unbind -b {bus_id}", encoding='utf-16')
    ensure_command_excuted_to_os(cmd=rf"usbipd bind -b {bus_id}", encoding='utf-16')
    # ensure_command_excuted_to_os_like_person(cmd=rf"usbipd attach --wsl --busid {bus_id} --auto-attach")
    ensure_command_excuted_to_os(cmd=rf'start "" usbipd attach --wsl --busid {bus_id} --auto-attach')

    # usb/ip attached to wsl
    # signiture="제공된 이름의 배포가 없습니다" or 'xxxx'
    std_list = ensure_command_excuted_to_os(cmd=rf"wsl -d {wsl_distro_n} lsusb", encoding='utf-16')  # watch -n 1 lsusb
    if check_signiture_in_loop(time_limit=10, working_list=std_list, signiture="제공된 이름의 배포가 없습니다",
                               signiture_found_ment="wsl 에 attach 할수없었습니다"):
        raise
    if check_signiture_in_loop(time_limit=10, working_list=std_list, signiture="NVidia Corp.",
                               signiture_found_ment="wsl 에 attach 되었습니다"):
        return
