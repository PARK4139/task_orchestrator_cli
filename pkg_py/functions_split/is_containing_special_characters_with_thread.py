import yt_dlp
import winreg
# import win32process
# import win32gui            
# import win32gui
import win32con
import win32con
import uuid
import undetected_chromedriver as uc
import traceback
import tomllib
import timeit
import tarfile
import subprocess
import speech_recognition as sr
import pywintypes
import pygetwindow
import pyautogui
import psutil
import nest_asyncio
import mutagen
import math
import keyboard
import inspect
import functools
import datetime
import colorama
import clipboard
import browser_cookie3
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import unquote, urlparse, parse_qs
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from queue import Queue, Empty
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_once import pk_print_once

from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.pk_system_object.etc import PkFilter
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.directories import D_WORKING
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.pk_system_object.Local_test_activate import LTA

from pathlib import Path
from paramiko import SSHClient, AutoAddPolicy
from os.path import dirname
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from gtts import gTTS
from dirsync import sync
from datetime import timedelta
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from collections import Counter
from base64 import b64decode
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.pk_system_object.directories import D_WORKING, D_DOWNLOADS, D_PKG_PKL, D_PKG_PY
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.get_pnx_list import get_pnx_list


def is_containing_special_characters_with_thread(text: str):
    import re
    import threading
    # 비동기 처리 설정 ( advanced  )
    nature_numbers = [n for n in range(1, 101)]  # from 1 to 100
    work_quantity = len(text)
    n = 4  # thread_cnt # interval_cnt
    d = work_quantity // n  # interval_size
    r = work_quantity % n
    start_1 = 0
    end_1 = d - 1
    starts = [start_1 + (n - 1) * d for n in nature_numbers[:n]]  # 등차수열 official
    ends = [end_1 + (n - 1) * d for n in nature_numbers[:n]]
    remained_start = ends[-1] + 1
    remained_end = work_quantity

    # print(rf'nature_numbers : {nature_numbers}')  # 원소의 길이의 합이 11넘어가면 1에서 3까지만 표기 ... 의로 표시 그리고 마지막에서 3번째에서 마지막에서 0번째까지 표기 cut_list_proper_for_pretty()
    # print(rf'work_quantity : {work_quantity}')
    # print(rf'n : {n}')
    # print(rf'd : {d}')
    # print(rf'r : {r}')
    # print(rf'start_1 : {start_1}')
    # print(rf'end_1 : {end_1}')
    # print(rf'starts : {starts}')
    # print(rf'ends : {ends}')
    # print(rf'remained_start : {remained_start}')
    # print(rf'remained_end : {remained_end}')

    # 비동기 이벤트 함수 설정 ( advanced  )
    async def is_containing_special_characters(start_index: int, end_index: int, text: str):
        pattern = "[~!@#$%^&*()_+|<>?:{}]"  # , 는 제외인가?
        if re.search(pattern, text[start_index:end_index]):
            # print(f"쓰레드 {start_index}에서 {end_index}까지 작업 성공 True return")
            result_list.append(True)
            # return 1
        else:
            result_list.append(False)
            # print(f"쓰레드 {start_index}에서 {end_index}까지 작업 성공 False return")
            # return 0

    # 비동기 이벤트 루프 설정
    def run_async_event_loop(start_index: int, end_index: int, text: str):
        import asyncio
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(is_containing_special_characters(start_index, end_index, text))

    # 스레드 객체를 저장할 리스트 생성
    threads = []

    # 각 스레드의 결과를 저장할 리스트
    # result_list=[None] * work_quantity
    result_list = []

    # 주작업 처리용 쓰레드
    for n in range(0, n):
        start_index = starts[n]
        end_index = ends[n]
        thread = threading.Thread(target=run_async_event_loop, args=(start_index, end_index, text))
        thread.start()
        threads.append(thread)

    # 남은 작업 처리용 쓰레드
    if remained_end <= work_quantity:
        start_index = remained_start
        end_index = remained_end
        thread = threading.Thread(target=run_async_event_loop, args=(start_index, end_index, text))
        thread.start()
        threads.append(thread)
    else:
        start_index = remained_start
        end_index = start_index  # end_index 를 start_index 로 하면 될 것 같은데 테스트필요하다.
        thread = threading.Thread(target=run_async_event_loop, args=(start_index, end_index, text))
        thread.start()
        threads.append(thread)

    # 모든 스레드의 작업이 종료될 때까지 대기
    for thread in threads:
        thread.join()

    # 먼저 종료된 스레드가 있는지 확인하고, 나머지 스레드 중지
    # for thread in threads:
    #     if not thread.is_alive():
    #         for other_thread in threads:
    #             if other_thread != thread:
    #                 other_thread.cancel()
    #         break

    # 바뀐 부분만 결과만 출력, 전체는 abspaths_and_mtimes 에 반영됨
    # print(rf'result_list : {result_list}')
    # print(rf'type(result_list) : {type(result_list)}')
    # print(rf'len(result_list) : {len(result_list)}')

    if all(result_list):
        # pk_print(str_working="쓰레드 작업결과 result_list의 모든 요소가 True이므로 True를 반환합니다")
        return 1
    else:
        # pk_print(str_working="쓰레드 작업결과 result_list에 False인 요소가 있어 False를 반환합니다")
        pass
