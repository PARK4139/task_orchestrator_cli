import pyautogui
from pynput import mouse
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_title_front import is_window_title_front

from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pathlib import Path
from os.path import dirname
from colorama import init as pk_colorama_init
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style


def get_random_pw(length_limit: int):
    import random
    import string
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length_limit))
