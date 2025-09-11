

import zipfile
import yt_dlp


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
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_state_printed import ensure_state_printed


from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER

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
from pathlib import Path
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_f import is_f
from sources.objects.pk_local_test_activate import LTA
from sources.functions.does_pnx_exist import is_pnx_existing

import logging
from sources.functions.get_d_working import get_d_working


def reconnect_to_qcy_h3_anc_headset_via_bluetooth():  # toogle_to_qcy_h3_anc_headset_via_bluetooth 이게 더 작명이 나은것..

    import time
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    # Bluetooth 설정창 띄우기
    cmd = 'start ms-settings:bluetooth'
    ensure_command_executed_like_human_as_admin(cmd=cmd)
    window_title_seg = "설정"
    timeout = 10
    start_time = time.time()
    while 1:
        if not is_window_opened(window_title_seg=window_title_seg):
            ensure_window_to_front(window_title_seg)
        else:
            break
        logging.debug(time.time() - start_time)
        if time.time() - start_time > timeout:
            break
        ensure_slept(seconds=0.5)

    # string 더블 클릭
    ensure_text_clicked_via_ocr(text="QCY H3 ANC HEADSET", doubleclick_mode=True)

    # string 더블 클릭
    import asyncio
    asyncio.run(shoot_custom_screenshot_via_asyncio())
    # click_img_via_autogui()

    # string 더블 클릭
    # ensure_text_clicked_via_ocr(text="연결", doubleclick_mode=True)
    pass
