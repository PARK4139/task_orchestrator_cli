import zipfile
import winreg

import webbrowser
import urllib
import undetected_chromedriver as uc
import tomllib
import toml
import string
import shutil
import pythoncom
import platform
import paramiko
import mysql.connector
import mutagen
import functools
import colorama
import chardet
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from urllib.parse import quote
from selenium.webdriver.chrome.options import Options
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical


from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title

from sources.objects.encodings import Encoding
from sources.objects.pk_state_via_database import PkSqlite3DB

from moviepy import VideoFileClip
from Cryptodome.Random import get_random_bytes
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.objects.pk_local_test_activate import LTA

import logging
from sources.functions.get_d_working import get_d_working


def validate_and_return(value: str):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    try:
        logging.debug(rf'[벨리데이션 테스트 결과] [value={value}] [type(value)={type(value)}] [len(value)={len(value)}]')
    except:
        pass
    if value is None:
        logging.debug(rf'[벨리데이션 테스트 결과] [value=None]')
        return 0
    if value == "":
        logging.debug(rf'[벨리데이션 테스트 결과] [value=공백]')
        return 0
    # if 전화번호만 같아 보이는지
    # if 특수문자만 같아 보이는지
    return value
