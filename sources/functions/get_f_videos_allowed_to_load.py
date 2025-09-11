import yt_dlp
import win32con
import win32com.client
import timeit
import time
import subprocess, time
import subprocess
import string
import sqlite3
import shlex
import re

import psutil
import pandas as pd
import os, inspect
import numpy as np
import nest_asyncio
import json
import ipdb
import inspect
import importlib
import hashlib
import datetime
import chardet
import calendar

from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from telegram import Bot
from selenium.webdriver.common.action_chains import ActionChains
from pynput import mouse
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession

from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_printed_once import ensure_printed_once

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_context import SpeedControlContext

from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from gtts import gTTS
from datetime import datetime, timedelta
from datetime import date
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from collections import Counter
from base64 import b64encode
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
import logging

from sources.objects.pk_local_test_activate import LTA
import logging


def get_f_videos_allowed_to_load(ext_list_allowed, d_working):
    import os
    if LTA:
        logging.debug(f'''ext_list_allowed={ext_list_allowed}  {'%%%FOO%%%' if LTA else ''}''')
    f_videos_allowed = []
    pnx_list = get_pnxs_from_d_working(d_working=d_working, with_walking=0)
    ensure_list_written_to_f(working_list=pnx_list, f=F_VIDEO_LIST_ALLOWED_TO_LOAD_TXT, mode='w')

    for f in get_list_from_f(F_VIDEO_LIST_ALLOWED_TO_LOAD_TXT):
        f = f.replace("\n", '')
        f_x = os.path.splitext(f)[1].replace("\n", '')
        f_nx = os.path.basename(f).lower()

        if not f_x:  # 확장자가 없을 경우 빈 문자열이기 때문에 예외 처리
            if LTA:
                logging.debug(f"[NOT ALLOWED] [확장자 없음]: {f}")
            continue

        f_x = f_x.lower()  # 확장자가 있을 때만 소문자로 변환

        if f_x not in ext_list_allowed:
            if LTA:
                logging.debug(f"[NOT ALLOWED] [확장자 불가]: f={f}")
            continue

        if any(keyword in f_nx for keyword in {"seg", "temp"}):
            if LTA:
                logging.debug(f"[NOT ALLOWED] [금지 키워드 포함] : f={f} f_x={f_x}")
            continue
        if LTA:
            logging.debug(f"[ALLOWED] [확장자 가능]: f={f} f_x={f_x}")
        f_videos_allowed.append(f)

    return f_videos_allowed
