import inspect
import os
import re
import shutil
import subprocess
import sys
import time
import traceback
from pathlib import Path

import win32gui
import win32process

from pkg_py.functions_split.chcp_65001 import chcp_65001
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_historical import get_history_file
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_os_n import get_os_n
from pkg_py.functions_split.get_pids import get_pids
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_time_as_ import get_time_as_
from pkg_py.functions_split.get_values_from_historical_file import get_values_from_history_file
from pkg_py.functions_split.get_window_title import get_window_title
from pkg_py.functions_split.kill_process_via_taskkill import kill_process_via_taskkill
from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
from pkg_py.functions_split.colorama_init_once import colorama_init_once
from pkg_py.functions_split.measure_seconds import measure_seconds
from pkg_py.functions_split.press import press
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_slept import ensure_slept
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.set_values_to_historical_file import set_values_to_historical_file
from pkg_py.functions_split.ensure_writen_like_person import ensure_writen_like_person
from pkg_py.pk_interface_graphic_user import get_windows_opened
from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP
from pkg_py.system_object.directories import D_PKG_HISTORY
from pkg_py.system_object.directories import D_PKG_WINDOWS
from pkg_py.system_object.directories_reuseable import D_PROJECT, D_HOME
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE


@measure_seconds

def ensure_files_stable_after_change(f_list, stable_seconds_limit, monitoring_interval_seconds=0.2):
    from pkg_py.functions_split.ensure_slept import ensure_slept
    import os
    import time
    from pkg_py.functions_split.get_nx import get_nx

    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style

    f_list = [get_pnx_os_style(f) for f in f_list]

    def get_mtime_map(f_list):
        result = {}
        for f in f_list:
            f_clean = os.path.abspath(f.strip())
            try:
                if os.path.exists(f_clean):
                    result[f] = os.path.getmtime(f_clean)
                else:
                    ensure_printed(f"❌ 경로 없음: {f_clean}", print_color='red')
            except Exception as e:
                ensure_printed(f"❌ getmtime 실패: {f_clean} | {e}", print_color='red')
        return result

    f_nx_list = [get_nx(f) for f in f_list]
    ensure_printed(f"⏳ {stable_seconds_limit}초간 f_nx_list={f_nx_list} 변경 감시 시작...", print_color='white')
    baseline = get_mtime_map(f_list)
    start_time = time.time()

    while True:
        current = get_mtime_map(f_list)
        for f in f_list:
            if f in baseline and f in current and baseline[f] != current[f]:
                ensure_printed(f"f_list is not stable ({f})")
                return False
        if time.time() - start_time >= stable_seconds_limit:
            ensure_printed(f"f_list is stable for ({stable_seconds_limit})")
            return True

        ensure_slept(monitoring_interval_seconds)


