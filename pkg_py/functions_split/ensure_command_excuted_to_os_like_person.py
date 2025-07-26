

from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.run_cmd_exe import run_cmd_exe
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


#
# from pkg_py.system_object.files_and_directories_maker_logic import ensure_pnx_made
# from pkg_py.system_object.mouse_and_keyboard import ensure_writen_like_person
# from pkg_py.system_object.is_os_windows import is_os_windows
# , ensure_state_printed
# from pkg_py.system_object.time_and_lanauge_util import sleep
# from pkg_py.system_object.directories import D_PKG_WINDOWS
# from pkg_py.system_object.encodings import Encoding
# from pkg_py.system_object.stamps import STAMP_REMOTE_ERROR, STAMP_REMOTE_DEBUG, STAMP_ATTEMPTED


def ensure_command_excuted_to_os_like_person(cmd, admin_mode=False, mode_exit=True):
    import time

    # todo : chore : return 에 대해서 개선필요
    '''
    return 재대로 안됨
    '''
    window_title_seg = rf'cmd.exe'
    # | clip 을 하여도 값을 읽어오기 어려운 경우가 있음
    ensure_printed(str_working=rf'''cmd="{cmd}"  {'%%%FOO%%%' if LTA else ''}''')
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
            ensure_copied_and_pasted_with_keeping_clipboard(prompt=cmd)
            # ensure_slept(milliseconds=1000)
            ensure_slept(milliseconds=500)
            if is_front_window_title(window_title_seg=window_title_seg):
                ensure_pressed("enter")
            std_str = get_str_from_clipboard()
            return std_str
        ensure_window_to_front(window_title_seg=window_title_seg)
        # # ensure_printed(str_working=time.time() - time_s)
        if time.time() - time_s > time_limit:
            ensure_printed(str_working=rf'''rf"{time_limit} seconds passed. Exiting loop."  {'%%%FOO%%%' if LTA else ''}''')
            break
        ensure_slept(seconds=0.5)  # CPU 점유율을 낮추기 위해 약간의 대기

    time_limit = 5
    time_s = time.time()
    while 1:
        print(2)
        if is_front_window_title(window_title_seg=window_title_seg):
            if mode_exit == True:
                ensure_copied_and_pasted_with_keeping_clipboard(prompt="exit")
                ensure_pressed("enter")
        # ensure_printed(str_working=time.time() - time_s)
        if time.time() - time_s > time_limit:
            ensure_printed(str_working="5 seconds passed. Exiting loop.")
            break
        ensure_slept(seconds=0.5)  # CPU 점유율을 낮추기 위해 약간의 대기
    return std_str
