import zlib
# import win32process
import toml
import toml
import time
import secrets
import requests
import random
import pywintypes
import psutil
import mysql.connector
import hashlib
import easyocr
import cv2
from seleniumbase import Driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from passlib.context import CryptContext
from os.path import dirname
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style

from pkg_py.pk_system_layer_100_Local_test_activate import LTA


def convert_img_to_img_flipped_horizontally(img_pnx):
    # todo : fix
    # import os

    # from PIL import Image
    # img_converted = Image.open(img_pnx).transpose(Image.FLIP_LEFT_RIGHT)
    # img_converted.show()
    # img_converted.save(f"{os.path.dirname(img_pnx)}   {os.path.splitext(img_pnx)[0]}_$flipped_h{os.path.splitext(img_pnx)[1]}")
    pass
