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
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.local_test_activate import LTA
from os.path import dirname
from functools import lru_cache
from enum import Enum
from datetime import timedelta
from concurrent.futures import ThreadPoolExecutor
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_os_windows import is_os_windows


def ask_to_wrtn(question: str):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    while 1:
        # 페이지 열기
        url = "https://wrtn.ai/"
        cmd = f'explorer  "{url}"  >nul'
        ensure_command_excuted_to_os_like_person_as_admin(cmd)

        # 크롬 창 활성화
        src_pid: int = get_pids(process_img_n="chrome.exe")  # chrome.exe pid 가져오기
        ensure_window_to_front(pid=src_pid)

        # 크롬 기본 배율로 변경
        ensure_pressed('ctrl', '0')

        # 광고닫기 버튼 클릭
        f_png = rf"{D_PROJECT}\pkg_image\ask_to_wrtn_ad_close.png"
        click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, loop_limit_cnt=10, is_zoom_toogle_mode=True)

        # 프롬프트 콘솔 클릭(광고 없어도 진행)
        f_png = rf"{D_PROJECT}\pkg_image\ask_to_wrtn.png"
        if click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, loop_limit_cnt=50, is_zoom_toogle_mode=True):
            # 질문 작성 및 확인
            ensure_writen_fast(question)
            ensure_pressed('enter')

        # 뤼튼 프롬프트 콘솔 최하단 이동 버튼 클릭
        break
