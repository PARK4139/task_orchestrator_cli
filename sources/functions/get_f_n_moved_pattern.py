

import yt_dlp
import time
import threading
import speech_recognition as sr
import random
import platform
import nest_asyncio
import importlib
import easyocr
import chardet
from seleniumbase import Driver
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern


from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.is_window_opened import is_window_opened
import logging
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f


from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_local_test_activate import LTA


from pathlib import Path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import lru_cache
from datetime import datetime
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging


def get_f_n_moved_pattern(pattern, pnx_working, mode_front):
    import re
    match = re.search(pattern=pattern, string=pnx_working)
    n = get_n(pnx_working)
    p = get_p(pnx_working)
    x = get_x(pnx_working)
    if match:
        pattern = match.group(1)
        if mode_front:
            pnx_working_new = rf"{p}\{pattern}_{n.replace(pattern, '')}{x}"
        else:
            pnx_working_new = rf"{p}\{n.replace(pattern, '')}_{pattern}{x}"
        return pnx_working_new
    else:
        # 패턴이 없으면 원래 f명 반환
        return pnx_working
