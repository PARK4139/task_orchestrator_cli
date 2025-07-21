import win32con
import toml
import toml
import timeit
import random
import cv2
import colorama
import clipboard
from urllib.parse import quote
from selenium.webdriver.chrome.service import Service
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_100_os import is_os_windows

from PIL import Image
from os import path
from functools import partial as functools_partial
from datetime import timedelta
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def get_last_digit(prompt):
    # todo : get_front_digit() 도 만드는 게 좋겠다.
    import inspect
    import re

    func_n = inspect.currentframe().f_code.co_name
    match = re.search(r'\d+\b$', prompt.strip())  # 끝에 위치한 모든 연속된 숫자를 찾음
    if match:
        return match.group(0)  # 매칭된 숫자 반환
    return "00"  # 숫자를 찾지 못한 경우 기본값 "00" 반환
