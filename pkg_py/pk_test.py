import inspect
import traceback

from pkg_py.ensure_python_program_reloaded_as_hot_reloader import get_value_via_fzf_or_history
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.get_f_historical import get_f_historical
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_values_from_historical_file import get_values_from_historical_file
from pkg_py.functions_split.pk_colorama_init_once import pk_colorama_init_once
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.set_values_to_historical_file import set_values_to_historical_file
from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.workspace.pk_workspace import get_value_via_fzf_or_history_routine

pk_colorama_init_once()



def pk_test():
    while True:
        key_name = 'commit_message'
        default_options = [
            "chore: ",  # 잡일
            "add: ",  # 신규추가
            # "chore: various improvements and updates across multiple files",
            # "chore: update dependencies",
            # "add: new feature for ~~",
            # "fix: resolve issue with ~~",
            # "refactor: improve code readability in ~~",
            # "refactor: improve code readability in user module",
            # "refactor: restructure and update multiple files with improved messages and translations",
            # "docs: update README.md and improved project documentation",
            # "feat: add user profile page",
            # f"feat: auto pushed (made savepoint) by {SCRIPT_NAME} at {get_time_as_("%Y-%m-%d %H:%M")}",
        ]
        func_n = inspect.currentframe().f_code.co_name
        file_id = get_file_id(key_name, func_n)
        # editable = False
        editable = True
        commit_message = get_value_via_fzf_or_history_routine(key_name, file_id, default_options, editable)
        pk_print(f'''commit_message={commit_message} {'%%%FOO%%%' if LTA else ''}''')


if __name__ == "__main__":
    try:
        pk_test()

        # TBD
        # pk_speak("good evening, sir")

        # pk_jarvis()

        # pk_assist_to_alert_time()

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

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
