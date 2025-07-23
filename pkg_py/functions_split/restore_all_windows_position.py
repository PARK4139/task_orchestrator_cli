# import win32gui
import toml
import timeit
import time
import tarfile
# import pywin32
import mutagen
import hashlib
import browser_cookie3
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from prompt_toolkit.styles import Style
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.pk_system_object.directories import D_WORKING
from pkg_py.pk_system_object.map_massages import PkMessages2025
from pkg_py.pk_system_object.local_test_activate import LTA
from os import path
from moviepy import VideoFileClip
from functools import partial as functools_partial
from fastapi import HTTPException
from datetime import timedelta
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.get_pnx_list import get_pnx_list


def restore_all_windows_position():
    import win32con  # pywin32
    # import win32gui  # pywin32
    def enum_windows_callback(hwnd, lparam):
        # func_n=inspect.currentframe().f_code.co_name
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            # # 예시: 시스템 창이나 보안 프로그램을 제외하는 조건
            # if "System" in window_title or "Security" in window_title:
            #     print(f"시스템 창 또는 보안 프로그램을 건너뛰는 중: {window_title}")
            #     return  # 건너뛰기
            try:
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
                print(f"창 {win32gui.GetWindowText(hwnd)}를 복원했습니다.")
            except Exception as e:
                print(f"Error while processing window {hwnd}: {str(e)}")
                pass

    win32gui.EnumWindows(enum_windows_callback, None)
