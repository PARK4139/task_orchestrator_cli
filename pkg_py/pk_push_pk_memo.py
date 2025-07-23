import os

from pkg_py.workspace.pk_workspace import ensure_git_project_pushed

if __name__ == "__main__":
    try:
        import traceback
        from pathlib import Path

        from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
        from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
        from pkg_py.functions_split.get_pk_token import get_pk_token
        from pkg_py.functions_split.get_time_as_ import get_time_as_
        from pkg_py.functions_split.get_value_completed import get_value_completed
        from pkg_py.functions_split.pk_colorama_init_once import pk_colorama_init_once
        from pkg_py.functions_split.push_pnx_to_github import push_pnx_to_github
        from pkg_py.pk_system_object.directories import D_PKG_TOML, D_PROJECT_MEMO
        from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
        from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE

        os.chdir(D_PROJECT_MEMO)
        ensure_git_project_pushed(with_commit_massage=False)

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
