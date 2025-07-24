import yt_dlp


import win32con
import webbrowser
import urllib
import tomllib
import tarfile
import sys
import subprocess
import string
import sqlite3
import pywintypes

import pyglet
import pygetwindow
import pyautogui
import pickle
import os
import numpy as np
import mysql.connector
import mutagen
import keyboard
import ipdb
import functools
import easyocr
import cv2
import clipboard
import chardet
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote, urlparse
from urllib.parse import quote
from typing import TypeVar, List
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories import D_WORKING
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from PIL import Image, ImageFilter
from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from enum import Enum
from dirsync import sync
from datetime import datetime
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from collections import Counter
from bs4 import ResultSet
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def merge_d_list(d_list: List[str]):
    import os
    import string

    # f명들을 나열한다.
    # f을 깊이 별로 나열을 하고 깊이가 깊은 것부터 시작해서 깊이가 낮은 것으로 처리해 나간다

    d_list = [x for x in d_list if x.strip()]  # 리스트 요소 "" remove,  from ["", A] to [A]    from [""] to []
    d_list = [x.strip() for x in d_list]  # 리스트 각 요소 strip(),  ["   A", "B   "] from ["A", "B"]
    d_list = [x.strip("\"") for x in d_list]  # 리스트 각 요소 strip("\""),  [""A""] from ["A"]
    d_list = [x.strip("\'") for x in d_list]  # 리스트 각 요소 strip("\'),  ["'A'""] from ["A"]

    pk_print(f'''d_list={d_list}  {'%%%FOO%%%' if LTA else ''}''')

    if 0 == len(d_list):
        pk_speak_v2("pnx가 아무것도 입력되지 않았습니다", comma_delay=0.98)
        return
    elif 1 == len(d_list):
        pk_speak_v2("하나의 pnx로는 머지를 시도할수 없습니다, 여러개의 pnx들을 입력해주세요", comma_delay=0.98)
        return
    elif 1 < len(d_list):
        for index, d in enumerate(d_list):
            connected_drives = []
            for drive_letter in string.ascii_uppercase:
                drive_path = drive_letter + ":\\"
                if os.path.exists(drive_path):
                    connected_drives.append(drive_path)
                    if d == drive_path:
                        pk_speak_v2("입력된 pnx는 너무 광범위하여, 진행할 수 없도록 설정되어 있습니다", comma_delay=0.98)
                        break

        # make_d_leaf(D_EMPTY)

        # indices_to_remove=[]  # remove할 인덱스를 기록할 리스트
        # for index, directory in enumerate(directoryies_):
        #     if is_d(directory):
        #         if is_empty_directory(directory):
        #             move_pnx_without_overwrite(pnx_todo=directory, dst=D_EMPTY)
        #             indices_to_remove.append(index)
        # for index in indices_to_remove:
        #     directoryies_.pop(index)

        # for index, directory in enumerate(directoryies_):
        #     if directory == "":
        #         speak_ments("하나 이상의 pnx가 공백으로 입력되었습니다", sleep_after_play=0.65)
        #         return
        #     if not os.path.exists(directory):
        #         speak_ments("하나 이상의 pnx가 존재하지 않습니다", sleep_after_play=0.65)
        #         return

        pk_print("빈 트리 리프d별로 해체한 뒤 remove")
        f_list_to_move = []
        for index, d in enumerate(d_list):
            for root, _, f_nx_list in os.walk(d, topdown=True):
                for f_nx in f_nx_list:
                    f_list_to_move.append(rf"{root}\{f_nx}")
        [pk_print(rf'f_to_move : {f_to_move}') for f_to_move in f_list_to_move]
        pk_print(f'''type(f_list_to_move)={type(f_list_to_move)}  {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''len(f_list_to_move)={len(f_list_to_move)}  {'%%%FOO%%%' if LTA else ''}''')
        dst = rf"{os.path.dirname(d_list[0])}\{os.path.basename(d_list[0]).replace("_$merged", "")}_$merged"
        ensure_pnx_made(dst, mode="d")
        pk_print(rf'dst : {dst}')

        for f_to_move in f_list_to_move:
            move_pnx(pnx=f_to_move, d_dst=dst)

        # 이 함수는 캐싱문제를 해결하지 못함.
        def count_f_in_folder(folder_path):
            f_cnt = 0
            for _, _, f_nx_list in os.walk(folder_path):
                f_cnt += len(f_nx_list)
            return f_cnt

        # 이 함수는 캐싱문제를 해결하지 못함.
        # def count_files_in_folder(folder_path):

        #     file_count=0
        #     with os.scandir(folder_path) as entries:
        #         for entry in entries:
        #             if entry.is_file():
        #                 file_count += 1
        #     return file_count

        # 분명히 f이 들어있는데 개수가 0개로 나오네  캐싱때문에 그럴 수 있어?
        # 운영체제 성능향상을 위한 d정보 캐싱으로 갱신이 안될 수 있음.
        # d를 다른 위치로 이동한 후 다시 이동합니다. 이렇게 하면 f 시스템이 d의 변경을 감지하고 캐시를 갱신할 수 있습니다.
        # current_path=os.getcwd()
        # chdir(os.path.dirname(current_path)) # 부모 d로 이동
        # chdir(current_path)

        # [fail] 분명히 가 틀렸다. 운영체제의 캐싱이 문제가 아닌,
        # 로직을 잘못 만든 것이었다.
        # d 변수를 엉뚱하게 초기화하였기 때문이다.
        # d 를 d_ 로 별도로 호출해서 해소하였다.

        # empty d 리프단위로 분해하여 이동
        while 1:
            d_list_to_move = []
            for index, d in enumerate(d_list):
                for root, d_nx_list, f_nx_list in os.walk(d, topdown=False):
                    for d_nx in d_nx_list:
                        f_cnt = count_f_in_folder(rf"{root}\{d_nx}")
                        if f_cnt == 0:
                            d_list_to_move.append(rf"{root}\{d_nx}")

            [pk_print(sample) for sample in d_list_to_move]
            pk_print(f'''d_list_to_move={d_list_to_move}''')
            pk_print(rf'''type(d_list_to_move)={type(d_list_to_move)}''')
            pk_print(rf'''len(d_list_to_move)={len(d_list_to_move)}''')

            pk_print(rf'dst : {dst}')
            ensure_pnx_made(dst, mode="d")

            if len(d_list_to_move) == 0:
                break

            for d_to_move in d_list_to_move:
                move_pnx(pnx=d_to_move, d_dst=dst)

        for d in d_list:
            gather_empty_d(d_working=d)

        print_success(rf'd 머지를 완료했습니다')
