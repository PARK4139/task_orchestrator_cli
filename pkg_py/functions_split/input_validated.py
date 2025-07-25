
#         continue
#         pk_print("Char not allowed in f_n/d_n. Retry.", print_color='red')
#     if any(char not in user_input for char in r'\/:*?"<>|'):
# if p_validation_mode == True:
# todo : pk_input_validated 를 pk_input 에 통합
# todo : p일 조건 을
'''
all mode default value is True
continue
def pk_input_validated(str_working, mode_verbose=1, mode_blank_validation=1, mode_nx_validation=1, mode_upper=1,
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from PIL import Image
from collections import Counter
from cryptography.hazmat.primitives import padding
from datetime import datetime
from functools import partial as functools_partial
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.press import pk_press
from pkg_py.functions_split.print import pk_print
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from telegram import Bot
from tkinter import UNDERLINE
from urllib.parse import quote
if any(char in user_input for char in r'\/:*?"<>|'):
if mode_blank_validation:
if mode_nx_validation:
if mode_upper:
if not user_input:
import asyncio
import inspect
import numpy as np
import os.path
import pythoncom
import secrets
import shutil
import socket
import speech_recognition as sr
input_str=":"):
pk_print("Char not allowed in f_n/d_n. Retry.", print_color='red')
pk_print("blank, name not allowed. Please try again.", print_color='red', mode_verbose=mode_verbose)
pk_print(str_working, print_color='white', mode_verbose=mode_verbose)
return user_input
str_working = str_working.upper()
user_input = input(input_str).strip()
while 1:
