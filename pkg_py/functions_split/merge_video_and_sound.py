# import win32process
import win32com.client
import uuid
import undetected_chromedriver as uc
import traceback
import tomllib
import toml
import time
import threading
import socket
import secrets
import random
import pywintypes
# import pywin32
import pyglet
import pyautogui
import paramiko
import os
import mutagen
import keyboard
import ipdb
import inspect
import colorama
import clipboard
import chardet
import calendar
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from telegram import Bot
from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_once import pk_print_once

from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from PIL import Image
from pathlib import Path
from moviepy import VideoFileClip
from functools import partial
from fastapi import HTTPException
from datetime import datetime, time
from collections import defaultdict, Counter
from pkg_py.pk_system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def merge_video_and_sound(f_v, f_a):
    import inspect
    import os
    import subprocess
    import traceback

    func_n = inspect.currentframe().f_code.co_name

    pk_print(f'다운로드 d 생성')
    d_nx_list = ["storage"]
    for d_nx in d_nx_list:
        if not is_d(rf'./{d_nx}'):
            os.makedirs(rf'{d_nx}')

    pk_print(rf'merge voiceless video and audio only video ')  # yotube 에서 고해상도 음성 없는 영상과 음성을 받아 하나의 영상으로 merge
    dst = D_VIDEOES_MERGED
    paths = [os.path.abspath(dst), os.path.basename(f_v)]
    f_va = os.path.join(*paths)
    pk_print(rf'f_v : {f_v}', print_color='blue')
    pk_print(rf'f_a : {f_a}', print_color='blue')
    pk_print(rf'f_va : {f_va}', print_color='blue')

    pk_print(f'ffmpeg.exe 위치 설정')
    f_ffmpeg_exe = F_FFMPEG_EXE
    trouble_characters = ['Ä']
    trouble_characters_alternatives = {'Ä': 'A'}
    for trouble_character in trouble_characters:
        f_v = f_v.replace(trouble_character, trouble_characters_alternatives[trouble_character])
        f_a = f_a.replace(trouble_character, trouble_characters_alternatives[trouble_character])
        f_va = f_va.replace(trouble_character, trouble_characters_alternatives[trouble_character])
        pk_print(f'f명 변경 시도')
        try:
            if trouble_character in f_va:
                os.rename(f_v,
                          f_v.replace(trouble_character, trouble_characters_alternatives[trouble_character]))
                os.rename(f_a,
                          f_a.replace(trouble_character, trouble_characters_alternatives[trouble_character]))
        except Exception as e:
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

    pk_print(f' f머지 시도')
    try:
        pk_print(rf'echo y | "{f_ffmpeg_exe}" -i "{f_v}" -i "{f_a}" -c copy "{f_va}"', print_color='blue')
        lines = subprocess.check_output(
            rf'echo y | "{f_ffmpeg_exe}" -i "{f_v}" -i "{f_a}" -c copy "{f_va}"', shell=True).decode(
            'utf-8').split("\n")
        for line in lines:
            pk_print(line, print_color='blue')
    except Exception as e:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

    pk_print(rf'다운로드 및 merge 결과 확인 시도', print_color='blue')
    try:
        pk_print(rf'explorer "{f_va}"', print_color='blue')
        subprocess.check_output(rf'explorer "{f_va}"', shell=True).decode('utf-8').split("\n")
    except Exception as e:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

    pk_print(f' 불필요 리소스 삭제 시도')
    try:
        if os.path.exists(f_va):
            subprocess.check_output(rf'echo y | del /f "{f_v}"', shell=True).decode('utf-8').split("\n")
            lines = subprocess.check_output(rf'echo y | del /f "{f_a}"', shell=True).decode('utf-8').split("\n")
            for line in lines:
                pk_print(line, print_color='blue')
    except Exception as e:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
