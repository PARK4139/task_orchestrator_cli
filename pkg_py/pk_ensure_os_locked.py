if __name__ == '__main__':
    try:
        import traceback
        from pkg_py.functions_split.ensure_os_locked import ensure_os_locked
        from pkg_py.functions_split.chcp_65001 import chcp_65001
        from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
        from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
        from pkg_py.functions_split.is_os_windows import is_os_windows
        from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
        from pkg_py.system_object.directories_reuseable import D_PROJECT
        from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
        from colorama import init as pk_colorama_init

        ensure_colorama_initialized_once()

        if is_os_windows():
            chcp_65001()

        pk_ensure_os_locked()

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
