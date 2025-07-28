import inspect
import logging
import os
import time

from pkg_py.pk_paste_as_auto import copy
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP
from pkg_py.system_object.directories import D_DESKTOP
from pkg_py.refactor.ensure_keyboard_mouse_macro import PkMacroRoutines
from pkg_py.functions_split.ensure_elapsed_time_logged import ensure_elapsed_time_logged
from pkg_py.functions_split.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
from pkg_py.functions_split.ensure_start_time_logged import ensure_start_time_logged
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_value_by_file_id import get_value_by_file_id
from pkg_py.functions_split.ensure_slept import ensure_slept
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_str_from_f import get_str_from_f
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_loop_delayed_at_loop_foot import ensure_loop_delayed_at_loop_foot
from pkg_py.functions_split.type import type



def open_pycharm_parrete():
    ensure_pressed("shift")
    ensure_slept(100)
    ensure_pressed("shift")
    ensure_slept(500)


