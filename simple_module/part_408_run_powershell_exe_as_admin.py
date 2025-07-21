import webbrowser
import traceback
import subprocess
import sqlite3
import speech_recognition as sr
import pandas as pd
import os.path
import keyboard
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os

from functools import lru_cache
from datetime import timedelta
from datetime import datetime
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows


def run_powershell_exe_as_admin():
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    # cmd_to_os('PowerShell -cmd "Start-Process powershell"')
    cmd_to_os('powershell -cmd "Start-Process powershell -Verb RunAs"')
    window_title_seg = "관리자: Windows PowerShell"
    while 1:
        if not is_front_window_title(window_title_seg=window_title_seg):
            ensure_window_to_front(window_title_seg=window_title_seg)
        if is_front_window_title(window_title_seg=window_title_seg):
            break
    # window_move_to_front_via_win32gui(window_title_seg=window_title_seg)
