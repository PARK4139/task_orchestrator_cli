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
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.is_window_title_front import is_window_title_front
import logging

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext
from sources.objects.pk_local_test_activate import LTA

from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from fastapi import HTTPException
from cryptography.hazmat.backends import default_backend
from colorama import init as pk_colorama_init
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.is_f import is_f
from sources.functions.is_os_windows import is_os_windows
from sources.objects.pk_local_test_activate import LTA

from sources.objects.pk_local_test_activate import LTA
import logging


def download_video_mp4(url: str):
    import inspect
    import os
    import traceback

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    while 1:
        if url.strip() == "":
            logging.debug(rf"if url.strip() == "":")
            break

        logging.debug(rf'''url="{url}"  {'%%%FOO%%%' if LTA else ''}''')
        video_id = ''
        cmd = rf'{F_YT_DLP} -F {url}'
        lines = ensure_command_executed(cmd=cmd)

        video_ids_allowed = VIDEO_IDS_ALLOWED
        audio_ids_allowed = AUDIO_IDS_ALLOWED
        audio_id = ""
        for line in lines:
            if 'video only' in line or 'audio only' in line:
                logging.debug(f"line: {line}")
                # video_id 설정
                for id in video_ids_allowed:
                    if id in line:
                        video_id = id
                        if video_id.strip() == "":
                            logging.debug(rf"{PkTexts.VIDEO_ID_NOT_DOWNLOADABLE} {video_id.strip()}")
                            break
                # audio_id 설정
                for id in audio_ids_allowed:
                    if id in line:
                        audio_id = id
                        if audio_id.strip() == "":
                            logging.debug(rf"{PkTexts.AUDIO_ID_NOT_DOWNLOADABLE} {audio_id.strip()}")
                            break
                        break

        cmd = rf'{F_YT_DLP} -f "bestvideo[ext=mp4]+bestaudio[ext=mp4]" {url}'  # ext=mp4 로 처리
        if video_id == "" or audio_id == "" == 1:
            # text="다운로드를 진행할 수 없습니다\n다운로드용 video_id 와 audio_id를 설정 후\nurl을 다시 붙여넣어 다운로드를 다시 시도하세요\n{url}"
            logging.debug(f"{PkTexts.INCOMPLETE_DOWNLOAD_COMMAND}....")
            ensure_spoken_v2(str_working="불완전한 다운로드 명령어가 감지되었습니다", comma_delay=0.98)
            dialog = GuiUtil.CustomQdialog(
                prompt=f"에러코드[E004]\n아래의 비디오 아이디를 저장하고 에러코드를 관리자에게 문의해주세요\nvideo id: {url}",
                btn_list=["확인"],
                input_box_mode=True,
                input_box_text_default=url,
            )
            dialog.exec()
            logging.debug(cmd)
            break

        try:
            lines = ensure_command_executed_like_human_as_admin(cmd=cmd)
        except:
            print_magenta("except:2024-04-12 1750")
            print_magenta(rf'''cmd : {cmd}''')

        if not os.path.exists(D_PK_DOWNLOADSING):
            os.makedirs(D_PK_DOWNLOADSING)

        logging.debug(f"{PkTexts.DOWNLOAD_FILE_MOVE_ATTEMPT}...")
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

            logging.debug(f'src_renamed : {src_renamed}')
            if src == os.getcwd():  # 여기 또 os.getcwd() 있는 부분 수정하자..
                dialog = GuiUtil.CustomQdialog(
                    prompt=f"에러코드[E001]\n아래의 비디오 아이디를 저장하고 에러코드를 관리자에게 문의해주세요\nvideo id: {url}",
                    btn_list=["확인"],
                    input_box_mode=True,
                    input_box_text_default=url,
                )
                dialog.exec()
                logging.debug("cmd")
                logging.debug(cmd)
                break
            if src != os.getcwd():  # 여기 또 os.getcwd() 있는 부분 수정하자..
                ensure_pnx_moved(src, src_renamed)

        except:
            logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
        logging.debug(rf'{PkTexts.DOWNLOAD_RESULT_CHECK}...')
        try:
            src_moved = rf'{D_PK_DOWNLOADSING}\{file}'
            logging.debug(rf'''src_moved : {src_moved}''')

            # 무조건 재생
            text_editor = 'explorer.exe'
            cmd = f'{text_editor} "{src_moved}" '
            ensure_command_executed(cmd=cmd)

        except Exception:
            logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")

        break
