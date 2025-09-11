import zipfile
import urllib
import tqdm
import tomllib
import time
import pygetwindow
import pickle
import pandas as pd
import nest_asyncio
import cv2
from urllib.parse import unquote, urlparse, parse_qs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_d_working import get_d_working
from sources.functions.ensure_command_executed import ensure_command_executed

from sources.objects.performance_logic import ensure_seconds_measured, pk_measure_memory

from PIL import Image
from moviepy import VideoFileClip
from Cryptodome.Cipher import AES

from pathlib import Path
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.objects.pk_local_test_activate import LTA

from sources.objects.pk_local_test_activate import LTA
import logging


def print_and_get_text_converted(text: str, convert_mode=0):
    import inspect

    """
    # str to str

    param str
    return str
    """
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    def convert_mode_1(text):
        text_converted = text
        while (True):
            if "  " in text:
                text_converted = text.replace("  ", " ")
            else:
                break
        text_converted = text_converted.replace(" ", "\",\"")
        text_converted = f"\"{text_converted}\""
        text_converted = f"[{text_converted}]"
        print_magenta(f'''{inspect.currentframe().f_code.co_name}={text_converted}''')
        return text_converted

    def convert_mode_2(text):
        text_converted = text
        while (True):
            if "  " in text:
                text_converted = text.replace("  ", " ")
            else:
                break
        text_converted = text_converted.replace(" ", "\",\"")
        text_converted = text_converted.replace("\"\"", "\"")
        text_converted = f"\"{text_converted}\""
        text_converted = f"[{text_converted}]"
        print_magenta(f'''{inspect.currentframe().f_code.co_name}={text_converted}''')
        return text_converted

    def convert_mode_3(text):
        text = text.replace("  ", " ")
        text_converted = text.replace(" ", ",")
        print_magenta(f'''{inspect.currentframe().f_code.co_name}={text_converted}''')
        return text_converted

    def convert_mode_4(text):
        texts = text.split(" ")
        texts = get_list_striped_element(working_list=texts)
        text_converted = text
        print_magenta(f'''{inspect.currentframe().f_code.co_name}={text_converted}''')
        return text_converted

    def convert_mode_x(text):
        text_converted = text
        if "  " in text:
            text_converted = text.replace("  ", " ")
        text_converted = text.replace(" ", "\",\"")
        text_converted = f"\"{text_converted}\""
        text_converted = f"[{text_converted}]"
        print_magenta(f'''{inspect.currentframe().f_code.co_name}={text_converted}''')
        return text_converted

    def convert_mode_0(text):
        convert_mode_1(text)
        convert_mode_2(text)
        convert_mode_3(text)
        convert_mode_4(text)
        convert_mode_x(text)

    if convert_mode == 0:
        convert_mode_0(text)
        return None

    elif convert_mode == 1:
        return convert_mode_1(text)
    elif convert_mode == 2:
        return convert_mode_2(text)
    else:
        return None
