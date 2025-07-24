import zipfile
# import win32process
import win32con
import win32con
import win32com.client
import webbrowser
import uuid
import urllib
import traceback
import tomllib
import tomllib
import toml
import time
import threading
import tarfile
import sys
import sqlite3
import speech_recognition as sr
import socket, time
import socket
import shutil
import secrets
import requests
import re
import pywintypes
import pyglet
import pygetwindow
import pyautogui
import pyaudio
import psutil
import paramiko
import pandas as pd
import os
import nest_asyncio
import mysql.connector
import math
import keyboard
import ipdb
import datetime
import cv2
import chardet
import browser_cookie3
import asyncio
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram import Bot, Update
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PKG_TXT, D_WORKING
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from PIL import Image, ImageFont, ImageDraw
from PIL import Image, ImageFilter
from PIL import Image
from pathlib import Path
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from dirsync import sync
from datetime import datetime, timedelta
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def kill_chrome_tab_duplicated():
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    chrome_tab_urls_processed = []  # 이미 처리된 URL을 저장하는 리스트
    loop_limit = 10
    loop_out_cnt = 0

    while 1:
        window_title = "Chrome"
        if is_window_opened(window_title_seg=window_title):
            ensure_window_to_front(window_title_seg=window_title)

        pk_print(str_working=rf'''loop_out_cnt="{loop_out_cnt}"  {'%%%FOO%%%' if LTA else ''}''')
        pk_print(str_working=rf'''loop_limit="{loop_limit}"  {'%%%FOO%%%' if LTA else ''}''')

        # 탭을 전환하고 URL을 가져옵니다.
        pk_press("ctrl", "l")
        pk_sleep(milliseconds=5)
        url_dragged = get_txt_dragged()

        # 중복 여부 확인
        if url_dragged in chrome_tab_urls_processed:
            pk_print(str_working=rf'''URL already processed: "{url_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
            pk_press("ctrl", "tab")  # 다음 탭으로 이동
            loop_out_cnt += 1
            if loop_out_cnt >= loop_limit:
                break
            continue

        # 다음 탭으로 전환 후 URL 가져오기
        pk_press("ctrl", "tab")
        pk_sleep(milliseconds=5)
        pk_press("ctrl", "l")
        pk_sleep(milliseconds=5)
        url_dragged_new = get_txt_dragged()

        pk_print(str_working=rf'''url_dragged="{url_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
        pk_print(str_working=rf'''url_dragged_new="{url_dragged_new}"  {'%%%FOO%%%' if LTA else ''}''')

        # 중복된 URL이면 탭 닫기
        if url_dragged == url_dragged_new:
            pk_print(str_working=rf'''Closing duplicate tab for URL: "{url_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
            pk_press("ctrl", "w")  # 탭 닫기
            continue

        # 처리된 URL을 리스트에 추가
        chrome_tab_urls_processed.append(url_dragged)
        pk_print(
            str_working=rf'''chrome_tab_urls_processed="{chrome_tab_urls_processed}"  {'%%%FOO%%%' if LTA else ''}''')

        # 최대 반복 횟수 초과 시 종료
        loop_out_cnt += 1
        if loop_out_cnt >= loop_limit:
            break
