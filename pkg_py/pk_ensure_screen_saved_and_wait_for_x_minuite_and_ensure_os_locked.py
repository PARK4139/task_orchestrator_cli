from pkg_py.functions_split.ensure_screen_saved_and_wait_for_x_minuite_and_ensure_os_locked import ensure_screen_saved_and_wait_for_x_minuite_and_ensure_os_locked

if __name__ == "__main__":
    import traceback
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.system_object.directories  import D_PROJECT
    # pk_#
    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))
        ensure_screen_saved_and_wait_for_x_minuite_and_ensure_os_locked()
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)