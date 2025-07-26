from pkg_py.functions_split.cmd_to_os import cmd_to_os

from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


def open_and_move_wsl_console_to_front(remote_os_distro_n, window_title_seg):
    import time

    ensure_wsl_distro_session(remote_os_distro_n)

    cmd = f'start cmd /k "wsl -d {remote_os_distro_n}"'
    cmd_to_os(cmd=cmd, mode='a')
    time_limit = 20
    time_s = time.time()
    while 1:
        # ensure_printed(str_working=time.time() - time_s)
        if time.time() - time_s > time_limit:
            break
        if is_window_opened(window_title_seg=window_title_seg):
            break
        ensure_slept(seconds=0.5)

    time_limit = 5
    time_s = time.time()
    while 1:
        # ensure_printed(str_working=time.time() - time_s)
        if time.time() - time_s > time_limit:
            break
        if is_front_window_title(window_title_seg=window_title_seg):
            break
        else:
            ensure_window_to_front(window_title_seg=window_title_seg)
        ensure_slept(seconds=0.5)
        break

    # cd

    # clear
