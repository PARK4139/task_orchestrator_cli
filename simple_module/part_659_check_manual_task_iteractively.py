import yt_dlp
# import win32process
import urllib
import undetected_chromedriver as uc
import time
import threading
import tarfile
import sys
import speech_recognition as sr
import shutil
import pythoncom
import pygetwindow
import pandas as pd
import mysql.connector
import math
import ipdb
import clipboard
import calendar
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_100_os import is_os_windows
from os import path
from functools import lru_cache
from dirsync import sync
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_etc import PkFilter, PK_UNDERLINE
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def check_manual_task_iteractively(question, ignore_uppercase_word_list=None):
    try:

        from colorama import init as pk_colorama_init

        import traceback

        import sys

        pk_colorama_init_once()

        if ignore_uppercase_word_list is None:
            ignore_uppercase_word_list = []

        question = question.upper()

        for word in ignore_uppercase_word_list:
            question = question.replace(word.upper(), word)

        # [OPTION]
        # line_feed_cnt = 6
        line_feed_cnt = 3
        line_feed_char = ''
        for _, __ in enumerate(get_list_from_integer_range(1, line_feed_cnt)):
            # print(f'''{__}''')
            print(f'''{line_feed_char}''')

        pk_print(working_str=question, print_color="white")

        while 1:
            answer = input(rf"{pk_get_colorful_working_str_with_stamp_enviromnet(func_n=func_n)} >").strip().lower()
            if answer is not None:
                if answer != '':
                    pk_print(working_str=rf"ANSWER='{answer}'")
                break
            else:
                pk_print(working_str="INVALID INPUT. PLEASE PRESS ENTER TO CONTINUE.")
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        import sys
        traceback.print_exc(file=sys.stdout)
