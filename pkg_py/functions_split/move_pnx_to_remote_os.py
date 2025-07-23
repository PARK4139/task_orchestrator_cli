



from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.cmd_to_os import cmd_to_os

from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


def move_pnx_to_remote_os(pnx, dst='~/Downloads', **config_remote_os):
    ensure_ssh_public_key_to_remote_os(**config_remote_os)

    ip = config_remote_os['ip']
    pw = config_remote_os['pw']
    port = config_remote_os['port']
    user_n = config_remote_os['user_n']

    if not does_pnx_exist(pnx=pnx):
        pk_print(f'''does not exist pnx to send {'%%%FOO%%%' if LTA else ''}''')
        return

    pnx = get_pnx_unix_style(pnx)
    dst = get_pnx_unix_style(dst)
    cmd = f'scp -P {port} -r "{pnx}" {user_n}@{ip}:{dst}'
    # cmd = f'rsync -avz -e "ssh -p {port}" "{src}" {users}@{ip}:{dst}' # windows 환경에는 rsync 없이 가능해야한다... wsl 설치하고 지우면...?너무 비효율적인가?

    cmd_to_os(cmd=cmd)  # warning : pw 물은 채로 정지
    window_title_seg = r"C:\Windows\system32\cmd"
    # pk_sleep(milliseconds=2000) # success : but late
    # pk_sleep(milliseconds=1000) # success : but late
    pk_sleep(milliseconds=500)
    while 1:
        if is_window_opened(window_title_seg=window_title_seg):
            ensure_window_to_front(window_title_seg=window_title_seg)
            # pk_sleep(milliseconds=500)  # success : but late
            # pk_sleep(milliseconds=200)
            pk_sleep(milliseconds=100)
            write_like_person(str_working=pw)
            pk_sleep(milliseconds=100)
            pk_press("enter")
            break
    pk_sleep(milliseconds=500)
