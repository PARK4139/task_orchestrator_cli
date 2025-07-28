import os

from pkg_py.functions_split.ensure_git_project_pushed import ensure_git_project_pushed
from pkg_py.functions_split.ensure_process_killed import ensure_process_killed
from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
from pkg_py.functions_split.get_nx import get_nx

if __name__ == "__main__":
    try:
        import traceback
        from pathlib import Path

        from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
        from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
        from pkg_py.functions_split.get_pk_token import get_pk_token
        from pkg_py.functions_split.get_time_as_ import get_time_as_
        from pkg_py.functions_split.get_value_completed import get_value_completed
        from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
        from pkg_py.functions_split.push_pnx_to_github import push_pnx_to_github
        from pkg_py.system_object.directories import D_PKG_TOML
        from pkg_py.system_object.directories_reuseable import D_PROJECT
        from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

        # python_file_base = D_PROJECT
        # python_filename = rf"pk_push_project_to_github.py"
        # python_file = get_pnx_os_style(rf'{python_file_base}/{python_filename}')
        # python_calling_program = 'start "" cmd /c python'
        # os.chdir(python_file_base)
        # ensure_command_excuted_to_os(cmd=f'{python_calling_program} "{python_file}"')
        # window_title_to_kill = python_filename
        # pk_ensure_process_killed(window_title=get_nx(window_title_to_kill)) # pk_option

        ensure_window_title_replaced(get_nx(__file__))
        os.chdir(D_PROJECT)
        state = ensure_git_project_pushed(with_commit_massage=False)
        if state["state"]:
            ensure_process_killed(window_title=get_nx(__file__)) # pk_option

        # SCRIPT_NAME = Path(__file__).name
        # ensure_colorama_initialized_once()
        # git_repo_url = get_pk_token(f_token=rf"{D_PKG_TOML}/pk_token_pk_system_github_repo_url.toml", initial_str="")
        # commit_msg = get_value_completed(key_hint='commit_msg=', values=[f"feat: auto pushed (made savepoint) by {SCRIPT_NAME} at {get_time_as_("%Y-%m-%d %H:%M")}"])
        # TBD branch_name
        # TBD git_repo_url
        # push_pnx_to_github(d_working=D_PROJECT, git_repo_url=git_repo_url, commit_msg=commit_msg, branch_n='dev')

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
