import yt_dlp

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
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
# pk_#
from pkg_py.system_object.directories import D_PKG_CACHE_PRIVATE, D_PK_WORKING

from paramiko import SSHClient, AutoAddPolicy
from os import path
from functools import partial as functools_partial
from datetime import date
from cryptography.hazmat.backends import default_backend
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.ensure_printed import ensure_printed


def on_left_click(x, y, button, pressed):
    from pynput import mouse
    if pressed and button == mouse.Button.left:
        click_detected = True  # 클릭 감지 상태 업데이트
        ensure_printed("마우스 왼쪽 클릭 감지됨!")
        return 0  # 마우스 왼쪽 클릭 감지되면 Listener 종료
