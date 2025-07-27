

import tqdm
import toml
import toml
import speech_recognition as sr
import random

import pythoncom
import pyaudio
import platform
import pickle
import numpy as np
import mysql.connector
import mutagen
import math
import functools
import easyocr
import datetime
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import UNDERLINE
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.local_test_activate import LTA
from PIL import Image
from functools import partial as functools_partial
from functools import partial
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from bs4 import BeautifulSoup
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_pnxs import get_pnxs


def get_coordinates_bounding_box(image, str_working):
    import inspect
    import easyocr
    func_n = inspect.currentframe().f_code.co_name
    # EasyOCR로 텍스트 및 위치 추출
    reader = easyocr.Reader(['en', 'ko'])  # 영어와 한글을 동시에 처리하려면 'en', 'ko' 지정
    results = reader.readtext(image)

    # 추출된 텍스트와 위치 반환
    for result in results:
        text = result[1]  # result[1]은 텍스트
        if str_working.lower() in text.lower():
            coord_bounding_box = result[0]  # result[0]은 바운딩 박스 좌표
            return coord_bounding_box
    print(f"{str_working}에 대한 바운딩 박스가 화면에 없습니다. ")
