

import winreg
import uuid
import time
import sqlite3
import socket
import shlex

import hashlib
from selenium.webdriver.common.keys import Keys
from pynput import mouse
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories  import D_PROJECT
from pkg_py.system_object.state_via_context import SpeedControlContext
from paramiko import SSHClient, AutoAddPolicy
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from pkg_py.functions_split.get_nx import get_nx
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def get_ip_available_list_v2():  # v1 보다 4배 빠름
    from concurrent.futures import ThreadPoolExecutor
    ip_conncetion_test_result = get_ip_conncetion_ping_test_result_list()
    available_ip_list = [result for result in ip_conncetion_test_result if result[2] == 1]
    with ThreadPoolExecutor(max_workers=20) as pool:
        results = list(pool.map(ping, available_ip_list))
    return [ip for ip, ok in zip(available_ip_list, results) if ok]
