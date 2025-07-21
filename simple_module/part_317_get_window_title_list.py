import winreg
import random
import mutagen
import json
import calendar
from selenium.webdriver.chrome.service import Service
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from passlib.context import CryptContext
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes
from collections import Counter

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def get_window_title_list(process_img_n=None):
    # @pk_measure_seconds 0.000 passed at 250413
    import traceback
    # import win32gui  # pywin32
    # import win32process

    import psutil
    if process_img_n is not None:
        titles = []

        # 프로세스 목록에서 이름으로 PID 찾기
        pids = [p.info['pid'] for p in psutil.process_iter(['name', 'pid']) if p.info['name'] == process_img_n]
        if LTA:
            pk_print(f"Found PIDs : '{process_img_n}': {pids}")

        if not pids:
            pk_print(f"Process '{process_img_n}' not found.")
            return titles

        # PID에 연결된 창 검색
        def enum_windows_callback(hwnd, pids):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid in pids:
                title = win32gui.GetWindowText(hwnd)
                if title:  # 제목이 있는 창만 추가
                    titles.append(title)

        for pid in pids:
            win32gui.EnumWindows(enum_windows_callback, [pid])
        if LTA:
            print(f"Window titles for process '{process_img_n}': {titles}")
        return titles
    if process_img_n is None:
        window_titles = []
        try:
            def enum_windows_callback(hwnd, lparam):
                if win32gui.IsWindowVisible(hwnd):
                    current_window_title = win32gui.GetWindowText(hwnd)
                    if current_window_title:  # 제목이 비어 있지 않은 경우에만 추가
                        window_titles.append(current_window_title)
                return 1  # 계속해서 다른 창들도 검색

            win32gui.EnumWindows(enum_windows_callback, None)
        except Exception as e:
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        return window_titles
