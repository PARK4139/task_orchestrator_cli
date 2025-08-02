import win32con
import win32com.client
import webbrowser
import tarfile
import sys
import string
import sqlite3
import socket
import re
import random

import pyglet
import pygetwindow
import pyautogui
import paramiko
import importlib
import easyocr
import clipboard
import chardet

from urllib.parse import quote, urlparse
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_state_printed import ensure_state_printed
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.directories import D_PK_WORKING
from passlib.context import CryptContext
from moviepy import VideoFileClip
from gtts import gTTS
from dirsync import sync
from datetime import datetime
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_printed import ensure_printed


def run_vpc_aifw_docker_container(vpc_data, config_remote_os):
    if vpc_data.vpc_type == 'no':
        config_remote_os(cmd='sudo run_container -b', **config_remote_os)
