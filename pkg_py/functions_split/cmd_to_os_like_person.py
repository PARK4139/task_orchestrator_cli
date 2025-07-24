

from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.run_cmd_exe import run_cmd_exe
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


#
# from pkg_py.system_object.files_and_directories_maker_logic import ensure_pnx_made
# from pkg_py.system_object.mouse_and_keyboard import write_like_person
# from pkg_py.system_object.is_os_windows import is_os_windows
# , pk_print_state
# from pkg_py.system_object.time_and_lanauge_util import pk_sleep
# from pkg_py.system_object.directories import D_PKG_WINDOWS
# from pkg_py.system_object.encodings import Encoding
# from pkg_py.system_object.stamps import STAMP_REMOTE_ERROR, STAMP_REMOTE_DEBUG, STAMP_ATTEMPTED


def cmd_to_os_like_person(cmd, admin_mode=False, mode_exit=True):
    import time

    # todo : chore : return 에 대해서 개선필요
    '''
    return 재대로 안됨
    '''
    window_title_seg = rf'cmd.exe'
    # | clip 을 하여도 값을 읽어오기 어려운 경우가 있음
    pk_print(str_working=rf'''cmd="{cmd}"  {'%%%FOO%%%' if LTA else ''}''')
    if not is_window_opened(window_title_seg=window_title_seg):
        if admin_mode == False:

            run_cmd_exe()
        else:
            run_cmd_exe_as_admin()

    std_str = ""
    time_limit = 10
    time_s = time.time()
    while 1:
        if LTA:
            print(1)
        if is_front_window_title(window_title_seg=window_title_seg):
            # cmd=rf"{cmd} | clip"
            copy_and_paste_with_keeping_clipboard(prompt=cmd)
            # pk_sleep(milliseconds=1000)
            pk_sleep(milliseconds=500)
            if is_front_window_title(window_title_seg=window_title_seg):
                pk_press("enter")
            std_str = get_str_from_clipboard()
            return std_str
        ensure_window_to_front(window_title_seg=window_title_seg)
        # # pk_print(str_working=time.time() - time_s)
        if time.time() - time_s > time_limit:
            pk_print(str_working=rf'''rf"{time_limit} seconds passed. Exiting loop."  {'%%%FOO%%%' if LTA else ''}''')
            break
        pk_sleep(seconds=0.5)  # CPU 점유율을 낮추기 위해 약간의 대기

    time_limit = 5
    time_s = time.time()
    while 1:
        print(2)
        if is_front_window_title(window_title_seg=window_title_seg):
            if mode_exit == True:
                copy_and_paste_with_keeping_clipboard(prompt="exit")
                pk_press("enter")
        # pk_print(str_working=time.time() - time_s)
        if time.time() - time_s > time_limit:
            pk_print(str_working="5 seconds passed. Exiting loop.")
            break
        pk_sleep(seconds=0.5)  # CPU 점유율을 낮추기 위해 약간의 대기
    return std_str
