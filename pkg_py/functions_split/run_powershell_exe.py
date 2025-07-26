from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


def run_powershell_exe():
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    ensure_command_excuted_to_os('start cmd /k powershell', mode='a')
    # ensure_command_excuted_to_os('start cmd /k powershell')
    window_title_seg = "powershell"
    while 1:
        if not is_front_window_title(window_title_seg=window_title_seg):
            ensure_window_to_front(window_title_seg=window_title_seg)
        if is_front_window_title(window_title_seg=window_title_seg):
            break
