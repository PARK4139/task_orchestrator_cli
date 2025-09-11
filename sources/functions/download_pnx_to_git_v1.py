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
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front


from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.ensure_command_executed import ensure_command_executed

from sources.functions.ensure_console_cleared import ensure_console_cleared

from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.encodings import Encoding


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
from sources.functions.get_nx import get_nx

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def download_pnx_to_git_v1(d_working, git_repo_url, commit_msg, branch_n):
    import traceback
    from colorama import init as pk_colorama_init

    ensure_task_orchestrator_cli_colorama_initialized_once()

    try:
        if not is_pnx_existing(pnx=d_working):
            ensure_pnx_made(pnx=d_working, mode='d')

        d_git = rf"{d_working}/.git"

        if not is_pnx_existing(pnx=d_git):
            std_list = ensure_command_executed(f'git clone -b {branch_n} {git_repo_url} {d_working}')
            debug_state_for_py_data_type('%%%CLONE%%%', std_list)

            if any("fatal:" in line.lower() for line in std_list):
                logging.debug(f"Git clone 실패: {std_list}")
                return
        else:
            os.chdir(d_working)
            std_list = ensure_command_executed(f'git pull origin {branch_n}')
            debug_state_for_py_data_type('%%%PULL%%%', std_list)

            if any("fatal:" in line.lower() for line in std_list):
                logging.debug(f"Git pull 실패: {std_list}")
                return

        logging.debug(f"Git 작업 완료: {d_working} {'%%%FOO%%%' if LTA else ''}")

    except Exception:
        logging.debug(f"{traceback.format_exc()} {'%%%FOO%%%' if LTA else ''}")
