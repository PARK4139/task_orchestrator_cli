import winreg
import win32con
import webbrowser
import timeit
import time
import shutil
import requests
import random
import pythoncom
import ipdb
import hashlib
import functools
from selenium.webdriver.common.keys import Keys
from prompt_toolkit import PromptSession
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_local_test_activate import LTA
from functools import partial as functools_partial
from concurrent.futures import ThreadPoolExecutor
from base64 import b64decode

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style

from sources.functions.get_d_working import get_d_working


def get_list_that_element_applyed_via_func(func, working_list):
    return [func(item) for item in working_list]
