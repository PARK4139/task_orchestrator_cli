import yt_dlp
# import win32gui
import webbrowser
import timeit
import threading
import requests
import pygetwindow
import json
import ipdb
import colorama
import chardet
from zipfile import BadZipFile
from typing import TypeVar, List
from seleniumbase import Driver
from selenium.webdriver.chrome.service import Service
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_directories import D_PKG_TXT, D_WORKING

from paramiko import SSHClient, AutoAddPolicy
from os import path
from functools import partial as functools_partial
from datetime import date
from cryptography.hazmat.backends import default_backend
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_014_pk_print import pk_print


def on_left_click(x, y, button, pressed):
    from pynput import mouse
    if pressed and button == mouse.Button.left:
        click_detected = True  # 클릭 감지 상태 업데이트
        pk_print("마우스 왼쪽 클릭 감지됨!")
        return 0  # 마우스 왼쪽 클릭 감지되면 Listener 종료
