import zlib
import win32com.client
import webbrowser
import undetected_chromedriver as uc
import traceback
import toml
import pyautogui
import numpy as np
from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from prompt_toolkit.styles import Style
from sources.functions.is_window_opened import is_window_opened
from sources.functions.get_list_sorted import get_list_sorted

from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.performance_logic import ensure_seconds_measured, pk_measure_memory


from pathlib import Path
from os.path import dirname
from mutagen.mp3 import MP3
from gtts import gTTS
from enum import Enum

from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

import logging


def here(item_str=None):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if item_str is None:
        item_str = ''
    logging.debug(rf"{str(str(item_str) + ' ') * 242:.100} here!")
