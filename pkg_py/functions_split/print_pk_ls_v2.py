

import zipfile
import win32con
import sys
import random
import pygetwindow
import easyocr
from telegram import Bot
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.print_red import print_red

from os import path
from dataclasses import dataclass
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.ensure_printed import ensure_printed


def print_pk_ls_v2(index_map: dict):
    #
    import os

    ensure_printed("실행 가능한 pk_ 프로그램 목록:")
    for idx, path in index_map.items():
        nx = os.path.basename(path)
        ensure_printed(f"[{idx}] {nx}")
