import winreg
import win32con
import webbrowser
import timeit
import time
import shutil
import requests
import random
import pythoncom
import ipdb
import hashlib
import functools
from selenium.webdriver.common.keys import Keys
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from functools import partial as functools_partial
from concurrent.futures import ThreadPoolExecutor
from base64 import b64decode
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style

from pkg_py.simple_module.part_330_get_d_working import get_d_working


def get_list_that_element_applyed_via_func(func, working_list):
    return [func(item) for item in working_list]
