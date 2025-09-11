import zipfile
import yt_dlp

import win32con
import win32con
import webbrowser
import urllib.parse
import undetected_chromedriver as uc
import tqdm
import toml
import tarfile
import sys
import subprocess, time
import subprocess
import string
import socket
import shutil
import re


import pyautogui
import psutil
import paramiko
import os.path
import math
import ipdb
import inspect
import importlib
import hashlib
import easyocr
import cv2
import colorama
import clipboard
import calendar
from zipfile import BadZipFile
from urllib.parse import urlparse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.get_d_working import get_d_working
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING, D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_database import PkSqlite3DB

from sources.objects.pk_local_test_activate import LTA
from pathlib import Path
from passlib.context import CryptContext
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from dirsync import sync
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from sources.functions.get_nx import get_nx

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from sources.objects.pk_local_test_activate import LTA
import logging


def organize_d_list_by_stamp(d: str):
    """
    d 내에서 특정 stamp를 포함하는 _d_를 해당 stamp 이름의 _d_로 이동하는 함수.

    :param d: 탐색할 d 경로
    :param PROJECT_D: 프로젝트 d 경로 (stamp 목록을 불러올 f이 위치한 곳)
    """
    import os
    import re

    working_list = get_list_from_f(f=rf'{D_TASK_ORCHESTRATOR_CLI}\task_orchestrator_cli_sensitive\collect_magnets_from_nyaa_si.txt')

    # 불필요한 항목 remove
    working_list = get_list_removed_element_contain_prompt(working_list=working_list, prompt="#")
    working_list = get_list_deduplicated(working_list=working_list)
    working_list = get_list_removed_empty(working_list=working_list)
    working_list = get_list_striped_element(working_list=working_list)

    # 정규식을 사용하여 stamp 리스트 추출
    pattern = re.compile(r"(\[.*?\])\s*(.*)")
    "[ LIST ]" = []

    for item in working_list:
        match = pattern.match(item)
        if match:
            stamp = match.group(1).strip()
            "[ LIST ]".append(stamp)

    # 중복 remove
    "[ LIST ]" = get_list_deduplicated(working_list="[ LIST ]")

    # d 탐색 및 이동
    for root, d_nx_list, _ in os.walk(d):
        for d_nx in d_nx_list:
            for stamp in "[ LIST ]":
                if d_nx != stamp and stamp in d_nx:  # _d_명이 stamp를 포함하는지 확인
                    d_stamp = os.path.join(root, stamp)  # stamp 이름의 d 경로 생성
                    os.makedirs(d_stamp, exist_ok=True)

                    d_src = os.path.join(root, d_nx)
                    d_dst = os.path.join(d_stamp, d_nx)
                    logging.debug(f'''d_dst={d_dst} d_src={d_src}  {'%%%FOO%%%' if LTA else ''}''')
                    try:
                        os.rename(d_src, d_dst)
                    except:
                        logging.debug(                f'''d_dst does exists already. 아마도 이동 안할것 d_dst={d_dst}  {'%%%FOO%%%' if LTA else ''}''')  # todo : 동작 모니터링 필요
