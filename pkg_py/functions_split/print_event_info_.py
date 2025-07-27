import zipfile
import yt_dlp

import toml
import subprocess, time
import sqlite3
import socket, time
import re
import random

import pygetwindow
import pyaudio
import numpy as np
import nest_asyncio
import colorama
import clipboard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.get_list_calculated import get_list_calculated

from PIL import Image
from os.path import dirname
from dirsync import sync
from datetime import timedelta
from colorama import init as pk_colorama_init
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.functions_split.is_f import is_f
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.functions_split.get_pnxs import get_pnxs


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
