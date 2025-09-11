import zlib
import urllib.parse
import undetected_chromedriver as uc
import toml
import toml
import socket
import shutil
import random
import psutil
import nest_asyncio
import ipdb
import colorama

from yt_dlp import YoutubeDL
from telegram import Bot
from prompt_toolkit import PromptSession
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.pk_local_test_activate import LTA

from passlib.context import CryptContext
from functools import partial as functools_partial
from dirsync import sync
from cryptography.hazmat.primitives import padding
from Cryptodome.Cipher import AES
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.does_pnx_exist import is_pnx_existing


def search_f_list_contains_search_key(target, search_key):
    import os
    # todo : chore : not working for encoding problem
    """
    특정 경로를 순회하며 f 내용을 검색하여 문자열이 포함된 f명을 출력합니다.  

    :param target_path: 검색할 d
    :param search_string: 찾고자 하는 문자열
    """
    for root, dirs, f_nx_list in os.walk(target):
        for f_nx in f_nx_list:
            f = os.path.join(root, f_nx)
            try:
                # f 바이너리 모드로 열기
                with open(file=f, mode='rb') as f_tmp:
                    raw_data = f_tmp.read()

                import chardet
                detected_encoding = chardet.detect(raw_data)['encoding']

                # 인코딩이 감지되지 않으면 utf-8로 시도
                if detected_encoding is None:
                    # detected_encoding=Encoding.UTF8
                    detected_encoding = 'cp949'

                # 감지된 인코딩으로 텍스트 읽기
                text_content = raw_data.decode(detected_encoding)

                # 특정 문자열 검색
                if search_key in text_content:
                    print(f"문자열 '{search_key}'이 포함된 f: {f}")

            except UnicodeDecodeError as e:
                print(f"f을 디코딩할 수 없습니다: {f}, 이유: {e}")
            except Exception as e:
                print(f"f을 읽을 수 없습니다: {f}, 이유: {e}")
