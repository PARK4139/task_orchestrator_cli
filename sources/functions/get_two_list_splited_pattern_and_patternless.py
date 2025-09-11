import threading
import string
import os
from selenium.webdriver.common.keys import Keys
from pytube import Playlist
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.objects.encodings import Encoding

from datetime import date
from sources.functions.get_pnxs import get_pnxs


def get_two_list_splited_pattern_and_patternless(items, pattern):
    import inspect
    import re
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    pnx_list_required_pattern = []
    pnx_list_required_patternless = []

    for item in items:
        match = re.match(pattern, item)  # 정규식에 맞는 부분 찾기
        if match:
            pnx_list_required_pattern.append(match.group(1))  # magnet 부분
            pnx_list_required_patternless.append(match.group(2))  # f명 부분

    return pnx_list_required_pattern, pnx_list_required_patternless
