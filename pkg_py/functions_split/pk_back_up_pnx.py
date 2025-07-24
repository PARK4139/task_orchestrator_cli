import yt_dlp

import win32con
import win32con
import uuid
import undetected_chromedriver as uc
import tqdm
import toml
import timeit
import time
import threading
import sys
import subprocess
import string
import socket
import re

import pythoncom
import pickle
import os
import nest_asyncio
import mutagen
import keyboard
import json
import hashlib
import functools
import easyocr
import datetime
import chardet
import calendar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.cmd_to_os import cmd_to_os

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.directories import D_WORKING
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.get_list_calculated import get_list_calculated

from PIL import Image, ImageFilter
from mysql.connector import connect, Error
from gtts import gTTS
from functools import lru_cache
from fastapi import HTTPException
from datetime import datetime, time
from datetime import datetime
from datetime import date
from collections import defaultdict, Counter
from bs4 import BeautifulSoup
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def pk_back_up_pnx(pnx_working, d_dst):
    if not does_pnx_exist(pnx=pnx_working):
        pk_print(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return

    # 용량을 확인하고 부족하면 95프로 이면 휴지통을 비울것을 가이드 하고
    # 하면안될것 같다고 이야기해줘

    # 압축
    return compress_pnx(src=pnx_working, dst=d_dst)
