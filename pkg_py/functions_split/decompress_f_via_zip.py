import win32con
import urllib
import toml
import toml
import subprocess, time
import subprocess
import sqlite3
import socket
import secrets
import pythoncom
import paramiko
import keyboard
import json
import clipboard
import asyncio
from tkinter import UNDERLINE
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from prompt_toolkit import PromptSession
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from os.path import dirname
from functools import lru_cache
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def decompress_f_via_zip(f):
    import inspect
    import os
    import zipfile

    func_n = inspect.currentframe().f_code.co_name
    # cmd=rf'bz.exe x "{pnx}"'  # 화면에 창이 안뜨는 모드
    # ensure_command_excuted_to_os(cmd=cmd)
    pnx_p = get_p(pnx=f)
    if pnx_p is None:
        pnx_p = os.path.dirname(f)
    pnx_p = get_pnx_unix_style(pnx=pnx_p)
    f = get_pnx_unix_style(pnx=f)
    with zipfile.ZipFile(f, 'r') as zip_ref:
        if not os.path.exists(pnx_p):
            os.makedirs(pnx_p)
        zip_ref.extractall(pnx_p)
        ensure_printed(str_working=rf'''pnx_p="{pnx_p}"  {'%%%FOO%%%' if LTA else ''}''')
