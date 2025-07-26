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

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from PySide6.QtWidgets import QApplication
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.press import press
from pkg_py.functions_split.print_state import print_state

from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_context import SpeedControlContext

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
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.ensure_printed import ensure_printed


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
