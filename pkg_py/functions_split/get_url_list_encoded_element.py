import win32con
import traceback
import timeit
import threading
import sys
import requests
import nest_asyncio
import calendar
from yt_dlp import YoutubeDL
from seleniumbase import Driver
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.is_os_windows import is_os_windows
from os import path
from gtts import gTTS
from enum import Enum
from datetime import datetime
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def get_url_list_encoded_element(working_list):
    import urllib.parse

    pk_print(f'''working_list={working_list}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    return [urllib.parse.quote(item) for item in working_list]
