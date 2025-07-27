import zipfile
import yt_dlp

import win32con
import webbrowser
import uuid
import urllib
import traceback
import tomllib
import time
import sys
import subprocess, time
import sqlite3
import speech_recognition as sr
import socket
import secrets
import random

import pythoncom
import pyglet
import pickle
import paramiko
import pandas as pd
import numpy as np
import nest_asyncio
import mutagen
import math
import json
import cv2
import colorama
from zipfile import BadZipFile
from urllib.parse import urlparse
from urllib.parse import quote
from typing import TypeVar, List
from tkinter import UNDERLINE
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from queue import Queue, Empty
from pytube import Playlist
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.performance_logic import ensure_seconds_measured, pk_measure_memory
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.get_list_calculated import get_list_calculated

from PIL import Image
from os import path
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from enum import Enum
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.is_d import is_d
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def ask_to_chat_gpt(question):
    import pyautogui
    # 페이지 열기
    url = "https://chatgpt.com/"
    ensure_command_excuted_to_os(cmd=f'explorer "{url}"')

    # 창 앞으로 이동
    window_title = "Chrome"
    window_title_seg = window_title,
    ensure_window_to_front(window_title_seg=window_title_seg)

    # chrome 창 탭 중 해당 url로 이동
    move_chrome_tab_by_url(url=url)

    # text_string 클릭
    # text_string="로그아웃 유지"
    # text_coordinates=get_text_coordinates_via_easy_ocr(string=text_string)
    # # text_coordinates=(692.0, 1047.5)
    # if not text_coordinates:
    #     print(rf"Text not found. {text_string}")
    #     return
    # x_abs, y_abs=text_coordinates
    # move_mouse(x_abs=x_abs, y_abs=y_abs)
    # click_mouse_left_btn(x_abs=x_abs, y_abs=y_abs)
    # print(rf"{text_string}")

    # 스크린샷 프로그램 exec
    # collect_img_for_autogui()
    # asyncio.run(shoot_custom_screenshot())

    # 이미지 바운딩박스 찾아 가운데 센터 클릭 ...
    f_png = rf"{D_PROJECT}\pk_image\screenshot_로그아웃_유지_2024_11_19_02_54_14.png"
    # click_center_of_img_recognized_by_mouse_left(img_abspath=f_png, loop_limit_cnt=10, is_zoom_toogle_mode=False)
    # 인식률 및 속도 개선 시도
    # pip install opencv-python # 이것은 고급 기능이 포함되지 않은 Python용 OpenCV의 미니 버전입니다. 우리의 목적에는 충분합니다.
    # confidence=0.7(70%)유사도를 낮춰 인식률개선시도, region 낮춰 속도개선시도, grayscale 흑백으로 판단해서 속도개선시도,
    # open cv 설치했는데 적용안되고 있음. 재부팅도 하였는 데도 안됨.
    # xy_infos_of_imgs=pyautogui.locateOnScreen(img_abspath, confidence=0.7, grayscale=True)
    # debug_as_gui(xy_infos_of_imgs is None)
    img = pyautogui.locateOnScreen(f_png, confidence=0.7, grayscale=True)

    # # 프롬프트 콘솔 클릭(광고 없어도 진행)
    # f_png=rf"{PROJECT_D}\pkg_png\ask_to_wrtn.png"
    # if click_center_of_img_recognized_by_mouse_left(img_abspath=f_png, recognize_loop_limit_cnt=50, is_zoom_toogle_mode=True):
    #     # 질문 작성 및 확인
    #     ensure_writen_fast(question)
    #     press('enter')

    # 뤼튼 프롬프트 콘솔 최하단 이동 버튼 클릭
