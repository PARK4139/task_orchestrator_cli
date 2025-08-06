if __name__ == "__main__":
    try:
        import traceback
        # from pkg_py.system_object.500_live_logic import back_up_pnx, ensure_os_shutdown, is_office_pc, is_internet_connected, save_power_as_s3, ensure_process_killed_as_async, pk_run_process_as_async, restart_f_list_with_new_window_as_async
        # from pkg_py.system_object.500_live_logic import back_up_pnx_without_venv_and_idea
        # from pkg_py.system_object.500_live_logic import copy, is_day
        # from pkg_py.system_object.500_live_logic import assist_to_upload_pnx_to_git, get_time_as_, get_pk_token
        #
        # from pkg_py.system_object.static_logic import D_ARCHIVED, D_PKG_PY
        from colorama import init as pk_colorama_init

        # from pkg_py.system_object.500_live_logic import deprecated_get_d_current_n_like_person, get_f_current_n, ensure_copied, assist_to_upload_pnx_to_git, get_time_as_, get_pk_token, ensure_input_preprocessed, ensure_d_size_stable, push_pnx_to_github, LTA
        #
        # from pkg_py.system_object.static_logic import D_PROJECT, UNDERLINE, '[ TRY GUIDE ]', '[ DEBUGGING NOTE ]', '[ EXCEPTION DISCOVERED ]', D_PKG_TOML
        # from pkg_py.system_object.static_logic import D_PROJECT
        #, '[ TRY GUIDE ]', '[ EXCEPTION DISCOVERED ]', D_PKG_TOML

        # backup to local
        pnx_working = D_PROJECT
        pk_back_up_pnx_without_venv_and_idea(pnx_working=pnx_working, d_dst=D_ARCHIVED, with_timestamp=1)
        if is_day(dd=15):
            pk_back_up_pnx(pnx_working=pnx_working, d_dst=D_ARCHIVED)

        # 2. puload to github
        if is_internet_connected():
            ensure_colorama_initialized_once()
            git_repo_url = get_pk_token(f_token=rf"{D_PKG_TOML}/pk_token_pk_system_github_repo_url.toml", initial_str="")
            commit_msg = ensure_input_preprocessed(str_working=f"commit_msg=", upper_seconds_limit=30, return_default=f"feat: auto pushed by pk_system at {get_time_as_("%Y-%m-%d %H:%M")}")
            push_pnx_to_github(d_working=D_PROJECT, git_repo_url=git_repo_url, commit_msg=commit_msg, branch_n='dev')

        # 3 kill or lock os
        if is_office_pc():
            ensure_os_shutdown()
        else:
            # make_os_power_saving_mode_as_s3()
            f_py_list = [
                rf"{D_PKG_PY}/pk_ensure_os_locked.py",
            ]
            restart_f_list_with_new_window_as_async(f_py_list)


    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
        
