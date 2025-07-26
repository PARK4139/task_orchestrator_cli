import webbrowser
import urllib.parse
import threading
import subprocess
import string
import re
import keyboard
import json
import ipdb
import inspect
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_pressed import ensure_pressed

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.is_os_windows import is_os_windows
from os import path
from datetime import date
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def get_pk_config(key: str, initial: str) -> str:
    import os

    path = os.path.join(D_PKG_TOML, f"pk_token_{key}.toml")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(initial)
        ensure_printed(f"[Config] Initialized '{key}' with default '{initial}' in {path}")
        return initial
    with open(path, 'r', encoding='utf-8') as f:
        value = f.readline().strip() or initial
    ensure_printed(f"[Config] Loaded '{key}' = '{value}'")
    return value
