import zipfile
import winreg
# import win32process
# import win32gui
import webbrowser
import urllib
import tqdm
import tomllib
import time
import tarfile
import sqlite3
import speech_recognition as sr
import socket
import secrets
import pywintypes
import pyglet
import pyaudio
import platform
import pickle
import os.path
import math
import functools
import easyocr
import clipboard
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PySide6.QtWidgets import QApplication
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from fastapi import HTTPException
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from bs4 import BeautifulSoup
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.is_f import is_f
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.pk_print import pk_print


def pk_input_v44_uv_theme(
        str_working: str,
        limit_seconds: int = 30,
        return_default: str | None = None,
        *,
        masked: bool = False,
        fuzzy_accept: list[tuple[str, ...]] | None = None,
        validator=None,
        vi_mode: bool = True,
