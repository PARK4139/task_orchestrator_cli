

from sources.objects.pk_local_test_activate import LTA

import logging
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_window_to_front import ensure_window_to_front


def ensure_command_to_remote_os_without_pw(port, users, ip, pw, cmd):
    import time

    cmd = f'ssh {users}@{ip} -p {port} "{cmd}"'
    logging.debug(rf'''cmd="{cmd}"  {'%%%FOO%%%' if LTA else ''}''')
    # ensure_command_executed(cmd=cmd) # fail : pw 물은 채로 정지
    ensure_command_executed_like_human(cmd=cmd)
    window_title_seg = r"C:\Windows\system32\cmd"
    if LTA:
        ensure_windows_printed()
    logging.debug(rf'''window_title_seg="{window_title_seg}"{'%%%FOO%%%' if LTA else ''}''')
    time_limit = 10
    time_s = time.time()
    while 1:
        # ensure_slept(milliseconds=2000) # success : 느림
        # ensure_slept(milliseconds=1500)
        if is_window_opened(window_title_seg=window_title_seg):
            ensure_window_to_front(window_title_seg)
            # ensure_slept(milliseconds=500)  # success : 느림
            ensure_slept(milliseconds=100)
            break
        if time.time() - time_s > time_limit:
            return 0
    ensure_slept(milliseconds=500)
