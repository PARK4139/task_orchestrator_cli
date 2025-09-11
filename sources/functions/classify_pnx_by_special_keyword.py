import yt_dlp
import webbrowser
import urllib.parse
import urllib
import undetected_chromedriver as uc
import traceback
import tqdm
import timeit
import socket, time

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
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_database import PkSqlite3DB

from paramiko import SSHClient, AutoAddPolicy
from datetime import datetime
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from sources.functions.get_nx import get_nx
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def classify_pnx_by_special_keyword(d_src, special_keyword, with_walking):
    import os
    import string

    d_src = d_src.strip()
    d_src = d_src.replace("\"", "")
    d_src = d_src.replace("\'", "")
    logging.debug(f'''d_src={d_src} special_keyword={special_keyword}''')
    connected_drives = []
    for drive_letter in string.ascii_uppercase:
        drive_path = drive_letter + ":\\"
        if os.path.exists(drive_path):
            connected_drives.append(drive_path)
            if d_src == drive_path:
                logging.debug(rf'''광범위진행제한 {'%%%FOO%%%' if LTA else ''}''')
                return

    if not os.path.exists(d_src):
        logging.debug(rf"입력된 d_src 가 존재하지 않습니다 d_src={d_src}")
        return

    if d_src == "":
        logging.debug(f'''d_src == "" ''')
        return

    special_dirs_promised = [
        # "blahblahblah_boom_boom_boom",
    ]
    # previous_keyword=get_text_from_clipboard()
    # if previous_keyword == pnx:
    #     previous_keyword=""

    special_keyword = special_keyword.strip()
    if special_keyword == "":
        logging.debug("special_keyword 는 ""일 수 없습니다.")
        return
    if "\n" in special_keyword:
        f_list = special_keyword.split("\n")
    else:
        f_list = [special_keyword]
    f_nx_list = [get_nx(f) for f in f_list]
    logging.debug(f'''len(f_list)={len(f_list)} {'%%%FOO%%%' if LTA else ''}''')
    logging.debug(f'''f_nx_list={f_nx_list}  {'%%%FOO%%%' if LTA else ''}''')
    for special_keyword in f_list:
        special_keyword = special_keyword.strip()
        if special_keyword != "":
            special_dirs_promised.append(special_keyword)
        for special_pnx in special_dirs_promised:
            ensure_pnx_made(rf"{D_PK_WORKING_EXTERNAL}\{special_pnx}", mode="d")
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

        logging.debug(rf'''len(pnxs_searched)="{len(pnxs_searched)}"  {'%%%FOO%%%' if LTA else ''}''')  # 검색된 f 개수
        dst = None
        for index, special_dir in enumerate(special_dirs_promised):
            dst = rf"{D_PK_WORKING_EXTERNAL}\{special_dirs_promised[index]}"
            for pnx_searched in pnxs_searched:
                if special_dir in os.path.basename(pnx_searched):
                    ensure_pnx_moved(pnx=pnx_searched, d_dst=dst)
        special_dirs_promised = []
        logging.debug(rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''')
