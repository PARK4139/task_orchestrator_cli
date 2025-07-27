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
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.get_list_calculated import get_list_calculated
from moviepy import VideoFileClip
from Cryptodome.Random import get_random_bytes
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def validate_and_return(value: str):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    func_n = inspect.currentframe().f_code.co_name
    try:
        ensure_printed(rf'[벨리데이션 테스트 결과] [value={value}] [type(value)={type(value)}] [len(value)={len(value)}]')
    except:
        pass
    if value is None:
        ensure_printed(rf'[벨리데이션 테스트 결과] [value=None]')
        return 0
    if value == "":
        ensure_printed(rf'[벨리데이션 테스트 결과] [value=공백]')
        return 0
    # if 전화번호만 같아 보이는지
    # if 특수문자만 같아 보이는지
    return value
