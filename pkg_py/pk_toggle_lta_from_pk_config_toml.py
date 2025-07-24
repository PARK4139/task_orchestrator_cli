if __name__ == "__main__":
    try:
        from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
        from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
        from pkg_py.functions_split.is_os_windows import is_os_windows
        from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
        from pkg_py.functions_split.pk_colorama_init_once import pk_colorama_init_once
        from pkg_py.functions_split.pk_toggle_pk_config_key import pk_toggle_pk_config_key
        from pkg_py.system_object.directories_reuseable import D_PROJECT
        from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
        import traceback
        from colorama import init as pk_colorama_init

        pk_colorama_init_once()
        pk_toggle_pk_config_key('LOCAL_TEST_ACTIVATE')
        if is_os_windows():
            kill_self_pk_program(self_f=__file__)
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
