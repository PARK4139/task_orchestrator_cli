import zlib

import toml
import string
import shutil
import pyaudio
import platform
import mysql.connector
import inspect
import cv2
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.files import F_HISTORICAL_PNX
from PIL import Image
from functools import partial
from dirsync import sync
from collections import Counter
from bs4 import BeautifulSoup
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_list_calculated import get_list_calculated

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def print_template_for_notion_issue_reporting(line_order, issues_list_csv):
    ensure_printed(str_working=rf'''노션 이슈발생 템플릿  {'%%%FOO%%%' if LTA else ''}''', print_color='white')
    collect_row_data = collect_row_data_from_csv(line_order=line_order, issues_list_csv=issues_list_csv)
    ensure_printed(string=f'''차량 : {collect_row_data["차량"]}''', print_color='white')
    ensure_printed(string=f'''지역 : {collect_row_data["지역"]}''', print_color='white')
    ensure_printed(string=f'''코스 : {collect_row_data["코스"]}''', print_color='white')
    ensure_printed(string=f'''운전자 : {collect_row_data['Crew']}''', print_color='white')
    # ensure_printed(string=f'''문제점 상세 : \n{collect_row_data["문제점 상세"].replace("\n\n","\n")}''', print_color='white')
    ensure_printed(string=f'''문제점 상세 : \n{collect_row_data["문제점 상세"].replace("\n", "")}''', print_color='white')
    ensure_printed(string=f'''''', print_color='white')
    ensure_printed(string=f'''SW 버전 : {collect_row_data["SW 버전"]}''', print_color='white')
    f위치 = collect_row_data["_f_ 위치"]
    if isinstance(f위치, float):
        f위치 = ""
    ensure_printed(string=f'''_f_명 : {f위치}''', print_color='white')
