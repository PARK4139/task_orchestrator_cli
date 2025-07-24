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
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.directories import D_PKG_TXT, D_WORKING

from paramiko import SSHClient, AutoAddPolicy
from os import path
from functools import partial as functools_partial
from datetime import date
from cryptography.hazmat.backends import default_backend
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.pk_print import pk_print


def on_left_click(x, y, button, pressed):
    from pynput import mouse
    if pressed and button == mouse.Button.left:
        click_detected = True  # 클릭 감지 상태 업데이트
        pk_print("마우스 왼쪽 클릭 감지됨!")
        return 0  # 마우스 왼쪽 클릭 감지되면 Listener 종료
