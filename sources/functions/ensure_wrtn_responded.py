import zlib
import webbrowser
import tqdm
import threading
import shutil
import requests
import re
import random
import pywintypes
import math
import json

import asyncio
from zipfile import BadZipFile
from selenium.webdriver.chrome.service import Service
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_command_executed import ensure_command_executed

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_local_test_activate import LTA
from os.path import dirname
from functools import lru_cache
from enum import Enum
from datetime import timedelta
from concurrent.futures import ThreadPoolExecutor
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_os_windows import is_os_windows


def ask_to_wrtn(question: str):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    while 1:
        # 페이지 열기
        url = "https://wrtn.ai/"
        cmd = f'explorer  "{url}"  >NUL'
        ensure_command_executed_like_human_as_admin(cmd)

        # 크롬 창 활성화
        src_pid: int = get_pids(process_img_n="chrome.exe")  # chrome.exe pid 가져오기
        ensure_window_to_front(pid=src_pid)

        # 크롬 기본 배율로 변경
        ensure_pressed('ctrl', '0')

        # 광고닫기 버튼 클릭
        f_png = rf"{D_TASK_ORCHESTRATOR_CLI}\resources\ask_to_wrtn_ad_close.png"
        click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, loop_limit_cnt=10, is_zoom_toogle_mode=True)

        # 프롬프트 콘솔 클릭(광고 없어도 진행)
        f_png = rf"{D_TASK_ORCHESTRATOR_CLI}\resources\ask_to_wrtn.png"
        if click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, loop_limit_cnt=50, is_zoom_toogle_mode=True):
            # 질문 작성 및 확인
            ensure_writen_fast(question)
            ensure_pressed('enter')

        # 뤼튼 프롬프트 콘솔 최하단 이동 버튼 클릭
        break
