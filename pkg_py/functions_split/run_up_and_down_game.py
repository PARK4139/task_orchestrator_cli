import zipfile
import win32con
import undetected_chromedriver as uc
import tqdm
import toml
import timeit
import time
import threading
import sys
import subprocess, time
import subprocess
import string
import sqlite3
import socket
import shutil
import secrets
import pywintypes


import pythoncom
import pyglet
import pygetwindow
import pyautogui
import pyaudio
import platform
import pandas as pd
import os.path
import nest_asyncio
import mysql.connector
import math
import json
import ipdb
import hashlib
import easyocr
import datetime
import colorama
import chardet
import calendar

from webdriver_manager.chrome import ChromeDriverManager
from typing import TypeVar, List
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from queue import Queue, Empty
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_state_printed import ensure_state_printed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.state_via_database import PkSqlite3DB


from PIL import Image, ImageFont, ImageDraw, ImageFilter
from PIL import Image, ImageFont, ImageDraw
from PIL import Image
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from dirsync import sync
from datetime import timedelta
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def run_up_and_down_game():
    import inspect
    import random

    func_n = inspect.currentframe().f_code.co_name
    correct_answer: int = random.randint(1, 100)
    left_oportunity: int = 10
    ment = f"<UP AND DOWN GAME>\n\nFIND CORRECT NUMBER"
    ensure_spoken_v2(str_working=ment, comma_delay=1.0)

    txt_clicked, function, txt_written = should_i_do(
        prompt=ment,
        btn_list=["START", "EXIT"],
        function=None,
        auto_click_negative_btn_after_seconds=30,
        title=f"{func_n}()",
        input_box_mode=False,
    )
    if txt_clicked != "START":
        return

    user_input = None
    is_game_strated = False
    btn_txt_clicked = txt_clicked

    if btn_txt_clicked == "START":
        ment = f"START IS PRESSED, LETS START GAME"
        ensure_spoken_v2(str_working=ment, comma_delay=0.98, thread_join_mode=True)
        while left_oportunity >= 0:
            if left_oportunity == 0:
                ment = f"LEFT CHANCE IS {left_oportunity} \nTAKE YOUR NEXT CHANCE."
                ensure_spoken_v2(str_working=ment, comma_delay=0.98)

                txt_clicked, function, txt_written = should_i_do(
                    prompt=ment,
                    btn_list=["EXIT"],
                    function=None,
                    auto_click_negative_btn_after_seconds=None,
                    title=f"{func_n}()",
                    #                    input_box_mode=True,
                )
                if txt_clicked == "EXIT":
                    return

                break
            elif is_game_strated == False or user_input is None:

                ment = f"TYPE NUMBER BETWEEN 1 TO 100"
                if user_input is None:
                    ment = rf"{ment} AGAIN"
                ensure_spoken_v2(str_working=ment, comma_delay=0.98)
                txt_clicked, function, txt_written = should_i_do(
                    prompt=ment,
                    btn_list=["SUBMIT", "EXIT"],
                    function=None,
                    auto_click_negative_btn_after_seconds=None,
                    title=f"{func_n}()",
                    input_box_mode=True,
                )
                if txt_clicked == "EXIT":
                    return

                user_input = is_user_input_required(txt_written)
                if user_input is not None:
                    left_oportunity = left_oportunity - 1
                is_game_strated = True
            elif user_input == correct_answer:
                ment = f"CONGRATULATIONS\n\nYOUR NUMBER IS {correct_answer}\nTHIS IS ANSWER\n\nSEE YOU AGAIN"
                ensure_spoken_v2(str_working=ment, comma_delay=0.98)

                txt_clicked, function, txt_written = should_i_do(
                    prompt=ment,
                    btn_list=["SUBMIT", "EXIT"],
                    function=None,
                    auto_click_negative_btn_after_seconds=None,
                    title=f"{func_n}()",
                    input_box_mode=True,
                )
                if txt_clicked == "EXIT":
                    return

            elif correct_answer < user_input:
                ment = f"YOUR NUMBER IS {user_input}\n\nYOU NEED DOWN\n\nYOUR LEFT CHANCE IS {left_oportunity}"
                ensure_spoken_v2(str_working=ment, comma_delay=0.98)

                txt_clicked, function, txt_written = should_i_do(
                    prompt=ment,
                    btn_list=["SUBMIT", "EXIT"],
                    function=None,
                    auto_click_negative_btn_after_seconds=None,
                    title=f"{func_n}()",
                    input_box_mode=True,
                )
                if txt_clicked == "EXIT":
                    return

                user_input = is_user_input_required(txt_written)
                if user_input is not None:
                    left_oportunity = left_oportunity - 1
            elif correct_answer > user_input:
                ment = f"YOUR NUMBER IS {user_input}\n\nYOU NEED UP\n\nYOUR LEFT CHANCE IS {left_oportunity}"
                ensure_spoken_v2(str_working=ment, comma_delay=0.98)

                txt_clicked, function, txt_written = should_i_do(
                    prompt=ment,
                    btn_list=["SUBMIT", "EXIT"],
                    function=None,
                    auto_click_negative_btn_after_seconds=None,
                    title=f"{func_n}()",
                    input_box_mode=True,
                )
                if txt_clicked == "EXIT":
                    return

                user_input = is_user_input_required(txt_written)
                if user_input is not None:
                    left_oportunity = left_oportunity - 1
    else:
        return
