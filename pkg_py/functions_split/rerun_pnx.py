import zlib
import win32con
import uuid
import urllib.parse
import urllib
import tqdm
import tomllib
import toml
import toml
import threading
import subprocess
import speech_recognition as sr
import socket
import shutil
import re
import pywintypes
# import pywin32
import pyautogui
import os.path
import nest_asyncio
import json
import inspect
import datetime
import colorama
import chardet
import browser_cookie3
import asyncio
from typing import TypeVar, List
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_once import pk_print_once

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_HISTORICAL_PNX

from pathlib import Path
from datetime import timedelta
from datetime import datetime, time
from datetime import date
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def rerun_pnx(my_name):  # 종료용이름 시작용이름 이 다름 따로 수집해서 코딩 필요
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    kill_process_via_taskkill(process_name=my_name)
    pk_sleep(milliseconds=200)  # 최적화 테스트 필요
    cmd = rf'start "{my_name}"'
    cmd_to_os(cmd=cmd, mode="a")
