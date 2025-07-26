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
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.press import press
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.state_via_context import SpeedControlContext
from PIL import Image
from moviepy import VideoFileClip
from functools import partial
from dirsync import sync
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.ensure_printed import ensure_printed


def print_built_in_info(thing_curious):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    ensure_printed(f"{inspect.currentframe().f_code.co_name} {str(thing_curious.__code__.co_varnames)}")
    ensure_printed(str_working="_______________________________________________________________ " + str() + "(" + str(
        thing_curious) + ") s")
    ensure_printed(str_working="print(inspect.getsource(thing_curious))")
    print(inspect.getsource(thing_curious))
    ensure_printed(str_working="for i in inspect.getmembers(thing_curious_):")
    for i in inspect.getmembers(thing_curious):
        print(i)
    ensure_printed(str_working="print(help(thing_curious))")
    print(help(thing_curious))
    ensure_printed(str_working="[x for x in dir(thing_curious) if '__' not in x]")
    foo = [x for x in dir(thing_curious) if '__' not in x]
    # dir() 함수는 값 없이 지정된 객체의 모든 속성과 메서드를 반환합니다 .
    # 이 함수는 모든 속성과 메서드를 반환하며, 모든 개체에 대한 기본값인 내장 속성도 반환합니다.
    ensure_printed(str_working="[x for x in dir(thing_curious) if '__' not in x]")
