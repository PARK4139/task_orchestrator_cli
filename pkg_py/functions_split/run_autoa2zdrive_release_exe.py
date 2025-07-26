

from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_opened import is_window_opened

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os


from pkg_py.functions_split.ensure_printed import ensure_printed


from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


def run_autoa2zdrive_release_exe():
    import time

    import inspect
    func_n = inspect.currentframe().f_code.co_name

    # autoa2zdrive_release_exe exec  # via local file

    window_title_seg = "AutoA2Z Drive"
    timeout = 20
    start_time = time.time()
    while 1:
        if not is_window_opened(window_title_seg=window_title_seg):
            pnx = rf"{D_DESKTOP}\AutoA2ZDrive\AutoA2ZDrive_Release.exe"
            cmd = rf' explorer "{pnx}" '
            ensure_command_excuted_to_os(cmd=cmd, mode="a")
        while 1:
            if is_window_opened(window_title_seg=window_title_seg):
                break
            if time.time() - start_time > timeout:
                break
            ensure_slept(seconds=1)
        break

    # 자동닫힘 여부확인 # 40초 동안에
    timeout = 40
    start_time = time.time()
    while 1:
        if not is_window_opened(window_title_seg=window_title_seg):
            break
        if time.time() - start_time > timeout:
            break
        ensure_slept(seconds=1)

    # 40초 동안에 안열리면 VS code exec
    window_title_seg = "AutoA2ZDrive_Release.exe"
    timeout = 5
    start_time = time.time()
    while 1:
        if not is_window_opened(window_title_seg=window_title_seg):
            cmd = rf' explorer "C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\devenv.exe" '
            ensure_command_excuted_to_os(cmd=cmd, mode="a")
            break
        while 1:
            if is_front_window_title(window_title_seg=window_title_seg):
                ensure_window_to_front(window_title_seg=window_title_seg)
                break
        ensure_printed(str_working=time.time() - start_time)
        if time.time() - start_time > timeout:
            break
        ensure_slept(milliseconds=1000)
