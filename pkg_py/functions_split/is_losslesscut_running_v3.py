import winreg
# import win32process
import traceback
import timeit
import shutil
import random, math
# import pywin32
import pythoncom
import cv2
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.pk_print_once import pk_print_once

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.local_test_activate import LTA

from dirsync import sync
from datetime import datetime
from cryptography.hazmat.backends import default_backend
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.pk_print import pk_print


def is_losslesscut_running_v3(F_CACHE):
    import inspect
    import os
    import pickle
    import time

    func_n = inspect.currentframe().f_code.co_name
    CACHE_TTL_SECONDS = 60

    f_losslesscut_exe = get_pnx_windows_style(pnx=F_LOSSLESSCUT_EXE)
    if not os.path.exists(F_CACHE):
        ensure_pnx_made(pnx=F_CACHE, mode='f')
        std_list = cmd_to_os(cmd='tasklist.exe | findstr "LosslessCut.exe"')
        status = len(std_list) > 0
        pk_print(f"status={status}", print_color='green')
        save_cash_to_f_pkl(F_CACHE, status=status)
    else:
        try:
            # 캐시, 유효한 캐시
            with open(F_CACHE, "rb") as f:
                cache = pickle.load(f)
            if time.time() - cache["timestamp"] < CACHE_TTL_SECONDS:
                status = cache["status"]
                pk_print(f"[CACHE] LosslessCut is {'running' if status else 'not running'}", print_color='blue')
                return status
            else:
                std_list = cmd_to_os(cmd='tasklist.exe | findstr "LosslessCut.exe"')
                status = len(std_list) > 0
                pk_print(f"status={status}", print_color='green')
                save_cash_to_f_pkl(F_CACHE, status=status)
                pk_print(f"{get_nx(f_losslesscut_exe)} is {'running' if status else 'not running'}",
                         print_color='green' if status else 'red')
                return status
        except Exception:
            pass

        # def assist_to_load_video_at_losslesscut_v1(d_working):
