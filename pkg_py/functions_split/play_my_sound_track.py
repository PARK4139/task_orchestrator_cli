import zipfile
import yt_dlp
import winreg
# import win32gui
# import win32gui
import win32con
import win32com.client
import webbrowser
import uuid
import urllib.parse
import undetected_chromedriver as uc
import tomllib
import tomllib
import toml
import toml
import subprocess
import string
import speech_recognition as sr
import shutil
import secrets
import re
import random, math
import random
import pywintypes
# import pywin32            
# import pywin32
import pyglet
import pyaudio
import psutil
import platform
import os.path
import os
import numpy as np
import nest_asyncio
import math
import json
import importlib
import hashlib
import colorama
import calendar
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from tkinter import UNDERLINE
from telegram import Bot, Update
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from queue import Queue, Empty
from pytube import Playlist
from pynput import mouse
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.map_massages import PkMessages2025
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated

from paramiko import SSHClient, AutoAddPolicy
from os.path import dirname
from mutagen.mp3 import MP3
from functools import lru_cache
from fastapi import HTTPException
from datetime import timedelta
from datetime import datetime, time
from cryptography.hazmat.primitives import padding
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def play_my_sound_track():
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    # cmd_to_os(cmd=rf'taskkill /f /im "alsong.exe" ', debug_mode=True)

    cmd_to_os(cmd=rf'explorer "{F_PKG_SOUND_POTPLAYER64_DPL}" ')
