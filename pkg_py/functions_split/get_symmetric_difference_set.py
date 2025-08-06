import yt_dlp

import win32con
import uuid
import urllib.parse
import urllib
import tomllib
import time
import threading
import tarfile
import socket
import secrets
import random, math
import pywintypes
import pygetwindow
import platform
import paramiko
import numpy as np
import nest_asyncio
import json
import inspect
import importlib
import hashlib
import datetime
import clipboard
import chardet
import calendar

import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from typing import TypeVar, List
from tkinter import UNDERLINE
from telegram import Bot, Update
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from pynput import mouse
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
# pk_#
# pk_#
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories  import D_PROJECT
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_CACHE_PRIVATE
from pkg_py.system_object.state_via_database import PkSqlite3DB

# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.get_list_calculated import get_list_calculated

from pathlib import Path
from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from moviepy import VideoFileClip
from fastapi import HTTPException
from datetime import timedelta
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from bs4 import ResultSet
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.is_d import is_d
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.get_d_working import get_d_working


def get_symmetric_difference_set(set_a, set_b):
    """대칭차집합 A △ B (A 또는 B에만 있는 요소들)"""
    return set(set_a) ^ set(set_b)
