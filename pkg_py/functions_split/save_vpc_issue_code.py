import yt_dlp
# import win32gui
import urllib.parse
import urllib
import tomllib
import timeit
import subprocess
import socket, time
import pyautogui
import os
import mutagen
import hashlib
import clipboard
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from telegram import Bot
from selenium.webdriver.common.by import By
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_object.etc import PkFilter
from PIL import Image, ImageFilter
from functools import partial as functools_partial
from datetime import timedelta
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.pk_system_object.local_test_activate import LTA

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def save_vpc_issue_code(issue_code):
    pk_print(f'''issu_code is saved {'%%%FOO%%%' if LTA else ''}''')
