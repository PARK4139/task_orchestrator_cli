import winreg
import webbrowser
import traceback
import tqdm
import tomllib
import toml
import timeit
import time
import shlex
import secrets
# import pywin32
import pythoncom
import pygetwindow
import paramiko
import pandas as pd
import os
import nest_asyncio
import json
import ipdb
import functools
import cv2
import colorama
import chardet
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PySide6.QtWidgets import QApplication
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_print_once import pk_print_once

from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.pk_system_object.etc import PkFilter
from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from enum import Enum
from dirsync import sync
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from bs4 import ResultSet
from bs4 import BeautifulSoup
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.functions_split.get_pnx_list import get_pnx_list


def rename_pnxs_from_pattern_to_pattern_new_via_routines_at_d(d, mode, with_walking):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    # pattern=r'(\[.*?\])'  # [문자열]
    rename_pnxs_from_pattern_twice_to_pattern_new(pnx=d,
                                                  pattern=r'\d{4}_\d{2}_\d{2}_(월|화|수|목|금|토|일)_\d{2}_\d{2}_\d{2}_\d{3}',
                                                  mode=mode, with_walking=with_walking)
    rename_pnxs_from_pattern_twice_to_pattern_new(pnx=d, pattern=r'\d{4}_\d{2}_\d{2}_\d{2}_\d{2}_\d{2}', mode=mode,
                                                  with_walking=with_walking)
    rename_pnxs_from_pattern_twice_to_pattern_new(pnx=d, pattern=r'_\d{11}_\d{11}_', mode=mode,
                                                  with_walking=with_walking)
    rename_pnxs_from_pattern_twice_to_pattern_new(pnx=d, pattern=r'_\d{10}_\d{10}_', mode=mode,
                                                  with_walking=with_walking)
    rename_pnxs_from_pattern_twice_to_pattern_new(pnx=d, pattern=r'_\d{11}_', mode=mode, with_walking=with_walking)

    rename_pnxs_from_pattern_once_to_pattern_new(src=d,
                                                 pattern=r'\d{4}_\d{2}_\d{2}_(월|화|수|목|금|토|일)_\d{2}_\d{2}_\d{2}_\d{3}',
                                                 pattern_new="_", mode=mode, with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'jhp##\d{4}_\d{2}_\d{2}', pattern_new="[jhp##]",
                                                 mode=mode, with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'jhp##\d{8}', pattern_new="[jhp##]", mode=mode,
                                                 with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'\$\d{22}', pattern_new="_", mode=mode,
                                                 with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'_\d{29}_', pattern_new="_", mode=mode,
                                                 with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'\d{4}_\d{2}_\d{2}_\d{2}_\d{2}_\d{2}', pattern_new=".",
                                                 mode=mode, with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'_\d{8}_', pattern_new=".", mode=mode,
                                                 with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'_\d{11}.', pattern_new=".", mode=mode,
                                                 with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'_\d{11}_', pattern_new=".", mode=mode,
                                                 with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'_\d{11}', pattern_new="", mode=mode,
                                                 with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'^seg ', pattern_new="_", mode=mode,
                                                 with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'^_', pattern_new="[시작문자]", mode=mode,
                                                 with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'^#', pattern_new="[시작문자]", mode=mode,
                                                 with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'^The ', pattern_new="[시작문자]", mode=mode,
                                                 with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'_$', pattern_new="[끝문자]", mode=mode,
                                                 with_walking=with_walking)
    rename_pnxs_from_pattern_once_to_pattern_new(src=d, pattern=r'\(([^)]+)\)(?=.*\(\1\))', pattern_new="[중복문자]",
                                                 mode=mode,
                                                 with_walking=with_walking)  # () 안의 중복문자인 경우데 대한 처리 (a)(a) 인 경우 (a)만 남김
    # rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'^.', pattern_new="_", mode=mode)  # 시작문자 # 첫글자가 없어진다... 씆지말자
    # rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'^ ', pattern_new="_", mode=mode)  # 시작문자 # 업데이트가 되긴하는데 ^_ 이 왜 안되는지 모르겠다.
    # rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{11}$', pattern_new="",mode=mode) # 끝문자 # 끝문자 안되는 것 같은데...
    # rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d+$', pattern_new="",mode=mode) # 끝문자
    # rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{10}_\d{10}_', pattern_new="",mode=mode)
    # rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{10}_', pattern_new="",mode=mode)
    # rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern= r'\d{10}', pattern_new="",mode=mode)
    # rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'\$\d{22}', pattern_new="",mode=mode)
    # rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{11}', pattern_new="",mode=mode)
