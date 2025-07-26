import win32con
import string
import sqlite3
import re
import random
import os.path
import keyboard
from urllib.parse import urlparse
from urllib.parse import quote
from selenium.webdriver.chrome.options import Options
from PySide6.QtWidgets import QApplication
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.state_via_context import SpeedControlContext
from PIL import Image
from os.path import dirname
from os import path
from gtts import gTTS
from functools import partial
from fastapi import HTTPException
from enum import Enum
from datetime import datetime
from base64 import b64decode
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def set_wake_up_next_HH_mm(HH, mm):
    """
    다음으로 오는 HH:mm 시각에 컴퓨터를 깨우도록 스케줄링합니다.
    - 이미 HH:mm이 지났다면 자동으로 다음 날 같은 시각으로 설정합니다.
    """
    from datetime import datetime, timedelta
    now = datetime.now()

    # 오늘 날짜의 HH:mm 만들기 (초는 0으로 설정)
    target_time = datetime(now.year, now.month, now.day, HH, mm, 0)

    # 이미 HH:mm이 지났다면, 다음 날로 +1일
    if target_time <= now:
        target_time += timedelta(days=1)

    # schtasks에서 "HH:MM" 포맷으로 쓰기 위해 시분만 추출
    wake_time_str = target_time.strftime("%H:%M")

    # schtasks 명령어 구성
    # /sc once 로 한 번만 exec
    # /st HH:MM 으로 exec  시각 지정
    # /f : 덮어쓰기
    # /it : 인터랙티브 모드
    task_name = "WakeComputer"
    cmd = f'schtasks /create /tn "{task_name}" /tr "cmd.exe /c exit" /sc once /st {wake_time_str} /f /it'

    # 실제 os 명령 exec  함수(sample: os.system) 대신 아래처럼 가정
    ensure_printed(f'{STAMP_DEBUG} CMD: {cmd}', print_color="blue")
    # sample: os.system(cmd)

    # 현재 시각과 예약 시각 출력
    current_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    readable_target_str = target_time.strftime("%Y-%m-%d %H:%M:%S")
    ensure_printed(f'현재 시간: {current_time_str}, 컴퓨터 깨우기 예약 시각: {readable_target_str} {'%%%FOO%%%' if LTA else ''}',
             print_color="blue")
