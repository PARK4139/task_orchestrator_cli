import winreg

import webbrowser
import urllib
import undetected_chromedriver as uc
import toml
import time
import sys
import socket, time
import requests
import random, math

import psutil
import platform
import pickle
import math
import cv2
import clipboard
import chardet
import calendar
from zipfile import BadZipFile
from selenium.common.exceptions import WebDriverException
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.pk_print_state import pk_print_state

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.local_test_activate import LTA

from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from fastapi import HTTPException
from cryptography.hazmat.backends import default_backend
from colorama import init as pk_colorama_init
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def download_video_mp4(url: str):
    import inspect
    import os
    import traceback

    func_n = inspect.currentframe().f_code.co_name
    while 1:
        if url.strip() == "":
            pk_print(rf"if url.strip() == "":", print_color='blue')
            break

        pk_print(str_working=rf'''url="{url}"  {'%%%FOO%%%' if LTA else ''}''')
        video_id = ''
        cmd = rf'{F_YT_DLP_EXE} -F {url}'
        lines = cmd_to_os(cmd=cmd)

        video_ids_allowed = VIDEO_IDS_ALLOWED
        audio_ids_allowed = AUDIO_IDS_ALLOWED
        audio_id = ""
        for line in lines:
            if 'video only' in line or 'audio only' in line:
                pk_print(f"line: {line}", print_color='blue')
                # video_id 설정
                for id in video_ids_allowed:
                    if id in line:
                        video_id = id
                        if video_id.strip() == "":
                            pk_print(rf"다운로드 할 수 있는 video_id가 아닙니다 {video_id.strip()}", print_color='blue')
                            break
                # audio_id 설정
                for id in audio_ids_allowed:
                    if id in line:
                        audio_id = id
                        if audio_id.strip() == "":
                            pk_print(rf"다운로드 할 수 있는 audio_id가 아닙니다 {audio_id.strip()}", print_color='blue')
                            break
                        break

        cmd = rf'{F_YT_DLP_EXE} -f "bestvideo[ext=mp4]+bestaudio[ext=mp4]" {url}'  # ext=mp4 로 처리
        if video_id == "" or audio_id == "" == 1:
            # text="다운로드를 진행할 수 없습니다\n다운로드용 video_id 와 audio_id를 설정 후\nurl을 다시 붙여넣어 다운로드를 다시 시도하세요\n{url}"
            pk_print("불완전한 다운로드 명령어가 감지되었습니다....", print_color='blue')
            pk_speak_v2(str_working="불완전한 다운로드 명령어가 감지되었습니다", comma_delay=0.98)
            dialog = GuiUtil.CustomQdialog(
                prompt=f"에러코드[E004]\n아래의 비디오 아이디를 저장하고 에러코드를 관리자에게 문의해주세요\nvideo id: {url}",
                btn_list=["확인"],
                input_box_mode=True,
                input_box_text_default=url,
            )
            dialog.exec()
            pk_print(cmd, print_color='blue')
            break

        try:
            lines = cmd_to_os_like_person_as_admin(cmd=cmd)
        except:
            print_magenta("except:2024-04-12 1750")
            print_magenta(rf'''cmd : {cmd}''')

        if not os.path.exists(D_PK_DOWNLOADSING):
            os.makedirs(D_PK_DOWNLOADSING)

        pk_print("다운로드 f 이동 시도 중...", print_color='blue')
        file = ""
        try:
            clip_id = parse_youtube_video_id(url)
            if clip_id is None:
                clip_id = url

            lines = os.listdir()  # todo : wording : lines vs f_list or f_nx_list ?
            for line in lines:
                if is_pattern_in_prompt(str(line), str(clip_id)):
                    file = line

            src = os.path.abspath(file)
            src_renamed = rf"{D_PK_DOWNLOADSING}\{os.path.basename(file)}"

            pk_print(f'src_renamed : {src_renamed}', print_color='blue')
            if src == os.getcwd():  # 여기 또 os.getcwd() 있는 부분 수정하자..
                dialog = GuiUtil.CustomQdialog(
                    prompt=f"에러코드[E001]\n아래의 비디오 아이디를 저장하고 에러코드를 관리자에게 문의해주세요\nvideo id: {url}",
                    btn_list=["확인"],
                    input_box_mode=True,
                    input_box_text_default=url,
                )
                dialog.exec()
                pk_print("cmd", print_color='blue')
                pk_print(cmd, print_color='blue')
                break
            if src != os.getcwd():  # 여기 또 os.getcwd() 있는 부분 수정하자..
                move_pnx(src, src_renamed)

        except:
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        pk_print(rf'다운로드 결과 확인 중...', print_color='blue')
        try:
            src_moved = rf'{D_PK_DOWNLOADSING}\{file}'
            pk_print(rf'''src_moved : {src_moved}''', print_color='blue')

            # 무조건 재생
            text_editor = 'explorer.exe'
            cmd = f'{text_editor} "{src_moved}" '
            cmd_to_os(cmd=cmd)

        except Exception:
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        break
