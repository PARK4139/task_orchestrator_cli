
"""
# 먼저 하위 항목들 처리
# 서브디렉토리 재귀 삭제
# 파일 삭제
# 하위 항목까지 다 비워졌으면 자신(빈 디렉토리)도 삭제
)
_delete_tree(d_working)
_delete_tree(path)
d_working = get_value_completed(
def _delete_tree(root_path: str):
def pk_delete_empty_d_list():
else:
for entry in os.scandir(root_path):
from PIL import Image
from PySide6.QtWidgets import QApplication
from base64 import b64encode
from colorama import init as pk_colorama_init
from cryptography.hazmat.backends import default_backend
from datetime import timedelta
from enum import Enum
from os.path import dirname
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.get_list_calculated import get_list_calculated
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from telegram import Bot, Update
if entry.is_dir(follow_symlinks=False):
if not os.path.isabs(d_working):
if not os.path.isdir(d_working):
import keyboard
import os
import pywintypes
import requests
import sys
import timeit
import win32com.client
key_hint='d_working=',
option_values = [D_PK_WORKING, D_PROJECT, D_DOWNLOADS]
os.remove(path)
os.rmdir(root_path)
path = entry.path
raise ValueError(f"절대경로를 입력해야 합니다: {d_working!r}")
return
values=option_values
주어진 디렉토리(root_path)를 후위 순회로 삭제합니다.
