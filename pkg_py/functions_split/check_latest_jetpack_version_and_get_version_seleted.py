import toml
import sqlite3
import shutil
import requests
import re
import psutil
import os.path
import json
import ipdb
import importlib
import chardet
from zipfile import BadZipFile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from PySide6.QtWidgets import QApplication
from pynput import mouse
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated
from passlib.context import CryptContext
from fastapi import HTTPException
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from collections import Counter
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def check_latest_jetpack_version_and_get_version_seleted(vpc_identifier, jetpack_version):
    return jetpack_version  # code for temp

    vpc_identifier = vpc_identifier.strip()
    vpc_identifier = vpc_identifier.lower()
    if 'no' in vpc_identifier:
        # todo gitlab 에서 latest 파싱하도록 후 vpc_aifw_version 와 비교, 같으면 진행, 다르면 질의(latest 는 몇입니다. 업데이트 할까요?)
        jetpack_version = "5.1.2"
    elif 'nx' in vpc_identifier:
        jetpack_version = "5.0.2"
    elif 'xc' in vpc_identifier:
        jetpack_version = "4.6.5"
    elif 'evm' in vpc_identifier:
        jetpack_version = "4.6.6"
    else:
        pk_print(f'''unknown vpc_identifier ({vpc_identifier}) {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        raise
    if LTA:
        pk_print(f'''jetpack_version={jetpack_version} {'%%%FOO%%%' if LTA else ''}''')
    return jetpack_version
