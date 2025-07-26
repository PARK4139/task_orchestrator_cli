
import win32con
import win32com.client
import tomllib
import toml
import string
import sqlite3
import secrets
import pywintypes

import pygetwindow
import psutil
import platform
import pickle
import paramiko
import os.path
import os
import mutagen
import math
import keyboard
import ipdb
import easyocr
import colorama
import colorama
import calendar

from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened

from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.print_red import print_red
from passlib.context import CryptContext
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from enum import Enum
from bs4 import BeautifulSoup
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def get_magnets_set_from_nyaa_si_v1(nyaa_si_supplier, search_keyword, driver):  # v1 : txt 파일에 데이터를 수집하는 방식

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from bs4 import BeautifulSoup
    import math
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    import random

    if driver is None:
        driver = get_driver_selenium(browser_debug_mode=False)

    url = f'https://nyaa.si/user/{nyaa_si_supplier}?f=0&c=0_0&q={get_str_encoded_url(search_keyword)}'
    ensure_printed(f'''url={url}  {'%%%FOO%%%' if LTA else ''}''')

    driver.get(url)
    page_src = driver.page_source
    soup = BeautifulSoup(page_src, "html.parser")

    page_number_last = None
    files_per_page = 75
    total_cnt_of_f_torrent_list = get_total_cnt_of_f_torrent_list(h3_text=soup.find("h3").text.strip())
    if total_cnt_of_f_torrent_list:
        page_number_last = math.ceil(total_cnt_of_f_torrent_list / files_per_page)
        ensure_printed(f'''files_per_page={files_per_page}  {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''displayable_magnets_cnt_per_page={files_per_page}  {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''page_number_last={page_number_last}  {'%%%FOO%%%' if LTA else ''}''')
    else:
        page_number_last = get_page_number_last_of_nyaa_si_page(url=url, driver=driver)

    page_number_str_list = [str(i) for i in get_list_from_int_a_to_int_b(int_a=1, int_b=page_number_last)]
    page_number_start_to_download = int(
        get_value_completed(key_hint='page_number_start_to_download=', values=page_number_str_list))
    page_number_end_to_download = int(
        get_value_completed(key_hint='page_number_end_to_download=', values=page_number_str_list))

    magnets_set = set()
    ensure_printed(f'''page_number_end_to_download={page_number_end_to_download}  {'%%%FOO%%%' if LTA else ''}''',
             print_color="blue")
    for page_number in range(page_number_start_to_download, page_number_end_to_download + 1):
        url_page = f'{url}&p={page_number}'
        url_decoded = get_str_url_decoded(str_working=url_page)
        ensure_printed(str_working=rf'''url_page={url_page:60s}  url_decoded={url_decoded}  {'%%%FOO%%%' if LTA else ''}''')
        driver.get(url_page)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        ensure_slept(milliseconds=random.randint(200, 333))
        page_src = driver.page_source
        soup = BeautifulSoup(page_src, "html.parser")
        # ensure_printed(f'''soup={soup}  {'%%%FOO%%%' if LTA else ''}''')
        magnet_links = {a["href"] for a in soup.find_all("a", href=True) if a["href"].startswith("magnet:")}
        ensure_printed(f'''Found {len(magnet_links)} magnet links on page {page_number}''')
        magnets_set |= magnet_links
    ensure_printed(f'''len(magnets_set)={len(magnets_set)}  {'%%%FOO%%%' if LTA else ''}''')
    return magnets_set
