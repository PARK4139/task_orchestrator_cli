import zipfile
import yt_dlp
# import win32process
import win32con
import urllib.parse
import tomllib
import toml
import threading
import tarfile
import subprocess
import string
import socket
import shutil
import secrets
import pywintypes
import pygetwindow
import pickle
import nest_asyncio
import mutagen
import inspect
import functools
import easyocr
import colorama
import asyncio
from zipfile import BadZipFile
from urllib.parse import urlparse
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from queue import Queue, Empty
from pytube import Playlist
from pynput import mouse
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated
from PIL import Image
from mysql.connector import connect, Error
from fastapi import HTTPException
from datetime import datetime, timedelta
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from bs4 import BeautifulSoup
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def get_cnts_of_line_of_f(f):
    with open(file=f, mode='r') as file:
        return sum(1 for line in file)
