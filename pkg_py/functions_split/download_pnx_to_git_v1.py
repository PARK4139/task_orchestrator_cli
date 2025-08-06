import zipfile
import winreg

import win32con
import win32con
import urllib.parse
import urllib
import undetected_chromedriver as uc
import traceback
import tqdm
import tomllib
import toml
import tarfile
import sys
import string
import speech_recognition as sr
import socket
import shutil
import secrets


import pythoncom
import pyglet
import pygetwindow
import pyaudio
import platform
import os.path
import os
import numpy as np
import nest_asyncio
import json
import ipdb
import inspect
import functools
import datetime
import cv2
import colorama
import colorama

from urllib.parse import quote, urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
# pk_#
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
# from pkg_py.system_object.print_red import print_red

from PIL import Image, ImageFilter
from PIL import Image
from pathlib import Path
from paramiko import SSHClient, AutoAddPolicy
from moviepy import VideoFileClip
from functools import partial
from functools import lru_cache
from dirsync import sync
from datetime import timedelta
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from bs4 import BeautifulSoup
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def download_pnx_to_git_v1(d_working, git_repo_url, commit_msg, branch_n):
    import traceback
    from colorama import init as pk_colorama_init

    ensure_colorama_initialized_once()

    try:
        if not does_pnx_exist(pnx=d_working):
            ensure_pnx_made(pnx=d_working, mode='d')

        d_git = rf"{d_working}/.git"

        if not does_pnx_exist(pnx=d_git):
            std_list = ensure_command_excuted_to_os(f'git clone -b {branch_n} {git_repo_url} {d_working}')
            debug_state_for_py_data_type('%%%CLONE%%%', std_list)

            if any("fatal:" in line.lower() for line in std_list):
                ensure_printed(f"Git clone 실패: {std_list}", print_color='red')
                return
        else:
            os.chdir(d_working)
            std_list = ensure_command_excuted_to_os(f'git pull origin {branch_n}')
            debug_state_for_py_data_type('%%%PULL%%%', std_list)

            if any("fatal:" in line.lower() for line in std_list):
                ensure_printed(f"Git pull 실패: {std_list}", print_color='red')
                return

        ensure_printed(f"Git 작업 완료: {d_working} {'%%%FOO%%%' if LTA else ''}", print_color='green')

    except Exception:
        ensure_printed(f"{traceback.format_exc()} {'%%%FOO%%%' if LTA else ''}", print_color='red')
