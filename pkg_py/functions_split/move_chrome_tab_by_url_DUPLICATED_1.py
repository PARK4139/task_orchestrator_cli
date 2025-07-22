import win32con
import win32com.client
import urllib
import speech_recognition as sr
import shlex
import secrets
import platform
import pickle
import os, inspect
import os
import ipdb
import hashlib
import easyocr
from yt_dlp import YoutubeDL
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_state import pk_print_state


from pkg_py.functions_split.set_pk_context_state import set_pk_context_state

from passlib.context import CryptContext
from functools import partial
from enum import Enum
from dirsync import sync
from datetime import datetime
from datetime import date
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.pk_print import pk_print


def move_chrome_tab_by_url(url):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    minimize_all_windows()
    window_title_seg = get_window_title(window_title_seg="Chrome")
    window_titles = get_window_title_list()
    for window_title in window_titles:
        if "Chrome".lower() in window_title.lower():
            ensure_window_to_front(window_title_seg=window_title)
            loop_limit = 30
            loop_cnt = 0
            while 1:
                if loop_cnt == loop_limit:
                    return
                loop_cnt = loop_cnt + 1
                pk_sleep(milliseconds=15)
                pk_press("ctrl", "l")
                pk_sleep(milliseconds=15)
                url_dragged = get_txt_dragged()
                if url_dragged == url:
                    pk_print(f'''url_to_move="{url}"''')
                    pk_print(f'''url_dragged="{url_dragged}"''')
                    break
                pass
