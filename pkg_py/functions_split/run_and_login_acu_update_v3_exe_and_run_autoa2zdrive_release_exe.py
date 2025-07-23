

from selenium.webdriver.common.by import By
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_press import pk_press

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.pk_system_object.directories import D_PKG_TXT

from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def run_and_login_acu_update_v3_exe_and_run_autoa2zdrive_release_exe(issue_log_index_data):
    import os.path

    import inspect
    func_n = inspect.currentframe().f_code.co_name

    AUTOA2ZDRIVE_RELEASE_SW_VERSION_EXE = rf"{D_HOME}\Desktop\AutoA2zDrive\AutoA2ZDrive_Release_{issue_log_index_data["SW 버전"]}.exe"
    pk_print(
        working_str=rf'''AUTOA2ZDRIVE_RELEASE_SW_VERSION_EXE="{AUTOA2ZDRIVE_RELEASE_SW_VERSION_EXE}"  {'%%%FOO%%%' if LTA else ''}''')
    window_title_seg = "acu_update_v3_exe"
    if not does_pnx_exist(pnx=AUTOA2ZDRIVE_RELEASE_SW_VERSION_EXE):
        acu_update_v3_exe = rf"{D_HOME}\Desktop\AutoA2zDrive\ACU_update_v3.exe"
        acu_update_v3_exe_p = get_p(pnx=acu_update_v3_exe)
        os.chdir(acu_update_v3_exe_p)
        cmd = rf' start cmd.exe /k "title {window_title_seg}&& {D_HOME}\Desktop\AutoA2zDrive\ACU_update_v3.exe &" '
        cmd_to_os(cmd=cmd, mode="a")
        pw = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\token_linux_pw.txt', initial_str="")
        user_n = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\token_linux_id.txt', initial_str="")
        while 1:
            pk_sleep(milliseconds=2000)
            if is_window_opened(window_title_seg=window_title_seg):
                ensure_window_to_front(window_title_seg=window_title_seg)
                pk_sleep(milliseconds=500)
                write_like_person(str_working=user_n)
                pk_press("enter")
                write_like_person(str_working=pw)
                pk_press("enter")
                write_like_person("2")
                pk_press("enter")
                write_like_person(rf"{issue_log_index_data["SW 버전"]}")
                pk_press("enter")
                break
    else:
        run_autoa2zdrive_release_exe()
