

import zlib
import yt_dlp
import winreg
import win32con
import win32com.client
import undetected_chromedriver as uc
import tomllib
import time
import tarfile
import sys
import speech_recognition as sr
import socket
import random
import pywintypes
import os.path
import mysql.connector
import ipdb
import inspect
import datetime
import colorama
import chardet
import browser_cookie3
import asyncio
from urllib.parse import urlparse
from selenium.webdriver.support import expected_conditions as EC
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from os.path import dirname
from gtts import gTTS
from functools import partial as functools_partial
from fastapi import HTTPException
from enum import Enum
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from base64 import b64decode
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def get_center_of_bounding_box(bounding_box):
    import inspect
    func_n = inspect.currentframe().f_code.co_name

    """
    바운딩 박스 좌표를 받아서, 그 중심 좌표를 반환하는 함수.

    :param bounding_box: 바운딩 박스 좌표 [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    :return: 중심 좌표 (x, y)
    """
    # 네 점의 x, y 좌표를 각각 합산
    if bounding_box is None:
        return None
    x_coords = [point[0] for point in bounding_box]
    y_coords = [point[1] for point in bounding_box]

    # x, y 평균값을 구하여 중심 좌표 계산
    center_x = sum(x_coords) / 4
    center_y = sum(y_coords) / 4

    return center_x, center_y
