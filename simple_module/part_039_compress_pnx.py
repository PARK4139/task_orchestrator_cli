

import win32con
import sqlite3
import secrets
import mutagen
import json
import cv2
from selenium.common.exceptions import WebDriverException
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from os.path import dirname
from functools import partial
from bs4 import BeautifulSoup
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style


def compress_pnx(src, dst, with_timestamp=1):
    return compress_pnx_via_rar(src=src, dst=dst, with_timestamp=with_timestamp)
