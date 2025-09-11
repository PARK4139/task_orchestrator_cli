
import win32con
import sys
import shutil
import requests
import pywintypes
import platform
import math
import datetime
import calendar
from tkinter import UNDERLINE
from PySide6.QtWidgets import QApplication
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.is_window_opened import is_window_opened
import logging
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE


from os import path
from fastapi import HTTPException
from enum import Enum
from colorama import init as pk_colorama_init
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS
from sources.functions.get_pnx_unix_style import get_pnx_unix_style

import logging
from sources.functions.get_pnxs import get_pnxs


def make_pnx_interested_list_to_f_txt(pnx_interested_list=None, string_exclude=None):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    # pnx_interested_list=[]
    if pnx_interested_list is None:
        pnx_interested_list = [
            rf'{D_DOWNLOADS}',
            rf'{D_HOME}\AppData\Roaming\bittorrent',

            rf'D:\\',
            rf'E:\\',
            rf'F:\\',
        ]
    # pnxs_exclude=[]
    if pnx_interested_list is None:
        string_exclude = [
            rf'{D_DOWNLOADS}\[]\docker_image_maker\venv',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\ios',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\macos',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\windows',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\web',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\linux',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\lib',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\build',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\asset',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\android',

            rf'D:\$RECYCLE.BIN',
            rf'D:\System Volume Information',

            rf'E:\$RECYCLE.BIN',
            rf'E:\System Volume Information',

            rf'F:\$RECYCLE.BIN',
            rf'F:\System Volume Information',

            rf'deprecated',
            rf'archived',
            rf'.git',
            rf'.idea',
            rf'venv',
            rf'node_modules',
            rf'test_flutter',
            rf'task_orchestrator_cli_sensitive_public',
            rf'telegram memo export by static web',
            rf'docker_image_maker',
            rf'e-magazine',
            rf'netlify-web',
        ]

    pnx_processed_list = []
    f_func_n_txt = rf"{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}\{func_n}.txt"
    ensure_str_writen_to_f(msg=f"", f=f_func_n_txt, mode="w")  # 내용 초기화
    for pnx_interested in pnx_interested_list:
        pnxs_with_walking = get_pnxs(d_working=pnx_interested, filtered="f", with_walking=True)
        for pnx_with_walking in pnxs_with_walking:
            if any(pnx_exclude in pnx_with_walking for pnx_exclude in string_exclude):
                continue
            pnx_processed_list.append(pnx_with_walking)
            ensure_str_writen_to_f(msg=f"{pnx_with_walking}\n", f=f_func_n_txt, mode="a")
