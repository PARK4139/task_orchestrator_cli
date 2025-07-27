import zipfile
import win32com.client
import traceback
import string
import socket
import keyboard
import inspect
import easyocr
import colorama
from telegram import Bot
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from prompt_toolkit import PromptSession
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.directories import D_PK_WORKING
from datetime import datetime
from dataclasses import dataclass
from collections import Counter
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.functions_split.is_d import is_d
from pkg_py.system_object.is_os_windows import is_os_windows

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def assist_to_make_d_for_work():
    try:
        while 1:
            # 1st input: 진행여부

            # 2nd input: 업무명 입력
            work_n = pk_input_validated("work_n", mode_nx_validation=1)

            # 3rd input: 경로 입력
            dst = pk_input_validated(str_working="dst", mode_nx_validation=1)

            # d 생성
            make_d_with_timestamp(d_nx=work_n, dst=dst)

            # 내용 비우기 # todo
            for idx, _ in enumerate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
                print()


    except Exception as e:
        ensure_printed(f"Error: {str(e)}")
