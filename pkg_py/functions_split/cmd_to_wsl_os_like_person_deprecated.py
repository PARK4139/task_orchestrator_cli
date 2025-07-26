


from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.press import press
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


def cmd_to_wsl_os_like_person_deprecated(cmd, remote_os_distro_n, wsl_window_title_seg, exit_mode=False):
    import time
    import inspect
    func_n = inspect.currentframe().f_code.co_name

    timeout = 20
    start_time = time.time()
    while 1:
        if is_window_opened(window_title_seg=wsl_window_title_seg):
            break
        open_and_move_wsl_console_to_front(remote_os_distro_n=remote_os_distro_n, window_title_seg=wsl_window_title_seg)
        ensure_printed(str_working=time.time() - start_time)
        if time.time() - start_time > timeout:
            break
        ensure_slept(seconds=0.5)

    std_output_stream = ""
    timeout = 5
    start_time = time.time()
    while 1:
        if is_front_window_title(window_title_seg=wsl_window_title_seg):
            copy_and_paste_with_keeping_clipboard(prompt=cmd, wsl_mode=True)
            pk_press("enter")
            break
        ensure_window_to_front(window_title_seg=wsl_window_title_seg)

        # 5초가 지났는지 확인
        ensure_printed(str_working=time.time() - start_time)
        if time.time() - start_time > timeout:
            ensure_printed(str_working="5 seconds passed. Exiting loop.")
            break
        ensure_slept(seconds=0.5)  # CPU 점유율을 낮추기 위해 약간의 대기

    if exit_mode == True:
        timeout = 5
        start_time = time.time()
        while 1:
            if is_front_window_title(window_title_seg=wsl_window_title_seg):
                copy_and_paste_with_keeping_clipboard(prompt="exit", wsl_mode=True)
                pk_press("enter")
                copy_and_paste_with_keeping_clipboard(prompt="exit", wsl_mode=True)
                pk_press("enter")
                break
            else:
                ensure_window_to_front(window_title_seg=wsl_window_title_seg)
            ensure_printed(str_working=time.time() - start_time)
            if time.time() - start_time > timeout:
                ensure_printed(str_working="5 seconds passed. Exiting loop.")
                break
            ensure_slept(seconds=0.5)  # CPU 점유율을 낮추기 위해 약간의 대기

    # return std_output_stream
