



import webbrowser
import urllib.parse
import undetected_chromedriver as uc
import timeit
import threading
import string
import socket
import shlex
import secrets

import pyaudio
import os
import mysql.connector
import json
import clipboard
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image, ImageFilter
from PIL import Image
from pathlib import Path
from paramiko import SSHClient, AutoAddPolicy
from os.path import dirname
from functools import lru_cache
from dirsync import sync
from datetime import datetime, time
from datetime import datetime
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def gather_pnxs_useless_at_tree(src, mode):
    pk_print(str_working=rf'''src="{src}"  {'%%%FOO%%%' if LTA else ''}''')
    pk_print(str_working=rf'''mode="{mode}"  {'%%%FOO%%%' if LTA else ''}''')

    if mode == 'd':
        # gather_pnxs_useless(src=src, debug_mode=True) #쓸라면 테스트 필요
        pass

    if mode == 'f':
        gather_f_useless_at_tree(d_working=src)
