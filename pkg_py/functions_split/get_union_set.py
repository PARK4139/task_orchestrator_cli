import zipfile
import yt_dlp

import urllib.parse
import traceback
import tqdm
import time
import string
import pyautogui
import pickle
import paramiko
import numpy as np
import nest_asyncio
import json
import importlib
import easyocr
import cv2
import clipboard

from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pytube import Playlist
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once

from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from enum import Enum
from datetime import datetime
from Cryptodome.Random import get_random_bytes
from base64 import b64encode
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.get_d_working import get_d_working


def get_union_set(set_a, set_b):
    """합집합 A ∪ B"""
    return set(set_a) | set(set_b)
