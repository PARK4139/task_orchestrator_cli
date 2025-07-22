import winreg
import urllib.parse
import traceback
import timeit
import subprocess
import colorama
from yt_dlp import YoutubeDL
from selenium.common.exceptions import WebDriverException
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_object.directories import D_WORKING

from functools import partial as functools_partial
from Cryptodome.Cipher import AES
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_object.etc import PK_UNDERLINE
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def kill_process_via_taskkill(process_name=None, pid=None, debug_mode=True):
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    if process_name is not None or pid is not None:
        pk_print(rf"{func_n}() 동작 조건 충족")
    else:
        pk_print(rf"{func_n}() 동작 조건 불충족")
        return

    cmd = None
    if process_name != None:
        cmd = f'taskkill /f /im {process_name}"'
    elif pid != None:
        cmd = f'taskkill /f /pid {pid}"'
    cmd_to_os(cmd=cmd)
