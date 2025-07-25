

import zlib

import win32com.client
import string
import requests

import pyglet
import pyautogui
import platform
import pickle
import os.path
import json
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.directories import D_PK_WORKING

from functools import partial
from enum import Enum
from datetime import timedelta
from datetime import datetime
from bs4 import BeautifulSoup
from base64 import b64encode
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.pk_print import pk_print


def get_text_coordinates_via_easy_ocr(string):  # 한글인식 잘 안되는 듯하다
    import string

    # 화면 캡처
    screenshot = get_screenshot()

    # EsayOCR을 통해 모든텍스트 바운딩박스좌표 추출
    # coordinates_bounding_box = get_all_text_with_coordinates_via_easy_ocr(screenshot)
    # print_list_as_vertical(working_list=coordinates_bounding_box, items_name="coordinates_bounding_box")

    # EsayOCR을 통해 특정텍스트 바운딩박스좌표 추출
    coordinates_bounding_box = get_coordinates_bounding_box(image=screenshot, str_working=string)
    # print_list_as_vertical(working_list=coordinates_bounding_box, items_name="coordinates_bounding_box")

    # 중심 좌표 구하기
    if get_center_of_bounding_box(coordinates_bounding_box) is not None:
        center_x, center_y = get_center_of_bounding_box(coordinates_bounding_box)
        # pk_print(string = rf'''center_x="{center_x}"  {'%%%FOO%%%' if LTA else ''}''')
        # pk_print(string = rf'''center_y="{center_y}"  {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''"text_coordinates = ({center_x}, {center_y})"''')
        return center_x, center_y
    return None
