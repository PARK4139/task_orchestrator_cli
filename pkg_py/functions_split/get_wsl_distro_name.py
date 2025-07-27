import yt_dlp

import win32com.client
import webbrowser
import traceback
import tqdm
import tomllib
import toml
import timeit
import time
import threading
import tarfile
import subprocess
import speech_recognition as sr
import socket
import shlex
import re
import random
import pythoncom
import pygetwindow
import pyautogui
import paramiko
import os, inspect
import numpy as np
import nest_asyncio
import mysql.connector
import math
import json
import ipdb
import hashlib
import functools
import colorama
import colorama
import chardet

import asyncio
from webdriver_manager.chrome import ChromeDriverManager
from telegram import Bot, Update
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext

from PIL import Image, ImageFont, ImageDraw
from paramiko import SSHClient, AutoAddPolicy
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import lru_cache
from dirsync import sync
from datetime import datetime
from datetime import date
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Cryptodome.Random import get_random_bytes
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def get_wsl_distro_name(cmd):
    wsl_distro_name = []
    std_out_list = ensure_command_excuted_to_os(cmd=cmd, encoding='utf-16')
    for line_str in std_out_list:
        line_str = line_str.strip()
        if line_str.startswith("NAME"):
            continue
        if line_str.startswith("*"):
            line_str = line_str.replace("* ", "")
            line_str = line_str.strip()
        parts = line_str.split(' ')
        name = parts[0]
        line_str = line_str.strip()
        wsl_distro_name.append(name)
    return wsl_distro_name
