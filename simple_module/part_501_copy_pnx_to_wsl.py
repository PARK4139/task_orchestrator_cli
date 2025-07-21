import zlib
import zipfile
import yt_dlp
import winreg
# import win32gui
import win32con
import webbrowser
import urllib.parse
import urllib
import timeit
import time
import subprocess, time
import subprocess
import string
import sqlite3
import speech_recognition as sr
import shutil
import shlex
import requests
# import pywin32
import pythoncom
import psutil
import paramiko
import pandas as pd
import os, inspect
import nest_asyncio
import mutagen
import keyboard
import hashlib
import functools
import easyocr
import datetime
import colorama
import clipboard
import chardet
import calendar
import browser_cookie3
import asyncio
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from urllib.parse import unquote, urlparse, parse_qs
from urllib.parse import quote
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_directories import D_WORKING, D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_os import is_os_windows

from pathlib import Path
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from fastapi import HTTPException
from datetime import timedelta
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_etc import PkFilter, PK_UNDERLINE
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def copy_pnx_to_wsl(f, dst="~/Downloads/"):
    f = get_pnx_wsl_unix_style(f)
    cmd_to_os(cmd=rf'wsl sudo cp -r {f} {dst}')
