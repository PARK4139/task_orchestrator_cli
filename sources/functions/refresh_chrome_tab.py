

import numpy as np
import inspect
import importlib
import calendar
from seleniumbase import Driver
from pytube import Playlist
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.ensure_pressed import ensure_pressed

from sources.functions.get_list_sorted import get_list_sorted

from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from datetime import date
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
import logging

from sources.objects.pk_local_test_activate import LTA
import logging


def refresh_chrome_tab(url_to_close):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    # ensure_windows_minimized()
    # window_title_seg = get_window_title(window_title_seg="Chrome")
    window_titles = get_window_titles()
    import time

    timeout_seconds = 10
    start_time = time.time()
    for window_title_seg in window_titles:
        if "chrome".lower() in window_title_seg.lower():
            if timeout_seconds == 50:
                logging.debug(rf'''window_title="{window_title_seg}"  {'%%%FOO%%%' if LTA else ''}''')
            while 1:
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout_seconds:
                    break
                ensure_window_to_front(window_title_seg)
                ensure_slept(milliseconds=15)
                ensure_pressed("ctrl", "l")
                ensure_slept(milliseconds=15)
                url_dragged = get_text_dragged()
                if url_dragged == url_to_close:
                    logging.debug(rf'''url_to_close="{url_to_close}"  {'%%%FOO%%%' if LTA else ''}''')
                    logging.debug(rf'''url_dragged="{url_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
                    ensure_pressed("f5")
                    # restore_all_windows()
                    return
