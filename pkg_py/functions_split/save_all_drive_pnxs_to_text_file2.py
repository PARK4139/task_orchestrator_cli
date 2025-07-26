


import win32con
import win32com.client
import uuid
import urllib.parse
import tqdm
import toml
import toml
import socket, time
import requests
import random

import pythoncom
import psutil
import platform
import pickle
import pandas as pd
import os, inspect
import nest_asyncio
import mysql.connector
import mutagen
import json
import importlib
import hashlib
import colorama

from urllib.parse import urlparse
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from seleniumbase import Driver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.press import press
from pkg_py.functions_split.print_state import print_state
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
from PIL import Image, ImageFilter
from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from functools import partial as functools_partial
from functools import lru_cache
from fastapi import HTTPException
from datetime import timedelta
from datetime import datetime
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from collections import Counter
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def save_all_drive_pnxs_to_text_file2():  # 루프 수정필요 # 이 함수는 거의 필요 없을 것 같다. 관심_d_만 확인하는 것으로 충분해 보인다.
    import os.path
    import string

    import os

    import inspect

    func_n = inspect.currentframe().f_code.co_name

    f_func_n_txt = rf'{D_PROJECT}\pkg_txt\{func_n}.txt'
    ensure_pnx_made(pnx=f_func_n_txt, mode="item")

    # if not is_window_open(window_title=f_func_n_txt):
    #     run_pnx_via_explorer_exe(f_func_n_txt, debug_mode=False)

    # 1. 특정 경로를 제외할 텍스트 f에서 경로 읽어오기
    def load_pnxs_exclude(file_path):

        import inspect
        func_n = inspect.currentframe().f_code.co_name

        exclude_paths = set()
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    exclude_paths.add(line.strip())
        except PermissionError as e:
            print(f"PermissionError: {e}. Check if the item is accessible and you have the right permissions.")
        except Exception as e:
            print(f"Error opening item {file_path}: {e}")
        return exclude_paths

    # 2. 모든 드라이브에서 f 목록 가져오기
    def get_drives_connected():

        import inspect
        func_n = inspect.currentframe().f_code.co_name

        drives = []
        for letter in string.ascii_uppercase:
            drive = f"{letter}:\\"
            if os.path.exists(drive):
                drives.append(drive)
        ensure_printed(str_working=rf'''drives="{drives}"  {'%%%FOO%%%' if LTA else ''}''')
        return drives

    # 3. 드라이브에서 f 검색하고 처리하기
    def list_files_in_drives(exclude_paths_txt):
        import inspect
        func_n = inspect.currentframe().f_code.co_name

        exclude_paths = load_pnxs_exclude(exclude_paths_txt)
        drives = get_drives_connected()
        cnt = 0
        pnxs = []
        limit = 10000
        cnt_files = limit
        cnt_txt_files = 0
        temp = set()
        # 모든 드라이브에서 f 탐색
        for drive in drives:
            ensure_printed(str_working=rf'''drive="{drive}"  {'%%%FOO%%%' if LTA else ''}''')
            for foldername, subfolders, filenames in os.walk(drive):
                for filename in filenames:
                    file_pnx = os.path.join(foldername, filename)
                    # ensure_printed(string = rf'''file_pnx="{file_pnx}"  {'%%%FOO%%%' if LTA else ''}''')
                    cnt_files = cnt_files - 1
                    pnxs.append(file_pnx)
                    if cnt_files == 0:
                        # ensure_printed(string = rf'''file_pnx="{file_pnx}"  {'%%%FOO%%%' if LTA else ''}''')
                        cnt_files = limit
                        cnt_txt_files = cnt_txt_files + 1
                        # ensure_printed(string = rf'''cnt_txt_files="{cnt_txt_files}"  {'%%%FOO%%%' if LTA else ''}''')
                        output_pnx_txt_before = rf"{D_PKG_TXT}\{func_n}_{cnt_txt_files - 1}.txt"
                        temp = get_list_from_f(f=output_pnx_txt_before)
                        if None != temp:
                            if 0 == len(temp):
                                cnt_txt_files = cnt_txt_files - 1

                        output_pnx_txt = rf"{D_PKG_TXT}\{func_n}_{cnt_txt_files}.txt"
                        # ensure_printed(string = rf'''output_pnx_txt="{output_pnx_txt}"  {'%%%FOO%%%' if LTA else ''}''')
                        # if any(exclude_path in file_pnx for exclude_path in exclude_paths):
                        #     continue
                        with open(output_pnx_txt, 'w', encoding='utf-8') as f:
                            for pnx in pnxs:
                                cnt = cnt + 1
                                # temp.add(rf"{pnx.split("\\")[0]}\{pnx.split("\\")[1]}")
                                # print(temp)
                                for exclude_path in exclude_paths:
                                    if exclude_path in pnx:
                                        break
                                else:
                                    if not pnx.strip() == "":
                                        f.write(f'{pnx}\n')
                                        ensure_printed(
                                            str_working=rf'''cnt="{cnt}" pnxs="{pnx}" output_pnx_txt="{output_pnx_txt}"  {'%%%FOO%%%' if LTA else ''}''')
                                    else:
                                        ensure_printed(f'''없다''')
        ensure_printed(str_working=rf'''temp="{temp}"  {'%%%FOO%%%' if LTA else ''}''')

    # exec
    exclude_paths_txt = rf'{D_PKG_TXT}\{func_n}_exclude_paths.txt'
    ensure_pnx_made(pnx=exclude_paths_txt, mode='item')
    list_files_in_drives(exclude_paths_txt)
