# import win32gui
# import win32gui
import win32con
import tarfile
import sqlite3
import socket, time
import re
import random, math
import pywintypes
import pyautogui
import pyaudio
import psutil
import pandas as pd
import os
import numpy as np
import nest_asyncio
import mysql.connector
import mutagen
import functools
import clipboard
import calendar
import asyncio
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.get_list_calculated import get_list_calculated

from PIL import Image
from functools import partial
from fastapi import HTTPException
from dirsync import sync
from datetime import datetime
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.pk_print import pk_print


def is_prompt_on_screen(prompt):
    # OCR을 통해 텍스트 추출
    screenshot = get_screenshot()
    extreact_texts = get_extreact_texts_from_image_via_easyocr(screenshot)
    text_extracted = " ".join([r[1] for r in extreact_texts])

    if is_prompt_in_text(prompt=prompt, text=text_extracted):
        return 1
    else:
        return 0
