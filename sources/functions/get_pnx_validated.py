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
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.ensure_printed_once import ensure_printed_once
import logging

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext



from PIL import Image, ImageFilter
from PIL import Image
from pathlib import Path
from dirsync import sync
from datetime import datetime, timedelta
from colorama import init as pk_colorama_init
from base64 import b64encode


from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.functions.is_f import is_f
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

import logging


def get_pnx_validated(pnx):
    import os
    pnx = pnx.strip()
    pnx = Path(pnx)
    if not os.path.exists(pnx):
        logging.debug(f"경로가 존재하지 않습니다: {pnx}")
        raise
    return pnx
