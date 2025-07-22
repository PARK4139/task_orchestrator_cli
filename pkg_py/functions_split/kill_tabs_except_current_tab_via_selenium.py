import urllib
import pygetwindow
import json
import functools
from zipfile import BadZipFile
from tkinter import UNDERLINE
from selenium.webdriver.common.keys import Keys
from PySide6.QtWidgets import QApplication

from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pathlib import Path
from moviepy import VideoFileClip
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.pk_print import pk_print


def kill_tabs_except_current_tab_via_selenium(driver):
    current_window = driver.current_window_handle
    for window in driver.window_handles:
        if window != current_window:
            driver.switch_to.window(window)
            # press("ctrl", "w"5)
            driver.close()  # 탭 닫기
            pk_sleep(seconds=0.1)
        #     pk_sleep(milliseconds=random.randint(a=22, b=2222))
        # pk_sleep(milliseconds=random.randint(a=22, b=2222))

    driver.switch_to.window(current_window)
