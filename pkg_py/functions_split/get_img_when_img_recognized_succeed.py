import yt_dlp
import tqdm
import tomllib
import toml
import shutil
import shlex
import requests
import pywintypes

import pythoncom
import pygetwindow
import pyaudio
import numpy as np
import math
import keyboard
import json
import hashlib
import functools
import easyocr
import clipboard
import chardet
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.get_list_calculated import get_list_calculated
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial
from datetime import timedelta
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_printed import ensure_printed


def get_img_when_img_recognized_succeed(img_abspath, recognize_loop_limit_cnt=0, is_zoom_toogle_mode=False):
    import inspect

    import pyautogui
    func_n = inspect.currentframe().f_code.co_name
    # speak("화면 이미지 분석을 시도합니다")
    GuiUtil.pop_up_as_complete(title="화면이미지분석 시도 전 보고", ment="화면 이미지 분석을 시도합니다",
                               auto_click_positive_btn_after_seconds=1)

    ensure_pressed('ctrl', '0'
    5)  # 이미지 분석 시 크롬 zoom 초기화(ctrl+0)

    # 고해상도/다크모드 에서 시도
    for i in range(0, 9):
        ensure_pressed('ctrl', '+')

    chrome_zoom_step = 0

    # 루프카운트 제한 n번 default 0번 으로 설정
    func_n = inspect.currentframe().f_code.co_name
    loop_cnt = 0
    # recognize_loop_limit_cnt=recognize_loop_limit_cnt
    if recognize_loop_limit_cnt == 0:
        while 1:
            # 인식률 및 속도 개선 시도
            # pip install opencv-python # 이것은 고급 기능이 포함되지 않은 Python용 OpenCV의 미니 버전입니다. 우리의 목적에는 충분합니다.
            # confidence=0.7(70%)유사도를 낮춰 인식률개선시도, region 낮춰 속도개선시도, grayscale 흑백으로 판단해서 속도개선시도,
            # open cv 설치했는데 적용안되고 있음. 재부팅도 하였는 데도 안됨.
            # xy_infos_of_imgs=pyautogui.locateOnScreen(img_abspath, confidence=0.7, grayscale=True)
            # debug_as_gui(xy_infos_of_imgs is None)
            ensure_printed("화면 이미지 인식 시도 중...")
            loop_cnt = loop_cnt + 1
            try:
                img = pyautogui.locateOnScreen(img_abspath, confidence=0.7, grayscale=True)
                ensure_printed(type(img), print_color='blue')
                ensure_printed(img, print_color='blue')
                ensure_printed(img is not None, print_color='blue')
                if img is not None:
                    return img
                else:
                    ensure_printed(f"화면 이미지 분석 중...")
                    ensure_printed(img_abspath, print_color='blue')
                    ensure_slept(milliseconds=15)
                    if is_zoom_toogle_mode == True:
                        if chrome_zoom_step == 14:
                            chrome_zoom_step = 0
                        elif chrome_zoom_step < 7:
                            ensure_pressed('ctrl', '-')
                            chrome_zoom_step = chrome_zoom_step + 1
                        elif 7 <= chrome_zoom_step:
                            ensure_pressed('ctrl', '+')
                            chrome_zoom_step = chrome_zoom_step + 1
            except pyautogui.ImageNotFoundException:
                ensure_printed(f"{loop_cnt}번의 화면인식시도를 했지만 인식하지 못하였습니다")
                pass
    else:
        while 1:
            loop_cnt = loop_cnt + 1
            ensure_printed("화면 이미지 인식 시도 중...")
            if recognize_loop_limit_cnt == loop_cnt:
                ensure_printed(f"{loop_cnt}번의 화면인식시도를 했지만 인식하지 못하였습니다")
                return None
            try:
                img = pyautogui.locateOnScreen(img_abspath, confidence=0.7, grayscale=True)
                ensure_printed(type(img), print_color='blue')
                ensure_printed(img, print_color='blue')
                ensure_printed(img is not None, print_color='blue')
                if img is not None:
                    return img
            except:
                ensure_printed(img_abspath, print_color='blue')
                ensure_slept(milliseconds=10)
                if is_zoom_toogle_mode == True:
                    if chrome_zoom_step == 14:
                        chrome_zoom_step = 0
                    elif chrome_zoom_step < 7:
                        ensure_pressed('ctrl', '-')
                        chrome_zoom_step = chrome_zoom_step + 1
                    elif 7 <= chrome_zoom_step:
                        ensure_pressed('ctrl', '+')
                        chrome_zoom_step = chrome_zoom_step + 1
