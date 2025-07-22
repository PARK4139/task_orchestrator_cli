import winreg
import uuid
import shlex
import pythoncom
import mysql.connector
import keyboard
import ipdb
import importlib
import cv2
import clipboard
import asyncio
from selenium.webdriver.support.ui import WebDriverWait
from pytube import Playlist
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from mutagen.mp3 import MP3
from fastapi import HTTPException
from collections import Counter
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def ensure_window_to_front_v0(window_title_seg=None, pid=None):
    import inspect
    import traceback
    import win32con  # pywin32
    # import win32gui  # pywin32
    # import win32process

    import psutil
    func_n = inspect.currentframe().f_code.co_name
    if window_title_seg is not None:
        while 1:
            window_title = get_window_title(window_title_seg=window_title_seg)
            if is_window_title_opened(window_title=window_title):
                if not is_window_title_front(window_title=window_title):
                    import pywintypes
                    try:
                        def enum_windows_callback(hwnd, lparam):
                            if win32gui.IsWindowVisible(hwnd):
                                current_window_title = win32gui.GetWindowText(hwnd)
                                if window_title.lower() in current_window_title.lower():
                                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                                    pk_sleep(seconds=0.2)
                                    try:
                                        win32gui.SetForegroundWindow(hwnd)  # 창을 제일 앞으로 가져옴
                                    except Exception as e:
                                        pk_sleep(seconds=0.2)
                                        pk_print(f''' can not move window ({window_title}) to front.''',
                                                 print_color='red')
                                        win32gui.SetForegroundWindow(hwnd)
                                    return 0  # 더 이상 검색하지 않음
                            return 1  # 계속 검색

                        try:
                            win32gui.EnumWindows(enum_windows_callback, None)
                        except pywintypes.error:
                            # pk_print(f"{traceback.format_exc()}", print_color='red')
                            pass
                    except Exception as e:
                        pk_print(f"{traceback.format_exc()}", print_color='red')
                if is_window_title_front(window_title=window_title):
                    pk_print(f'''move window ({window_title}) to front via {func_n}()''', print_color='blue')
                    break
            else:
                return
    if pid is not None:
        if not str(pid).isdigit():
            # pk_print(f"PID 분석 결과 숫자가 아닌 것으로 판단: {pid}  {'%%%FOO%%%' if LTA else ''}", print_color='red')
            return
        pid = int(pid)
        try:
            # PID에 해당하는 프로세스 객체 가져오기
            process = psutil.Process(pid)
            if process.is_running() and process.status() != psutil.STATUS_ZOMBIE:
                hwnd = win32gui.FindWindow(None, None)  # 첫 번째 창 핸들을 가져옴
                while hwnd:
                    _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
                    if found_pid == pid:
                        try:
                            win32gui.SetForegroundWindow(hwnd)  # 창 활성화
                            break
                        except Exception as e:
                            # pk_print(f"창 활성화 실패: {e}", print_color='red')
                            pass
                    # 다음 창 핸들 검색
                    hwnd = win32gui.FindWindowEx(None, hwnd, None, None)
                else:
                    # pk_print(f"PID {pid}에 해당하는 창 핸들을 찾을 수 없습니다.", print_color='red')
                    pass
            else:
                # pk_print(f"{UNDERLINE}프로세스가 exec  중이지 않거나 좀비 상태입니다.", print_color='red')
                pass
        except psutil.NoSuchProcess:
            # pk_print(f"{UNDERLINE}유효하지 않은 PID입니다.", print_color='red')
            pass
        except Exception as e:
            pk_print(f"알 수 없는 {e}", print_color='red')
            pass
