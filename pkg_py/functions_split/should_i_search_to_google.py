import zipfile
import yt_dlp

import win32con
import win32com.client
import webbrowser
import urllib.parse
import undetected_chromedriver as uc
import traceback
import tqdm
import tomllib
import tomllib
import timeit
import time
import tarfile
import sys
import subprocess
import socket
import secrets
import requests
import re
import random
import pywintypes
import pythoncom
import pyglet
import pygetwindow
import platform
import pickle
import paramiko
import os, inspect
import mutagen
import inspect
import hashlib
import functools
import easyocr
import datetime
import colorama
import colorama
import clipboard
import chardet
import calendar
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from tkinter import UNDERLINE
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.get_list_calculated import get_list_calculated

from PIL import Image, ImageFont, ImageDraw
from PIL import Image, ImageFilter
from passlib.context import CryptContext
from os.path import dirname
from os import path
from mysql.connector import connect, Error
from functools import partial as functools_partial
from functools import partial
from dirsync import sync
from datetime import datetime, timedelta
from datetime import datetime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def should_i_search_to_google():
    # todo : ref : as gui : demerit : slow
    # import system_object.static_logic
    # txt_clicked, function, txt_written = should_i_do(
    #     string=rf"can i search contents dragged to google?",
    #     btns=[system_object.static_logic.POSITIVE, system_object.static_logic.NEGATIVE],
    #     function=partial(ask_to_google, question=question),
    #     auto_click_negative_btn_after_seconds=30,
    #     title=f" {'%%%FOO%%%' if LTA else ''}",
    #     input_box_mode=True,
    #     input_box_text_default=question,
    # )
    # if txt_clicked == system_object.static_logic.NEGATIVE:
    #     ensure_printed(f'''{system_object.static_logic.NEGATIVE} pressed  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    #     return
    # if txt_clicked == system_object.static_logic.POSITIVE:
    #     ensure_printed(f'''txt_clicked={txt_clicked}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    #     ensure_printed(f'''txt_written={txt_written}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    #     function()

    # todo : ref : as cli
    txt_written = should_i_do_cli(
        title=rf"can i search contents dragged to google?",
        search_keyword_default="",
    )
    txt_written = txt_written.strip()
    if txt_written != "":
        ask_to_google(txt_written)
