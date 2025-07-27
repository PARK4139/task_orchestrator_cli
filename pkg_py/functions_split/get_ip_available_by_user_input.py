import zlib


import win32con
import webbrowser
import undetected_chromedriver as uc
import tqdm
import time
import threading
import tarfile
import speech_recognition as sr
import re
import pywintypes
import pyautogui
import psutil
import paramiko
import os.path
import nest_asyncio
import mysql.connector
import ipdb
import inspect
import datetime

import asyncio
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from urllib.parse import quote
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image, ImageFont, ImageDraw
from PIL import Image
from os.path import dirname
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from datetime import datetime, timedelta
from datetime import datetime
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_d_working import get_d_working


def get_ip_available_by_user_input():
    try:
        while True:
            available_ip_list = get_ip_available_list()
            available_ip_without_localhost_list = []
            available_ip_only_localhost_list = []
            local_ip = get_local_ip()
            # ensure_printed(str_working=rf'''SELECT REMOTE DEVICE IP BY NUMBER REFER TO BELOW (or 'R'=RETRY   0='TBD IP')  {'%%%FOO%%%' if LTA else ''}''', print_color='white')
            # ensure_printed("AVAILABLE IP LIST:", print_color='blue')
            for idx, ip_info in enumerate(available_ip_list):
                if len(ip_info) >= 2:
                    name, ip = ip_info[0], ip_info[1]
                else:
                    ip = ip_info[0]  # name 정보가 없으면 그냥 ip만 사용
                me_marker = ' (me)' if ip == local_ip or ip == 'localhost' else ''
                # ensure_printed(f"{idx + 1}: {ip}{me_marker}", print_color='blue')
                if me_marker == '':
                    available_ip_without_localhost_list.append(f'{ip}')
                elif not me_marker == '':
                    available_ip_only_localhost_list.append(f'{ip}{me_marker}')

            available_ip_without_localhost_list.append('R(RETRY)')
            available_ip_without_localhost_list.append('0(TBD IP)')

            user_input = get_value_completed(key_hint="user_input=", values=available_ip_without_localhost_list)
            if user_input.upper() == '0' or '0(TBD IP)':
                ip = None
                return ip
            if user_input.upper() == '':  # IF USER INPUTS '', RETRY
                continue
            if user_input.upper() == 'R' or 'R(RETRY)':
                ensure_printed("RETRYING THE CONNECTION TEST...", print_color='yellow')
                continue
            user_input = int(user_input) - 1
            if 0 <= user_input < len(available_ip_list):
                ip = available_ip_list[user_input][1]
                return ip
            else:
                ensure_printed("Invalid choice. Please run the program again.", print_color='red')
                raise
    except ValueError:
        ensure_printed("Invalid input. Please enter a number.", print_color='red')
        raise
