import win32con
import uuid
import urllib.parse
import tqdm
import tomllib
import toml
import tarfile
import shlex
import secrets
import re

import pyautogui
import platform
import nest_asyncio
import mutagen
import math
import json
import functools
import colorama
from webdriver_manager.chrome import ChromeDriverManager
from telethon import TelegramClient, events
from telegram import Bot, Update
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.get_list_calculated import get_list_calculated

from PIL import Image, ImageFilter
from PIL import Image
from pathlib import Path
from dirsync import sync
from datetime import datetime, timedelta
from colorama import init as pk_colorama_init
from base64 import b64encode
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.ensure_printed import ensure_printed


def get_pnx_validated(pnx):
    import os
    pnx = pnx.strip()
    pnx = get_pnx_os_style(pnx)
    if not os.path.exists(pnx):
        ensure_printed(f"❌ 경로가 존재하지 않습니다: {pnx}", print_color='red')
        raise
    return pnx
