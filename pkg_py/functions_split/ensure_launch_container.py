import zlib
import yt_dlp

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
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once

from pkg_py.functions_split.cmd_to_os import cmd_to_os

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.state_via_database import PkSqlite3DB

from PIL import Image
from mutagen.mp3 import MP3
from enum import Enum
from dirsync import sync
from datetime import datetime, time
from datetime import date
from colorama import init as pk_colorama_init
from collections import Counter
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_launch_container(docker_cmd: list, container: str, name: str, pwd: str, port: int, data_dir: str):
    #
    import subprocess, time

    mount_arg = f"{data_dir}:/var/lib/mysql"
    try:
        subprocess.run(docker_cmd + ['inspect', container], check=True, stdout=subprocess.DEVNULL)
        ensure_printed(f"Container '{container}' already running")
    except subprocess.CalledProcessError:
        ensure_printed(f"Creating container '{container}'...", print_color='yellow')
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
            ensure_printed(f"Failed to create MariaDB container: {e}", print_color='red')
            raise
        ensure_printed('Waiting 20s for DB initialization')
        time.sleep(20)
