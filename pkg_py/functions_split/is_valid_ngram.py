import yt_dlp

import webbrowser
import threading
import random, math


import ipdb
import datetime
import calendar
from zipfile import BadZipFile
from urllib.parse import urlparse
from tkinter import UNDERLINE
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.system_object.local_test_activate import LTA
from mutagen.mp3 import MP3
from dirsync import sync
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def is_valid_ngram(k: str) -> bool:
    import re
    if len(k.split()) < 2:
        return False

    # 숫자 단독, (1080p), 등 무의미한 값 제외
    if re.fullmatch(r"\d+|\d{3,4}p|\(\d{3,4}p\)", k.strip()):
        return False

    # "- 12" 같은 기호+숫자 조합 제거
    if re.fullmatch(r"[-~–—]\s*\d+", k.strip()):
        return False

    # "12 (1080p)" 같은 회차 + 화질 제거
    if re.search(r"\b\d{1,2} ?\(\d{3,4}p\)", k):
        return False

    return True
