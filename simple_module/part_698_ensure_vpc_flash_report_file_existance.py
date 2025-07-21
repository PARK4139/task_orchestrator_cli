import zlib
import win32con
import uuid
import urllib
import undetected_chromedriver as uc
import traceback
import tomllib
import toml
import timeit
import time
import subprocess
import socket
import pywintypes
# import pywin32
import pythoncom
import pyaudio
import math
import keyboard
import functools
import easyocr
import datetime
import cv2
import browser_cookie3
from urllib.parse import urlparse
from telegram import Bot, Update
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from pytube import Playlist
from PySide6.QtWidgets import QApplication
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_os import is_os_windows, is_os_wsl_linux

from PIL import Image
from pathlib import Path
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial
from datetime import timedelta
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from base64 import b64decode
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_etc import PkFilter, PK_UNDERLINE
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_330_get_d_working import get_d_working


def ensure_vpc_flash_report_file_existance(**config):
    # TODO
    vpc_type = config['vpc_type']
    flash_report_file_path = f"{vpc_type}_flash_report.txt"
    ensure_pnx_made(pnx=flash_report_file_path, mode='f', script_list=[
        "====================== ACU NO flash report ======================\n",
    ])
    with open(flash_report_file_path, "a") as f:
        f.write("ACU NO flash report\n")
