

from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


def cmd_to_os_via_powershell_exe(cmd, console_keep_mode=False, admin_mode=False):
    import time

    # | clip 을 하여도 값을 읽어오기 어려운 경우가 있음
    window_title_seg = rf'PowerShell'
    pk_print(str_working=rf'''cmd="{cmd}"  {'%%%FOO%%%' if LTA else ''}''')
    if not is_window_opened(window_title_seg=window_title_seg):
        # run_cmd_exe()
        if admin_mode == False:
            window_title_seg = rf'powershell'
            run_powershell_exe()
        else:
            window_title_seg = rf'PowerShell'
            run_powershell_exe_as_admin()
    ensure_window_to_front(window_title_seg=window_title_seg)

    std_output_stream = ""
    time_limit = 5
    time_s = time.time()
    while 1:
        if is_front_window_title(window_title_seg=window_title_seg):
            # copy_and_paste_with_keeping_clipboard(string=rf"cd {wsl_pnx} | xclip -sel clip", mode="wsl") # fail: cd는 xclip 으로 pipe 할 수 없음
            copy_and_paste_with_keeping_clipboard(prompt=cmd)
            pk_press("enter")
            std_output_stream = get_str_from_clipboard()
            break
        # 5초가 지났는지 확인
        # pk_print(str_working=time.time() - time_s)
        if time.time() - time_s > time_limit:
            pk_print(str_working="5 seconds passed. Exiting loop.")
            break
        pk_sleep(seconds=0.5)  # CPU 점유율을 낮추기 위해 약간의 대기

    if console_keep_mode == False:
        time_limit = 5
        time_s = time.time()
        while 1:
            if is_front_window_title(window_title_seg=window_title_seg):
                copy_and_paste_with_keeping_clipboard(prompt="exit")
                pk_press("enter")
                if admin_mode == False:
                    copy_and_paste_with_keeping_clipboard(prompt="exit")
                    pk_press("enter")
                break
            # pk_print(str_working=time.time() - time_s)
            if time.time() - time_s > time_limit:
                pk_print(str_working="5 seconds passed. Exiting loop.")
                break
            pk_sleep(seconds=0.5)  # CPU 점유율을 낮추기 위해 약간의 대기
    return std_output_stream
