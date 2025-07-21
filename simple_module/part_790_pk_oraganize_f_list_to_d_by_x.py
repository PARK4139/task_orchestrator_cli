import undetected_chromedriver as uc
import traceback
import tomllib
import tomllib
import toml
import time
import subprocess, time
import pywintypes
import pyautogui
import psutil
import pickle
import os
import numpy as np
import nest_asyncio
import mysql.connector
import mutagen
import importlib
import hashlib
import easyocr
import cv2
import colorama
import calendar
import browser_cookie3
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from tkinter import UNDERLINE
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated
from PIL import Image, ImageFilter
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from mutagen.mp3 import MP3
from functools import partial
from datetime import timedelta
from cryptography.hazmat.primitives import padding
from Cryptodome.Cipher import AES
from base64 import b64encode
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def pk_oraganize_f_list_to_d_by_x(d_working, ext, d_dst):
    import os

    if not os.path.exists(d_dst):
        os.makedirs(d_dst)  # 대상 디렉토리가 없으면 생성

    # 파일 이름별로 정리
    f_nx_list_dict = {}
    for f_nx in os.listdir(d_working):
        f_n, f_x = os.path.splitext(f_nx)
        if f_x == ext:
            if f_n in f_nx_list_dict:
                f_nx_list_dict[f_n].append(f_nx)
            else:
                f_nx_list_dict[f_n] = [f_nx]
        else:
            if f_n not in f_nx_list_dict:
                f_nx_list_dict[f_n] = []

    for f_n, files in f_nx_list_dict.items():
        for f_nx in files:
            f_src = os.path.join(d_working, f_nx)
            d_dst = os.path.join(d_dst, f_nx)
            pk_print(f"Moving: {f_src} -> {d_dst}", print_color='green')
            move_pnx(pnx=f_src, d_dst=d_dst, sequential_mode=1)
