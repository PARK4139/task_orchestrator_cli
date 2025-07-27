import zlib
import zipfile
import yt_dlp
import winreg


import win32con
import win32com.client
import webbrowser
import uuid
import urllib
import traceback
import tqdm
import tomllib
import toml
import toml
import timeit
import time
import threading
import tarfile
import sys
import subprocess, time
import subprocess
import string
import sqlite3
import speech_recognition as sr
import socket
import shutil
import secrets
import requests
import re
import random, math
import random
import pywintypes


import pyglet
import pygetwindow
import pyautogui
import pyaudio
import psutil
import platform
import pickle
import pandas as pd
import os, inspect
import os
import numpy as np
import nest_asyncio
import math
import keyboard
import json
import ipdb
import inspect
import functools
import easyocr
import datetime
import cv2
import colorama
import colorama
import clipboard
import calendar

import asyncio
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import urlparse
from urllib.parse import unquote, urlparse, parse_qs
from urllib.parse import quote, urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from queue import Queue, Empty
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext

from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA

from PIL import Image, ImageFilter
from PIL import Image
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from datetime import timedelta
from datetime import datetime, timedelta
from datetime import datetime, time
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def assist_to_do_pk_schedule():
    from colorama import init as pk_colorama_init

    colorama_init_once()

    loop_cnt = 0
    while 1:
        ment = f'pk scheduler loop {loop_cnt} is started'
        ensure_printed(f"{ment}")
        if loop_cnt == 0:
            # speak_ment_experimental(ment=ment, comma_delay=0.98, thread_join_mode=True)
            guide_to_check_routines()

        # 특정시간에 OS 부팅
        # should_i_do(ment="백업할 타겟들을 크기에 따라 분류를 해둘까요?", function=classify_pnxs_between_smallest_pnxs_biggest_pnxs, auto_click_positive_btn_after_seconds=10)
        # should_i_do(ment="백업할 타겟들을 크기에 따라 분류를 해둘까요?", function=classify_pnxs_between_smallest_pnxs_biggest_pnxs, auto_click_negative_btn_after_seconds=5)

        # mkr_특정시간에 한번
        # if is_same_time(time1=get_time_as_('%Y_%m_%d_%H_%M_%S_%f'), time2=datetime(year=2024, month=10, day=31, hour=22, minute=27 , second=0)):
        #     print_as_gui(ment="약속된 시간이 되었습니다.")

        # yyyy = get_time_as_('%Y')
        # MM = get_time_as_('%m')
        # dd = get_time_as_('%d')
        # HH = get_time_as_('%H')
        # mm = get_time_as_('%M')
        # ss = get_time_as_('%S')
        yyyy = '2024'
        daily_greeting = None
        if is_month(mm=3) and is_day(dd=22):
            daily_greeting = get_state_from_f_pk_config_toml(
                pk_state_address=f"state_pk_schedule/{yyyy}_{get_time_as_('%m')}_{get_time_as_('%d')}_daily_greeting")
            if daily_greeting:
                daily_greeting = 0
                set_state_from_f_pk_config_toml(
                    pk_state_address=f"state_pk_schedule/{yyyy}_{get_time_as_('%m')}_{get_time_as_('%d')}_daily_greeting",
                    pk_state_value=daily_greeting)
            if daily_greeting == 0:
                daily_greeting = 1
                set_state_from_f_pk_config_toml(
                    pk_state_address=f"state_pk_schedule/{yyyy}_{get_time_as_('%m')}_{get_time_as_('%d')}_daily_greeting",
                    pk_state_value=daily_greeting)
        if daily_greeting:
            ment = f'{yyyy} happy today! good lock for you!'
            ensure_printed(f'''{ment} {'%%%FOO%%%' if LTA else ''}''', print_color='green')

        # if is_midnight():  # 자정이면 초기화
        #     state_toml = toml.load(F_PK_CONFIG_TOML)["state_pk_schedule"]
        #     state_toml[f'{yyyy}_{get_time_as_('%m')}_{get_time_as_('%d')}_greeting'] = 0
        #     with open(F_PK_CONFIG_TOML, "w") as f:
        #         toml.dump(state_toml, f)

        if is_newyear():
            state_toml = toml.load(F_PK_CONFIG_TOML)["state_pk_schedule"]
            state_yearly_greeting = state_toml[f'{yyyy}_{get_time_as_('%m')}_{get_time_as_('%d')}_newyear_greeting']
            if not state_yearly_greeting:
                state_toml[f'{yyyy}_{get_time_as_('%m')}_{get_time_as_('%d')}_newyear_greeting'] = 0
                state_yearly_greeting = 0
            if state_yearly_greeting == 0:
                state_toml[f'{yyyy}_{get_time_as_('%m')}_{get_time_as_('%d')}_newyear_greeting'] = 1
                state_yearly_greeting = 1
            if state_yearly_greeting == 1:
                ment = f'{yyyy} happy new year! good lock for you!'
                ensure_printed(f'''{ment} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
                ensure_spoken(str_working=ment)

        if is_christmas():
            state_toml = toml.load(F_PK_CONFIG_TOML)["state_pk_schedule"]
            state_christmas_greeting = state_toml[
                f'{yyyy}_{get_time_as_('%m')}_{get_time_as_('%d')}_christmas_greeting']
            if not state_christmas_greeting:
                state_christmas_greeting = 0
                state_toml[
                    f'{yyyy}_{get_time_as_('%m')}_{get_time_as_('%d')}_christmas_greeting'] = state_christmas_greeting
                return 0
            if state_christmas_greeting == 0:
                state_christmas_greeting = 1
                state_toml[
                    f'{yyyy}_{get_time_as_('%m')}_{get_time_as_('%d')}_christmas_greeting'] = state_yearly_greeting
                return 1
            if state_yearly_greeting == 1:
                ment = f'{yyyy} happy christmas! good lock for you!'
                ensure_printed(f'''{ment} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
                ensure_spoken(str_working=ment)

        # mkr_매시간 한시간에한번
        #     랜덤미션
        #      do_random_schedules()

        # # mkr_스케쥴러_트리거 : 하루에 24번
        # back_up_pnxs_to_deprecated_via_text_file()

        # # mkr_0시에서 24시 사이, # 분단위 스케쥴,
        # if 0 <= int(HH) <= 24 and int(ss) == 0:
        #     monitor_target_edited_and_back_up(pnx_todo=pk_system_ARCHIVE_TOML)  # seconds_performance_test_results : ['11.95sec', '26.78sec', '11.94sec', '3.7sec', '11.72sec']
        #     if int(HH) == 6 and int(mm) == 30:
        #         # speak_ments(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)  # 쓰레드가 많아지니 speak() 하면서 부정확한 재생이 늘어났다. 쓰레드의 정확한 타이밍 제어가 필요한 것 같다. 급한대로 thread_join_mode 를 만들었다)
        #         # speak_ments(f'아침음악을 준비합니다, 아침음악을 재생할게요', sleep_after_play=0.65, thread_join_mode=True)
        #         pass
        #     if int(HH) == 7 and int(mm) == 30:
        #         # speak_ments(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
        #         # speak_ments('지금 나가지 않는다면 지각할 수 있습니다, 더이상 나가는 것을 지체하기 어렵습니다', sleep_after_play=0.65, thread_join_mode=True)
        #         pass
        #
        #     if int(HH) == 8 and int(mm) == 50:
        #         # speak_ments(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
        #         # speak_ments('업무시작 10분전입니다, 업무준비를 시작하세요, 업무 전에 세수와 양치는 하셨나요', sleep_after_play=0.65, thread_join_mode=True)
        #         pass
        #
        #     if int(HH) == 9:
        #         # speak_ments(f'{int(mm)}시 정각, 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
        #         # speak_ments('근무시간이므로 음악을 종료합니다', sleep_after_play=0.65, thread_join_mode=True)
        #         pass
        #     if int(HH) == 11 and int(mm) == 30:
        #         # # speak_ments('용량이 큰 약속된 타겟들을 백업을 수행 시도합니다', sleep_after_play=0.65, thread_join_mode=True)
        #         # back_up_biggest_pnxs()
        #         # # speak_ments('용량이 작은 약속된 타겟들을 백업을 수행 시도합니다', sleep_after_play=0.65, thread_join_mode=True)
        #         # back_up_smallest_pnxs()
        #         # # speak_ments('흩어져있는 storage 들을 한데 모으는 시도를 합니다', sleep_after_play=0.65, thread_join_mode=True)
        #         # gather_storages()
        #         pass
        #     if int(HH) == 22 and int(mm) == 10:
        #         speak_ment_experimental('씻으실 것을 추천드립니다, 샤워루틴을 수행하실 것을 추천드립니다', comma_delay=0.98, thread_join_mode=True)  # 샤워루틴 확인창 띄우기
        #     if int(HH) == 22 and int(mm) == 30:
        #         speak_ment_experimental('건강을 위해서 지금 씻고 주무실 것을 추천드려요', comma_delay=0.98, thread_join_mode=True)
        #         speak_ment_experimental('건강을 위해서 24시에 최대 절전 모드에 예약이 되었습니다', comma_delay=0.98, thread_join_mode=True)
        #     if int(HH) == 23 and int(mm) == 55:
        #         speak_ment_experimental('5분 뒤 최대 절전 모드로 진입합니다', comma_delay=0.98, thread_join_mode=True)
        #     if int(HH) == 24 and int(mm) == 0:
        #         speak_ment_experimental(f'자정이 되었습니다', comma_delay=0.98, thread_join_mode=True)
        #         speak_ment_experimental('최대 절전 모드에 진입합니다', comma_delay=0.98, thread_join_mode=True)
        #         back_up_target(pnx_todo=SERVICE_D)
        #         enter_power_saving_mode()
        #     if int(HH) == 2 and int(mm) == 0:
        #         speak('새벽 두시입니다', after_delay=0.55)
        #         speak('지금부터 예약된 최대 절전 모드에 진입합니다', after_delay=1)
        #     if int(mm) % 15 == 0:
        #         # speak_ments(f'15분 간격 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
        #         # speak_ments(f'랜덤 스케줄을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
        #         do_random_schedules()
        #         # speak_ments(f'프로젝트 d 싱크를 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
        #     if int(mm) % 30 == 0:
        #         # speak_ments(f'30분 간격 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
        #         # speak_ments(f'깃허브로 파이썬 아카이브 프로젝트 백업을 시도합니다', sleep_after_play=0.65, thread_join_mode=True)
        #         # git_push_by_auto()
        #         monitor_target_edited_and_sync(pnx_todo=SERVICE_D)  # seconds_performance_test_results : ['28.46sec', '27.53sec', '2.85sec', '2.9sec', '2.91sec']
        #     if int(mm) % 60 == 0:
        #         # speak_ments(f'1시간 간격 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
        #         should_i_do(ment="쓰레기통을 비울까요?", function=empty_recycle_bin, auto_click_negative_btn_after_seconds=10)
        #         should_i_do(ment="오늘 시간정보를 말씀드릴까요?", function=speak_today_time_info, auto_click_negative_btn_after_seconds=10)
        #         monitor_target_edited_and_sync(pnx_todo=SERVICE_D)  # seconds_performance_test_results : ['28.46sec', '27.53sec', '2.85sec', '2.9sec', '2.91sec']

        # mkr_ 23시에서 5시 사이, 30초 마다
        # if (23 <= int(HH) <= 24 or 0 <= int(HH) <= 5) and int(ss) % 30 == 0:
        #     guide_to_sleep() #최대절전모드 가이드

        # yyyy = get_time_as_('%Y')
        # MM = get_time_as_('%m')
        # dd = get_time_as_('%d')
        # HH = get_time_as_('%H')
        # mm = get_time_as_('%M')
        # ss = get_time_as_('%S')

        # update_state_to_sql(SCHECLUER_CFG)
        # pickle 에 상태를 저장
        # checklist = [] 를 pickle 에 저장 # 상태초기화시기 : 프로그램 런타임 시
        # pk_schedule.db # 상태초기화시기 : 프로그램 런타임 시
        # config.toml /pk_schedule / # 상태초기화시기 : 프로그램 런타임 시
        # context # 상태초기화시기 : 프로그램 실행 시
        # checklist = []
        # bring checklist
        # checklist.append(line)
        # print_magenta(rf'''checklist={checklist}''')
        # print_magenta(rf'''len(checklist)={len(checklist)}''')

        # 매월 월에한번
        #     DbTomlUtil.update_db_toml(key=DbTomlUtil.get_db_toml_key(unique_id=unique_id), value=False)

        # 1년에 한번 수행 아이디어
        # random_schedule.json 에서 leaved_max_count를 읽어온다
        # leaved_max_count=10 이면 년에 1씩 깍아서 수행
        # leaved_max_count=0 이면 올해에는 더이상 수행하지 않음
        # leaved_max_count 를 random_schedule_tb.toml 에 저장

        # - 1시간 뒤 시스템 종료 예약 기능
        # - 즉시 시스템 종료 시도 기능
        # - 시간 시현기능 기능(autugui 이용)
        #   ment ='pc 정밀검사를 한번 수행해주세요'
        #   ensure_printed(ment)
        # - 하드코딩된 스케줄 작업 수행 기능
        # - 미세먼지 웹스크래핑 기능
        # - 초미세먼지 웹스크래핑 기능
        # - 종합날씨 웹스크래핑 기능
        # - 습도 웹스크래핑 기능
        # - 체감온도 웹스크래핑 기능
        # - 현재온도 웹스크래핑 기능
        # - 음악재생 기능
        # - 영상재생 기능

        ensure_slept(milliseconds=200)
        ment = f'pk scheduler loop {loop_cnt} is ended'
        ensure_printed(f"{ment}")
        loop_cnt = loop_cnt + 1
