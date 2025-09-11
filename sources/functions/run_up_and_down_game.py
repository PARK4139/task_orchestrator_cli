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

from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front


from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_state_printed import ensure_state_printed
from sources.functions.ensure_printed_once import ensure_printed_once
import logging

from sources.functions.ensure_console_cleared import ensure_console_cleared


from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.pk_state_via_database import PkSqlite3DB


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
from sources.functions.get_nx import get_nx
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided

from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.does_pnx_exist import is_pnx_existing


def run_up_and_down_game():
    import inspect
    import random

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
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
