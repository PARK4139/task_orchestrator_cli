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
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from PIL import Image
from functools import partial
from dirsync import sync
from collections import Counter
from bs4 import BeautifulSoup

from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_list_calculated import get_list_calculated

from sources.objects.pk_local_test_activate import LTA
import logging


def print_template_for_notion_issue_reporting(line_order, issues_list_csv):
    logging.debug(rf'''노션 이슈발생 템플릿  {'%%%FOO%%%' if LTA else ''}''')
    collect_row_data = collect_row_data_from_csv(line_order=line_order, issues_list_csv=issues_list_csv)
    logging.debug(string=f'''차량 : {collect_row_data["차량"]}''')
    logging.debug(string=f'''지역 : {collect_row_data["지역"]}''')
    logging.debug(string=f'''코스 : {collect_row_data["코스"]}''')
    logging.debug(string=f'''운전자 : {collect_row_data['Crew']}''')
    # logging.debug(string=f'''문제점 상세 : \n{collect_row_data["문제점 상세"].replace("\n\n","\n")}''')
    logging.debug(string=f'''문제점 상세 : \n{collect_row_data["문제점 상세"].replace("\n", "")}''')
    logging.debug(string=f'''''')
    logging.debug(string=f'''SW 버전 : {collect_row_data["SW 버전"]}''')
    f위치 = collect_row_data["_f_ 위치"]
    if isinstance(f위치, float):
        f위치 = ""
    logging.debug(string=f'''_f_명 : {f위치}''')
