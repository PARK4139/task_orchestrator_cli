
@pk_measure_seconds
baseline = get_mtime_map(f_list)
current = get_mtime_map(f_list)
def ensure_files_stable_after_change(f_list, stable_seconds_limit, monitoring_interval_seconds=0.2):
def get_mtime_map(f_list):
else:
except Exception as e:
f_clean = os.path.abspath(f.strip())
f_list = [get_pnx_os_style(f) for f in f_list]
f_nx_list = [get_nx(f) for f in f_list]
for f in f_list:
from pathlib import Path
from pkg_py.functions_split.chcp_65001 import chcp_65001
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.colorama_init_once import pk_colorama_init_once
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
from pkg_py.functions_split.measure_seconds import pk_measure_seconds
from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
from pkg_py.functions_split.press import pk_press
from pkg_py.functions_split.print import pk_print
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.set_values_to_historical_file import set_values_to_historical_file
from pkg_py.functions_split.sleep import pk_sleep
from pkg_py.functions_split.write_like_person import write_like_person
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
if f in baseline and f in current and baseline[f] != current[f]:
if os.path.exists(f_clean):
if time.time() - start_time >= stable_seconds_limit:
import inspect
import os
import re
import shutil
import subprocess
import sys
import time
import traceback
import win32gui
import win32process
pk_print(f"f_list is not stable ({f})")
pk_print(f"f_list is stable for ({stable_seconds_limit})")
pk_print(f"⏳ {stable_seconds_limit}초간 f_nx_list={f_nx_list} 변경 감시 시작...", print_color='white')
pk_print(f"❌ getmtime 실패: {f_clean} | {e}", print_color='red')
pk_print(f"❌ 경로 없음: {f_clean}", print_color='red')
pk_sleep(monitoring_interval_seconds)
result = {}
result[f] = os.path.getmtime(f_clean)
return False
return True
return result
start_time = time.time()
try:
while True:
