if __name__ == "__main__":
    try:
        import traceback

        from colorama import init as pk_colorama_init

        # from pkg_py.system_object.500_live_logic import deprecated_get_d_current_n_like_person, get_f_current_n, ensure_copied, assist_to_upload_pnx_to_git, get_time_as_, get_pk_token
        #
        # from pkg_py.system_object.static_logic import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED, D_PKG_TOML

        ensure_colorama_initialized_once()

        git_repo_url = get_pk_token(f_token=rf"{D_PKG_TOML}/pk_token_pk_system_github_repo_url.toml", initial_str="")
        d_working = D_PROJECT
        branch_n = 'dev'
        assist_to_upload_pnx_to_git(d_working=d_working, git_repo_url=git_repo_url,branch_n=branch_n)

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
