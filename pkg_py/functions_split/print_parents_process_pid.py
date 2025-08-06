import win32con
import timeit
import threading
import tarfile
import sqlite3
import cv2
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pynput import mouse
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_title_front import is_window_title_front
# pk_#
from functools import lru_cache
from dataclasses import dataclass
from colorama import init as pk_colorama_init
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style


def print_parents_process_pid():
    import inspect
    import os
    func_n = inspect.currentframe().f_code.co_name
    os.system(rf'powershell (Get-WmiObject Win32_Process -Filter ProcessId=$PID).ParentProcessId')
