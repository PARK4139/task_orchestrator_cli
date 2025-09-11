import win32con
import timeit
import threading
import tarfile
import sqlite3
import cv2
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pynput import mouse
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.is_window_title_front import is_window_title_front

from functools import lru_cache
from dataclasses import dataclass
from colorama import init as pk_colorama_init
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_pnx_windows_style import get_pnx_windows_style


def print_parents_process_pid():
    import inspect
    import os
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    os.system(rf'powershell (Get-WmiObject Win32_Process -Filter ProcessId=$PID).ParentProcessId')
