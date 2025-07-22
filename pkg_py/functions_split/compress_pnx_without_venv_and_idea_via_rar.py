# import win32gui
import win32con
import win32con
import uuid
import urllib
import traceback
import tqdm
import tomllib
import tarfile
import sys
import string
import requests
import random
# import pywin32
import pythoncom
import pygetwindow
import pyaudio
import platform
import pickle
import paramiko
import os.path
import os
import mysql.connector
import keyboard
import importlib
import easyocr
import clipboard
import browser_cookie3
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_print_state import pk_print_state

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.pk_system_object.etc import PkFilter
from pkg_py.pk_system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.is_os_windows import is_os_windows

from gtts import gTTS
from functools import partial as functools_partial
from fastapi import HTTPException
from dirsync import sync
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def compress_pnx_without_venv_and_idea_via_rar(pnx, d_dst, with_timestamp=1):
    import inspect

    import os
    # todo : 불필요 파일 삭제하는 코드 만들어야함.

    if not LTA:
        # ensure wsl
        config_remote_os = {}
        wsl_distro_n = "Ubuntu-24.04"
        config_remote_os['os_distro_n'] = wsl_distro_n
        config_remote_os['ip'] = get_wsl_ip(wsl_distro_n)
        config_remote_os['port'] = ensure_and_get_wsl_port(wsl_distro_n)
        config_remote_os['user_n'] = get_wsl_user_n(wsl_distro_n)
        config_remote_os['pw'] = get_wsl_pw(wsl_distro_n)
        config_remote_os['local_ssh_public_key'] = os.path.join(D_HOME, ".ssh", "id_ed25519.pub")
        config_remote_os['local_ssh_private_key'] = os.path.expanduser("~/.ssh/id_ed25519")
        ensure_wsl_distro_installed(wsl_distro_n=wsl_distro_n)
        ensure_wsl_distro_session(wsl_distro_n=wsl_distro_n)

        ensure_ubuntu_pkg_to_remote_os(ubuntu_pkg_n='rar', **config_remote_os)

    # 전처리
    pnx = get_pnx_unix_style(pnx=pnx)
    d_dst = get_pnx_unix_style(pnx=d_dst)

    # 정의
    working_d = get_d_working()
    p = get_p(pnx)
    n = get_n(pnx)
    nx = get_nx(pnx)
    x = get_x(pnx)
    x = x.lstrip('.')  # 확장자에서 점 remove

    _rar = ".rar"  # via rar
    timestamp = ""
    if with_timestamp:
        timestamp = rf"{PK_BLANK}{get_time_as_('%Y_%m_%d_%H_%M_%S')}"
    f_rar = rf"{p}/{n}{_rar}"
    f_rar_new = rf"{d_dst}/{n}{_rar}"
    f_rar_new_timestamp = rf"{d_dst}/{n}{timestamp}{_rar}"

    # remove
    move_pnx_to_pk_recycle_bin(pnx=f_rar)
    move_pnx_to_pk_recycle_bin(pnx=f_rar_new)

    # make d
    ensure_pnx_made(pnx=d_dst, mode='d')

    # move
    pk_chdir(p)

    # todo 압축대상의 용량 확인
    pk_print("압축대상의 용량이 1GB 이상이면 1분 이상 걸릴 수 있습니다", print_color='blue')

    # compress by rar (".venv" 및 ".idea" 제외)
    f_rar_wsl = get_pnx_wsl_unix_style(pnx=f_rar)
    cmd = f'wsl rar a "{f_rar_wsl}" "{nx}" -x"*.venv/*" -x"*.idea/*"'
    cmd_to_os(cmd=cmd, encoding=Encoding.UTF8)

    # copy
    copy_pnx_with_overwrite(pnx=f_rar, dst=d_dst)

    # rename
    rename_pnx(src=f_rar_new, pnx_new=f_rar_new_timestamp)

    dst_nx = rf"{d_dst}/{nx}"

    # del
    if LTA:
        # todo 불필요한 거 최종적으로 삭제하려면 찾아야 한다.
        pk_print(f'''dst_nx={dst_nx} {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''f_rar_new={f_rar_new} {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''dst_nx={dst_nx} {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''f_rar_wsl={f_rar_wsl}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    # move_pnx_to_trash_bin(src=f_rar_new)
    move_pnx_to_pk_recycle_bin(pnx=dst_nx)
    move_pnx_to_pk_recycle_bin(pnx=f_rar_wsl)

    # chdir
    pk_chdir(working_d)

    # logging
    if does_pnx_exist(pnx=f_rar_new_timestamp):
        STAMP_func_n = rf'[{inspect.currentframe().f_code.co_name}()]'
        pk_print(
            working_str=rf'''{STAMP_func_n} f_rar_new_timestamp={f_rar_new_timestamp}  {'%%%FOO%%%' if LTA else ''}''',
            print_color='green')
    return f_rar_new_timestamp
