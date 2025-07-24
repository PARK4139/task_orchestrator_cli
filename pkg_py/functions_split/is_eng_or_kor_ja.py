import zlib
import winreg


import traceback
import toml
import threading
import sqlite3
import socket
import shlex
import pythoncom
import platform
import paramiko
import numpy as np
import mysql.connector
import math
import keyboard
import json
import ipdb
import datetime
import cv2
import colorama
import calendar

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE

from PIL import Image, ImageFilter
from PIL import Image
from pathlib import Path
from os.path import dirname
from moviepy import VideoFileClip
from gtts import gTTS
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from base64 import b64decode
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.is_f import is_f
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.system_object.local_test_activate import LTA


def is_eng_or_kor_ja(text: str):
    """
    한글처리 :
        한영숫특 :
        한숫특 :
        한숫
        한특
        숫특
        특
        숫
    영어처리 :
        영숫특
        영특
        영숫
        영
    일어처리 :
    빠진거있나? 일단 여기까지

    문자구성 판별기가 필요하다
        return "eng, kor, jap, special_characters ", ... 이런식 > what_does_this_consist_of() 를 만들었다.
    """
    if is_only_speacial_characters(text=text):
        return "ko"
    elif is_only_no(text=text):
        return "ko"
    elif is_containing_kor(text=text):
        return "ko"
    if is_only_eng_and_no_and_speacial_characters(text=text):
        return "en"
    elif is_only_eng_and_speacial_characters(text=text):
        return "en"
    elif is_only_eng_and_no(text=text):
        return "en"
    elif is_only_eng(text=text):
        return "en"
    else:
        return "ko"
