if __name__ == "__main__":
    from pkg_py.functions_split.chcp_65001 import chcp_65001
    from pkg_py.functions_split.ensure_files_organized_by_keyword_and_x import ensure_files_organized_by_keyword_and_x
    from pkg_py.functions_split.get_os_n import get_os_n
    import traceback
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        if get_os_n() == 'windows':
            chcp_65001()

        ensure_files_organized_by_keyword_and_x()
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
