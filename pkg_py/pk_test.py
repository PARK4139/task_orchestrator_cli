import traceback

import ipdb

from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.pk_assist_to_alert_time import pk_jarvis
from pkg_py.functions_split.pk_speak import pk_speak
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.workspace.pk_workspace import ensure_this_code_operated


def pk_test():
    from pkg_py.functions_split.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
    from pkg_py.functions_split.pk_colorama_init_once import pk_colorama_init_once

    pk_colorama_init_once()

    while True:
        ensure_this_code_operated(ipdb=ipdb)

        pk_speak("good evening, sir")

        pk_jarvis()

        # if not ensure_pk_wsl_distro_installed():
        #     raise RuntimeError("WSL 배포판 설치/이름 변경에 실패했습니다.")

        # if is_os_linux():
        #     # cmd_to_os('exit')
        #     # available_pk_python_program_pnx = get_pnx_from_fzf(D_PKG_PY)
        #     available_pk_python_program_pnx = None
        #     pnx_list = get_pnx_list(d_working=D_PKG_PY, mode="f", with_walking=0)
        #     for pnx in pnx_list:
        #         if __file__ not in pnx:
        #             continue
        #         available_pk_python_program_pnx = pnx
        #     tmux_session = get_nx(available_pk_python_program_pnx).replace(".", "_")
        #     ensure_tmux_pk_session_removed(tmux_session)

        ensure_pk_system_exit_silent()

if __name__ == "__main__":
    try:
        pk_test()
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
