import zlib
import zipfile
import webbrowser
import urllib.parse
import traceback
import tqdm
import toml
import toml
import re

import pythoncom
import pyglet
import os
import numpy as np
import nest_asyncio
import chardet
import calendar
from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.is_os_windows import is_os_windows
from os.path import dirname
from mutagen.mp3 import MP3
from dirsync import sync
from datetime import datetime, time
from dataclasses import dataclass
from colorama import init as pk_colorama_init
from collections import Counter
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_d_working import get_d_working


def ensure_remote_os_as_nopasswd(**config_remote_os):
    try:

        local_ssh_public_key = config_remote_os['local_ssh_public_key']
        local_ssh_private_key = config_remote_os['local_ssh_private_key']
        ip = config_remote_os['ip']
        port = config_remote_os['port']
        user_n = config_remote_os['user_n']
        pw = config_remote_os['pw']
        # public_key = config_remote_os['public_key']

        cmd = f"sudo grep -n '{user_n} ALL=(ALL:ALL) NOPASSWD:ALL' /etc/sudoers"
        std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=cmd, **config_remote_os)
        signiture = f"{user_n} ALL=(ALL:ALL) NOPASSWD:ALL"
        for std_out_str in std_out_list:
            if signiture in std_out_str:
                ensure_printed("THE ENTRY IS ALREADY PRESENT")
                return 1
            else:
                cmd = f"echo '{pw}' | sudo -S bash -c \"echo '{user_n} ALL=(ALL:ALL) NOPASSWD:ALL' >> /etc/sudoers\""
                std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=cmd, **config_remote_os)
                if not len(std_err_list) == 0:
                    for std_err_str in std_err_list:
                        ensure_printed(str_working=rf'{STAMP_REMOTE_ERROR} {std_err_str}', print_color='red')
                if not len(std_out_list) == 0:
                    for std_out_str in std_out_list:
                        ensure_printed(str_working=rf'{STAMP_REMOTE_DEBUG} {std_out_str}')
                cmd = f"sudo visudo -c"
                std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=cmd, **config_remote_os)
                if not len(std_err_list) == 0:
                    for std_err_str in std_err_list:
                        ensure_printed(str_working=rf'{STAMP_REMOTE_ERROR} {std_err_str}', print_color='red')
                if not len(std_out_list) == 0:
                    for std_out_str in std_out_list:
                        ensure_printed(str_working=rf'{STAMP_REMOTE_DEBUG} {std_out_str}')
    except:
        import traceback
        ensure_printed(str_working=rf"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''} ", print_color='red')
