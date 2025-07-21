import pyglet
import pandas as pd
import mutagen
import ipdb
import functools
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

from pkg_py.simple_module.part_014_pk_print import pk_print


def get_yymmdd():
    import datetime
    today = datetime.datetime.now()
    yymmdd = today.strftime("%y%m%d")
    return yymmdd
