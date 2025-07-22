

from pkg_py.functions_split.pk_press import pk_press


def cmd_to_wsl_os_like_person(cmd, remote_os_distro_n, wsl_window_title_seg, sleep_time=500):
    run_wsl(remote_os_distro_n=remote_os_distro_n, wsl_window_title_seg=wsl_window_title_seg)
    write_like_person(cmd)
    pk_sleep(milliseconds=sleep_time)
    pk_press('enter')
