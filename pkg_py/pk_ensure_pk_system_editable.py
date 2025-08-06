from pkg_py.functions_split.ensure_claude_enabled import ensure_claude_enabled

if __name__ == "__main__":
    import traceback

    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_cursor_enabled import ensure_cursor_enabled
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_memo_editable import ensure_memo_editable
    from pkg_py.functions_split.ensure_pycharm_opened import ensure_pycharm_opened
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.system_object.directories  import D_PROJECT
    # pk_#

    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        ensure_memo_editable()
        ensure_pycharm_opened()
        ensure_cursor_enabled()

        ensure_claude_enabled()

        # ensure_slept(milliseconds=5000)
        # ensure_program_suicided(__file__)  # pk_option
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
