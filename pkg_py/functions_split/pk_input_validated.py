

import speech_recognition as sr
import socket
import shutil
import secrets
import pythoncom
import os.path
import numpy as np
import inspect
import asyncio
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.pk_press import pk_press

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.system_object.directories import D_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from PIL import Image
from functools import partial as functools_partial
from datetime import datetime
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from collections import Counter
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.functions_split.pk_print import pk_print


def pk_input_validated(str_working, mode_verbose=1, mode_blank_validation=1, mode_nx_validation=1, mode_upper=1,
                       input_str=":"):
    # todo : pk_input_validated 를 pk_input 에 통합
    '''
    all mode default value is True
    '''

    while 1:
        if mode_upper:
            str_working = str_working.upper()
        pk_print(str_working, print_color='white', mode_verbose=mode_verbose)
        user_input = input(input_str).strip()
        if mode_blank_validation:
            if not user_input:
                pk_print("blank, name not allowed. Please try again.", print_color='red', mode_verbose=mode_verbose)
                continue
        if mode_nx_validation:
            if any(char in user_input for char in r'\/:*?"<>|'):
                pk_print("Char not allowed in f_n/d_n. Retry.", print_color='red')
                continue
        # todo : p일 조건 을
        # if p_validation_mode == True:
        #     if any(char not in user_input for char in r'\/:*?"<>|'):
        #         pk_print("Char not allowed in f_n/d_n. Retry.", print_color='red')
        #         continue
        return user_input
