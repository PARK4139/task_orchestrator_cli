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

import pyautogui
import os.path
import nest_asyncio
import json
import inspect
import datetime
import colorama
import chardet

import asyncio
from typing import TypeVar, List
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from sources.functions.get_historical_list import get_historical_list


from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_printed_once import ensure_printed_once

from sources.functions.ensure_command_executed import ensure_command_executed

from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX

from pathlib import Path
from datetime import timedelta
from datetime import datetime, time
from datetime import date
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from base64 import b64encode
from base64 import b64decode
from sources.functions.get_nx import get_nx
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

from sources.objects.pk_local_test_activate import LTA
from sources.functions.get_pnxs import get_pnxs


def rerun_pnx(my_name):  # 종료용이름 시작용이름 이 다름 따로 수집해서 코딩 필요
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    ensure_process_killed_via_taskkill(process_name=my_name)
    ensure_slept(milliseconds=200)  # 최적화 테스트 필요
    cmd = rf'start "{my_name}"'
    ensure_command_executed(cmd=cmd, mode="a")
