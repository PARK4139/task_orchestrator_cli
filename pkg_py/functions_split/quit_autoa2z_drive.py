

import win32con
import win32com.client
import undetected_chromedriver as uc
import string
import socket
import shlex
import pyautogui
import pyaudio
import pickle
import pandas as pd
import mutagen
import hashlib
import easyocr
import datetime
import cv2
import colorama
import browser_cookie3
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from telegram import Bot
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pynput import mouse
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.state_via_database import PkSqlite3DB

from datetime import timedelta
from datetime import date
from cryptography.hazmat.backends import default_backend
from bs4 import ResultSet
from base64 import b64decode
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.pk_print import pk_print


def quit_autoa2z_drive():
    import time

    window_title_seg = "AutoA2Z Drive"
    timeout = 5
    start_time = time.time()
    while 1:
        if time.time() - start_time > timeout:
            break
        if is_window_opened(window_title_seg=window_title_seg):
            window_title_seg = "AutoA2ZDrive_Release.exe"
            while 1:
                pid = get_pid_by_window_title_via_tasklist(window_title_seg=window_title_seg)
                if is_number_v2(prompt=pid):
                    # cmd = rf' taskkill /f /pid {pid} '
                    # cmd_to_os_like_person(cmd=cmd, admin_mode=True) # fail
                    # cmd_to_os_like_person_as_admin(cmd=cmd)

                    cmd = rf' Stop-Process -Id {pid} -Force'
                    cmd_to_os_via_powershell_exe(cmd=cmd)
                    write_like_person(str_working='exit')
                    pk_press("enter")
                else:
                    break

            break
        else:
            break
