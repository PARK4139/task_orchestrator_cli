import yt_dlp
import webbrowser
import urllib.parse
import urllib
import undetected_chromedriver as uc
import traceback
import tqdm
import timeit
import socket, time
# import pywin32
import pickle
import os.path
import numpy as np
import ipdb
import importlib
import datetime
import colorama
import clipboard
import asyncio
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.state_via_database import PkSqlite3DB

from paramiko import SSHClient, AutoAddPolicy
from datetime import datetime
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def classify_pnx_by_special_keyword(d_src, special_keyword, with_walking):
    import os
    import string

    d_src = d_src.strip()
    d_src = d_src.replace("\"", "")
    d_src = d_src.replace("\'", "")
    pk_print(f'''d_src={d_src} special_keyword={special_keyword}''')
    connected_drives = []
    for drive_letter in string.ascii_uppercase:
        drive_path = drive_letter + ":\\"
        if os.path.exists(drive_path):
            connected_drives.append(drive_path)
            if d_src == drive_path:
                pk_print(str_working=rf'''광범위진행제한 {'%%%FOO%%%' if LTA else ''}''', print_color='red')
                return

    if not os.path.exists(d_src):
        pk_print(str_working=rf"입력된 d_src 가 존재하지 않습니다 d_src={d_src}", print_color='red')
        return

    if d_src == "":
        pk_print(f'''  d_src == "" ''', print_color='red')
        return

    special_dirs_promised = [
        # "blahblahblah_boom_boom_boom",
    ]
    # previous_keyword=pk_paste()
    # if previous_keyword == pnx:
    #     previous_keyword=""

    special_keyword = special_keyword.strip()
    if special_keyword == "":
        pk_print(str_working="special_keyword 는 ""일 수 없습니다.", print_color='red')
        return
    if "\n" in special_keyword:
        f_list = special_keyword.split("\n")
    else:
        f_list = [special_keyword]
    f_nx_list = [get_nx(f) for f in f_list]
    pk_print(f'''len(f_list)={len(f_list)} {'%%%FOO%%%' if LTA else ''}''')
    pk_print(f'''f_nx_list={f_nx_list}  {'%%%FOO%%%' if LTA else ''}''')
    for special_keyword in f_list:
        special_keyword = special_keyword.strip()
        if special_keyword != "":
            special_dirs_promised.append(special_keyword)
        for special_pnx in special_dirs_promised:
            ensure_pnx_made(rf"{D_WORKING_EXTERNAL}\{special_pnx}", mode="d")
        pnxs_searched = []
        if is_d(d_src):
            if with_walking == True:
                for root, d_nx_list, f_nx_list in os.walk(d_src, topdown=False):  # os.walk()는 with walking 으로 동작한다
                    for f_nx in f_nx_list:
                        f = os.path.join(root, f_nx)
                        for special_keyword in special_dirs_promised:
                            if special_keyword in os.path.basename(f):
                                pnxs_searched.append(f)
            else:
                # todo : without_waling
                return

        pk_print(
            str_working=rf'''len(pnxs_searched)="{len(pnxs_searched)}"  {'%%%FOO%%%' if LTA else ''}''')  # 검색된 f 개수
        dst = None
        for index, special_dir in enumerate(special_dirs_promised):
            dst = rf"{D_WORKING_EXTERNAL}\{special_dirs_promised[index]}"
            for pnx_searched in pnxs_searched:
                if special_dir in os.path.basename(pnx_searched):
                    move_pnx(pnx=pnx_searched, d_dst=dst)
        special_dirs_promised = []
        pk_print(str_working=rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''', print_color='green')
