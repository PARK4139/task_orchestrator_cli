

from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.is_window_opened import is_window_opened

from sources.functions.ensure_command_executed import ensure_command_executed


import logging


from sources.functions.ensure_command_executed import ensure_command_executed

import logging
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_window_to_front import ensure_window_to_front


def run_autoTBDdrive_release_exe():
    import time

    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    # autoTBDdrive_release_exe exec  # via local file

    window_title_seg = "AutoTBD Drive"
    timeout = 20
    start_time = time.time()
    while 1:
        if not is_window_opened(window_title_seg=window_title_seg):
            pnx = rf"{D_DESKTOP}\AutoTBDDrive\AutoTBDDrive_Release.exe"
            cmd = rf' explorer "{pnx}" '
            ensure_command_executed(cmd=cmd, mode="a")
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
    window_title_seg = "AutoTBDDrive_Release.exe"
    timeout = 5
    start_time = time.time()
    while 1:
        if not is_window_opened(window_title_seg=window_title_seg):
            cmd = rf' explorer "C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\devenv.exe" '
            ensure_command_executed(cmd=cmd, mode="a")
            break
        while 1:
            if ensure_window_to_front(window_title_seg):
                ensure_window_to_front(window_title_seg)
                break
        logging.debug(time.time() - start_time)
        if time.time() - start_time > timeout:
            break
        ensure_slept(milliseconds=1000)
