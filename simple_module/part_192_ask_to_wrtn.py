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
import browser_cookie3
import asyncio
from zipfile import BadZipFile
from selenium.webdriver.chrome.service import Service
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from os.path import dirname
from functools import lru_cache
from enum import Enum
from datetime import timedelta
from concurrent.futures import ThreadPoolExecutor
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows


def ask_to_wrtn(question: str):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    while 1:
        # 페이지 열기
        url = "https://wrtn.ai/"
        cmd = f'explorer  "{url}"  >nul'
        cmd_to_os_like_person_as_admin(cmd)

        # 크롬 창 활성화
        src_pid: int = get_pids(process_img_n="chrome.exe")  # chrome.exe pid 가져오기
        ensure_window_to_front(pid=src_pid)

        # 크롬 기본 배율로 변경
        pk_press('ctrl', '0')

        # 광고닫기 버튼 클릭
        f_png = rf"{D_PROJECT}\pkg_png\ask_to_wrtn_ad_close.png"
        click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, loop_limit_cnt=10, is_zoom_toogle_mode=True)

        # 프롬프트 콘솔 클릭(광고 없어도 진행)
        f_png = rf"{D_PROJECT}\pkg_png\ask_to_wrtn.png"
        if click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, loop_limit_cnt=50, is_zoom_toogle_mode=True):
            # 질문 작성 및 확인
            write_fast(question)
            pk_press('enter')

        # 뤼튼 프롬프트 콘솔 최하단 이동 버튼 클릭
        break
