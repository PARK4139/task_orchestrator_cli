
import webbrowser
import urllib.parse
import tqdm
import tomllib
import tarfile
import subprocess
import sqlite3
import socket, time
import socket
import random
import pywintypes
import pyglet
import pygetwindow
import pandas as pd
import mutagen
import keyboard
import colorama
import calendar

from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
from pynput import mouse
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.performance_logic import ensure_seconds_measured, pk_measure_memory
from pathlib import Path
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.is_f import is_f
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.ensure_printed import ensure_printed


def keyDown(key: str):
    import inspect
    import pyautogui
    func_n = inspect.currentframe().f_code.co_name
    pyautogui.keyDown(key)
