


import win32con
import uuid
import tomllib
import toml
import threading
import sqlite3
import platform
import nest_asyncio
import mutagen
import ipdb
import importlib
import easyocr
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.ensure_state_printed import ensure_state_printed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PK_WORKING

from passlib.context import CryptContext
from os import path
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from enum import Enum
from dirsync import sync
from datetime import timedelta
from datetime import date
from dataclasses import dataclass
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs


def remove_block_hidden(driver):
    from selenium.webdriver.common.by import By
    # driver.execute_script("""
    #     const backdrop = document.querySelector('.MuiBackdrop-root');
    #     if (backdrop) {
    #         backdrop.style.display = 'none';
    #     }
    # """)
    try:
        overlay = driver.find_element(By.CSS_SELECTOR, ".MuiModal-root")
        overlay.click()  # 가려진 요소 클릭으로 닫기
        ensure_printed(str_working="가려진 요소 닫기 성공")
    except Exception as e:
        print(f"가려진 요소 닫기 중 오류 발생: {e}")
