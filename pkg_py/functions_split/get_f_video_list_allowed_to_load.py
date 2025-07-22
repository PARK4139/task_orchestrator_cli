import yt_dlp
import win32con
import win32com.client
import timeit
import time
import subprocess, time
import subprocess
import string
import sqlite3
import shlex
import re
# import pywin32
import psutil
import pandas as pd
import os, inspect
import numpy as np
import nest_asyncio
import json
import ipdb
import inspect
import importlib
import hashlib
import datetime
import chardet
import calendar
import browser_cookie3
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from telegram import Bot
from selenium.webdriver.common.action_chains import ActionChains
from pynput import mouse
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.pk_print_once import pk_print_once

from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.pk_system_object.etc import PkFilter
from pkg_py.pk_system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated
from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from gtts import gTTS
from datetime import datetime, timedelta
from datetime import date
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from collections import Counter
from base64 import b64encode
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def get_f_video_list_allowed_to_load(ext_list_allowed, d_working):
    import os
    if LTA:
        pk_print(f'''ext_list_allowed={ext_list_allowed}  {'%%%FOO%%%' if LTA else ''}''')
    f_video_list_allowed = []
    pnx_list = get_pnx_list_from_d_working(d_working=d_working, with_walking=0)
    write_list_to_f(working_list=pnx_list, f=F_VIDEO_LIST_ALLOWED_TO_LOAD_TXT, mode='w')

    for f in get_list_from_f(F_VIDEO_LIST_ALLOWED_TO_LOAD_TXT):
        f = f.replace("\n", '')
        f_x = os.path.splitext(f)[1].replace("\n", '')
        f_nx = os.path.basename(f).lower()

        if not f_x:  # 확장자가 없을 경우 빈 문자열이기 때문에 예외 처리
            if LTA:
                pk_print(f"[NOT ALLOWED] [확장자 없음]: {f}", print_color='red')
            continue

        f_x = f_x.lower()  # 확장자가 있을 때만 소문자로 변환

        if f_x not in ext_list_allowed:
            if LTA:
                pk_print(f"[NOT ALLOWED] [확장자 불가]: f={f}", print_color='red')
            continue

        if any(keyword in f_nx for keyword in {"seg", "temp"}):
            if LTA:
                pk_print(f"[NOT ALLOWED] [금지 키워드 포함] : f={f} f_x={f_x}", print_color='red')
            continue
        if LTA:
            pk_print(f"[ALLOWED] [확장자 가능]: f={f} f_x={f_x}", print_color='green')
        f_video_list_allowed.append(f)

    return f_video_list_allowed
