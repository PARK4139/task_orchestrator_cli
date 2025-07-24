import pyglet
import pandas as pd
import mutagen
import ipdb
import functools
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.pk_print_once import pk_print_once

from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.map_massages import PkMessages2025
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.pk_print import pk_print


def get_yymmdd():
    import datetime
    today = datetime.datetime.now()
    yymmdd = today.strftime("%y%m%d")
    return yymmdd
