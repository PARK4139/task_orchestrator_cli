import zipfile
import yt_dlp
import win32con
import win32con
import win32com.client
import webbrowser
import tqdm
import threading
import subprocess
import string
import sqlite3
import speech_recognition as sr
import random
import pygetwindow
import mutagen
import importlib
import easyocr
import colorama
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once


from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.get_list_calculated import get_list_calculated
from os.path import dirname
from os import path
from datetime import timedelta
from datetime import datetime
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.functions_split.is_d import is_d
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def assist_to_run_project_cmake():
    import os

    wsl_distro_n = 'Ubuntu-24.04'
    ensure_wsl_distro_session(wsl_distro_n=wsl_distro_n)
    config_remote_os = {
        'port': ensure_and_get_wsl_port(wsl_distro_n),
        'ip': get_wsl_ip(wsl_distro_n),
        'user_n': get_wsl_user_n(wsl_distro_n),
        'pw': get_wsl_pw(wsl_distro_n),
        'local_ssh_public_key': os.path.join(D_HOME, ".ssh", "id_ed25519.pub"),
        'local_ssh_private_key': os.path.expanduser("~/.ssh/id_ed25519"),
    }
    ip = config_remote_os['ip']
    pw = config_remote_os['pw']
    port = config_remote_os['port']
    user_n = config_remote_os['user_n']
    local_ssh_public_key = config_remote_os['local_ssh_public_key']
    local_ssh_private_key = config_remote_os['local_ssh_private_key']

    ensure_ssh_public_key_to_remote_os(**config_remote_os)
    ensure_remote_os_as_nopasswd(**config_remote_os)

    project_pnx = D_PROJECT_CMAKE

    ensure_printed(f'''{STAMP_TRY_GUIDE} ssh -p {port} {user_n}@{ip} {'%%%FOO%%%' if LTA else ''}''')

    std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=rf"sudo apt update", **config_remote_os)
    std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=rf"echo y | sudo apt install build-essential",
                                                              **config_remote_os)
    std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=rf"echo y | sudo apt install libyaml-cpp-dev",
                                                              **config_remote_os)

    build_project_cmake(project_pnx=project_pnx, **config_remote_os)
    exec_project_cmake(project_pnx=project_pnx, **config_remote_os)
