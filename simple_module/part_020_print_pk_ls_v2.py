

import zipfile
import win32con
import sys
import random
import pygetwindow
import easyocr
from telegram import Bot
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_800_print_util import print_red

from os import path
from dataclasses import dataclass
from base64 import b64encode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style

from pkg_py.simple_module.part_014_pk_print import pk_print


def print_pk_ls_v2(index_map: dict):
    #
    import os

    pk_print("실행 가능한 pk_ 프로그램 목록:")
    for idx, path in index_map.items():
        nx = os.path.basename(path)
        pk_print(f"[{idx}] {nx}")
