import yt_dlp
import winreg
# import win32gui
import win32con
import webbrowser
import uuid
import urllib
import tqdm
import tomllib
import tomllib
import toml
import time
import threading
import tarfile
import sys
import subprocess, time
import subprocess
import sqlite3
import speech_recognition as sr
import shutil
import shlex
import secrets
import requests
# import pywin32
import pythoncom
import pygetwindow
import psutil
import platform
import pickle
import paramiko
import os.path
import os
import mysql.connector
import math
import ipdb
import cv2
import colorama
import colorama
import calendar
import browser_cookie3
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext

from pathlib import Path
from passlib.context import CryptContext
from os import path
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import lru_cache
from dirsync import sync
from datetime import timedelta
from datetime import datetime, timedelta
from datetime import datetime, time
from datetime import datetime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def push_pnx_to_github(d_working, git_repo_url, commit_msg, branch_n):
    from colorama import init as pk_colorama_init
    pk_colorama_init_once()
    pk_print(f'''commit_msg={commit_msg} {'%%%FOO%%%' if LTA else ''}''')
    if not is_internet_connected():
        return
    if not does_pnx_exist(pnx=d_working):
        ensure_pnx_made(pnx=d_working, mode='d')
    pk_chdir(d_dst=d_working)
    d_git = rf"{d_working}/.git"
    std_list = None
    state_done = [0, 0, 0, 0]
    while 1:
        if state_done[0] == 0:
            if not does_pnx_exist(pnx=d_git):
                std_list = cmd_to_os(cmd=rf'git init')
                continue
        state_done[0] = 1
        pk_print(f'''state_done={state_done} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        if state_done[1] == 0:
            std_list = cmd_to_os(cmd=rf'git add .')  # git add * 과는 약간 다름.
            # signiture_list = ["The following paths are ignored by one of your .gitignore files:"]
            if not len(std_list) == 0:
                pk_print(working_str=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
                continue
            # if not any(str_working in std_list for str_working in signiture_list):
            #     continue
        state_done[1] = 1
        pk_print(f'''state_done={state_done} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        if state_done[2] == 0:
            std_list = cmd_to_os(cmd=rf'git commit -m "{commit_msg}"')
            std_list = cmd_to_os(cmd=rf'git commit -m "{commit_msg}"')
            signiture_list = ["nothing to commit, working tree clean"]
            if not any(str_working in std_list for str_working in signiture_list):
                pk_print(working_str=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
                continue
        state_done[2] = 1
        pk_print(f'''state_done={state_done} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        if state_done[3] == 0:
            std_list = cmd_to_os(cmd=rf'git push origin {branch_n}')
            signiture_list = ["Everything up-to-date", "branch 'main' set up to track 'origin/main'."]
            if not any(str_working in std_list for str_working in signiture_list):
                continue
        state_done[3] = 1
        pk_print(f'''state_done={state_done} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        break
