# import win32process
# import win32gui
import win32com.client
import timeit
import sys
import requests
import pywintypes
import keyboard
from telegram import Bot, Update
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PySide6.QtWidgets import QApplication
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_directories import D_PKG_TXT, D_WORKING
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated
from PIL import Image
from os.path import dirname
from enum import Enum
from datetime import timedelta
from cryptography.hazmat.backends import default_backend
from colorama import init as pk_colorama_init
from base64 import b64encode
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.pk_system_layer_directories import D_WORKING, D_DOWNLOADS
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style


def pk_delete_empty_d_list():
    import os

    def _delete_tree(root_path: str):
        """
        주어진 디렉토리(root_path)를 후위 순회로 삭제합니다.
        """
        # 먼저 하위 항목들 처리
        for entry in os.scandir(root_path):
            path = entry.path
            if entry.is_dir(follow_symlinks=False):
                # 서브디렉토리 재귀 삭제
                _delete_tree(path)
            else:
                # 파일 삭제
                os.remove(path)
        # 하위 항목까지 다 비워졌으면 자신(빈 디렉토리)도 삭제
        os.rmdir(root_path)

    option_values = [D_WORKING, D_PROJECT, D_DOWNLOADS]
    d_working = get_value_completed(
        key_hint='d_working=',
        values=option_values
    )

    if not os.path.isabs(d_working):
        raise ValueError(f"절대경로를 입력해야 합니다: {d_working!r}")
    if not os.path.isdir(d_working):
        return

    _delete_tree(d_working)
