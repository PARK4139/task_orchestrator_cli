import winreg
import win32con
import uuid
import urllib.parse
import urllib
import traceback
import timeit
import shlex
import requests
import re
import random
import pygetwindow
import pickle
import paramiko
import math
import keyboard
import json
import colorama
import colorama
from yt_dlp import YoutubeDL
from PySide6.QtWidgets import QApplication
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_800_print_util import print_red
from fastapi import HTTPException
from dirsync import sync
from datetime import datetime, timedelta
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows

from pkg_py.simple_module.part_330_get_d_working import get_d_working


def get_str_replaced_special_characters(target: str, replacement: str):  # str to str
    import re

    target_replaced = re.sub(pattern=r'[^a-zA-Z0-9가-힣\s]', repl=replacement,
                             string=target)  # 정규표현식을 사용하여 특수문자(알파벳, 숫자, 한글, 공백을 제외한 모든 문자) remove
    return target_replaced
