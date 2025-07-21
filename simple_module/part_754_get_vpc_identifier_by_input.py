import zipfile
# import win32gui
import tqdm
import requests
# import pywin32
import pygetwindow
import pickle
import paramiko
import os.path
import math
import ipdb
import importlib
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from telegram import Bot
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_encodings import Encoding
from os import path
from gtts import gTTS
from fastapi import HTTPException
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def get_vpc_identifier_by_input(input_ment, vpc_type):
    # todo 숫자 아니면 continue
    state_nick_name_passed = 0
    while 1:
        vpc_identifier_number = input(input_ment)
        vpc_identifier = f'{vpc_type}_#{vpc_identifier_number}'.lower()
        if 'no_#' or 'nx_#' or 'xc_#' or 'evm_#' in vpc_identifier:
            state_nick_name_passed = 1
        if state_nick_name_passed == 1:
            if LTA:
                pk_print(f'''vpc_identifier={vpc_identifier} {'%%%FOO%%%' if LTA else ''}''')
            return vpc_identifier
