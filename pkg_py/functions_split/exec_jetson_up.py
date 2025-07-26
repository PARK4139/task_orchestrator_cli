

import win32com.client
import urllib.parse
import undetected_chromedriver as uc
import tqdm
import toml
import toml
import string
import sqlite3
import speech_recognition as sr
import shutil
import secrets
import pywintypes


import platform
import paramiko
import keyboard
import json
import ipdb
import hashlib
import datetime
import cv2
import colorama

from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from telethon import TelegramClient, events
from telegram import Bot
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.press import press
from pkg_py.functions_split.print_state import print_state

from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.is_os_windows import is_os_windows

from PIL import Image, ImageFont, ImageDraw
from PIL import Image
from passlib.context import CryptContext
from os import path
from moviepy import VideoFileClip
from fastapi import HTTPException
from dirsync import sync
from datetime import timedelta
from datetime import datetime, time
from datetime import date
from dataclasses import dataclass
from base64 import b64decode
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.ensure_printed import ensure_printed


def exec_jetson_up():
    todo('%%%FOO%%%')
    # ./install.py
    # ./install.py
