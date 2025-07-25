
# from project_database.test_project_database import MySqlUtil
# 파일 이름별로 정리
d_dst = os.path.join(d_dst, f_nx)
def pk_oraganize_f_list_to_d_by_x(d_working, ext, d_dst):
else:
f_n, f_x = os.path.splitext(f_nx)
f_nx_list_dict = {}
f_nx_list_dict[f_n] = []
f_nx_list_dict[f_n] = [f_nx]
f_nx_list_dict[f_n].append(f_nx)
f_src = os.path.join(d_working, f_nx)
for f_n, files in f_nx_list_dict.items():
for f_nx in files:
for f_nx in os.listdir(d_working):
from Cryptodome.Cipher import AES
from PIL import Image, ImageFilter
from PySide6.QtWidgets import QApplication
from base64 import b64encode
from cryptography.hazmat.primitives import padding
from datetime import timedelta
from functools import partial
from mutagen.mp3 import MP3
from os.path import dirname
from passlib.context import CryptContext
from pathlib import Path
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.print import pk_print
from pkg_py.functions_split.print_state import pk_print_state
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.get_list_calculated import get_list_calculated
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.state_via_database import PkSqlite3DB
from prompt_toolkit import PromptSession
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import Driver
from tkinter import UNDERLINE
from urllib.parse import quote
from webdriver_manager.chrome import ChromeDriverManager
from yt_dlp import YoutubeDL
if f_n in f_nx_list_dict:
if f_n not in f_nx_list_dict:
if f_x == ext:
if not os.path.exists(d_dst):
import calendar
import colorama
import cv2
import easyocr
import hashlib
import importlib
import mutagen
import mysql.connector
import nest_asyncio
import numpy as np
import os
import pickle
import psutil
import pyautogui
import pywintypes
import subprocess, time
import time
import toml
import tomllib
import traceback
import undetected_chromedriver as uc
move_pnx(pnx=f_src, d_dst=d_dst, sequential_mode=1)
os.makedirs(d_dst)  # 대상 디렉토리가 없으면 생성
pk_print(f"Moving: {f_src} -> {d_dst}", print_color='green')
