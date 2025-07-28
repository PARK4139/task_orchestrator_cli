import winreg
import win32com.client
import tomllib
import toml
import timeit
import threading
import subprocess
import pickle
import colorama
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.common.action_chains import ActionChains
from prompt_toolkit import PromptSession
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.directories import D_PK_WORKING
# from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_context import SpeedControlContext
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial as functools_partial
from dirsync import sync
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_list_calculated import get_list_calculated
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.ensure_printed import ensure_printed


def set_wired_connection(vpc_wired_connection, **config_remote_os):
    cmd_list = []
    if vpc_wired_connection["address"] == "":
        cmd_list.append(
            f'sudo nmcli connection modify "Wired connection {vpc_wired_connection['wired_connection_no']}" ipv4.method "{vpc_wired_connection["method"]}"')
        cmd_list.append(
            f'sudo nmcli connection modify "Wired connection {vpc_wired_connection['wired_connection_no']}" ipv4.address "{vpc_wired_connection["address"]}"')
    else:
        cmd_list.append(
            f'sudo nmcli connection modify "Wired connection {vpc_wired_connection["wired_connection_no"]}" ipv4.address "{vpc_wired_connection["address"]}"')
        cmd_list.append(
            f'sudo nmcli connection modify "Wired connection {vpc_wired_connection["wired_connection_no"]}" ipv4.method "{vpc_wired_connection["method"]}"')
    cmd_list.append(
        f'sudo nmcli connection modify "Wired connection {vpc_wired_connection['wired_connection_no']}" ipv4.gateway "{vpc_wired_connection["gateway"]}"')
    cmd_list.append(
        f'sudo nmcli connection modify "Wired connection {vpc_wired_connection['wired_connection_no']}" ipv4.dns "{vpc_wired_connection["dns"]}"')
    for cmd in cmd_list:
        std_out_list, std_err_list = cmd_to_remote_os(cmd=cmd, **config_remote_os)
        std_err = get_str_from_list(working_list=std_err_list)
        if std_err:
            if "\n" in std_err:
                error_list = std_err.split("\n")
                for error_str in error_list:
                    ensure_printed(f"{STAMP_ERROR}{error_str}", print_color='red')
            else:
                ensure_printed(f"{STAMP_ERROR}{std_err}", print_color='red')
    cmd_to_remote_os(cmd="sudo systemctl restart NetworkManager", **config_remote_os)
