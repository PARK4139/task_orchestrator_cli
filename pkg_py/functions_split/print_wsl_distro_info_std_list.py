import win32con
import win32com.client
import traceback
import tomllib
import tomllib
import tarfile
import subprocess
import socket


import platform
import paramiko
import pandas as pd
import mutagen
import math
import functools
import colorama
import chardet
import asyncio
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.is_os_windows import is_os_windows

from functools import partial
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def print_wsl_distro_info_std_list() -> list[str]:
    try:
        ensure_printed("======== wsl -l -v ========")
        std_list = get_wsl_distro_info_std_list()
        highlight_config_dict = {
            "green": [
                'Running'
            ],
            'red': [
                'Stopped'
            ],
        }
        pk_debug_state_for_py_data_type(pk_stamp='%%%FOO%%%-1', data_working=std_list,
                                        highlight_config_dict=highlight_config_dict, with_LTA=0)
        return std_list
    except Exception as e:
        ensure_printed(f"Failed to get WSL details: {e}", print_color='red')
        return []
