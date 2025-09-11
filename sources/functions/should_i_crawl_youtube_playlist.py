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

from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_state_printed import ensure_state_printed

from sources.objects.pk_etc import PkFilter

from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_state_via_context import SpeedControlContext

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
from sources.functions.get_nx import get_nx

from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

import logging


def should_i_crawl_youtube_playlist():
    while 1:
        # 테스트용
        keyword = 'blahblah'
        url = f'https://www.youtube.com/@{keyword}/playlists'

        dialog = GuiUtil.CustomQdialog(prompt="해당 페이지의 video title, video url을 크롤링할까요?", btn_list=[YES, NO],
                                       input_box_mode=True, input_box_text_default=url)
        dialog.exec()
        btn_txt_clicked = dialog.btn_txt_clicked

        if btn_txt_clicked == PkTexts.YES:
            crawl_youtube_playlist(url=dialog.input_box.text())
            break
        else:
            break
