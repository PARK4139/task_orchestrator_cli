import zlib
import win32con
import urllib.parse
import undetected_chromedriver as uc
import tqdm
import tomllib
import subprocess


import paramiko
import os.path
import os
import json
import inspect
from yt_dlp import YoutubeDL
from tkinter import UNDERLINE
from PySide6.QtWidgets import QApplication

from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_context import SpeedControlContext
from PIL import Image
from moviepy import VideoFileClip
from functools import partial
from dirsync import sync
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.is_f import is_f
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.does_pnx_exist import is_pnx_existing

import logging


def print_built_in_info(thing_curious):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    logging.debug(f"{inspect.currentframe().f_code.co_name} {str(thing_curious.__code__.co_varnames)}")
    logging.debug("_______________________________________________________________ " + str() + "(" + str(
        thing_curious) + ") s")
    logging.debug("print(inspect.getsource(thing_curious))")
    print(inspect.getsource(thing_curious))
    logging.debug("for i in inspect.getmembers(thing_curious_):")
    for i in inspect.getmembers(thing_curious):
        print(i)
    logging.debug("print(help(thing_curious))")
    print(help(thing_curious))
    logging.debug("[x for x in dir(thing_curious) if '__' not in x]")
    foo = [x for x in dir(thing_curious) if '__' not in x]
    # dir() 함수는 값 없이 지정된 객체의 모든 속성과 메서드를 반환합니다 .
    # 이 함수는 모든 속성과 메서드를 반환하며, 모든 개체에 대한 기본값인 내장 속성도 반환합니다.
    logging.debug("[x for x in dir(thing_curious) if '__' not in x]")
