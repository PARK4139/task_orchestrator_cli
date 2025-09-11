

from selenium.webdriver.common.by import By
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE

from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging


def run_and_login_acu_update_v3_exe_and_run_autoTBDdrive_release_exe(issue_log_index_data):
    import os.path

    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    AUTOTBDDRIVE_RELEASE_SW_VERSION_EXE = rf"{D_HOME}\Desktop\AutoA2zDrive\AutoTBDDrive_Release_{issue_log_index_data["SW 버전"]}.exe"
    logging.debug(
        str_working=rf'''AUTOTBDDRIVE_RELEASE_SW_VERSION_EXE="{AUTOTBDDRIVE_RELEASE_SW_VERSION_EXE}"  {'%%%FOO%%%' if LTA else ''}''')
    window_title_seg = "acu_update_v3_exe"
    if not is_pnx_existing(pnx=AUTOTBDDRIVE_RELEASE_SW_VERSION_EXE):
        acu_update_v3_exe = rf"{D_HOME}\Desktop\AutoA2zDrive\ACU_update_v3.exe"
        acu_update_v3_exe_p = get_p(pnx=acu_update_v3_exe)
        os.chdir(acu_update_v3_exe_p)
        cmd = rf' start cmd.exe /k "title {window_title_seg}&& {D_HOME}\Desktop\AutoA2zDrive\ACU_update_v3.exe &" '
        ensure_command_executed(cmd=cmd, mode="a")
        pw = get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\token_linux_pw.txt', initial_str="")
        user_n = get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\token_linux_id.txt', initial_str="")
        while 1:
            ensure_slept(milliseconds=2000)
            if is_window_opened(window_title_seg=window_title_seg):
                ensure_window_to_front(window_title_seg)
                ensure_slept(milliseconds=500)
                ensure_writen_like_human(str_working=user_n)
                ensure_pressed("enter")
                ensure_writen_like_human(str_working=pw)
                ensure_pressed("enter")
                ensure_writen_like_human("2")
                ensure_pressed("enter")
                ensure_writen_like_human(rf"{issue_log_index_data["SW 버전"]}")
                ensure_pressed("enter")
                break
    else:
        run_autoTBDdrive_release_exe()
