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
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_printed_once import ensure_printed_once
import logging
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.ensure_console_cleared import ensure_console_cleared


from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER

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

from sources.functions.is_f import is_f

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.objects.pk_local_test_activate import LTA

from sources.objects.pk_local_test_activate import LTA


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
