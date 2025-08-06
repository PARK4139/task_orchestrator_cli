import yt_dlp
import urllib.parse
import tomllib
import requests
import paramiko
import importlib
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pynput import mouse
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PKG_CACHE_PRIVATE
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from datetime import datetime
from datetime import date
from collections import Counter
from bs4 import BeautifulSoup
from pkg_py.functions_split.get_list_calculated import get_list_calculated
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def find_pnx_interested_list_from_txt_f_x(including_texts=[], exclude_texts=[], except_extensions=[],
                                          f_ext_list_including=[]):
    import os
    import re

    # d 내의 모든 f 리스트 가져오기
    # d="."  # 현재 d에서 확인
    d = D_PKG_CACHE_PRIVATE
    # d=get_pnx_os_style(pnx=d)
    # pattern=rf"{re.escape(d)}\update_pnx_interested_list_to_text_file_\d\.txt$"
    # pattern=rf"{re.escape(d)}\\update_pnx_interested_list_to_text_file_\d\.txt$"
    pattern = rf"^update_pnx_interested_list_to_text_file_\d\.txt$"
    ensure_printed(str_working=rf'''pattern="{pattern}"  {'%%%FOO%%%' if LTA else ''}''')
    # f_list_in_d 아니고 f_nx_list_in_d 인지 확인필요
    f_list_in_d = os.listdir(d)
    ensure_iterable_printed_as_vertical(item_iterable=f_list_in_d, item_iterable_n="f_list_in_d")
    f_nx_list_matched = [file for file in f_list_in_d if re.match(pattern, file)]
    pnxs_required = []
    if f_nx_list_matched:
        ensure_printed(str_working=rf'''files_matched="{f_nx_list_matched}"  {'%%%FOO%%%' if LTA else ''}''')
        for files_nx_matched in f_nx_list_matched:
            pnx = rf"{d}\{files_nx_matched}"
            ensure_printed(str_working=rf'''pnx="{pnx}"  {'%%%FOO%%%' if LTA else ''}''')
            lines = get_list_from_f(f=pnx)
            for line in lines:
                if not including_texts == []:
                    if any(text in line for text in including_texts):
                        pnxs_required.append(line)
                else:
                    pnxs_required.append(line)
        pnxs_required = get_list_replaced_element_from_str_to_str(working_list=pnxs_required, from_str="\n", to_str="")
        # print_list_as_vertical(working_list=pnxs_required, items_name="pnxs_required")
    else:
        ensure_printed(str_working="정규식 패턴에 맞는 f이 존재하지 않습니다.")

    pnxs_excluded = []
    for pnx in pnxs_required:
        # txt_to_exclude_list의 어떠한 요소도 포함되지 않은 경우만 추가
        if not any(exclude_text in pnx for exclude_text in exclude_texts):  # 배제할 확장자 체크
            f_ext_list = os.path.splitext(pnx)[1]
            if f_ext_list not in except_extensions:  # 제외할 확장자 체크
                if not f_ext_list_including == []:
                    if any(f_ext_list == f_ext for f_ext in f_ext_list_including):  # 반드시 포함할 확장자 체크
                        pnxs_excluded.append(pnx)
                else:
                    pnxs_excluded.append(pnx)
    ensure_iterable_printed_as_vertical(item_iterable=pnxs_excluded, item_iterable_n="pnxs_excluded")
    return pnxs_excluded
