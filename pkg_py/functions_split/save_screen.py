
import urllib.parse
import traceback
import tomllib
import subprocess, time
import string

import platform
import functools
import easyocr
import asyncio
from urllib.parse import urlparse
from telegram import Bot
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.cmd_to_os import cmd_to_os

from PIL import Image
from functools import partial as functools_partial
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_d_working import get_d_working


def save_screen():
    # cmd_to_os_like_person(cmd=rf'''%systemroot%\system32\scrnsave.scr /s''')# 성공
    cmd = rf'''%systemroot%\system32\scrnsave.scr /s '''  # 성공
    if is_os_windows():
        cmd_to_os(cmd=cmd)
    else:
        cmd = get_pnx_wsl_unix_style(pnx=cmd)
        cmd_to_os(cmd=cmd)
