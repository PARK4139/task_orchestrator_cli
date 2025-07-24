import yt_dlp
import win32com.client
import urllib.parse
import urllib
import traceback
import tarfile
import subprocess
import sqlite3
import shlex
import pywintypes
import pyautogui
import pyaudio
import platform
import pandas as pd
import ipdb
import inspect
import cv2
import asyncio
from yt_dlp import YoutubeDL
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from prompt_toolkit.styles import Style
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.is_os_windows import is_os_windows
from pathlib import Path
from passlib.context import CryptContext
from os import path
from functools import partial as functools_partial
from functools import partial
from colorama import init as pk_colorama_init
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.is_d import is_d
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def click_tag_as_with_tag_text(driver, tag_name, tag_text):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    try:
        h3_element = driver.find_element(By.XPATH, rf"//{tag_name}[text()='{tag_text}']")
        actions = ActionChains(driver)
        actions.move_to_element(h3_element).click().perform()
    except Exception as e:
        pk_print(f'''click {tag_name} tag with text as {tag_text} fail  {'%%%FOO%%%' if LTA else ''}''',
                 print_color='red')
