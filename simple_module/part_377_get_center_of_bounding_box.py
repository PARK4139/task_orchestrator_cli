import zlib
import zipfile
import tarfile
import string
import speech_recognition as sr
import requests
import random, math
import random
# import pywin32
import pythoncom
import pygetwindow
import pickle
import paramiko
import os.path
import nest_asyncio
import mysql.connector
import json
import ipdb
import inspect
import easyocr
import cv2
import calendar
from yt_dlp import YoutubeDL
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from gtts import gTTS
from functools import partial
from datetime import timedelta
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from collections import Counter
from base64 import b64decode
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.pk_system_layer_100_Local_test_activate import LTA


def get_center_of_bounding_box(bounding_box):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    """
    바운딩 박스 좌표를 받아서, 그 중심 좌표를 반환하는 함수.

    :param bounding_box: 바운딩 박스 좌표 [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    :return: 중심 좌표 (x, y)
    """
    # 네 점의 x, y 좌표를 각각 합산
    if bounding_box is None:
        return None
    x_coords = [point[0] for point in bounding_box]
    y_coords = [point[1] for point in bounding_box]

    # x, y 평균값을 구하여 중심 좌표 계산
    center_x = sum(x_coords) / 4
    center_y = sum(y_coords) / 4

    return center_x, center_y
