import tomllib
import speech_recognition as sr
import shutil
import pythoncom
import importlib
import colorama
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_once import pk_print_once

from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from moviepy import VideoFileClip
from fastapi import HTTPException
from datetime import timedelta
from cryptography.hazmat.backends import default_backend


def find_direction_via_naver_map(destination: str):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    while 1:
        # 배경화면으로 나가기(옵션로직)
        # press("win", "m")
        # press("win", "m")
        # sleep(10)

        # 페이지 열기
        # url="https://map.naver.com/"
        url = "https://map.naver.com/p/directions"
        cmd = f'explorer  "{url}"  >nul'
        cmd_to_os_like_person_as_admin(cmd)
        pk_sleep(300)

        # 크롬 창 활성화
        pid_chrome_exe = get_pids(process_img_n="chrome.exe")  # chrome.exe pid 가져오기
        ensure_window_to_front(pid=pid_chrome_exe)
        pk_sleep(30)

        # 반쪽화면 생성(옵션로직)
        # press("alt", "up")
        # press("alt", "left")

        # 출발지 입력 클릭
        f_png = rf"{D_PROJECT}\pkg_png\find_direction_via_naver_direction.png"
        click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, loop_limit_cnt=100, is_zoom_toogle_mode=True)
        pk_sleep(30)

        # 한가람한양아파트상가 입력
        write_fast("한가람한양아파트상가")
        pk_sleep(30)
        pk_press('enter')
        pk_sleep(300)
        pk_press('tab')
        pk_sleep(30)

        # 목적지 입력
        write_fast(destination)
        pk_sleep(30)
        pk_press('down')
        pk_press('enter')

        # 길찾기 클릭
        pk_press('tab')
        pk_press('tab')
        pk_press('tab')
        pk_press('enter')

        # 작업마침 알림
        pk_speak_v2(str_working='길찾기가 시도되었습니다', comma_delay=0.98)
        break
