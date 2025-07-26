

from pkg_py.functions_split.ensure_pressed import ensure_pressed


def cmd_to_wsl_os_like_person(cmd, remote_os_distro_n, wsl_window_title_seg, sleep_time=500):
    run_wsl(remote_os_distro_n=remote_os_distro_n, wsl_window_title_seg=wsl_window_title_seg)
    ensure_writen_like_person(cmd)
    ensure_slept(milliseconds=sleep_time)
    ensure_pressed('enter')
