


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

from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.ensure_state_printed import ensure_state_printed
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared


from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING

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
from sources.functions.get_nx import get_nx
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


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
        logging.debug("가려진 요소 닫기 성공")
    except Exception as e:
        print(f"가려진 요소 닫기 중 오류 발생: {e}")
