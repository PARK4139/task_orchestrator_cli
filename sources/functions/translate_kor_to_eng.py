import win32con
import webbrowser
import traceback
import timeit
import tarfile
import sqlite3
import re

import psutil

from telegram import Bot
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
from prompt_toolkit import PromptSession
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from os.path import dirname
from base64 import b64encode

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from pathlib import Path
from sources.functions.is_d import is_d
from sources.functions.is_os_wsl_linux import is_os_wsl_linux

from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def translate_kor_to_eng(question: str):
    import sys
    import traceback

    import pyautogui
    if not is_internet_connected():
        raise
    try:
        while 1:
            try:
                question = question.strip('""')
            except AttributeError:
                break
            ensure_pressed("win", "m")

            # 페이지 열기
            url = "https://www.google.com/search?q=kor+to+eng"
            cmd = f'explorer "{url}" >NUL'
            ensure_command_executed_like_human_as_admin(cmd)

            # 크롬 창 활성화
            target_pid = get_pids(process_img_n="chrome.exe")  # chrome.exe pid 가져오기
            ensure_window_to_front(pid=target_pid)

            # Enter Text 클릭
            f_png = rf"{D_TASK_ORCHESTRATOR_CLI}\resources\kor to eng.png"
            click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, is_zoom_toogle_mode=True, loop_limit_cnt=100)

            # 번역할 내용 작성
            ensure_writen_fast(question)

            # 글자수가 많으면 text to voice icon 이 잘려서 보이지 않음. 이는 이미지의 객체 인식이 불가능해지는데
            # 스크롤를 내려서 이미지 인식을 가능토록
            if len(question) > 45:
                pyautogui.vscroll(-15)
            ensure_slept(30)

            # text to voice icon
            f_png = rf"{D_TASK_ORCHESTRATOR_CLI}\resources\text to voice icon.png"
            click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, is_zoom_toogle_mode=True, loop_limit_cnt=100)

            break
    except:
        traceback.print_exc(file=sys.stdout)
