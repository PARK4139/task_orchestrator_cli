import yt_dlp
import time
import shlex
import requests

import pyglet
import pyautogui
import os
import numpy as np
import nest_asyncio
import mutagen
import ipdb
import calendar
import asyncio
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from pytube import Playlist
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.system_object.directories_reuseable import D_PROJECT
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from datetime import datetime
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from bs4 import BeautifulSoup
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def replace_text_B_and_text_C_interchangeably_at_text_A_by_using_(____text_A, ____text_B, ____text_C, _____and):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    foo_foo = "{{kono foo wa sekai de uituna mono ni motomo chikai desu}}"
    text_special = "{{no}}"
    text_B_cnt = ____text_A.count(____text_B)
    foo_list = []
    foo_str = ""
    foo_cmt = 0
    if ____text_C == "":
        ____text_A = ____text_A.replace(____text_B, ____text_C)
    elif text_special in ____text_C:
        ensure_printed(str_working="text_A 에서 " + ____text_B + " 를 총" + str(text_B_cnt) + "개 발견하였습니다")
        foo_list = ____text_A.split(____text_B)
        if ____text_B in ____text_C:
            foo_cmt = 0
            for j in foo_list:
                if j == foo_list[-1]:
                    pass
                else:
                    foo_str = foo_str + j + ____text_C.split(text_special)[0] + str(foo_cmt)
                foo_cmt = foo_cmt + 1
            ____text_A = ""
            ____text_A = foo_str
        else:
            foo_cmt = 0
            for j in foo_list:
                if j == foo_list[-1]:
                    pass
                else:
                    foo_str = foo_str + j + ____text_C.split(text_special)[0] + str(foo_cmt)
                foo_cmt = foo_cmt + 1
            ____text_A = ""
            ____text_A = foo_str
    else:
        ____text_A = ____text_A.replace(____text_C, foo_foo)
        ____text_A = ____text_A.replace(____text_B, ____text_C)
        ____text_A = ____text_A.replace(foo_foo, ____text_B)
