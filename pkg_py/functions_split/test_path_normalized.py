import glob
import inspect
import os
import subprocess
from pathlib import Path
from types import ModuleType

import psutil
import win32gui

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable
from pkg_py.functions_split.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pids import get_pids
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_time_as_ import get_time_as_
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_window_title import get_window_title
from pkg_py.functions_split.get_window_title_list import get_window_title_list
from pkg_py.functions_split.measure_seconds import measure_seconds
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.pk_interface_graphic_user import get_windows_opened
from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.system_object.files import F_PK_WORKSPACE_PY
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025



def test_path_normalized():
    f = str(Path(f).resolve())


