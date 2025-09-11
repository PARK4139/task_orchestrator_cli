import pyglet
import pandas as pd
import mutagen
import ipdb
import functools
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.common.action_chains import ActionChains
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_printed_once import ensure_printed_once

from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.encodings import Encoding
from sources.objects.pk_map_texts import PkTexts
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.objects.pk_local_test_activate import LTA

import logging


def get_yymmdd():
    import datetime
    today = datetime.datetime.now()
    yymmdd = today.strftime("%y%m%d")
    return yymmdd
