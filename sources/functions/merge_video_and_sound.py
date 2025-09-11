
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


from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_printed_once import ensure_printed_once

from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE

from PIL import Image
from pathlib import Path
from moviepy import VideoFileClip
from functools import partial
from fastapi import HTTPException
from datetime import datetime, time
from collections import defaultdict, Counter
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


def merge_video_and_sound(f_v, f_a):
    import inspect
    import os
    import subprocess
    import traceback

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    logging.debug(f'다운로드 d 생성')
    d_nx_list = ["storage"]
    for d_nx in d_nx_list:
        if not is_d(rf'./{d_nx}'):
            os.makedirs(rf'{d_nx}')

    logging.debug(rf'merge voiceless video and audio only video ')  # yotube 에서 고해상도 음성 없는 영상과 음성을 받아 하나의 영상으로 merge
    dst = D_VIDEOES_MERGED
    paths = [os.path.abspath(dst), os.path.basename(f_v)]
    f_va = os.path.join(*paths)
    logging.debug(rf'f_v : {f_v}')
    logging.debug(rf'f_a : {f_a}')
    logging.debug(rf'f_va : {f_va}')

    logging.debug(f'ffmpeg.exe 위치 설정')
    f_ffmpeg_exe = F_FFMPEG_EXE
    trouble_characters = ['Ä']
    trouble_characters_alternatives = {'Ä': 'A'}
    for trouble_character in trouble_characters:
        f_v = f_v.replace(trouble_character, trouble_characters_alternatives[trouble_character])
        f_a = f_a.replace(trouble_character, trouble_characters_alternatives[trouble_character])
        f_va = f_va.replace(trouble_character, trouble_characters_alternatives[trouble_character])
        logging.debug(f'f명 변경 시도')
        try:
            if trouble_character in f_va:
                os.rename(f_v,
                          f_v.replace(trouble_character, trouble_characters_alternatives[trouble_character]))
                os.rename(f_a,
                          f_a.replace(trouble_character, trouble_characters_alternatives[trouble_character]))
        except Exception as e:
            logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")

    logging.debug(f'f머지 시도')
    try:
        logging.debug(rf'echo y | "{f_ffmpeg_exe}" -i "{f_v}" -i "{f_a}" -c copy "{f_va}"')
        lines = subprocess.check_output(
            rf'echo y | "{f_ffmpeg_exe}" -i "{f_v}" -i "{f_a}" -c copy "{f_va}"', shell=True).decode(
            'utf-8').split("\n")
        for line in lines:
            logging.debug(line)
    except Exception as e:
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")

    logging.debug(rf'다운로드 및 merge 결과 확인 시도')
    try:
        logging.debug(rf'explorer "{f_va}"')
        subprocess.check_output(rf'explorer "{f_va}"', shell=True).decode('utf-8').split("\n")
    except Exception as e:
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")

    logging.debug(f'불필요 리소스 삭제 시도')
    try:
        if os.path.exists(f_va):
            subprocess.check_output(rf'echo y | del /f "{f_v}"', shell=True).decode('utf-8').split("\n")
            lines = subprocess.check_output(rf'echo y | del /f "{f_a}"', shell=True).decode('utf-8').split("\n")
            for line in lines:
                logging.debug(line)
    except Exception as e:
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
