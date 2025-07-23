

import zipfile
import yt_dlp
# import win32gui
# import win32gui
import threading
import tarfile
import sys
import shutil
import secrets
import requests
import re
import nest_asyncio
import mutagen
import easyocr
import cv2
import colorama
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_print_state import pk_print_state

from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from os.path import dirname
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from dirsync import sync
from datetime import timedelta
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from base64 import b64encode
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def reconnect_to_qcy_h3_anc_headset_via_bluetooth():  # toogle_to_qcy_h3_anc_headset_via_bluetooth 이게 더 작명이 나은것..

    import time
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    # Bluetooth 설정창 띄우기
    cmd = 'start ms-settings:bluetooth'
    cmd_to_os_like_person_as_admin(cmd=cmd)
    window_title_seg = "설정"
    timeout = 10
    start_time = time.time()
    while 1:
        if not is_window_opened(window_title_seg=window_title_seg):
            ensure_window_to_front(window_title_seg=window_title_seg)
        else:
            break
        pk_print(working_str=time.time() - start_time)
        if time.time() - start_time > timeout:
            break
        pk_sleep(seconds=0.5)

    # string 더블 클릭
    click_string(string="QCY H3 ANC HEADSET", doubleclick_mode=True)

    # string 더블 클릭
    import asyncio
    asyncio.run(shoot_custom_screenshot_via_asyncio())
    # click_img_via_autogui()

    # string 더블 클릭
    # click_string(string="연결", doubleclick_mode=True)
    pass
