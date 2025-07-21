import zlib
import yt_dlp
# import win32gui
import win32con
import win32con
import undetected_chromedriver as uc
import toml
import timeit
import time
import tarfile
import sys
import sqlite3
import shlex
import re
import random
# import pywin32
# import pywin32
import pyglet
import pygetwindow
import psutil
import paramiko
import os.path
import numpy as np
import nest_asyncio
import json
import importlib
import easyocr
import clipboard
import chardet
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse, parse_qs, unquote
from tkinter import UNDERLINE
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB

from PIL import Image
from mutagen.mp3 import MP3
from enum import Enum
from dirsync import sync
from datetime import datetime, time
from datetime import date
from colorama import init as pk_colorama_init
from collections import Counter
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def ensure_launch_container(docker_cmd: list, container: str, name: str, pwd: str, port: int, data_dir: str):
    #
    import subprocess, time

    mount_arg = f"{data_dir}:/var/lib/mysql"
    try:
        subprocess.run(docker_cmd + ['inspect', container], check=True, stdout=subprocess.DEVNULL)
        pk_print(f"Container '{container}' already running")
    except subprocess.CalledProcessError:
        pk_print(f"Creating container '{container}'...", print_color='yellow')
        try:
            subprocess.run([
                *docker_cmd, 'run', '-d',
                '--name', container,
                '-e', f"MYSQL_ROOT_PASSWORD={pwd}",
                '-e', f"MYSQL_DATABASE={name}",
                '-p', f"{port}:3306",
                '-v', mount_arg,
                'mariadb:10.6'
            ], check=True)
        except subprocess.CalledProcessError as e:
            pk_print(f"Failed to create MariaDB container: {e}", print_color='red')
            raise
        pk_print('Waiting 20s for DB initialization')
        time.sleep(20)
