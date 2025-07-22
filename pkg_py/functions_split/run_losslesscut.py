import winreg
import win32con
import keyboard
import hashlib
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.pk_system_object.files import F_LOSSLESSCUT_EXE

from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def run_losslesscut():
    import os
    f_losslesscut_exe = get_pnx_windows_style(pnx=F_LOSSLESSCUT_EXE)
    if not os.path.exists(f_losslesscut_exe):
        if LTA:
            pk_print(f"{get_nx(f_losslesscut_exe)} is not installed", print_color='red')
    else:
        if LTA:
            pk_print(f"{get_nx(f_losslesscut_exe)} is installed", print_color='green')
    cmd_to_os(cmd=rf'''start "" /MAX "{f_losslesscut_exe}"''', mode='a')
