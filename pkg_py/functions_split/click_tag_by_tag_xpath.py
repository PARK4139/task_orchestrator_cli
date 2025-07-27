

import zlib
import yt_dlp
import win32con
import win32con
import win32com.client
import urllib.parse
import undetected_chromedriver as uc
import traceback
import tqdm
import tomllib
import toml
import threading
import sys
import speech_recognition as sr
import socket, time
import shlex
import requests
import re
import random
import pywintypes
import pythoncom
import pyaudio
import platform
import pickle
import paramiko
import pandas as pd
import os, inspect
import numpy as np
import nest_asyncio
import mysql.connector
import keyboard
import json
import ipdb
import inspect
import datetime
import colorama
import colorama

from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import quote
from telegram import Bot, Update
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from gtts import gTTS
from datetime import datetime, time
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import ResultSet
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def click_tag_by_tag_xpath(driver, tag_name, tag_property, tag_property_value):
    timeout = 10
    try:
        # Lazy Import (이 시점에 모듈을 불러옵니다)
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import ElementClickInterceptedException

        # 페이지가 로딩될 때까지 대기
        WebDriverWait(driver, timeout).until(lambda d: d.execute_script('return document.readyState') == 'complete')

        # 태그가 DOM에 존재하고 표시될 때까지 대기
        tag = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, f"//{tag_name}[{tag_property}()='{tag_property_value}']")))

        # 태그가 클릭 가능할 때까지 대기
        tag = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, f"//{tag_name}[{tag_property}()='{tag_property_value}']")))

        # 클릭을 방해하는 요소가 있을 경우, 배경을 클릭하거나 강제로 클릭을 시도
        try:
            tag.click()  # 클릭 시도
            print(f"태그 '{tag_name}' 속성 '{tag_property}={tag_property_value}' 클릭 완료.")
        except ElementClickInterceptedException:
            # 클릭 방해 요소가 있을 경우, 배경 요소 클릭 또는 배경 숨기기
            ensure_printed(str_working="클릭 방해 요소 발견, 배경을 클릭하거나 숨기려 시도합니다.")
            remove_block_hidden(driver=driver)
            # driver.execute_script("document.querySelector('.MuiBackdrop-root').style.display = 'none';")  # 배경 숨기기
            tag.click()  # 다시 클릭 시도
            print(f"태그 '{tag_name}' 속성 '{tag_property}={tag_property_value}' 클릭 완료.")

    except Exception as e:
        import traceback
        ensure_printed(f"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}", print_color='red')
        print(f"태그 '{tag_name}' 속성 '{tag_property}={tag_property_value}' 클릭 실패.")
