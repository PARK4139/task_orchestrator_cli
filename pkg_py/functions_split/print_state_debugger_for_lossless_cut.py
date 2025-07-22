import zlib
# import win32gui
import uuid
import traceback
import timeit
import random
import pygetwindow
import inspect
import easyocr
import browser_cookie3
import asyncio
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.cmd_to_os import cmd_to_os

from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT

from paramiko import SSHClient, AutoAddPolicy
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import lru_cache
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.get_pnx_list import get_pnx_list

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def print_state_debugger_for_lossless_cut(stamp, state_running, state_loading, state_loaded, state_playing):
    if LTA:
        pk_print(f'''state_running={state_running} {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''state_loading={state_loading} {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''state_loaded={state_loaded} {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''state_playing={state_playing} {'%%%FOO%%%' if LTA else ''}''')
        pk_print(stamp)
        input('press enter')
