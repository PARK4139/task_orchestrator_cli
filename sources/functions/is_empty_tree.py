

import tomllib
import threading
import secrets
import pywintypes
import pyglet
import os
import hashlib
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from selenium.webdriver.common.keys import Keys
from prompt_toolkit.styles import Style
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
import logging

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from passlib.context import CryptContext
from os import path
from functools import partial as functools_partial
from dirsync import sync
from datetime import datetime
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup

from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES

from sources.objects.pk_local_test_activate import LTA
import logging


def is_empty_tree(d):
    import os

    logging.debug(f"d={d}  {'%%%FOO%%%' if LTA else ''}")

    try:
        with os.scandir(d) as entries:
            for entry in entries:
                if entry.is_file():
                    logging.debug(rf"is not empty d {d}")
                    return 0
        logging.debug(rf"is not empty d 있습니다.{d}")
        return 1
    except:
        # logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
        return 0
