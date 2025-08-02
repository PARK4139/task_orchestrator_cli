import traceback

from pkg_py.functions_split.assist_to_upload_pnx_to_git import assist_to_upload_pnx_to_git
from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
from pkg_py.functions_split.get_pk_token import get_pk_token
from pkg_py.system_object.directories import D_PKG_TOML
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

if __name__ == "__main__":
    try:
        ensure_colorama_initialized_once()

        git_repo_url = get_pk_token(f_token=rf"{D_PKG_TOML}/pk_token_pk_system_github_repo_url.toml", initial_str="")
        d_working = D_PROJECT
        branch_n = 'dev'
        assist_to_upload_pnx_to_git(d_working=d_working, git_repo_url=git_repo_url, branch_n=branch_n)

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
