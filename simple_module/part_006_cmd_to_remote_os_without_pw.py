

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front


def cmd_to_remote_os_without_pw(port, users, ip, pw, cmd):
    import time

    cmd = f'ssh {users}@{ip} -p {port} "{cmd}"'
    pk_print(rf'''cmd="{cmd}"  {'%%%FOO%%%' if LTA else ''}''')
    # cmd_to_os(cmd=cmd) # fail : pw 물은 채로 정지
    cmd_to_os_like_person(cmd=cmd)
    window_title_seg = r"C:\Windows\system32\cmd"
    if LTA:
        print_window_opened_list()
    pk_print(rf'''window_title_seg="{window_title_seg}"{'%%%FOO%%%' if LTA else ''}''')
    time_limit = 10
    time_s = time.time()
    while 1:
        # pk_sleep(milliseconds=2000) # success : 느림
        # pk_sleep(milliseconds=1500)
        if is_window_opened(window_title_seg=window_title_seg):
            ensure_window_to_front(window_title_seg=window_title_seg)
            # pk_sleep(milliseconds=500)  # success : 느림
            pk_sleep(milliseconds=100)
            break
        if time.time() - time_s > time_limit:
            return 0
    pk_sleep(milliseconds=500)
