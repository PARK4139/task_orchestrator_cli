

from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


def cmd_to_remote_os_without_pw(port, users, ip, pw, cmd):
    import time

    cmd = f'ssh {users}@{ip} -p {port} "{cmd}"'
    ensure_printed(rf'''cmd="{cmd}"  {'%%%FOO%%%' if LTA else ''}''')
    # cmd_to_os(cmd=cmd) # fail : pw 물은 채로 정지
    cmd_to_os_like_person(cmd=cmd)
    window_title_seg = r"C:\Windows\system32\cmd"
    if LTA:
        print_window_opened_list()
    ensure_printed(rf'''window_title_seg="{window_title_seg}"{'%%%FOO%%%' if LTA else ''}''')
    time_limit = 10
    time_s = time.time()
    while 1:
        # ensure_slept(milliseconds=2000) # success : 느림
        # ensure_slept(milliseconds=1500)
        if is_window_opened(window_title_seg=window_title_seg):
            ensure_window_to_front(window_title_seg=window_title_seg)
            # ensure_slept(milliseconds=500)  # success : 느림
            ensure_slept(milliseconds=100)
            break
        if time.time() - time_s > time_limit:
            return 0
    ensure_slept(milliseconds=500)
