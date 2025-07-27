

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
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f

from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.get_list_calculated import get_list_calculated

from pathlib import Path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import lru_cache
from datetime import datetime
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed


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
