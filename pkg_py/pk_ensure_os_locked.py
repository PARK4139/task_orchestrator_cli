from pkg_py.functions_split import ensure_slept

if __name__ == '__main__':
    try:
        import traceback
        from pkg_py.functions_split.ensure_os_locked import ensure_os_locked
        from pkg_py.functions_split.chcp_65001 import chcp_65001
        from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
        from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
        from pkg_py.functions_split.is_os_windows import is_os_windows
        from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
        from pkg_py.system_object.directories  import D_PROJECT
        # pk_#
        from colorama import init as pk_colorama_init

        ensure_colorama_initialized_once()

        if is_os_windows():
            chcp_65001()

        ensure_slept(minutes=10) # pk_option

        ensure_os_locked()

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
