import urllib
import pygetwindow
import json
import functools
from zipfile import BadZipFile
from tkinter import UNDERLINE
from selenium.webdriver.common.keys import Keys
from PySide6.QtWidgets import QApplication

from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE

from pathlib import Path
from moviepy import VideoFileClip
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging


def kill_tabs_except_current_tab_via_selenium(driver):
    current_window = driver.current_window_handle
    for window in driver.window_handles:
        if window != current_window:
            driver.switch_to.window(window)
            # press("ctrl", "w"5)
            driver.close()  # 탭 닫기
            ensure_slept(seconds=0.1)
        #     ensure_slept(milliseconds=random.randint(a=22, b=2222))
        # ensure_slept(milliseconds=random.randint(a=22, b=2222))

    driver.switch_to.window(current_window)
