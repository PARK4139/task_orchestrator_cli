import zipfile
import winreg

import undetected_chromedriver as uc
import traceback
import tomllib
import tomllib
import socket
import pyaudio
import mysql.connector
import asyncio
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI

from os.path import dirname
from moviepy import VideoFileClip
from functools import partial
from functools import lru_cache
from enum import Enum
from colorama import init as pk_colorama_init
from collections import Counter

from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


def get_f_video_of_d_working(d_working, ext_list_allowed):
    import os
    logging.debug(f'''d_working={d_working} extension_list_allowed={ext_list_allowed} {'%%%FOO%%%' if LTA else ''}''')
    if not os.path.exists(d_working):
        logging.debug(f"d_working does not exists {d_working}")
    if os.path.exists(d_working):
        for f_nx in os.listdir(d_working):
            f = os.path.join(d_working, f_nx)
            ext = os.path.splitext(f)[1].lower()
            if not ext in ext_list_allowed:
                # logging.debug(f"f={f}, ext={ext}, 조건 만족 여부: {ext in extensions}")
                pass
    f_list_of_d_working = [os.path.join(d_working, f) for f in os.listdir(d_working)]
    logging.debug(f'''len(f_list_of_d_working)={len(f_list_of_d_working)}  {'%%%FOO%%%' if LTA else ''}''')
    f_videos_allowed = [
        f for f in f_list_of_d_working
        if os.path.splitext(f)[1].lower() in ext_list_allowed
           and not any(keyword in os.path.basename(f).lower() for keyword in ["seg", "temp"])
    ]
    logging.debug(f'''len(f_videos_allowed)={len(f_videos_allowed)}  {'%%%FOO%%%' if LTA else ''}''')
    if f_videos_allowed:
        f_videos_allowed.sort()
        return f_videos_allowed[0]
    else:
        logging.debug("조건에 맞는 f 없습니다.")
        return None
