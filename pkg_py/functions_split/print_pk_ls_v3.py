

import tomllib
import string
import pickle
import os
import json

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.system_object.directories import D_WORKING
from pathlib import Path
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from base64 import b64encode
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.pk_print import pk_print


def print_pk_ls_v3(index_map: dict, limit=None):
    #
    import os
    pk_print("실행 가능한 pk_ 프로그램 목록:")

    for idx, filepath in index_map.items():

        if limit is not None and idx >= limit:
            pk_print(f"... (이하 {len(index_map) - limit}개 생략됨)")
            break
        pk_print(f"[{idx}] {os.path.basename(filepath)}")
