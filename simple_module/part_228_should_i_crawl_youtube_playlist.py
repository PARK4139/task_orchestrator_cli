import zlib
import winreg
import win32con
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tqdm
import toml
import time
import tarfile
import sys
import shutil
import secrets
import requests
import random
import pywintypes
import pyglet
import pygetwindow
import psutil
import pickle
import pandas as pd
import numpy as np
import math
import ipdb
import inspect
import hashlib
import easyocr
import datetime
import colorama
import colorama
import calendar
import browser_cookie3
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from PySide6.QtWidgets import QApplication
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_directories import D_PKG_TXT, D_WORKING
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext

from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from datetime import timedelta
from datetime import datetime
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from collections import defaultdict, Counter
from collections import Counter
from base64 import b64decode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style

from pkg_py.simple_module.part_014_pk_print import pk_print


def should_i_crawl_youtube_playlist():
    while 1:
        # 테스트용
        keyword = 'blahblah'
        url = f'https://www.youtube.com/@{keyword}/playlists'

        dialog = GuiUtil.CustomQdialog(prompt="해당 페이지의 video title, video url을 크롤링할까요?", btn_list=[YES, NO],
                                       input_box_mode=True, input_box_text_default=url)
        dialog.exec()
        btn_txt_clicked = dialog.btn_txt_clicked

        if btn_txt_clicked == PkMessages2025.YES:
            crawl_youtube_playlist(url=dialog.input_box.text())
            break
        else:
            break
