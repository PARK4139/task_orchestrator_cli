

import tomllib
import shlex
import pygetwindow
import psutil
import pandas as pd
import nest_asyncio
import easyocr
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.system_object.files import F_FFMPEG_EXE

from os import path
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def download_issue_log_f(issue_log_index_data, original_log=False):
    import re

    # 전처리
    if isinstance(issue_log_index_data["_f_ 위치"], float):
        issue_log_index_data["_f_ 위치"] = ""

    issue_file_name = issue_log_index_data["_f_ 위치"].split('/')[-1]

    def get_origin_log_file_name(issue_file_name):
        # 정규식 패턴 정의: "_숫자(최대 2자리)_VIDEO"
        pattern = r"_\d{1,2}_VIDEO"
        original_filename = re.sub(pattern, "", issue_file_name)
        return original_filename

    origin_log_file_name = get_origin_log_file_name(issue_file_name)
    issue_log_index_data["주행일자"] = issue_log_index_data["_f_ 위치"].split('/')[0]
    issue_log_index_data["_f_ 위치"] = issue_log_index_data["_f_ 위치"].replace("/", f"\\")

    src = rf"\\192.168.1.33\01_Issue\{issue_log_index_data["_f_ 위치"]}"
    pk_print(str_working=rf'''src="{src}"  {'%%%FOO%%%' if LTA else ''}''')
    if original_log == True:
        src = rf"\\192.168.1.33\02_Orignal\{issue_log_index_data["차량"]}\{issue_log_index_data["지역"]}\{issue_log_index_data["주행일자"]}\{issue_log_index_data["코스"]}\{origin_log_file_name}"
        pk_print(str_working=rf'''src="{src}"  {'%%%FOO%%%' if LTA else ''}''')
        return

    # pause()
    dst = rf"C:\log"
    cmd = rf"copy {src} {dst}"
    src_nx = get_nx(pnx=src)
    src_new = rf"{dst}\{src_nx}"

    while 1:
        if does_pnx_exist(pnx=src_new):
            pk_print(str_working=rf'''{src_new} 가 이미 있습니다."  {'%%%FOO%%%' if LTA else ''}''')
            break
        else:
            if not does_pnx_exist(pnx=src_new):
                cmd_to_os(cmd=cmd, mode="a")
                pk_print(str_working=rf'''이슈데이터 다운로드 완료 "{src_new}"  {'%%%FOO%%%' if LTA else ''}''',
                         print_color='blue')
                return
