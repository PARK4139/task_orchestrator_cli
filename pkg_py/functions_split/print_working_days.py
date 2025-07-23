import win32con
import pyautogui
import paramiko
import pandas as pd
import json
from tkinter import UNDERLINE
from seleniumbase import Driver
from pynput import mouse
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.pk_system_object.print_red import print_red
from pathlib import Path
from base64 import b64decode
from pkg_py.functions_split.is_f import is_f
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def print_working_days(task_name, year):
    from datetime import datetime, timedelta
    import calendar
    # year년의 첫날과 마지막 날
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)

    # 요일 딕셔너리
    weekday_dict = {0: "월", 1: "화", 2: "수", 3: "목", 4: "금", 5: "토", 6: "일"}

    # 현재 날짜를 시작 날짜로 설정
    current_date = start_date

    while current_date <= end_date:
        # 요일 계산
        weekday = weekday_dict[current_date.weekday()]

        # 월요일 ~ 금요일(근무일)만 출력
        if current_date.weekday() < 5:  # 월(0) ~ 금(4)
            print(rf'mkr_{current_date.strftime("%Y-%m-%d")} ({weekday}) __:__ "{task_name}"')

        # 말일 구분선 출력
        last_day_of_month = calendar.monthrange(current_date.year, current_date.month)[1]
        if current_date.day == last_day_of_month:
            print(rf"{UNDERLINE}")

        # 다음 날로 이동
        current_date += timedelta(days=1)
