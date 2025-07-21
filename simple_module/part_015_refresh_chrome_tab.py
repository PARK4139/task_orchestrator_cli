

import numpy as np
import inspect
import importlib
import calendar
from seleniumbase import Driver
from pytube import Playlist
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from datetime import date
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def refresh_chrome_tab(url_to_close):
    import inspect
    func_n = inspect.currentframe().f_code.co_name

    # minimize_all_windows()
    # window_title_seg = get_window_title(window_title_seg="Chrome")
    window_titles = get_window_title_list()
    import time

    timeout_seconds = 10
    start_time = time.time()
    for window_title_seg in window_titles:
        if "chrome".lower() in window_title_seg.lower():
            if timeout_seconds == 50:
                pk_print(working_str=rf'''window_title="{window_title_seg}"  {'%%%FOO%%%' if LTA else ''}''')
            while 1:
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout_seconds:
                    break
                ensure_window_to_front(window_title_seg=window_title_seg)
                pk_sleep(milliseconds=15)
                pk_press("ctrl", "l")
                pk_sleep(milliseconds=15)
                url_dragged = get_text_dragged()
                if url_dragged == url_to_close:
                    pk_print(working_str=rf'''url_to_close="{url_to_close}"  {'%%%FOO%%%' if LTA else ''}''')
                    pk_print(working_str=rf'''url_dragged="{url_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
                    pk_press("f5")
                    # restore_all_windows()
                    return
