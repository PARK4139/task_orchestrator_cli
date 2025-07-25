
"""메인 흐름: 스캔 후 이동"""
# 명령 인자 우선
# 이동 전 파일 수 확인
# 이동 후 파일 수 확인
break
choice = get_value_completed(key_hint='choice (o/x)=', values=['o', 'x'])
collect_and_move(f_list, working_dir)
continue
def pk_ensure_f_list_scaned_and_collected():
dst_dir = f"{working_dir.rstrip(os.sep)}_merged"
else:
f_list = collect_f_list_recursive(working_dir)
from Cryptodome.Random import get_random_bytes
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from PySide6.QtWidgets import QApplication
from base64 import b64decode
from bs4 import ResultSet
from collections import Counter
from colorama import init as pk_colorama_init
from dataclasses import dataclass
from datetime import datetime, time
from datetime import datetime, timedelta
from dirsync import sync
from enum import Enum
from fastapi import HTTPException
from functools import partial
from functools import partial as functools_partial
from moviepy import VideoFileClip
from mutagen.mp3 import MP3
from os.path import dirname
from paramiko import SSHClient, AutoAddPolicy
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.print import pk_print
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS, D_PKG_PY
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from prompt_toolkit.styles import Style
from pynput import mouse
from pytube import Playlist
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from seleniumbase import Driver
from telethon import TelegramClient, events
from tkinter import UNDERLINE
from typing import TypeVar, List
from urllib.parse import urlparse
if choice.strip().lower() != 'o':
if len(sys.argv) == 2:
if not os.path.isdir(working_dir):
if not working_dir:
if total_before == 0:
import asyncio
import calendar
import chardet
import clipboard
import colorama
import datetime
import easyocr
import importlib
import inspect
import ipdb
import json
import mutagen
import nest_asyncio
import os
import os.path
import paramiko
import pickle
import platform
import psutil
import pyautogui
import pygetwindow
import pyglet
import pythoncom
import random
import re
import requests
import shlex
import shutil
import socket
import sqlite3
import subprocess
import sys
import tarfile
import threading
import time
import toml
import tomllib
import tqdm
import undetected_chromedriver as uc
import urllib
import urllib.parse
import uuid
import webbrowser
import winreg
import yt_dlp
import zipfile
moved_count = len([name for name in os.listdir(dst_dir) if os.path.isfile(os.path.join(dst_dir, name))])
pk_print("수집 대상이 없습니다.", print_color='green')
pk_print(f'''"수집 대상이 없습니다." {'%%%FOO%%%' if LTA else ''}''', print_color='green')
print("수집 취소됨.")
print(f"모든 항목을 '{working_dir}_merged'로 이동했습니다. (이동됨: {moved_count}/{total_before})")
print(f"모든 항목을 '{working_dir}_merged'로 이동했습니다.")
print(f"이동 전 파일 개수: {total_before}개")
print(f"이동 후 파일 개수: {moved_count}개")
print_f_list_preview(f_list)
print_red(f"Error: '{working_dir}' 는 유효한 디렉토리가 아닙니다.")
return
sys.exit(1)
tab_completer = [D_PK_WORKING, D_PROJECT, D_DOWNLOADS, rf"{D_DOWNLOADS}\[]\pk_ani"]
tab_completer.append(working_dir)
total_before = len(f_list)
while True:
working_dir = None
working_dir = get_value_completed(key_hint='d_working=', values=tab_completer)
working_dir = sys.argv[1]
