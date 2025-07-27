if __name__ == "__main__":
    try:
        import traceback

        from pkg_py.functions_split.colorama_init_once import colorama_init_once
        from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
        from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
        from pkg_py.functions_split.ensure_files_gathered import ensure_files_gathered
        from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
        from pkg_py.functions_split.get_nx import get_nx
        from pkg_py.system_object.directories_reuseable import D_PROJECT
        from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

        colorama_init_once()
        ensure_window_title_replaced(get_nx(__file__))
        ensure_files_gathered()

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
