import zipfile
import yt_dlp
# import win32process
import toml
import subprocess, time
import sqlite3
import socket, time
import re
import random
# import pywin32
import pygetwindow
import pyaudio
import numpy as np
import nest_asyncio
import colorama
import clipboard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated

from PIL import Image
from os.path import dirname
from dirsync import sync
from datetime import timedelta
from colorama import init as pk_colorama_init
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.pk_system_layer_etc import PkFilter, PK_UNDERLINE
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def print_event_info_(event, thing_curious):
    import inspect
    """
        jhp_debugger.print_event_info_(event)
        # └>call sample
    """
    func_n = inspect.currentframe().f_code.co_name
    print(str(event))
    # print(event.type())
    # if type(thing_curious)==str:
    #     print('{{mkr}}')
    # if type(thing_curious)==list:
    #     print(thing_curious[str(event.type())])
    # if type(thing_curious) == tuple:
    #     print('{{mkr}}')
