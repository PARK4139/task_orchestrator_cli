import zipfile
import winreg
# import win32gui
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
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated
from moviepy import VideoFileClip
from Cryptodome.Random import get_random_bytes
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def validate_and_return(value: str):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    func_n = inspect.currentframe().f_code.co_name
    try:
        pk_print(rf'[벨리데이션 테스트 결과] [value={value}] [type(value)={type(value)}] [len(value)={len(value)}]')
    except:
        pass
    if value is None:
        pk_print(rf'[벨리데이션 테스트 결과] [value=None]')
        return 0
    if value == "":
        pk_print(rf'[벨리데이션 테스트 결과] [value=공백]')
        return 0
    # if 전화번호만 같아 보이는지
    # if 특수문자만 같아 보이는지
    return value
