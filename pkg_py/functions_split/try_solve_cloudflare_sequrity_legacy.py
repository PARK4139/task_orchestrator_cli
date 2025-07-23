# import win32gui
import uuid
import threading
import socket
import numpy as np
import mysql.connector
import mutagen
import inspect
import colorama
import colorama
import chardet
import calendar
import browser_cookie3
import asyncio
from urllib.parse import quote
from selenium.webdriver.common.action_chains import ActionChains
from pynput import mouse
from prompt_toolkit.styles import Style
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load

from pkg_py.pk_system_object.is_os_windows import is_os_windows

from passlib.context import CryptContext
from functools import partial
from fastapi import HTTPException
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from bs4 import ResultSet
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def try_solve_cloudflare_sequrity_legacy(driver):  # fail
    import random

    url = f'https://torrentqq348.com'
    url_decoded = get_str_url_decoded(url)
    pk_print(working_str=rf'''url={url:60s}  url_decoded={url_decoded}  {'%%%FOO%%%' if LTA else ''}''',
             print_color='blue')
    driver.get(url_decoded)
    # driver.get(url)
    pk_sleep(milliseconds=random.randint(a=222, b=1333))
    try_cnt_limit = 22
    try_cnt = 0
    tab_title_negative = "잠시만 기다리십시오"
    f_png = rf'{D_PKG_PNG}\collect_img_for_autogui_2024_11_03_19_41_12.png'
    while 1:
        if does_normal_tab_exist(driver_selenium=driver, tab_title_negative=tab_title_negative):
            # move to tab
            window_required = driver.current_window_handle  # 현재 창 핸들 저장
            driver.switch_to.window(window_required)
            break
        try_cnt += 1
        if try_cnt == try_cnt_limit:
            kill_tabs_except_current_tab_via_selenium(driver)
            driver.get(url)
            pk_sleep(milliseconds=random.randint(a=1222, b=2333))
            try_cnt = 0

        # click checkbox
        ensure_window_to_front(window_title_seg=tab_title_negative)  # 창을 맨앞으로 가져오기
        pk_sleep(milliseconds=200)
        click_img_via_autogui(f_png, x_cal=random.randint(a=3, b=150))

        # edit url like person
        edit_browser_url_like_person()

        # copy tab
        # copy_tab_like_pserson()
        # open_tab_via_selenium(driver, url)
